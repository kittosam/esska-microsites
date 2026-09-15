# -*- coding: utf-8 -*-
"""Regenerates the programme markup in index.html from data.py. Run from sites/rome-2027."""
import sys, pathlib, re
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import rome_programme as data

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
    """What the day header says: span, sessions (+ finale) and talk count."""
    items = day[3]
    a0, b0 = times(day[2])
    nses = sum(1 for i in items if i[2].startswith("Session"))
    fin = any("Finale" in i[2] for i in items)
    ntalks = sum(len(i[3]) for i in items if not i[5])
    return f"{a0} to {b0}", f"{nses} sessions" + (" + finale" if fin else ""), f"{ntalks} talks"

def day_block(day, num, label, iso, wk, dnum, mon, full, hidden):
    span, sess, talks_txt = day_facts(day)
    rows=[]
    for (rng,dur,title,talks,note,brk) in day[3]:
        a,b=times(rng); m=mins(a,b)
        if brk or not talks:
            rows.append(
f'''          <div class="prow{" break" if brk else ""}" data-day="{num}">
            <div class="prow-static">
              <span class="ptime"><span class="pstart">{a}</span><span class="pdur">{m} min</span></span>
              <span class="pmain-head"><span class="ptitle">{title}</span></span>
            </div>
          </div>''')
            continue
        lis="".join(f'<li class="ptalk"><span class="ptx">{tx}</span><span class="psp">{sp}</span></li>'
                    for tx,sp in (split_speaker(x) for x in talks))
        rows.append(
f'''          <div class="prow" data-day="{num}">
            <button class="prow-btn" type="button" aria-expanded="false">
              <span class="ptime"><span class="pstart">{a}</span><span class="pdur">{m} min</span></span>
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

p=pathlib.Path("index.html"); s=p.read_text(encoding="utf-8")
i=s.index('      <div class="pdays" id="progDays">')
j=s.index('      <div style="margin-top:2.4rem"><a class="tlink',i)
s=(s[:i]+'      <div class="pdays" id="progDays">\n'
   + day_block(data.DAY1,"1","Day one","2027-10-08","Fri","8","Oct","Friday 8 October 2027",False)+"\n"
   + day_block(data.DAY2,"2","Day two","2027-10-09","Sat","9","Oct","Saturday 9 October 2027",True)+"\n      </div>\n"
   + s[j:])
p.write_text(s,encoding="utf-8")
print("site programme regenerated:", day_facts(data.DAY1), day_facts(data.DAY2))
