# -*- coding: utf-8 -*-
"""Istanbul 2027 programme PDF. Run from sites/istanbul-2027 with the istanbul preview on
http://localhost:8012; writes _tmp_pdf.html for Chrome to print. Same measured
pagination and masthead as the Athens generator, in Istanbul's ink and turquoise;
data comes from istanbul_programme.py."""
import sys, re, json, subprocess, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import istanbul_programme as P

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
MM = 3.7795275591  # px per mm at 96dpi
BASE = "http://localhost:8012"

CSS = """
@page{size:A4;margin:0}
*{box-sizing:border-box}
:root{--navy:#0E1E22;--navy-d:#060F11;--ac:#0A6E80;--ac-br:#0E8FA0;
  --ice2:#EDF7F9;--muted:#444E55;--ink:#1F2B30;--line:rgba(14,30,34,.12)}
html,body{margin:0;padding:0;background:#FBFAF6;color:var(--ink);
  font-family:"Onest",system-ui,-apple-system,sans-serif;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}
.sheet{position:relative;width:210mm;height:297mm;overflow:hidden;page-break-after:always;background:#FBFAF6}
.sheet:last-child{page-break-after:auto}

.mast{position:relative;height:46mm;overflow:hidden;
  background:linear-gradient(100deg,#FBFAF6 0%,#EEF7F9 42%,#D9EFF4 100%)}
.mast .art{position:absolute;right:0;top:0;height:46mm;width:auto;
  -webkit-mask-image:linear-gradient(to right,transparent 0,#000 26%);
          mask-image:linear-gradient(to right,transparent 0,#000 26%)}
.mast .logo{position:absolute;right:62mm;top:7mm;width:14mm}
.mast-in{position:relative;z-index:3;padding:7mm 0 0 14mm;max-width:118mm}
.eyebrow{margin:0 0 2.4mm;font-size:7.6pt;font-weight:800;letter-spacing:.16em;text-transform:uppercase;
  color:var(--navy);padding-bottom:1.5mm;border-bottom:1px solid rgba(14,143,160,.6);display:inline-block}
.mast h1{margin:0;color:var(--navy);font-size:17pt;font-weight:800;letter-spacing:-.02em;line-height:1.13}
.mast h1 .l2{display:block;font-size:12.5pt}
.mast h1 .l3{display:block;font-size:12.5pt;font-weight:400}
.mast-meta{position:absolute;left:14mm;bottom:4mm;z-index:3;display:flex;gap:11mm;
  font-size:7.6pt;font-weight:700;color:var(--ac);letter-spacing:.03em}
.mast-meta span:nth-child(2),.mast-meta span:nth-child(3){color:var(--muted);font-weight:600}
.dash{font-style:normal;display:inline;font-weight:400;font-size:.72em;vertical-align:.06em;margin:0 .06em;opacity:.7}

.rh{height:14mm;background:var(--navy);color:#fff;display:flex;align-items:center;
  justify-content:space-between;padding:0 14mm;font-size:7.6pt;font-weight:700;
  letter-spacing:.12em;text-transform:uppercase}
.rh span:last-child{color:#E3C078}

.body{padding:8mm 14mm 0}
h2.sec{margin:0 0 4.5mm;color:var(--navy);font-size:13pt;font-weight:800;text-transform:uppercase;
  padding-bottom:2.2mm;border-bottom:2px solid var(--navy)}
h3.sub{margin:5mm 0 2.6mm;color:var(--ac);font-size:7.6pt;font-weight:800;letter-spacing:.16em;
  text-transform:uppercase;padding-bottom:1.4mm;border-bottom:1px solid var(--line)}

.sum{display:grid;grid-template-columns:repeat(4,1fr);gap:2.6mm;margin:0 0 5mm}
.sum div{background:var(--ice2);border-left:1.1mm solid var(--ac-br);border-radius:0 1.4mm 1.4mm 0;padding:2.6mm 3mm}
.sum b{display:block;color:var(--navy);font-size:12pt;font-weight:800;letter-spacing:-.02em;line-height:1}
.sum span{display:block;color:var(--navy);font-weight:700;font-size:7.2pt;margin-top:1.4mm}
.sum em{display:block;font-style:normal;color:var(--muted);font-size:6.4pt;margin-top:.6mm;line-height:1.3}

.day{display:flex;align-items:center;gap:4mm;background:var(--navy);color:#fff;
  border-radius:1.6mm;padding:2.2mm 4mm 2.2mm 2.4mm;margin:0 0 4mm}
.day .cal{flex:none;display:flex;flex-direction:column;width:11.5mm;text-align:center;background:#fff;
  border-radius:1.2mm;overflow:hidden}
.day .cal i{font-style:normal;background:var(--ac-br);color:#fff;font-size:5.4pt;font-weight:800;
  letter-spacing:.14em;text-transform:uppercase;padding:.5mm 0}
.day .cal b{font-size:13pt;font-weight:800;color:var(--navy);line-height:1;padding:.9mm 0 .1mm;letter-spacing:-.03em}
.day .cal em{font-style:normal;font-size:5.2pt;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
  color:var(--muted);padding-bottom:.8mm}
.day .dl{display:flex;flex-direction:column;gap:1mm}
.day .dl > b{font-size:11pt;font-weight:800;line-height:1}
.day .dm{display:flex;align-items:center;gap:2.4mm;font-size:7.6pt;color:#CFE9EE}
.day .dm strong{color:#fff;font-weight:700}
.day .sep{width:1mm;height:1mm;border-radius:50%;background:#E3C078}

/* one session per row: time on the left, everything else in a single column */
.slot{display:grid;grid-template-columns:24mm 1fr;gap:4mm;padding:2.6mm 0 3mm;
  border-bottom:.3mm solid var(--line)}
.slot .t{font-size:8pt;font-weight:800;color:var(--ac);line-height:1.25;white-space:nowrap}
.slot .t em{display:block;font-style:normal;font-size:6.2pt;font-weight:700;letter-spacing:.08em;
  text-transform:uppercase;color:var(--muted);margin-top:.6mm}
.slot .ttl{font-size:9.5pt;font-weight:800;color:var(--navy);letter-spacing:-.01em;line-height:1.3}

/* talks read straight down, numbered, with the speaker in its own column */
ul.talks{list-style:none;margin:2mm 0 0;padding:0}
ul.talks li{display:grid;grid-template-columns:5mm 1fr 38mm;gap:2mm;align-items:baseline;
  padding:1mm 0;border-bottom:.25mm solid rgba(14,30,34,.07)}
ul.talks li:last-child{border-bottom:0}
ul.talks .n{font-size:6.6pt;font-weight:800;color:var(--ac-br);text-align:right;
  font-variant-numeric:tabular-nums}
ul.talks .tx{font-size:7.8pt;color:var(--ink);line-height:1.35}
ul.talks .sp{font-size:7.2pt;font-weight:700;color:var(--navy);line-height:1.35}


/* the format note is context, so it sits under the talks, not beside them */
.fmt{margin:1.2mm 0 0;font-size:7.4pt;color:var(--muted);line-height:1.45}
.fmt-l{font-size:6.4pt;font-weight:800;letter-spacing:.13em;text-transform:uppercase;
  color:var(--ac);margin-right:2mm}

.slot.brk{grid-template-columns:24mm 1fr;background:var(--ice2);padding:1.8mm 0}
.slot.brk .ttl{font-weight:600;color:var(--muted);font-size:8.4pt}
.slot.brk .t{color:var(--muted)}

.fac{display:grid;grid-template-columns:repeat(4,1fr);gap:2.2mm}
.fac div{border:.3mm solid var(--line);border-radius:1.4mm;padding:2.4mm 2.8mm;background:#FBFAF6}
.fac b{display:block;color:var(--navy);font-size:7.8pt;font-weight:700;line-height:1.3}
.fac span{display:block;color:var(--muted);font-size:6.4pt;font-weight:700;letter-spacing:.1em;
  text-transform:uppercase;margin-top:.7mm}
.fac.inv div{background:var(--ice2);border-color:rgba(14,143,160,.35)}
.note{margin:4mm 0 0;font-size:6.9pt;color:var(--muted)}
.foot{position:absolute;left:0;right:0;bottom:0;height:10mm;background:var(--navy-d);
  color:rgba(255,255,255,.72);display:flex;align-items:center;justify-content:space-between;
  padding:0 14mm;font-size:6.6pt}
.foot b{color:#fff;font-weight:700}

/* Athens: several labelled lines per session (moderators, format) and a discussion note under the talks */
.slot .fmt + .fmt{margin-top:.6mm}
.disc{margin:1.6mm 0 0;font-size:7.1pt;color:var(--muted);line-height:1.45;padding-top:1.2mm;border-top:.25mm dashed rgba(14,30,34,.14)}
.disc .fmt-l{color:var(--ac)}
.mast .art{-webkit-mask-image:linear-gradient(to right,transparent 0,#000 34%);mask-image:linear-gradient(to right,transparent 0,#000 34%)}

/* masthead: the ESSKA logo leads the eyebrow on one line, as the site header pairs the
   logo with the meeting name, and the artwork gets a wider, full-height panel on the
   right instead of a narrow strip */
.mast{height:54mm}
.mast-in{padding-top:6.5mm}
.mast-brand{display:flex;align-items:center;gap:3.4mm;margin:0 0 3.6mm}
.mast-brand img{width:12.5mm;height:auto;display:block}
.mast-brand i{display:block;width:.3mm;height:9mm;background:rgba(14,30,34,.25)}
.mast-brand .eyebrow{margin:0;padding:0;border:0}
.mast .art{height:54mm;width:96mm;object-fit:cover;object-position:58% 40%;
  -webkit-mask-image:linear-gradient(to right,transparent 0,#000 30%);mask-image:linear-gradient(to right,transparent 0,#000 30%)}
.mast-meta{bottom:5mm}
"""

def times(rng):
    return [x.strip() for x in rng.split("&ndash;")] if rng != "TBC" else None

def split_speaker(t):
    m = re.search(r"\s*<i>(.*?)</i>\s*$", t)
    return (t[:m.start()].strip(), m.group(1)) if m else (t.strip(), "")

def slot_html(item):
    rng, dur, title, talks, note, brk = item
    t = times(rng)
    when = f"{t[0]} to {t[1]}" if t else "Time TBC"
    if brk:
        return (f'<div class="slot brk"><div class="t">{when}</div>'
                f'<div><div class="ttl">{title} &middot; {dur}</div></div></div>')
    body = f'<div class="ttl">{title}</div>'
    if note:
        lbl, sep, txt = note.partition("|")
        body += (f'<p class="fmt"><span class="fmt-l">{lbl}</span>{txt}</p>' if sep
                 else f'<p class="fmt">{note}</p>')
    if talks:
        body += '<ul class="talks">' + "".join(
            f'<li><span class="n">{i}</span><span class="tx">{tx}</span><span class="sp">{sp}</span></li>'
            for i, (tx, sp) in enumerate((split_speaker(x) for x in talks), 1)) + '</ul>'
    sub = f"<em>{dur}</em>" if dur else "<em>to be confirmed</em>"
    return f'<div class="slot"><div class="t">{when}{sub}</div><div>{body}</div></div>'

def banner(label, day, dnum, wk):
    num, full, span, items = day
    a0, b0 = times(span)
    nses = sum(1 for i in items if not i[5] and i[0] != "TBC")
    ntalks = sum(len(i[3]) for i in items if not i[5])
    return (f'<div class="day"><span class="cal"><i>Sep</i><b>{dnum}</b><em>{wk}</em></span>'
            f'<span class="dl"><b>{label}</b><span class="dm"><strong>{a0} to {b0}</strong>'
            f'<span class="sep"></span>{nses} sessions<span class="sep"></span>{ntalks} talks</span></span></div>')

D = '10<i class="dash">&ndash;</i>11 September 2027'
VENUE = "Ac&#305;badem Altunizade Hospital"
FOOT = (f'<div class="foot"><span><b>ESSKA Shoulder Focus Meeting</b> &nbsp;|&nbsp; {VENUE}, Istanbul &nbsp;|&nbsp; {D}</span>'
        '<span>Preliminary programme, subject to change</span></div>')
MAST = f"""<div class="mast"><img class="art" src="assets/img/key-visual-istanbul.jpg" alt="">
<div class="mast-in"><div class="mast-brand"><img src="assets/img/logo-02.png" alt="ESSKA"><i></i><p class="eyebrow">ESSKA Shoulder Focus Meeting</p></div>
<h1>Massive Rotator Cuff Tears<span class="l3">From repair to replace</span></h1></div>
<div class="mast-meta"><span>{D}</span><span>{VENUE}</span><span>Istanbul, Turkey</span></div></div>"""
RH = f'<div class="rh"><span>Massive Rotator Cuff Tears</span><span>Istanbul &middot; {D}</span></div>'
SUMMARY = [("1.5 days","Scientific programme","Friday and Saturday morning"),
           ("6","Scientific sessions","plus the grand finale debate"),
           ("4","Relive surgical videos","on day one"),
           ("TBC","CME credits","details to follow")]
summary = "".join(f"<div><b>{v}</b><span>{l}</span><em>{s}</em></div>" for v, l, s in SUMMARY)
def fac(people, extra=""):
    return (f'<div class="fac{extra}">' + "".join(
        f"<div><b>{n}</b>{f'<span>{c}</span>' if c else ''}</div>" for n, c in people) + "</div>")

HEAD = ('<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        '<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700;800&display=swap" rel="stylesheet">'
        '<title>ESSKA Shoulder Focus Meeting 2027 - Programme</title><style>' + CSS + '</style></head><body>')

blocks = []
blocks.append(("banner", banner("Day one", P.DAY1, 10, "Fri")))
for it in P.DAY1[3]:
    blocks.append(("slot", slot_html(it)))
blocks.append(("banner", banner("Day two", P.DAY2, 11, "Sat")))
for it in P.DAY2[3]:
    blocks.append(("slot", slot_html(it)))
# ---- measure each block at the real content width ----
measure = (HEAD + '<div class="sheet"><div class="body" id="m">' +
           "".join(f'<div class="probe">{h}</div>' for _, h in blocks) +
           '</div></div><script>addEventListener("load",function(){setTimeout(function(){'
           'var out=[].slice.call(document.querySelectorAll("#m > .probe")).map(function(e){'
           'return Math.round(e.getBoundingClientRect().height)});'
           'document.title="H:"+JSON.stringify(out);},800)});</script></body></html>')
pathlib.Path("_measure.html").write_text(measure, encoding="utf-8")
dom = subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
                      "--virtual-time-budget=6000", "--window-size=794,1123",
                      "--dump-dom", BASE + "/_measure.html"],
                     capture_output=True, text=True).stdout
m = re.search(r"H:(\[[0-9,\s]*\])", dom)
if not m:
    # never paginate on guesses: a dead server here once produced a PDF of a 404 page
    raise SystemExit("MEASURE FAILED: is the istanbul preview on :8012 running? No PDF source written.")
heights = json.loads(m.group(1))
if len(heights) != len(blocks) or min(heights) < 10:
    raise SystemExit(f"MEASURE SUSPECT: got {heights}. No PDF source written.")
pathlib.Path("_measure.html").unlink(missing_ok=True)

# ---- fill pages by real height ----
FIRST = 297 - 54 - 8 - 13 - 26 - 10 - 4      # mast, pad, section head, summary, footer, slack
CONT  = 297 - 14 - 8 - 10 - 4                # running header, pad, footer, slack
# how many pages the content actually needs
def cap_of(i): return (FIRST if i == 0 else CONT) * MM

# Each day starts on a fresh page: split the blocks at every day banner after
# the first, then paginate each day on its own.
segs, cur = [], []
for i, (kind, _) in enumerate(blocks):
    if kind == "banner" and cur:
        segs.append(cur); cur = []
    cur.append(i)
segs.append(cur)

def greedy_pages(idxs, start):
    """How many pages this day needs if each page is filled to capacity."""
    n, used = 1, 0.0
    for i in idxs:
        if used and used + heights[i] > cap_of(start + n - 1):
            n += 1; used = 0.0
        used += heights[i]
    return n

def paginate(idxs, start, npages):
    """Even out the fill within one day: each page aims for whatever is left
    divided by the pages left, but never goes past its real capacity."""
    pages, k, remaining = [], 0, float(sum(heights[i] for i in idxs))
    while k < len(idxs):
        p = len(pages)
        cap = cap_of(start + p)
        target = min(cap, remaining / max(1, npages - p))
        cur, used = [], 0.0
        while k < len(idxs):
            h = heights[idxs[k]]
            if cur and used + h > cap: break                     # hard page limit
            # Istanbul's sessions are long blocks, so evening out the fill left the first
            # page half empty: fill each page to capacity instead
            cur.append(blocks[idxs[k]][1]); used += h; remaining -= h; k += 1
        pages.append(cur)
    return pages

pages = []
for seg in segs:
    start = len(pages)
    n = greedy_pages(seg, start)
    day = paginate(seg, start, n)
    if len(day) > n:               # balancing must never cost an extra page
        day = paginate(seg, start, len(day))
    pages += day

sheets = []
for i, page in enumerate(pages):
    if i == 0:
        sheets.append(f'<div class="sheet">{MAST}<div class="body">'
                      f'<h2 class="sec">Scientific Programme</h2><div class="sum">{summary}</div>'
                      + "".join(page) + f'</div>{FOOT}</div>')
    else:
        sheets.append(f'<div class="sheet">{RH}<div class="body">' + "".join(page)
                      + f'</div>{FOOT}</div>')
sheets.append(f'<div class="sheet">{RH}<div class="body"><h2 class="sec">Faculty</h2>'
              f'<h3 class="sub">Chairs</h3>{fac(P.CHAIRS," inv")}'
              f'<h3 class="sub">Proposed speakers</h3>{fac(P.PROPOSED)}'
              f'<p class="note">Preliminary programme, subject to change. Session moderators will be announced, and faculty '
              f'participation, lecture scheduling and programme details remain subject to confirmation.</p>'
              f'</div>{FOOT}</div>')

pathlib.Path("_tmp_pdf.html").write_text(HEAD + "".join(sheets) + "</body></html>", encoding="utf-8")
print(f"measured {len(heights)} blocks -> {len(pages)} schedule pages + 1 faculty = {len(sheets)} total")
