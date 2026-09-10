# ESSKA focus meeting microsites

Six standalone microsites, one per ESSKA focus meeting. Each is a one-off: it goes
live before its event and is not maintained afterwards. The client is ESSKA
(esska.org), a non-profit professional society.

## Repo layout

```
sites/<event-slug>/       one deployable site, fully self-contained
  index.html              all markup and page content
  assets/css/styles.css   all styles
  assets/js/app.js        all behaviour
  assets/img/             images
  netlify.toml            deploy config for this site
_template/                copy this to start a new event site
```

Each site folder is deployed as its own Netlify site, with the Netlify "base
directory" set to `sites/<event-slug>`. That means **every site folder must be
self-contained** — no relative paths that reach outside the folder, or the files
won't be published.

Sites deliberately duplicate CSS and JS rather than sharing it. They are one-off
sites with different content and no post-event maintenance, so a shared build step
would add more risk than it removes. If a fix genuinely needs to land in all six,
apply it folder by folder across the repo.

## How the pages work

Each site is one HTML file behaving like a small single-page site. `PAGES` in
`app.js` lists the section ids; `go(id)` shows one and hides the rest. Nav links
use `data-go="<id>"`. Sections are: welcome, programme, venue, registration,
industry, contacts.

Other behaviour in `app.js`:
- `.rv` elements fade in on scroll via IntersectionObserver — add the class to
  animate something, don't write new observers.
- `[data-to="<number>"]` counts up to that number when scrolled into view.
- Programme day tabs are `.tabs button` with `data-day="1"` / `data-day="2"`,
  toggling `#day1` / `#day2`.
- Two dates near the bottom of `app.js` drive the countdowns:
  `MEETING_START` and `EARLY_RATE`. These change per event.

## Conventions

- Plain HTML, CSS and JS. No framework, no build step, no package manager.
- Design tokens are CSS custom properties in `:root` at the top of `styles.css`
  (`--navy`, `--blue`, `--ice`, `--ink`, `--muted`, `--line`, `--f`, `--pad`).
  Use them rather than hard-coded colours.
- Font is Onest, loaded from Google Fonts (chosen for readable body text and clear figures).
- Never inline images as base64 data URIs. Save them into `assets/img/` and link
  them. The original version of this site was a single 2 MB file for that reason.
- Images: photos as `.jpg`, logos and anything needing transparency as `.png`.
  Keep photos under roughly 1300px wide.
- British English in page copy. Content is English only.
- Every site must link back to esska.org.

## Things to check before a site goes live

- `MEETING_START` and `EARLY_RATE` match the real dates for that event.
- Page `<title>` and the hero heading name the right meeting and city.
- Registration rates, venue, chairs and faculty are the ones ESSKA supplied.
- Links to esska.org and the hotel booking page resolve.
- Reduced-motion is respected — the `prefers-reduced-motion` block in
  `styles.css` should not be removed.
