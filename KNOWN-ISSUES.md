# Known issues and parked features

Items parked so the other sections can be finished before the deadline. Come back to them after that. Each entry: what's wrong or wanted, why it's parked, and the planned fix.

## Parked features

### F1. Hero: products stay on the shelves on every screen (photo-anchored products)
*Parked 2026-11-11.*

**Issue.** A merchant places a hero product on a shelf in the editor, but on another screen size it is off the shelf.
- The desktop background photo uses `object-fit: cover`, so each screen shape crops and scales it differently.
- Products are placed in % of the *hero's products area*, not of the photo, so the photo moves under them.
- Phones don't have this problem: the hero is exactly the mobile photo's shape and products are % of that photo.

**Wanted.** The same look on every screen within each range:
- **Phones, small to large:** the mobile photo.
- **Large tablets to monitors:** the desktop photo.

Products must move and scale with the photo. The positions already placed must keep their current look.

**Planned fix: a "photo stage".**
- **The stage.** `.hero__stage` is a box with the photo's aspect ratio. CSS sizes and offsets it exactly like the cover-fitted photo:
  - `container-type: size` on the hero
  - `inline-size: max(100cqw, 100cqh * R)`
  - `block-size: max(100cqh, 100cqw / R)`
  - `left: (100cqw − stage-w) × focal x`, `top: (100cqh − stage-h) × focal y`, with the focal point from `image.presentation.focal_point`
- **Products on the stage.** Products are positioned and sized in % of the stage, i.e. of the photo, so they stay on the same shelf at the same relative size.
- **Tablet breakpoint (decided).** The mobile photo is used only below 768px. From 768px up, tablets use the desktop photo and stage. Today the cutoff is 1024px.
- **Merchant-friendly settings.**
  - Labels: "% of the photo".
  - A faint 10% placement grid on the stage while a Hero product block is selected in the theme editor (editor only).
  - Help text pointing to the photo's focal point for narrow screens.
- **Edge case.** On squarer screens the cover crop cuts the photo's edges, so a product near the edge can go off-screen with its shelf. The focal point decides what stays visible.
- **Converting existing placements (research first).**
  1. Read the current x / y / width values, Products area start, and the photo's size and focal point.
  2. Pick the reference screen they were placed on (probably 1920×1031) and confirm it.
  3. Convert:
     - `photoX = (areaLeft + x × areaW − stageLeft) / stageW`
     - `photoY = (y × heroH − stageTop) / stageH`
     - `photoW = width × areaW / stageW`
  4. Preview the result on a scratch page at 1920 / 1280 / 1024 / 768 before writing `templates/index.json`.
- **Backup.** Homepage before this change: `design/backups/index-2026-11-11-1257.json`.

**Files:** `sections/hero.liquid` (Liquid variables, stage markup, CSS, editor grid JS), `blocks/_hero-product.liquid` (labels), `locales/en.default.schema.json`, `templates/index.json`.

### F2. Hero: layout that follows the content position (shelves on the left, or on both sides)
*Parked 2026-11-11. Built, then removed.*

**Wanted.** Hero photos with shelves on the left and a plain wall on the right, or shelves on both sides. The products area should follow the Horizontal content position:
- **Start:** products on the right (today).
- **End:** products area mirrored to the left.
- **Center:** products area = full width.

Text alignment should follow the content position too.

**Why it was removed.** It depends on F1: without photo-anchored products, the positions still drift with screen size. Build it together with F1. The removed CSS was:
- `.hero--x-end .hero__products { inset-inline: 0 var(--hero-products-start); }`
- `.hero--x-center .hero__products { inset-inline: 0; }`
- text-align rules on `.hero-content`

## Known issues

### I1. Hero decorations drift between 768 and ~1384px
- **Issue.** With Content spacing "between", decorations' Y is a % of a content box as tall as the screen, while the text scales with the screen width. The gold magnolia lands on the brush word between about 768 and 1384px.
- **Tried and removed (too confusing for merchants).** A per-decoration "Own position on tablets" setting, a decoration layer scaled like the text, and a `fit-content` content box.
- **Idea for later.** Anchor decorations to the photo stage (F1) or to the heading block.

### I2. Hero at 320px
At 320px the mobile photo, and so the hero, gets shorter than at 375px. Two options, left undecided:
- proportional text scaling (looks the same as at 375px, smaller text)
- more room for the text (Text area height grows below 375px)

### I3. Red right-side band on phones
- **Issue.** Tried on phones; it doesn't look good at the right edge.
- **Current behaviour.** Phones and small screens show the bar above the header. The band appears only from 990px.
