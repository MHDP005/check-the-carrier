#!/usr/bin/env python3
"""Regenerate sitemap.xml for every HTML page in the site.

Run from the repository root, or from anywhere:

    python3 tools/build_sitemap.py

The nightly page routine must run this before each commit so new area or
guide pages are listed with an up-to-date lastmod date.
"""

from __future__ import annotations

import datetime as dt
import subprocess
import sys
from pathlib import Path
from xml.sax.saxutils import escape

BASE_URL = "https://checkmyskip.co.uk"
ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "tools", "screenshots", "assets"}


def lastmod_for(path: Path) -> str:
    """Prefer the last git commit date (YYYY-MM-DD); fall back to file mtime."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", str(path.relative_to(ROOT))],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        date = (result.stdout or "").strip()
        if result.returncode == 0 and date:
            return date
    except OSError:
        pass
    stamp = dt.datetime.fromtimestamp(path.stat().st_mtime, tz=dt.timezone.utc)
    return stamp.date().isoformat()


def page_url(rel: Path) -> str:
    posix = rel.as_posix()
    if posix == "index.html":
        return f"{BASE_URL}/"
    return f"{BASE_URL}/{posix}"


def iter_html_pages() -> list[Path]:
    pages: list[Path] = []
    for path in ROOT.rglob("*.html"):
        rel = path.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        pages.append(rel)
    pages.sort(key=lambda p: (p.as_posix() != "index.html", p.as_posix()))
    return pages


def build() -> str:
    urls = []
    for rel in iter_html_pages():
        loc = escape(page_url(rel))
        lastmod = lastmod_for(ROOT / rel)
        urls.append(
            "  <url>\n"
            f"    <loc>{loc}</loc>\n"
            f"    <lastmod>{lastmod}</lastmod>\n"
            "  </url>"
        )
    body = "\n".join(urls)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{body}\n"
        "</urlset>\n"
    )


def main() -> int:
    xml = build()
    out = ROOT / "sitemap.xml"
    out.write_text(xml, encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)} with {xml.count('<url>')} URL(s).", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
