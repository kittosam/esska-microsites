# Tools

Dev-only scripts. They are never served: the published site is the `sites/<slug>`
folder itself, so nothing here is copied into a deploy.

| Script | What it does |
|---|---|
| `rome_programme.py` | Rome 2027 programme data (days, sessions, talks, faculty) |
| `rome_site_programme.py` | Regenerates the Rome programme markup inside `index.html` |
| `rome_pdf.py` | Builds the Rome programme PDF |
| `athens_programme.py` | Athens 2027 programme data and the site markup generator |
| `athens_pdf.py` | Builds the Athens programme PDF |

## Building a programme PDF

The generators measure the real height of every row in a browser before
paginating, so the local preview for that site must be running:

```bash
# Rome, preview on :8010
cd sites/rome-2027 && python3 ../../tools/rome_pdf.py
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
  --no-pdf-header-footer --print-to-pdf=assets/ESSKA-Rome-2027-Programme.pdf \
  "http://localhost:8010/_tmp_pdf.html" && rm -f _tmp_pdf.html
```

Athens is the same with `athens_pdf.py`, port 8011 and the Athens PDF name.
If the measuring step cannot reach the preview it stops rather than guessing,
because a dead server once produced a PDF of a 404 page.
