"""Replace code-styled file-name link text with the target page's title.

Reader-facing files only (guide/, README.md, TABLE-OF-CONTENTS.md,
CONTRIBUTING.md). Backend files keep path-style link text on purpose.
Run after linkify.py whenever pages are added:  python maintainers/titleize.py [--dry]
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "archive", "research"}
DRY = "--dry" in sys.argv
LINK = re.compile(r"\[`([A-Za-z0-9_./\-]+\.md)`\]\(([^)]+)\)")

mds = [p for p in ROOT.rglob("*.md")
       if not any(x in SKIP_DIRS for x in p.relative_to(ROOT).parts)]

titles = {}
for p in mds:
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            titles[p.resolve()] = line[2:].strip()
            break

def is_reader(p):
    rel = p.relative_to(ROOT)
    return rel.parts[0] == "guide" or p.name in ("README.md", "TABLE-OF-CONTENTS.md", "CONTRIBUTING.md")

changed, missing = [], set()
for p in mds:
    if not is_reader(p):
        continue
    text = p.read_text(encoding="utf-8")

    def sub(m):
        ref, rel = m.group(1), m.group(2)
        tgt = (p.parent / rel).resolve()
        title = titles.get(tgt)
        if not title:
            missing.add((p.relative_to(ROOT).as_posix(), rel)); return m.group(0)
        return f"[{title}]({rel})"

    new = LINK.sub(sub, text)
    if new != text:
        changed.append(p.relative_to(ROOT).as_posix())
        if not DRY:
            p.write_text(new, encoding="utf-8")

print(f"{'would change' if DRY else 'changed'} {len(changed)} files")
for c in changed: print("  ", c)
for m in sorted(missing): print("NO TITLE", m)
