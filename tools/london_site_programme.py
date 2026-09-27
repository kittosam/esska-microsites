# -*- coding: utf-8 -*-
"""Writes London's programme, faculty and skills lab lists into its index.html,
between the <!-- name --> and <!-- /name --> markers.
Run from sites/london-2027:  python3 ../../tools/london_site_programme.py"""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import london_programme as data

def mins(a, b):
    f = lambda s: (lambda h, m: h*60+m)(*map(int, s.split(":")))
    return f(b) - f(a)

def slot(rng):
    if "|" not in rng:
        return f'<span class="ptime"><span class="pstart">{rng}</span></span>'
    a, b = rng.split("|")
    return f'<span class="ptime"><span class="pstart">{a}</span><span class="pdur">{mins(a,b)} min</span></span>'

def dash(rng):
    return rng.replace("|", "&ndash;")

def head(title, sub, mods, label="Moderators"):
    out = f'<span class="ptitle">{title}</span>'
    if sub:
        out += f'<span class="psub">{sub}</span>'
    if mods:
        out += (f'<span class="psub psub-note"><span class="pnote-l">{label}</span>'
                f'<span class="pnote-t">{mods}</span></span>')
    return out

ICON = {
 "clock": '<svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="7.5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M10 5.8V10l2.8 1.8" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
 "list": '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 5.5h12M4 10h12M4 14.5h8" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
 "mic": '<svg viewBox="0 0 20 20" aria-hidden="true"><rect x="7.2" y="2.8" width="5.6" height="9" rx="2.8" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M4.8 9.6a5.2 5.2 0 0 0 10.4 0M10 14.8v2.6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
}

def rows():
    out = []
    for rng, title, sub, mods, talks, kind in data.PROGRAMME:
        if kind != "session":
            label = "Speakers" if kind == "static" else "Moderators"
            out.append(
f'''          <div class="prow{" break" if kind == "break" else ""}" data-day="1">
            <div class="prow-static">
              {slot(rng)}
              <span class="pmain-head">{head(title, sub, mods, label)}</span>
            </div>
          </div>''')
            continue
        lis = "".join(
            f'<li class="ptalk"><span class="ptt">{dash(t)}</span><span class="ptx">{tx}</span>'
            f'<span class="psp">{sp}</span></li>' for t, tx, sp in talks)
        out.append(
f'''          <div class="prow" data-day="1">
            <button class="prow-btn" type="button" aria-expanded="false">
              {slot(rng)}
              <span class="pmain-head">{head(title, sub, mods)}</span>
              <span class="pchev" aria-hidden="true"></span>
            </button>
            <div class="ptalks-wrap" hidden>
              <ul class="ptalks timed">{lis}</ul>
            </div>
          </div>''')
    return "\n".join(out)

def day():
    sessions = sum(1 for r in data.PROGRAMME if r[5] == "session")
    talks = sum(1 for r in data.PROGRAMME if r[5] == "session"
                for t in r[4] if t[1] != "Discussion")
    first = data.PROGRAMME[0][0].split("|")[0]
    last = data.PROGRAMME[-1][0].split("|")[-1]
    return f'''        <section class="pday" data-day="1">
          <div class="pday-head">
            <time class="pcal" datetime="{data.DATE_ISO}"><span class="pcal-m" aria-hidden="true">Oct</span><span class="pcal-d" aria-hidden="true">29</span><span class="pcal-w" aria-hidden="true">Fri</span><span class="vh">Friday 29 October 2027</span></time>
            <div class="pday-id">
              <span class="pday-label">The meeting</span>
              <span class="pday-meta"><span>{ICON["clock"]}<b>{first} to {last}</b></span><span>{ICON["list"]}{sessions} sessions</span><span>{ICON["mic"]}{talks} talks</span></span>
            </div>
            <button class="pcollapse" type="button">Expand all</button>
          </div>
{rows()}
        </section>'''

def initials(name):
    plain = re.sub(r"&[a-z]+;", "", name)
    parts = [p for p in plain.split() if p[0].isalpha()]
    return (parts[0][0] + parts[-1][0]).upper()

def fac(people):
    out = []
    for i, (name, sub) in enumerate(people):
        d = ["", " d1", " d2", " d3"][i % 4]
        c = f'<div class="c">{sub}</div>' if sub else ""
        out.append(f'        <div class="fac rv{d}"><div class="av">{initials(name)}</div><b>{name}</b>{c}</div>')
    return "\n".join(out)

def modules():
    return "\n".join(
        f'        <li class="sl-mod rv{["", " d1", " d2", " d3"][i % 4]}"><span class="sl-n">{i+1:02d}</span>'
        f'<div><h3>{t}</h3><p>{d}</p></div></li>'
        for i, (t, d) in enumerate(data.SKILLS_MODULES))

BLOCKS = {
 "prog-days": day(),
 "chairs": fac(data.CHAIRS),
 "faculty": fac([(n, "") for n in data.FACULTY]),
 "skills-modules": modules(),
 "skills-faculty": fac(data.SKILLS_FACULTY),
}

p = pathlib.Path("index.html"); s = p.read_text(encoding="utf-8")
for name, html in BLOCKS.items():
    pat = re.compile(r"(<!-- %s -->).*?(<!-- /%s -->)" % (name, name), re.S)
    if not pat.search(s):
        sys.exit(f"marker {name} not found")
    s = pat.sub(lambda m: m.group(1) + "\n" + html + "\n" + m.group(2), s)
p.write_text(s, encoding="utf-8")
print("london programme, faculty and skills lab written")
