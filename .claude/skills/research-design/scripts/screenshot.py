#!/usr/bin/env python3
"""Screenshot one or more URLs for design research.

Captures a full-page PNG per URL so the caller can Read them and actually see
the design. Screenshots are written to the system temp dir by default so they
never land in the repo (web.md: never commit screenshots).

Usage:
    python3 screenshot.py URL [URL ...] [--out DIR] [--width 1280] [--height 900]

Each saved path is printed on its own line.
"""
import argparse
import os
import re
import sys
import tempfile
from urllib.parse import urlparse


def slugify(url):
    parsed = urlparse(url)
    base = (parsed.netloc + parsed.path).strip("/")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", base).strip("-").lower()
    return slug or "page"


def main():
    parser = argparse.ArgumentParser(description="Screenshot URLs for design research.")
    parser.add_argument("urls", nargs="+", help="One or more URLs to capture")
    parser.add_argument(
        "--out",
        default=os.path.join(tempfile.gettempdir(), "research-design"),
        help="Output directory (default: a research-design folder in the system temp dir)",
    )
    parser.add_argument("--width", type=int, default=1280, help="Viewport width")
    parser.add_argument("--height", type=int, default=900, help="Viewport height")
    parser.add_argument("--wait", type=int, default=2500, help="ms to wait after load")
    args = parser.parse_args()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sys.exit(
            "Playwright not installed. Run:\n"
            "  pip install playwright && playwright install chromium"
        )

    os.makedirs(args.out, exist_ok=True)
    saved = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        for i, url in enumerate(args.urls):
            page = browser.new_page(viewport={"width": args.width, "height": args.height})
            try:
                page.goto(url, wait_until="networkidle", timeout=30000)
            except Exception:
                # networkidle can hang on busy/ad-heavy sites; fall back to load.
                page.goto(url, wait_until="load", timeout=30000)
            page.wait_for_timeout(args.wait)
            path = os.path.join(args.out, f"{i:02d}-{slugify(url)}.png")
            page.screenshot(path=path, full_page=True)
            page.close()
            saved.append(path)
            print(path)
        browser.close()

    if not saved:
        sys.exit("No screenshots captured.")


if __name__ == "__main__":
    main()
