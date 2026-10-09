# Handoff 04 : Formatting and cleanup pass done, repo reads clean on GitHub

**Date:** 2026-10-08.

## Where things stand

- **Rendering checked live** (README, a method page, a problem page, `evidence/sources.md`). Headings, tables, and page shape render fine. One real defect: every cross-link showed as a code-styled file name (`recall.md`), which reads as jargon to the owner audience.
- **Fixed with a new script.** [`titleize.py`](titleize.py) rewrites `[`file.md`](path)` to `[Page title](path)` using each target's H1, in reader-facing files only (`guide/`, README, TOC, CONTRIBUTING). 50 files changed. Backend files keep path-style links on purpose. Run order after adding pages: `linkify.py`, then `titleize.py`.
- **`sources.md` table widths fixed.** [`shortlinks.py`](shortlinks.py) turns bare URLs in the Link column into `[doi](url)`, so the Citation column gets the width. 40 links.
- **README routing table:** the three bare folder paths are now linked folder names with a plain word ("the problems folder").
- **Privacy:** the local Windows path and surname are out of `CLAUDE.md` and `linkify.py` (now relative to the repo). Archived handoffs were already clean. The GitHub username stays; it is the repo address.
- **`.gitattributes`** marks the helper scripts `linguist-vendored`, so GitHub stops labeling the guide "Python 100%".
- **Budgets:** all 53 guide pages under 80 lines (longest: decision-tree at 73). No em dashes, no emojis, one H1 per file. Writing protocol and problem template now state the link-text rule.
- **Verification queue unchanged:** 28 of 55 sources verified; two full-text checks open (Herron 2009 Fig. 3; Simpson 2007 n).

## Next session

1. Verification pass 3: the two full-text follow-ups, then priority 2 ([`TASKS.md`](TASKS.md) Verify).
2. Nick test-reads [`decision-tree.md`](../guide/01-start-here/decision-tree.md) and [`children-and-dogs.md`](../guide/03-problems/children-and-dogs.md) cold.
3. Consider body-language diagrams ([`TASKS.md`](TASKS.md) Build).

## Retro (session 04)

- Went wrong: the method template's Related link is written relative to `_templates/`, so a copied page needs `linkify.py` to re-resolve it. Noted in the problem template; method template left as is.
- Went right: screenshotting the live repo found the one defect that mattered in minutes; the rest was already within budget.
- Changed: 50 reader files (link text), README (3 rows, 1 row), sources.md (40 links), CLAUDE.md (2 lines), linkify.py, writing-protocol.md, _TEMPLATE-problem.md, new titleize.py, shortlinks.py, .gitattributes, TASKS, this file. Handoff 03 archived.
- Try next time: nothing new; the session protocol held.
