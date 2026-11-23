---
name: design-brief
description: Turn a design screenshot, Figma URL/node id or screen slug into a precise implementation brief (a prompt another model can build from), using exact Figma measurements, Oroskin tokens and existing theme components.
disable-model-invocation: true
argument-hint: "<image path(s)> [figma URL | node id | screen slug] [one-line purpose]"
---

# /design-brief: design → implementation prompt

**Input:** $ARGUMENTS

The goal is a brief that a model with **no other context** can implement correctly in this theme. Most screenshot-to-code errors come from guessed pixel values and rebuilding things that already exist. So: measure from Figma data, map every value to a theme token, reuse existing files, and keep observations apart from guesses.

## 1. Collect the inputs

- **Images:** Read every image path given. If none is given but there's a slug, use `design/figma/screens/<slug>/*.png`.
- **Node:** take the node id from a Figma URL (`node-id=1-49257` → `1:49257`), a raw id or a slug (`python design/figma/tools/figma_node.py --frames` lists them).
- **Purpose:** if the user didn't say what the screen or part is for (which page template, which section), and it isn't obvious, ask once before going on.

## 2. Measure: metadata first, pixels second

1. **If a node or slug is known**, run `python design/figma/tools/figma_node.py <node> --depth 3` (use `--find "<text>"` to locate a part). **Every size, position and gap in the brief comes from this output**, in Figma px at a 1920px frame. Also read `design/figma/screens/<slug>/notes.md`.
2. **The screenshot is used only for** hierarchy, visual weight, alignment, effects (blur, glass, shadows, gradients, overlaps, image cropping) and anything the metadata can't show.
3. **Scale:** run `python design/figma/tools/inspect_image.py info <img> --frame-width <frame width>`. Divide screenshot px by the scale. If there is no node, or the scale warning appears, mark every pixel value in the brief as `~approx`.
4. **Detail:** small text, icons and borders are unreadable in a downscaled image. Crop and zoom them, then Read the crop: `inspect_image.py crop <img> X Y W H --zoom 3 --out <scratchpad>/x.png`. Use `grid` if positions are hard to judge.
5. **Colours:** `inspect_image.py color <img> X,Y ...` on **flat interior areas only** (not text, edges, glass or photos). Anything "close" or "UNMATCHED" goes to Open questions, not into the spec as a new colour.
6. Use the Figma MCP (`get_design_context`) **only** if the local snapshot lacks something essential. The account is on a call-limited plan; say so before calling it.

## 3. Map to the theme

- **Tokens:** read `design/figma/tokens.md` and `snippets/css-variables.liquid`. Express every value as an existing variable: `--space-*`, `--font-size-*`, `--radius-*`, `--color-*` scheme slots, the page width. Write the Figma px next to it, e.g. `gap: var(--space-xl) /* 32px */`. If no token fits, say "no token: <px>, add one or round to <token>?".
- **Reuse:** list `sections/`, `blocks/`, `snippets/` and grep for similar class names. For each part of the design, say **reuse / extend / new**, naming the file. Never propose a new file when an existing one fits (for example `product-card`, `price`, `image`, `button`, `heading`, `text`, `explore-button`, `quick-add`).
- **Merchant settings:** decide what becomes a section setting, a block or a locale string. Give the setting type for each (`image_picker`, `richtext`, `collection`, `product_list`, `color_scheme`, `range`…).
- **Project rules** (from `CLAUDE.md`): fonts only through the `font_picker` settings (never Canela or Satoshi files); hex colours; every visible string in `locales/en.default.json`; animations via `<animate-on-scroll>` + `data-animate`, never on section 1 or the LCP image; parked features (decision 6) are flagged, not built; mobile layouts are **asked about, not designed** (decision 7); the `context*.jsx` files are reference only.

## 4. Write the brief

Save it to `design/briefs/<slug-or-part>.md` (`design/` is local only, not in git). Use exactly these headings:

~~~markdown
# <Name>: implementation brief
Source: <images> · Figma node <id> (<frame name>, <w>x<h>) · scale <n> · captured <date>

## 1. Purpose and placement
Template(s), where on the page, what the visitor does here. Section order on the page.

## 2. Reuse map
| Part of the design | Reuse / extend / new | File | Notes |

## 3. Layout
Container (page width / full bleed), grid or flex, columns, column widths, gaps, vertical padding.
All as tokens, with Figma px in comments. Alignment and overlaps (z-order).

## 4. Component inventory (top → bottom, left → right)
For each element: role (heading level, link, button, image, decorative), content, type style
(font role + size token + weight + case + letter-spacing + line-height), colour slot, size, spacing,
radius, border, shadow/blur, image aspect ratio and crop.

## 5. Merchant-editable content
| Element | Section setting / block / locale key | Setting type | Default |

## 6. States and behaviour
Hover, focus-visible, active/selected, disabled, loading, empty state (`!= blank`), sold out,
editor placeholder. Links: where each one goes.

## 7. Animation
`data-animate` value per element (fade-up / zoom-in / none), stagger, and reduced-motion behaviour.

## 8. Responsive
What the design shows (desktop 1920). Sensible fluid behaviour down to tablet.
Mobile: "no design: ask" unless the user provided one.

## 9. Accessibility
Heading order, alt text source, accessible names for icon buttons, contrast checks
(text vs background, with ratios), keyboard order.

## 10. Flags
Parked features present in the design (do not build). Things that look like Dawn/Horizon patterns (do not copy).

## 11. Open questions
Everything guessed, unmatched, unreadable or ambiguous. One question per line, with your suggested default.

## 12. Acceptance checklist
- [ ] Checks the implementer can verify side by side with the screenshot (sizes, gaps, colours, states)
- [ ] `shopify theme check` clean, no hardcoded text, preset works, empty state renders

## 13. Prompt
```text
<A self-contained prompt that restates the above for a model that can only see this text and the
screenshot: the goal, files to create or edit, exact tokens and values, settings, states, rules,
and "ask before guessing" for the open questions. Under ~600 words.>
```
~~~

Rules for the content: write **observed** values plainly and mark inferred ones `(inferred)`. No vague words ("nice spacing", "modern look"). Every number either comes from metadata, or is marked `~approx`.

## 5. Report back

In chat: the brief's path, a 3-line summary, the Open questions list, and which extra input would remove the most guesswork (a Figma URL with `node-id`, a 1x PNG export, hover/open-state frames, zoomed crops of small text). Don't write theme code; implementing is a separate step (`/learn-guide`).
