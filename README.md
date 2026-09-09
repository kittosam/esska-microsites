# ESSKA focus meeting microsites

Standalone microsites for ESSKA focus meetings. One folder per event under
`sites/`, each deployed as its own Netlify site.

| Event | Folder | Dates | Live URL |
|---|---|---|---|
| Revision Knee Arthroplasty and PJI, Rome | `sites/rome-2027` | 8–9 Oct 2027 | _add once deployed_ |

## Working on a site

Everything is plain HTML, CSS and JS. There is no build step and nothing to
install. To preview a site locally:

```bash
cd sites/rome-2027
python3 -m http.server 8000
```

Then open http://localhost:8000

## Deploying

Each site folder is connected to its own Netlify site:

1. Netlify → Add new site → Import from GitHub → pick this repo
2. Site configuration → Build & deploy → Base directory: `sites/<event-slug>`
3. Publish directory: `sites/<event-slug>`
4. Build command: leave empty

Netlify then rebuilds that site whenever you push to `main`. Pull requests get
their own preview URL, which is useful for sending a draft to the client before
it goes live.

## Starting a new event site

Copy the most recent site folder and replace its content:

```bash
cp -r sites/rome-2027 sites/<new-event-slug>
```

Delete the photos that don't apply, keep the ESSKA logos, then work through the
checklist at the bottom of `CLAUDE.md`.

## Notes

`CLAUDE.md` holds the project conventions and is read automatically by Claude
Code. Update it when a convention changes, so it stays the single source of
truth rather than drifting.
