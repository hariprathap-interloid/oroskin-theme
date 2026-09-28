# Oroskin Figma snapshot

- **Figma file:** [Dev-OroSkin](https://www.figma.com/design/EcvT6hH5DXNRzan3G8uVwf/Dev-OroSkin), file key `EcvT6hH5DXNRzan3G8uVwf`, page `0:1`
- **Captured:** 2026-09-28. **Status: PARTIAL.** The Figma MCP stopped with *"You've reached the Figma MCP tool call limit on the Starter plan"*.
- **Rule:** read this folder before calling the Figma MCP. The `context*.jsx` files are React+Tailwind **reference only**; never paste them into the theme.

## What's complete
| File | Contents |
|---|---|
| [tokens.md](tokens.md) / [tokens.json](tokens.json) | ✅ Colours, buttons, cards, header, type scale and fonts (your values plus the MCP's) |
| [metadata.xml](metadata.xml) | ✅ Full layer tree: every node id, name, text, position and size |
| `screens/*/notes.md` | ✅ Layer-by-layer notes built from metadata.xml, with PARKED items flagged |
| `assets/logo/logo-mark-flame.png` | ✅ Logo flame mark |
| [tools/save_assets.py](tools/save_assets.py) | Downloads the asset URLs in a context file (they expire after 7 days) |

## Per-screen status
✅ = saved, ❌ = still to capture. "Context" means the exact styles from `get_design_context`.

| Slug | Node | Screenshot | Context | Notes |
|---|---|---|---|---|
| home | 1:49229 | ✅ hero | ❌ | 1920×1031 hero viewport |
| after-home-1 / -2 | 1:49237 / 1:49239 | ❌ | ❌ | |
| new-arrivals / -after-login | 1:49233 / 1:49235 | ❌ | ❌ | |
| collection | 1:49257 | ✅ | ❌ | Filters, grid, compare bar (PARKED) |
| pdp | 1:49251 | ❌ | ❌ | |
| cart | 1:49245 | ❌ | ❌ | |
| about-us / contact-us / faq | 1:49241 / 1:49253 / 1:49255 | ❌ | ❌ | |
| blog / blog-details | 1:49243 / 1:18396 | ❌ | ❌ | blog-details is 10764px tall |
| shipping | 1:17093 | ✅ | 🟡 styles summarised in tokens.md | |
| returns | 1:18125 | ✅ | ❌ | |
| cookies / terms / privacy | 1:17171 / 1:18208 / 1:18280 | ❌ | ❌ | |
| signout / track-order-1 / -2 | 1:49231 / 1:49247 / 1:49249 | ❌ | ❌ | |
| account-* (9 pages) | see folders | ✅ all 9 | ❌ | PARKED (decision 6) |
| components (27) | board 1:18658 | ❌ | ❌ | Header 1:17155, footer 1:17151 |
| animations (7) | board 1:27106 | ✅ home overview only | ❌ | See animations/home-sequence/notes.md |

## How to finish the snapshot
1. **Wait for the Figma MCP limit to reset, or upgrade the seat.** Figma's Starter plan allows only a few MCP calls. Check the current limits in Figma's pricing and help pages.
2. **Re-run only the ❌ items.** Use one `get_screenshot` per screen, then `get_design_context` on the whole frame or on a few large groups, not every loose layer. After each context file, run `python design/figma/tools/save_assets.py <file>`.
3. **Alternative with no MCP limit:** export frames as PNG from Figma yourself (select the frame → Export → PNG 1x), and save them as `screens/<slug>/screenshot.png`.
