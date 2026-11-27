# Check My Skip

Version one of an independent UK directory for licensed skip hire, skip bags and junk/man-and-van removal.

Built as a static HTML/CSS site. No live affiliate links. One small Python script (`tools/build_site.py`, standard library only) keeps the shared header, nav, footer, home-page cards and sitemap in sync.

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
- `/areas/uxbridge.html` — local page for Uxbridge, Hillingdon and UB8/UB10, with Hillingdon skip permits and Harefield Civic Amenity Site rules (listings verified 26 November 2026)
- `/credits.html` — photo credits and licences (generated from `tools/site.json`)

## Preview locally

From this directory:

```bash
python3 -m http.server 4173
```

Then open http://127.0.0.1:4173/

## Screenshots

`screenshots/` is git-ignored and only holds local preview PNGs. Each page's `og:image` now points at its own photo in `assets/img/`.

## Listings

Local listings were verified on 19 November 2026 against the Environment Agency public register and each company’s website. Always re-check before hiring.

## Publishing a new page (nightly routine)

1. **Copy a template**: `tools/templates/area-page.html` → `areas/<town>.html`, or `tools/templates/guide-page.html` → `guides/<slug>.html`. Replace every `{{...}}` placeholder and delete the template comment at the top. Leave `<!-- SITE HEADER --><!-- /SITE HEADER -->` and the `<!-- SITE FOOTER -->` block in place: the build fills them. Only edit the `<div class="disclosure">` text inside the footer (council names, "Last reviewed" date).
2. **Register the page in `tools/site.json`**: add an object to `"areas"` (`path`, `name` for the nav, `card_title`, `blurb` of under 90 characters, `postcodes`, `image` or `null`) or to `"guides"` (`path`, `name`, `card_title`, `blurb`, `icon` from `assets/icons.svg`, `image` or `null`). That one entry adds the page to the nav, footer, home-page cards and area picker on every page.
3. **Build and validate**: `python3 tools/build_site.py`. It rewrites the shared chrome on all pages, regenerates `sitemap.xml`, and exits non-zero on invalid JSON-LD, a missing canonical, a missing `AFFILIATE CTA SLOT`, a broken local link or a missing image. Fix any error before committing. `python3 tools/build_site.py --check` validates without writing.
4. Commit and push. (`python3 tools/build_sitemap.py` still works on its own, but `build_site.py` already runs it.)

### Writing style for every page

- Plain English for homeowners. One idea per paragraph, about 2 sentences (300 characters max).
- Start with **Quick answer** (1–2 sentences) and **Key facts** (4–5 bullets, each with a figure). Only use facts that appear, with their source, lower down the page.
- One `<section class="block">` per H2, with an icon. Show the first 1–2 short paragraphs; put longer detail in `<details class="more"><summary>Show the full detail</summary><div class="more-body">…</div></details>`.
- Two-column "situation / what the council says" tables become fact cards (`.fact-cards-block`). Wider comparison tables use `<table class="stack">` with `data-label` on each `<td>`.
- Carrier listings are `.listing` cards with the green `badge-licence` ("Licence checked D Mon YYYY"), a one-sentence `.teaser`, prices and detail in a collapsed `details.more`, the registration line in `p.reg`, and the two buttons.
- Keep every fact and every source; collapse, don't delete. Sources go in `<details class="sources-box">` at the end, with the count in the summary.
- Keep the `AFFILIATE CTA SLOT` comment and `aside.cta-placeholder` on every page. No live affiliate links until a deal is agreed and disclosed.

## Design system

All styles are in `assets/styles.css` (mobile-first, one font: Nunito). Icons are an SVG sprite in `assets/icons.svg`: `<svg class="icon" aria-hidden="true" focusable="false"><use href="../assets/icons.svg#i-check"/></svg>`.

| Component | Markup |
| --- | --- |
| Page hero | `section.page-hero > .wrap.page-hero-grid` with breadcrumb, `p.kicker`, `h1`, `p.lead`, `ul.chip-row`, `figure.hero-photo` |
| Quick answer | `div.callout.callout-quick` with `p.callout-title` |
| Key facts | `div.key-facts > h2 + ul.fact-list > li > span.icon-bubble + span` |
| Callouts | `callout-watch` (coral, "Watch out"), `callout-tip` (green), `callout-note` (blue) |
| Section card | `section.block > h2.block-title > span.icon-bubble[.sun/.coral/.sky] + span` |
| Collapsible detail | `details.more > summary + div.more-body` |
| Icon card grid | `div.item-grid > section.block.item-card`, or `div.card-grid > article.card` |
| Fact cards | `div.fact-cards-block > p.fact-cards-caption + div.fact-cards > div.fact-card` |
| Checklist | `ol.steps` (numbered) or `ul.checklist` (ticks) |
| Skip sizes | `div.size-grid > div.size-card` (inline SVG skip, `p.size-bags`, `p.size-heavy.yes/.no`) |
| Carrier card | `div.listings > article.listing` (see template) |
| Affiliate slot | `<!-- AFFILIATE CTA SLOT: … -->` + `aside.cta-placeholder` |
| Sources | `details.sources-box` |

Generated blocks (do not edit by hand): `<!-- GENERATED:area-cards -->`, `area-options`, `area-links`, `guide-cards`, `photo-credits`, plus the `SITE HEADER` and `SITE FOOTER` blocks.

## Photos

- Only photos whose licence allows commercial reuse (CC0, CC BY, CC BY-SA, Unsplash or Pexels licence). Download them into `assets/img/`; never hotlink.
- Save each photo as `<slug>-<width>.webp` for every width and `<slug>-<smallest width>.jpg` as the fallback (3:2 crop, 640 and 1200 wide; the home hero is 16:9 at 800 and 1600). Quality about 70; keep each file under about 150 KB.
- Add the photo to `"images"` in `tools/site.json` with `alt`, `author`, `licence`, `licence_url`, `source_url`, `source_name`, `changes` (e.g. "cropped and resized"), `widths` and `ratio`. `credits.html` is built from that list.
- Show the credit under the photo (`figcaption`) when the licence requires attribution (CC BY and CC BY-SA do).
- Photos must not show, or look like an endorsement of, a listed firm. No photo? Use `assets/img/illustration-skips.svg`.

## Live site

The site is published on GitHub Pages at [https://checkmyskip.co.uk/](https://checkmyskip.co.uk/). The previous project URL, `https://mhdp005.github.io/check-the-carrier/`, should redirect once the custom domain is attached.

## Search engines

- `sitemap.xml` lists every HTML page with an absolute URL under `https://checkmyskip.co.uk/`.
- `robots.txt` sits at the domain root and points crawlers at that sitemap, so Google will honour it once the custom domain is serving the site.
