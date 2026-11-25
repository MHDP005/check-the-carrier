# Check the Carrier

Version one of an independent UK directory for licensed skip hire, skip bags and junk/man-and-van removal.

Built as a static HTML/CSS site. No build step. No live affiliate links.

## Pages

- `/index.html` — home
- `/guides/check-a-waste-carrier.html` — how to check a waste carrier is licensed
- `/guides/skip-vs-skip-bag-vs-man-and-van.html` — comparison guide
- `/guides/skip-sizes.html` — skip size guide (published figures checked 21 November 2026)
- `/guides/what-cant-go-in-a-skip.html` — what you can’t put in a skip, and the legal route for each item (sources checked 23 November 2026)
- `/guides/skip-permits.html` — when a skip on the highway needs a council permit, who applies, and published fees/timescales for Slough, RBWM, Surrey, Hillingdon and Buckinghamshire (sources checked 25 November 2026)
- `/areas/slough.html` — first local page for Slough and Langley
- `/areas/windsor.html` — local page for Windsor (listings verified 20 November 2026)
- `/areas/maidenhead.html` — local page for Maidenhead, Cookham and SL6 (listings verified 22 November 2026)
- `/areas/staines.html` — local page for Staines-upon-Thames, Spelthorne and TW18 (listings verified 24 November 2026)

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

## Live site

The site is published on GitHub Pages at [https://checkmyskip.co.uk/](https://checkmyskip.co.uk/). The previous project URL, `https://mhdp005.github.io/check-the-carrier/`, should redirect once the custom domain is attached.

## Search engines

- `sitemap.xml` lists every HTML page with an absolute URL under `https://checkmyskip.co.uk/`.
- `robots.txt` sits at the domain root and points crawlers at that sitemap, so Google will honour it once the custom domain is serving the site.
