# -*- coding: utf-8 -*-
"""Writes the programme and faculty markup into Istanbul's index.html.
Run from sites/istanbul-2027:  python3 ../../tools/istanbul_site_programme.py"""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import istanbul_programme as data

def times(r): return [x.strip() for x in r.replace("&ndash;","|").split("|")]
def mins(a,b):
    f=lambda s:(lambda h,m:h*60+m)(*map(int,s.split(":")))
    return f(b)-f(a)
def split_speaker(t):
    m=re.search(r"\s*<i>(.*?)</i>\s*$",t)
    return (t[:m.start()].strip(), m.group(1)) if m else (t.strip(),"")
def head_line(note, n):
    if note:
        lbl, sep, txt = note.partition("|")
        if sep:
            return (f'<span class="psub psub-note"><span class="pnote-l">{lbl}</span>'
                    f'<span class="pnote-t">{txt}</span></span>')
        return f'<span class="psub psub-note"><span class="pnote-t">{note}</span></span>'
    return f'<span class="psub">{n} talk{"s" if n!=1 else ""}</span>'

ICON = {
 "clock":'<svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="7.5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M10 5.8V10l2.8 1.8" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
 "list":'<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 5.5h12M4 10h12M4 14.5h8" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
 "mic":'<svg viewBox="0 0 20 20" aria-hidden="true"><rect x="7.2" y="2.8" width="5.6" height="9" rx="2.8" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M4.8 9.6a5.2 5.2 0 0 0 10.4 0M10 14.8v2.6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>',
}

def day_facts(day):
    items=day[3]
    a0,b0 = times(day[2])
    nses = sum(1 for i in items if not i[5] and i[0]!="TBC")
    ntalks = sum(len(i[3]) for i in items if not i[5])
    return f"{a0} to {b0}", f"{nses} sessions", f"{ntalks} talks"

def slot(rng):
    """The time column: a start and a duration, or TBC when ESSKA has not set one."""
    if rng=="TBC":
        return '<span class="ptime"><span class="pstart">TBC</span><span class="pdur">time to follow</span></span>'
    a,b=times(rng)
    return f'<span class="ptime"><span class="pstart">{a}</span><span class="pdur">{mins(a,b)} min</span></span>'

def day_block(day, num, label, iso, wk, dnum, mon, full, hidden):
    span, sess, talks_txt = day_facts(day)
    rows=[]
    for (rng,dur,title,talks,note,brk) in day[3]:
        if brk or not talks:
            rows.append(
f'''          <div class="prow{" break" if brk else ""}" data-day="{num}">
            <div class="prow-static">
              {slot(rng)}
              <span class="pmain-head"><span class="ptitle">{title}</span>{head_line(note,0) if note else ""}</span>
            </div>
          </div>''')
            continue
        lis="".join(f'<li class="ptalk"><span class="ptx">{tx}</span><span class="psp">{sp}</span></li>'
                    for tx,sp in (split_speaker(x) for x in talks))
        rows.append(
f'''          <div class="prow" data-day="{num}">
            <button class="prow-btn" type="button" aria-expanded="false">
              {slot(rng)}
              <span class="pmain-head"><span class="ptitle">{title}</span>{head_line(note, len(talks))}</span>
              <span class="pchev" aria-hidden="true"></span>
            </button>
            <div class="ptalks-wrap" hidden>
              <ul class="ptalks">{lis}</ul>
            </div>
          </div>''')
    return (
f'''        <section class="pday" data-day="{num}"{" hidden" if hidden else ""}>
          <div class="pday-head">
            <time class="pcal" datetime="{iso}"><span class="pcal-m" aria-hidden="true">{mon}</span><span class="pcal-d" aria-hidden="true">{dnum}</span><span class="pcal-w" aria-hidden="true">{wk}</span><span class="vh">{full}</span></time>
            <div class="pday-id">
              <span class="pday-label">{label}</span>
              <span class="pday-meta"><span>{ICON["clock"]}<b>{span}</b></span><span>{ICON["list"]}{sess}</span><span>{ICON["mic"]}{talks_txt}</span></span>
            </div>
            <button class="pcollapse" type="button">Expand all</button>
          </div>
{chr(10).join(rows)}
        </section>''')

def initials(name):
    plain=re.sub(r"&#\d+;","x",name)
    parts=[p for p in plain.split() if p[0].isalpha()]
    return (parts[0][0]+parts[-1][0]).upper() if len(parts)>1 else parts[0][:2].upper()

def fac_grid(people, extra=""):
    out=[]
    for i,(name,sub) in enumerate(people):
        d=["","d1","d2","d3"][i%4]
        out.append(f'        <div class="fac rv {d}{extra}"><div class="av">{initials(name)}</div>'
                   f'<b>{name}</b>{f"<div class=\"c\">{sub}</div>" if sub else ""}</div>')
    return "\n".join(out)

PROG = f'''      <div class="head rv"><p class="eyebrow">Scientific programme</p><h2>Day <span class="lt">by day</span></h2></div>
      <p class="prog-note rv">Preliminary programme, subject to change. Session moderators will be announced, and faculty participation, lecture scheduling and programme details remain subject to confirmation.</p>
      <div class="prog-controls rv">
        <div class="pctl-top">
          <div class="pctl-search">
            <label class="plbl" for="progQ">Search the programme</label>
            <input id="progQ" type="search" autocomplete="off"
                   placeholder="Search talks and sessions">
          </div>
        </div>
        <div class="pctl-row">
          <div class="pchips" id="progChips" role="group" aria-label="Choose a day">
            <button class="pchip" type="button" data-filter="1" aria-pressed="true">Day one<span class="pchip-date"> &middot; 10 September</span></button>
            <button class="pchip" type="button" data-filter="2" aria-pressed="false">Day two<span class="pchip-date"> &middot; 11 September</span></button>
          </div>
        </div>
      </div>
      <p class="pempty" id="progEmpty" hidden>Nothing in this day matches that search.
        <button type="button" id="progClear">Clear search</button></p>
      <div class="pdays" id="progDays">
{day_block(data.DAY1,"1","Day one","2027-09-10","Fri","10","Sep","Friday 10 September 2027",False)}
{day_block(data.DAY2,"2","Day two","2027-09-11","Sat","11","Sep","Saturday 11 September 2027",True)}
      </div>'''

FAC = f'''      <div class="head rv"><p class="eyebrow">Faculty</p><h2>Chairs <span class="lt">and faculty</span></h2></div>
      <h3 class="sub-h rv">The chairs</h3>
      <div class="fac-grid rv">
{fac_grid(data.CHAIRS)}
      </div>
      <h3 class="sub-h rv">Proposed speakers</h3>
      <div class="fac-grid rv">
{fac_grid(data.PROPOSED)}
      </div>
      <p class="routes-note rv">Proposed participation, to be confirmed. The full faculty will be published here as invitations are accepted.</p>'''

p=pathlib.Path("index.html"); s=p.read_text(encoding="utf-8")
prog_old = re.search(r'      <div class="head rv"><p class="eyebrow">Scientific programme</p>.*?(?=\n    </div>\n  </section>)', s, re.S)
s = s[:prog_old.start()] + PROG + s[prog_old.end():]
fac_old = re.search(r'      <div class="head rv"><p class="eyebrow">Faculty</p>.*?(?=\n    </div>\n  </section>)', s, re.S)
s = s[:fac_old.start()] + FAC + s[fac_old.end():]
p.write_text(s, encoding="utf-8")
print("istanbul programme and faculty written")
