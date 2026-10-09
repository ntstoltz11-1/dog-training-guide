"""Shorten bare URLs in the Link column of evidence tables to [host](url)
so the Citation column gets the width. Idempotent.
Run:  python maintainers/shortlinks.py
"""
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
FILES = [ROOT / "evidence" / "sources.md", ROOT / "evidence" / "legal-status.md"]
BARE = re.compile(r"(?<![\(\[<])(https?://[^\s|<>]+)")  # DOIs may contain parentheses

def label(url):
    host = urlparse(url).netloc.lower().removeprefix("www.")
    return "doi" if host == "doi.org" else host

for f in FILES:
    if not f.exists():
        continue
    text = f.read_text(encoding="utf-8")
    new = BARE.sub(lambda m: f"[{label(m.group(1))}]({m.group(1)})", text)
    if new != text:
        f.write_text(new, encoding="utf-8")
        print("changed", f.relative_to(ROOT).as_posix(), len(BARE.findall(text)), "links")
    else:
        print("no change", f.relative_to(ROOT).as_posix())
