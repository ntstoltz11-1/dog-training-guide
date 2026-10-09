import os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "archive", "research"}
# backtick-wrapped path ending in .md, optionally with a trailing "(see ...)"
PAT = re.compile(r"`([A-Za-z0-9_./\-]+\.md)`")
# bare "evidence/claims.md" inside the evidence footer line
FOOTER = re.compile(r"^(Evidence:.*?)\(see evidence/claims\.md\)\s*$", re.M)

def resolve(ref, src):
    cands = [src.parent / ref, ROOT / ref]
    for c in cands:
        if c.is_file():
            return c.resolve()
    if "/" not in ref:
        hits = [p for p in ROOT.rglob(ref) if not any(x in SKIP_DIRS for x in p.relative_to(ROOT).parts)]
        if len(hits) == 1:
            return hits[0].resolve()
    return None

changed = []; unresolved = set()
for md in ROOT.rglob("*.md"):
    if any(p in SKIP_DIRS for p in md.relative_to(ROOT).parts):
        continue
    text = md.read_text(encoding="utf-8")
    orig = text

    def sub(m):
        ref = m.group(1)
        tgt = resolve(ref, md)
        if tgt is None or tgt == md.resolve():
            unresolved.add((md.relative_to(ROOT).as_posix(), ref)); return m.group(0)
        rel = os.path.relpath(tgt, md.parent).replace(os.sep, "/")
        return f"[`{ref}`]({rel})"

    # avoid double-wrapping already-linked refs
    text = re.sub(r"(?<!\]\()" + PAT.pattern + r"(?!\]\()", sub, text)
    text = re.sub(r"\[\[`", "[`", text)

    def foot(m):
        tgt = ROOT / "evidence" / "claims.md"
        rel = os.path.relpath(tgt, md.parent).replace(os.sep, "/")
        return f"{m.group(1)}(see [evidence/claims.md]({rel}))"
    text = FOOTER.sub(foot, text)

    if text != orig:
        md.write_text(text, encoding="utf-8")
        changed.append(md.relative_to(ROOT).as_posix())

print(f"changed {len(changed)} files")
for u in sorted(unresolved): print("UNRESOLVED", u)
