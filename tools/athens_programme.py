# -*- coding: utf-8 -*-
"""Athens 2027 programme data (from ESSKA_Hip_Focus_Meeting_Athens_2027_INTERNAL_V3,
public programme content only) and the markup generator for the site."""
MP="Oliver Mar&iacute;n-Pe&ntilde;a"; AP="Athanasios Papavasiliou"
# item: (start, end, title, [(label, text)], [(talk, speaker)], discussion or None, is_break)
# a talk is (talk, speaker), or (time, talk, speaker) when ESSKA gives talk times; a timed
# (time, title, who, "disc") entry is the session's discussion slot and is not counted as a talk.
# is_break is "rec" for a break that also carries the pre-recorded surgery session: it opens
# like a session to list the proposed topics, and its talks are not counted as lectures.
REC_TOPICS=['Labral injury management: from repair to reconstruction', 'Access and capsular management in hip arthroscopy', 'Cartilage lesion management: from repair to microfracture', 'Gluteal tendon repair in greater trochanteric pain syndrome']
REC_NOTE='The final selection, the allocation between the two days, the surgeons and the moderators are to be confirmed.'
DAY1=("1","2027-04-15","Thu","Thursday 15 April 2027","10:00","18:00",[
 ("10:00","10:10","Welcome and Educational Objectives",[("Moderators",f"{MP} and {AP}")],
  [("Opening, Olympic theme and meeting objectives",f"{MP} and {AP}"),("ESSKA Academy content pathway and interactive format",MP)],None,False),
 ("10:10","10:17","ESSKA Keynote Lecture",[("Introduction","by the Meeting Chairs")],
  [("The Athletic Hip in 2027: What Should We Be Doing Differently?","Vikas Khanduja")],None,False),
 ("10:17","11:17","Session I &middot; FAI in the High-Impact Athlete",[("Moderators",f"{MP} and Tahsin Beyzadeoglu")],
  [("FAIS and return to high-impact sport after hip arthroscopy: which morphology really matters?","Filippo Randelli"),("Labrum: repair, augmentation or reconstruction?","Bar&#305;&#351; Kocao&#287;lu"),
   ("Capsule: when is closure not enough?","Safa G&uuml;rsoy"),("Cartilage damage in the athlete: when does arthroscopy stop making sense?","Ali Bajwa")],
  "About 32 minutes of interactive case discussion, with stepwise cases, audience voting and re-voting after discussion. Panel: Filippo Randelli, Bar&#305;&#351; Kocao&#287;lu, Safa G&uuml;rsoy, Ali Bajwa and Nicolas Bonin.",False),
 ("11:17","12:17","Session II &middot; Groin, Lateral Hip and Extra-Articular Sports Injuries",[("Moderators","Lior Laver and Dora Papadopoulou")],
  [("Groin pain in athletes: a practical diagnostic pathway","Per H&ouml;lmich"),("Deep gluteal syndrome: who really needs surgery?","Bruno Capurro"),
   ("Proximal hamstring pathology: when should we repair?","Marc Tey Pons"),("Lateral hip pain: rehabilitation before intervention","Aleksandra Kr&oacute;likowska")],
  "About 32 minutes of multidisciplinary case discussion. Panel: Per H&ouml;lmich, Bruno Capurro, Marc Tey Pons, Aleksandra Kr&oacute;likowska and Suzanne Huurman.",False),
 ("12:17","13:17","Working lunch and pre-recorded surgery session",[("Format","Moderated pre-recorded surgical demonstrations, with the industry exhibition and networking")],[(x,"") for x in REC_TOPICS],REC_NOTE,"rec"),
 ("13:17","14:17","Session III &middot; The Athlete with DDH and Structural Borderlines",[("Moderators",f"{AP} and Panayiotis Christofilopoulos")],
  [("Borderline dysplasia: instability or impingement?","Michael Wettstein"),("Imaging structural instability beyond the LCEA","Margarita Natsika"),
   ("PAO in active patients: indications and return to sport","Sufian S. Ahmad"),("Arthroscopy, PAO, femoral osteotomy or combined treatment?","Ajay Malviya")],
  "About 32 minutes of interactive structural-decision cases, with votes on arthroscopy, PAO, osteotomy, combined treatment or no surgery. Panel: Michael Wettstein, Margarita Natsika, Sufian S. Ahmad, Ajay Malviya and Panayiotis Christofilopoulos.",False),
 ("14:17","14:47","Afternoon coffee and industry exhibition",[],[],None,True),
 ("14:47","15:47","Session IV &middot; Rehabilitation and Return to Sport",[("Moderators","Dora Papadopoulou and Tahsin Beyzadeoglu")],
  [("Rehabilitation progression after hip preservation surgery","Suzanne Huurman"),("Functional testing: what should we actually measure?","Francesco Della Villa"),
   ("Return to training, sport and performance","Robert Prill"),("Sport-specific readiness and return-to-performance decision-making","Stefano Di Paolo")],
  "About 32 minutes of return-to-sport cases, with audience votes on readiness to train, compete or delay, and on missing criteria. Panel: Suzanne Huurman, Francesco Della Villa, Robert Prill, Stefano Di Paolo and Lior Laver.",False),
 ("15:47","16:42","Session V &middot; Innovation: Evidence or Enthusiasm?",[("Moderators","Jakub Kautzner and Daniel P&eacute;rez-Prieto")],
  [("Orthobiologics in the athletic hip: what is actually supported?","Laura de Girolamo"),("AI, advanced imaging and 3D planning: what changes clinical decisions?","Klemen Stra&#382;ar"),
   ("Traction-free hip arthroscopy: evolution or revolution?","Matti Sepp&auml;nen")],
  "About 34 minutes of evidence-versus-innovation case discussion. Panel: Laura de Girolamo, Klemen Stra&#382;ar, Matti Sepp&auml;nen, Vikas Khanduja and Jakub Kautzner.",False),
 ("16:42","17:42","Final Interactive Challenge: The Athletic Hip Case That Divides the Faculty",[("Case presenters",f"{MP} and {AP}")],[],
  "Two complex cases of about 30 minutes each: vote, panel debate, audience questions, re-vote, then the actual treatment and outcome. Panel: Vikas Khanduja, Ajay Malviya, Bar&#305;&#351; Kocao&#287;lu, Michael Wettstein, Filippo Randelli and Panayiotis Christofilopoulos.",False),
 ("17:42","18:00","Day 1 Synthesis and Take-Home Messages",[("Moderators",f"{MP} and {AP}"),("Format","Faculty synthesis of the decisions that changed during discussion, and a preview of Friday morning")],[],None,False),
])
# Friday runs to 12:00, with a 50-minute break for the recorded surgery session (October 2026).
DAY2=("2","2027-04-16","Fri","Friday 16 April 2027","08:00","12:00",[
 ("08:00","08:50","Session VI &middot; ESSKA Hip Research and Rapid Communications",[("Moderators","Andr&eacute; Sarmento and Filippo Randelli")],
  [("ESSKA Hip collaborative research: where should we go next?","Andr&eacute; Sarmento"),("Five selected rapid communications, 5 minutes each","Selected abstract presenters")],
  "Moderated research discussion. Panel: Andr&eacute; Sarmento, Filippo Randelli, Sufian S. Ahmad and Vikas Khanduja.",False),
 ("08:50","09:50","Session VII &middot; Training the Hip Preservation Surgeon of the Future",[("Moderators","Eleftherios Tsiridis and Safa G&uuml;rsoy")],
  [("How should hip arthroscopy be taught?","Jacek Mazek"),("Cadaveric training: what skills should be assessed?",AP),
   ("ESSKA Hip Core Curriculum &rarr; Academy &rarr; Courses","Daniel P&eacute;rez-Prieto"),("From course attendance to competency-based certification",MP)],
  f"About 32 minutes of faculty discussion, with votes on competencies and assessment standards. Panel: Jacek Mazek, {AP}, Daniel P&eacute;rez-Prieto, {MP}, Vikas Khanduja and Andr&eacute; Sarmento.",False),
 ("09:50","10:40","Morning coffee and pre-recorded surgery session",[("Format","Moderated pre-recorded surgical demonstrations, with the industry exhibition")],[(x,"") for x in REC_TOPICS],REC_NOTE,"rec"),
 ("10:40","11:40","Session VIII &middot; Failed Hip Preservation: Revision, Salvage and Treatment Boundaries",[("Moderators and case presenters","Filippo Randelli and Michael Wettstein")],
  [("10:40&ndash;10:47","Why does hip arthroscopy fail?","Nicolas Bonin"),("10:47&ndash;10:54","Revision hip arthroscopy: what can realistically be corrected?","Jacek Mazek"),
   ("10:54&ndash;11:01","Structural failure after preservation: reassess the diagnosis","Panayiotis Christofilopoulos"),("11:01&ndash;11:08","When should the young active patient move to arthroplasty?","Dani&euml;l Haverkamp"),
   ("11:08&ndash;11:15","Spinopelvic fulcrum phenotypes and understanding the mechanics in young adults with DDH &ndash; data from 450 cases","Eleftherios Tsiridis"),
   ("11:15&ndash;11:40","Interactive case discussions and audience voting","Moderators and faculty panel","disc")],
  "Case-based discussion led by Filippo Randelli and Michael Wettstein, with votes on revision arthroscopy, PAO, osteotomy, combined reconstruction or THA. Panel: Nicolas Bonin, Jacek Mazek, Panayiotis Christofilopoulos, Dani&euml;l Haverkamp, Ajay Malviya and Eleftherios Tsiridis.",False),
 ("11:40","12:00","Academy Integration, Next Steps and Closing",[("Moderators",f"{MP} and {AP}")],
  [("Academy-ready content and educational gaps","Daniel P&eacute;rez-Prieto"),("Strategic next steps and certification pathway",MP)],None,False),
])
CHAIRS=[(MP,"Spain"),(AP,"Greece"),("Ajay Malviya","United Kingdom")]
FACULTY=[("Sufian S. Ahmad","Germany"),("Ali Bajwa","United Kingdom"),("Nicolas Bonin","France"),("Bruno Capurro","Spain"),
 ("Francesco Della Villa","Italy"),("Safa G&uuml;rsoy","T&uuml;rkiye"),("Dani&euml;l Haverkamp","Netherlands"),("Per H&ouml;lmich","Denmark"),
 ("Suzanne Huurman","Netherlands"),("Vikas Khanduja","United Kingdom"),("Bar&#305;&#351; Kocao&#287;lu","T&uuml;rkiye"),("Aleksandra Kr&oacute;likowska",'<abbr class="tbc" title="To be confirmed">TBC</abbr>'),("Lior Laver","Israel"),
 ("Jacek Mazek","Poland"),("Filippo Randelli","Italy"),("Andr&eacute; Sarmento","Portugal"),("Matti Sepp&auml;nen","Finland"),("Klemen Stra&#382;ar","Slovenia"),
 ("Marc Tey Pons","Spain"),("Michael Wettstein","Switzerland"),("Robert Prill","Germany"),("Stefano Di Paolo","Italy"),("Daniel P&eacute;rez-Prieto","Spain"),
 ("Laura de Girolamo","Italy"),("Panayiotis Christofilopoulos","Switzerland"),("Dora Papadopoulou","United Kingdom and Greece"),
 ("Tahsin Beyzadeoglu","T&uuml;rkiye"),("Jakub Kautzner","Czech Republic"),("Eleftherios Tsiridis","Greece"),("Margarita Natsika","Greece")]

def mins(a,b):
    if "TBC" in (a,b): return None
    f=lambda s:(lambda h,m:h*60+m)(*map(int,s.split(":"))); return f(b)-f(a)
ICON_CLOCK='<svg viewBox="0 0 20 20" aria-hidden="true"><circle cx="10" cy="10" r="7.5" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M10 5.8V10l2.8 1.8" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>'
ICON_LIST='<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 5.5h12M4 10h12M4 14.5h8" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>'
ICON_MIC='<svg viewBox="0 0 20 20" aria-hidden="true"><rect x="7.2" y="2.8" width="5.6" height="9" rx="2.8" fill="none" stroke="currentColor" stroke-width="1.7"/><path d="M4.8 9.6a5.2 5.2 0 0 0 10.4 0M10 14.8v2.6" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/></svg>'
def notes_html(notes):
    return "".join(f'<span class="psub psub-note"><span class="pnote-l">{l}</span><span class="pnote-t">{t}</span></span>' for l,t in notes)
def day_block(day, label, hidden):
    num, iso, wk, full, a0, b0, items = day
    nses=sum(1 for i in items if i[2].startswith("Session"))
    extra=" + final challenge" if any(i[2].startswith("Final Interactive") for i in items) else ""
    ntalks=sum(1 for i in items if not i[6] for t in i[4] if len(t)<4)
    rows=[]
    for (a,b,title,notes,talks,disc,brk) in items:
        m=mins(a,b)
        head=f'<span class="ptime"><span class="pstart">{a}</span><span class="pdur">{m} min</span></span>\n              <span class="pmain-head"><span class="ptitle">{title}</span>{notes_html(notes)}</span>'
        if brk or (not talks and not disc):
            rows.append(f'''          <div class="prow{" break" if brk else ""}" data-day="{num}">
            <div class="prow-static">
              {head}
            </div>
          </div>''')
            continue
        timed=bool(talks) and all(len(t)>=3 for t in talks)
        if timed:
            lis="".join(f'<li class="ptalk{" ptalk-disc" if len(t)>3 else ""}"><span class="ptt">{t[0]}</span><span class="ptx">{t[1]}</span><span class="psp">{t[2]}</span></li>' for t in talks)
        else:
            lis="".join(f'<li class="ptalk"><span class="ptx">{t}</span><span class="psp">{sp}</span></li>' for t,sp in talks)
        body=(f'<ul class="ptalks{" timed" if timed else ""}">{lis}</ul>' if talks else "")+(f'<p class="pnote"><span class="pnote-l">Discussion</span><span class="pnote-t">{disc}</span></p>' if disc else "")
        rows.append(f'''          <div class="prow" data-day="{num}">
            <button class="prow-btn" type="button" aria-expanded="false">
              {head}
              <span class="pchev" aria-hidden="true"></span>
            </button>
            <div class="ptalks-wrap" hidden>
              {body}
            </div>
          </div>''')
    return f'''        <section class="pday" data-day="{num}"{" hidden" if hidden else ""}>
          <div class="pday-head">
            <time class="pcal" datetime="{iso}"><span class="pcal-m" aria-hidden="true">Apr</span><span class="pcal-d" aria-hidden="true">{int(iso[-2:])}</span><span class="pcal-w" aria-hidden="true">{wk}</span><span class="vh">{full}</span></time>
            <div class="pday-id">
              <span class="pday-label">{label}</span>
              <span class="pday-meta"><span>{ICON_CLOCK}<b>{a0} to {b0}</b></span><span>{ICON_LIST}{nses} sessions{extra}</span><span>{ICON_MIC}{ntalks} talks</span></span>
            </div>
            <button class="pcollapse" type="button">Expand all</button>
          </div>
{chr(10).join(rows)}
        </section>'''
def initials(n):
    parts=[p for p in n.replace("-"," ").split() if p[0].isalpha() and p[0].isupper()]
    return (parts[0][0]+parts[-1][0]) if len(parts)>1 else n[:2].upper()
def fac_grid(people):
    ds=["",""," d1"," d2"," d3"]
    return "\n".join(f'        <div class="fac rv{["", " d1"," d2"," d3"][i%4]}"><div class="av">{initials(n)}</div><b>{n}</b><div class="c">{c}</div></div>' for i,(n,c) in enumerate(people))
