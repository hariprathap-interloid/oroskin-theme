"""Download every Figma MCP asset URL found in a context.jsx file into design/figma/assets/.

Usage:  python design/figma/tools/save_assets.py <path/to/context.jsx> [more files...]

- Files are named by content hash, so the same asset is stored only once across all screens.
- SVGs go to assets/icons/, raster images to assets/images/.
- Writes <folder>/assets-map.json mapping the JSX constant name -> local path (relative to design/figma/).
- The Figma MCP asset URLs expire after 7 days, so run this right after saving context.jsx.
"""
import hashlib
import json
import pathlib
import re
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent  # design/figma
CONST_RE = re.compile(r'const\s+(\w+)\s*=\s*"(https://www\.figma\.com/api/mcp/asset/[^"]+)"')
EXT = {"image/svg+xml": ".svg", "image/png": ".png", "image/jpeg": ".jpg", "image/webp": ".webp", "image/gif": ".gif"}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "oroskin-design-snapshot"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read(), r.headers.get("Content-Type", "").split(";")[0].strip()


def main(paths):
    for p in paths:
        ctx = pathlib.Path(p)
        mapping = {}
        for name, url in CONST_RE.findall(ctx.read_text(encoding="utf-8")):
            try:
                data, ctype = fetch(url)
            except Exception as e:  # noqa: BLE001
                mapping[name] = f"ERROR: {e}"
                continue
            ext = EXT.get(ctype) or pathlib.Path(url).suffix or ".bin"
            sub = "icons" if ext == ".svg" else "images"
            out = ROOT / "assets" / sub / (hashlib.sha1(data).hexdigest()[:12] + ext)
            out.parent.mkdir(parents=True, exist_ok=True)
            if not out.exists():
                out.write_bytes(data)
            mapping[name] = out.relative_to(ROOT).as_posix()
        map_file = ctx.parent / "assets-map.json"
        existing = json.loads(map_file.read_text(encoding="utf-8")) if map_file.exists() else {}
        existing.setdefault(ctx.name, {}).update(mapping)
        map_file.write_text(json.dumps(existing, indent=2), encoding="utf-8")
        errors = sum(1 for v in mapping.values() if v.startswith("ERROR"))
        print(f"{ctx}: {len(mapping)} assets, {errors} errors")


if __name__ == "__main__":
    main(sys.argv[1:])
