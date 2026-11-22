# Check the Carrier

Version one of an independent UK directory for licensed skip hire, skip bags and junk/man-and-van removal.

Built as a static HTML/CSS site. No build step. No live affiliate links.

## Pages

- `/index.html` — home
- `/guides/check-a-waste-carrier.html` — how to check a waste carrier is licensed
- `/guides/skip-vs-skip-bag-vs-man-and-van.html` — comparison guide
- `/guides/skip-sizes.html` — skip size guide (published figures checked 21 November 2026)
- `/areas/slough.html` — first local page for Slough and Langley
- `/areas/windsor.html` — local page for Windsor (listings verified 20 November 2026)
- `/areas/maidenhead.html` — local page for Maidenhead, Cookham and SL6 (listings verified 22 November 2026)

## Preview locally

From this directory:

```bash
python3 -m http.server 4173
```

Then open http://127.0.0.1:4173/

## Screenshots

Full-page PNGs of the home and Slough pages are in `screenshots/`.

## Listings

Local listings were verified on 19 November 2026 against the Environment Agency public register and each company’s website. Always re-check before hiring.

## Publishing a new page

After adding or editing a page, regenerate the sitemap before you commit:

```bash
python3 tools/build_sitemap.py
```

The nightly routine must run that script so `sitemap.xml` stays complete.

## Search engines

- `sitemap.xml` lists every HTML page with an absolute URL under `https://mhdp005.github.io/check-the-carrier/`.
- `robots.txt` points crawlers at that sitemap. Google only reads `robots.txt` at the site root (`https://mhdp005.github.io/robots.txt`), not at a project subpath, so this file will not control crawling while the site is served from `/check-the-carrier/`. The sitemap can still be submitted in Google Search Console.
- Once the site has its own domain, move `robots.txt` to that domain root so Google will honour it.
