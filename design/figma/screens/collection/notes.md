# collection (1:49257)

Frame: `Collection` 1920x6818

## CAPTURE FAILED (2026-09-28)

get_screenshot and get_design_context both returned: "You've reached the Figma MCP tool call limit on the Starter plan." Retried once; still blocked. No screenshot.png, context*.jsx or assets-map.json were saved. Re-run this screen once the Figma MCP quota resets or the plan is upgraded.

## What metadata.xml tells us (direct children, sorted top to bottom)

- y=0 `1:49282` rounded-rectangle "image 639" 521x402
- y=24 `1:49722` frame "Frame 26080041" 1380x77 -- shared header bar (captured by another agent)
- y=155 `1:49262` instance "Button" 49x33
- y=155 `1:49263` frame "Button" 49x33
- y=175 `1:49266` vector "Vector" 5x8
- y=197 `1:49275` text "Clinical Beauty" 326x52
- y=197 `1:49279` rounded-rectangle "image 627" 150x50
- y=203 `1:49280` rounded-rectangle "image 633" 184x183
- y=226 `1:49277` text "with" 254x75
- y=264 `1:49276` text "formulations" 326x52
- y=275 `1:49278` text "Absolute Integrity." 256x75
- y=302 `1:49281` rounded-rectangle "image 635" 48x51
- y=437 `1:49258` frame "Component 1485" 121x50
- y=437 `1:49683` instance "Component 1484" 203x50
- y=440 `1:49268` instance "Component 1521" 129x50
- y=440 `1:49269` instance "Component 1520" 111x50
- y=440 `1:49270` instance "Component 1523" 81x50
- y=440 `1:49271` instance "Component 1522" 118x50
- y=450 `1:49697` instance "Toggle" 68x30
- y=452 `1:49267` text "30 Products" 71x26
- y=452 `1:49684` text "COMPARE" 79x26
- y=483 `1:49272` line "Line 122" 0x37
- y=483 `1:49273` line "Line 124" 0x37
- y=483 `1:49274` line "Line 123" 0x37
- y=562 `1:49283` frame "Component 1540" 892x399
- y=563 `1:49619` frame "Component 1542" 429x653
- y=563 `1:49632` frame "Component 1543" 439x653
- y=996 `1:49454` frame "Component 1544" 427x309
- y=996 `1:49544` frame "Component 1545" 427x566
- y=1251 `1:49361` frame "Component 1546" 892x728
- y=1341 `1:49589` frame "Component 1547" 427x638
- y=1597 `1:49514` frame "Component 1548" 427x382
- y=2014 `1:49309` frame "Component 1550" 892x399
- y=2014 `1:49439` frame "Component 1547" 427x638
- y=2014 `1:49657` frame "Component 1549" 429x743
- y=2448 `1:49484` frame "Component 1552" 429x309
- y=2448 `1:49499` frame "Component 1553" 429x309
- y=2687 `1:49670` frame "Component 1554" 437x828
- y=2792 `1:49387` frame "Component 1551" 892x728
- y=2814 `1:49574` frame "Component 1555" 427x706
- y=3555 `1:49469` frame "Component 1561" 427x309
- y=3555 `1:49559` frame "Component 1563" 427x566
- y=3560 `1:49413` frame "Component 1566" 892x544
- y=3900 `1:49604` frame "Component 1564" 427x638
- y=4139 `1:49335` frame "Component 1565" 892x399
- y=4156 `1:49529` frame "Component 1562" 427x382
- y=4616 `1:49686` frame "Group 1000003395" 550x60
- y=4630 `1:49685` text "Page 1 of 11" 69x17
- y=4805 `1:49714` instance "Component 1591" 517x257
- y=4805 `1:49715` instance "Component 1592" 516x260
- y=4805 `1:49716` instance "Component 1593" 516x260
- y=5194 `1:49718` instance "Component 2069" 350x309
- y=5194 `1:49719` instance "Component 2070" 350x309
- y=5194 `1:49720` instance "Component 2071" 350x309
- y=5194 `1:49721` instance "Component 2072" 350x309
- y=5794 `1:49698` frame "Group 1000003403" 1920x133
- y=5794 `1:49717` instance "Component 85" 1920x974 -- shared footer (captured by another agent)

## Plain-English reading (from metadata only, not verified visually)

- Header bar (1:49722, shared) at top; breadcrumb-style buttons (1:49262, 1:49263 "Cart"?) at y=155.
- Hero heading: "Clinical Beauty / formulations / with / Absolute Integrity." with small inline images (1:49279-1:49281) and a large image at top-right (1:49282, 521x402).
- Toolbar at y~440: "Filters" button (1:49258), four filter/sort pills (Components 1520-1523), "COMPARE" label + Toggle (1:49697), "30 Products" count, sort dropdown (1:49683).
- Product grid y=562-4538: masonry-style mix of wide cards (892 wide) and narrow cards (427-439 wide) - Components 1540-1566.
- Pagination: "Page 1 of 11" + pager group (1:49686) at y~4616.
- Three promo cards (Components 1591-1593, ~516x258) at y=4805.
- Four small cards (Components 2069-2072, 350x309) at y=5194.
- Group 1000003403 (1:49698) and footer Component 85 (1:49717) at y=5794 -- shared footer.

Interactive: filters, sort, pagination, product cards, COMPARE toggle.
**PARKED:** COMPARE toggle (product compare is not native to Shopify).
Colours/fonts/shadows: unknown until design context can be fetched.

> **Update:** `screenshot.png` was added afterwards, from a capture made earlier in the session (1024–1600px). The shipping styles are already summarised in `../../tokens.md`.
