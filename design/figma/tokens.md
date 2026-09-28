# Oroskin design tokens

- **Source:** Figma file `EcvT6hH5DXNRzan3G8uVwf` (Dev-OroSkin). The HSLA values were taken from Figma by the developer. The hex values and the "extracted" rows come from the Figma MCP, on 2026-09-28.
- **Machine-readable copy:** [tokens.json](tokens.json)
- **Rule:** when the HSLA value and a Figma variable disagree, use the **Figma variable**. For example, `hsla(0,100%,25%)` works out to `#800000`, but the variable `color/primary` is exactly `#7d0000`.

## Colours

| Token | HSLA (from Figma) | Hex | Used for |
|---|---|---|---|
| `background` | hsla(42, 100%, 97%, 1) | `#fffaf0` | Main page background (cream) |
| `background-alt` | hsla(0, 0%, 100%, 1) | `#ffffff` | White sections and pages |
| `foreground` | hsla(0, 0%, 12%, 1) | `#1f1f1f` | Body text. Figma variable `color/secondary` |
| `primary` | hsla(0, 100%, 25%, 1) | `#7d0000` | Accent red: labels, links, active nav. Figma variable `color/primary` |
| `secondary-primary` | hsla(42, 53%, 54%, 1) | `#c8a34c` | Gold: home hero band, highlighted words |
| `primary-text` | hsla(0, 0%, 100%, 1) | `#ffffff` | Text on primary (red) backgrounds |
| `secondary-text` | hsla(0, 100%, 25%, 1) | `#7d0000` | Accent text |
| `white-text` | hsla(0, 0%, 100%, 1) | `#ffffff` | Text on dark or image backgrounds |
| `icons` | hsla(0, 0%, 12%, 1) | `#1f1f1f` | Icon colour |

### Extracted from the MCP (not in the pasted list)
| Value | Where it's used |
|---|---|
| `#eedede` | 1px divider lines (shipping page rules, card separators) |
| `#f6ecec` | Card border, shipping "dispatched from" cards |
| `#787878` | Footer link text |
| `rgba(125,0,0,0.05)` + border `rgba(125,0,0,0.25)` | Tinted info box (shipping note) |
| `rgba(125,0,0,0.10)` | Big faded background letters (e.g. "PAR", "NYO") |
| `rgba(255,255,255,0.25)` | Glass surface: header bar, round icon buttons, footer panel |
| `rgba(255,255,255,0.5)` + 1.5px white border | Newsletter input |

## Buttons

| Token | Value |
|---|---|
| `primary-button` background | hsla(0, 100%, 25%, 0.85), i.e. `rgba(125,0,0,0.85)`, with a 1px `#7d0000` border |
| `primary-button` text | `#ffffff`, Satoshi Medium ~16.5px, uppercase, letter-spacing 0.12em |
| `primary-button` shadow (extracted) | `0 4px 20px 0 rgba(0,0,0,0.2)` |
| `primary-button` shape (extracted) | pill, radius 50px, height 50px, padding 13px 35px |
| `secondary-button` text | `#7d0000` |
| `secondary-button` shadow | `inset -1px 0 5px 0 hsla(0,0%,100%,0.5)` (glass edge) |
| Round icon button, "Liquid Glass" (extracted) | 50×50px, radius 50px, `rgba(255,255,255,0.25)`, shadow = header-nav shadow |

## Cards

| Token | Value |
|---|---|
| `card-background` | hsla(36, 36%, 95%, 0.2), i.e. `#f7f3ee` at 20% |
| `card-border` | hsla(0, 56%, 87%, 0.31), i.e. `#f0cbcb` at 31% |
| `card-box-shadow` | `0 0 10px 0 hsla(0,0%,0%,0.05)` |
| `collection-card-box-shadow` | `0 5px 25px 0 hsla(0,0%,0%,0.05)` |
| `card-secondary-box-shadow` | `0 4px 25px 0 hsla(0,45%,82%,0.26)` (rose glow, `#e6bcbc` at 26%) |
| Card radius (extracted) | 19px (small cards), 25px (info boxes), 50px (footer panel) |
| Card shadow variant (extracted) | `0 2px 10px 0 rgba(125,0,0,0.06)` |

## Header / navigation

| Token | Value |
|---|---|
| `header-nav-box-shadow` | `0 4px 15px 0 hsla(0,0%,73%,0.25)` (`#bababa` at 25%) |
| Header bar (extracted) | floating pill, 1363×77px at 1920 wide, 24px from the top, `rgba(255,255,255,0.25)`, radius 50px |
| Nav link (extracted) | Satoshi Medium 18px, uppercase, letter-spacing 0.12em (2.16px). Active link = `primary` plus a hand-drawn underline SVG |

## Typography (from the MCP; the full sweep is in [typography.md](typography.md))

| Role | Figma font | Our font (decision 5, `font_picker`) | Sizes seen |
|---|---|---|---|
| Headings / display | Canela Text Trial, Regular | **Newsreader** `newsreader_n4` | 96 (faded letters), 60 (H1), 40 (stats, card titles), 26 (list titles) |
| Body | Satoshi Regular | **Plus Jakarta Sans** `plus_jakarta_sans_n4` | 22 / 20 / 18 / 16. Line-height 35px on 20–22px text; letter-spacing 0.01em |
| Labels / eyebrow / nav | Satoshi Medium, UPPERCASE | Plus Jakarta Sans, weight 500 | 18px, letter-spacing 0.21em (3.78px). Nav: 0.12em. Breadcrumb: 14px / 2px |
| Logo | Cormorant Garamond SemiBold + SemiBold Italic ("Oro" + red italic "Skin") | Uploaded logo image (text fallback in the heading font) | 46.8px in the header; 500px as the giant footer wordmark |
| Misc | Switzer Bold, Inter Medium (badge counter, 12px) | Body font | — |

## Layout (extracted)
- Design width: **1920px**. Content is inset about 135px on each side, so the content width is about 1650px.
- Section eyebrow pattern: a 66×2px `primary` rule followed by an uppercase label.
- Section divider pattern: uppercase `primary` label, then a 1px `#eedede` line filling the rest of the row.
- **No mobile frames exist yet** (decision 7).
