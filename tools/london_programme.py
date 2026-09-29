# -*- coding: utf-8 -*-
"""London 2027 (Foot and Ankle), preliminary programme, as ESSKA supplied it in
ESSKA_Focus_Meeting_2027_Web_Programme.docx (September 2026). One day, 29 October 2027.

Each row: (time range, title, subtitle, moderators, talks, kind)
  time range  "08:50|10:00", or a single "17:30" for a moment with no duration
  talks       list of (time range, talk title, speaker); a round table has no titles
  kind        "break", "static" (no detail to open) or "session"
"""

DATE_ISO = "2027-10-29"

PROGRAMME = [
 ("08:00|08:15", "Registration and coffee", "", "", [], "break"),
 ("08:15|08:35", "Industry symposium", "", "", [], "static"),
 ("08:40|08:50", "Welcome to London", "", "Mette Andersen and Pieter D&rsquo;Hooghe", [], "static"),
 ("08:50|10:00", "Syndesmosis in motion",
  "Anatomy, biomechanics and pathomechanics of injury",
  "Guillaume Cordier and Maiti M&uuml;nchgesang", [
   ("08:50|09:05", "Syndesmosis anatomy unveiled", "Pim van Dijk"),
   ("09:05|09:20", "Biomechanics and stability of the ankle mortise", "Francesco Della Villa"),
   ("09:20|09:35", "The syndesmotic diagnostic pathway", "Robbie Ray"),
   ("09:35|09:50", "Syndesmosis injuries in the athlete: how to treat them?", "Pieter D&rsquo;Hooghe"),
   ("09:50|10:00", "Discussion", ""),
  ], "session"),
 ("10:00|10:30", "Coffee break and networking", "", "", [], "break"),
 ("10:30|12:00", "Workup and diagnosis of ligamentous syndesmosis injuries",
  "Optimising non-surgical treatment",
  "Mette Andersen and Pierre-Henri Vermorel", [
   ("10:30|10:50", "What you see first matters: optimising the initial ankle injury exam", "Cinthya Vargas and Enric Vila"),
   ("10:50|11:10", "Classification and treatment decision-making: the IFASC consensus on HAS in elite athletes", "Arianna Gianakos"),
   ("11:10|11:30", "What I&rsquo;ve learned on syndesmosis injuries over the years", "Ioan Tudur Jones"),
   ("11:30|11:50", "Return to play vs a ticket to the OR? Surgical decision-making rationale", "James Calder"),
   ("11:50|12:00", "Discussion", ""),
  ], "session"),
 ("12:00|13:00", "Lunch", "", "", [], "break"),
 ("13:00|13:20", "Industry symposium", "", "", [], "static"),
 ("13:20|14:50", "Management of unstable syndesmosis injuries", "",
  "Pieter D&rsquo;Hooghe and Cinthya Vargas", [
   ("13:20|13:40", "Surgical treatment: stabilisation options", "Mette Andersen"),
   ("13:40|14:00", "The chronic syndesmosis", "Cesc Malagelada"),
   ("14:00|14:20", "Chronic syndesmosis in the athlete: repair, reconstruct, or rehab?", "Anthony Perera"),
   ("14:20|14:40", "Postoperative treatment and return to sport", "Enric Vila"),
   ("14:40|14:50", "Discussion", ""),
  ], "session"),
 ("14:50|15:20", "Coffee break and networking", "", "", [], "break"),
 ("15:20|16:20", "Syndesmosis under fire &middot; Round table",
  "Real-life cases and tough decisions",
  "Pim van Dijk and James Calder", [
   ("15:20|15:40", "Case presentation", "Francesco Della Villa"),
   ("15:40|16:00", "Case presentation", "Arianna Gianakos"),
   ("16:00|16:20", "Case presentation", "Anthony Perera"),
  ], "session"),
 ("16:30|17:10", "Sponsored re-live surgery session", "",
  "Arianna Gianakos and Anthony Perera", [
   ("16:30|16:50", "Re-live surgery", "Pieter D&rsquo;Hooghe"),
   ("16:50|17:10", "Re-live surgery", "Guillaume Cordier"),
  ], "session"),
 ("17:10|17:30", "Discussion", "", "", [], "static"),
 ("17:30", "End of meeting", "", "", [], "break"),
]

# name, role (roles as ESSKA gave them, September 2026)
CHAIRS = [
 ("Mette Andersen", "Focus Meeting Chair"),
 ("Pieter D&rsquo;Hooghe", "Focus Meeting Co-Chair"),
 ("Jordi Vega", "ESSKA Foot and Ankle Section Chair"),
]

# everyone else who speaks or moderates, by surname; countries not supplied yet
FACULTY = [
 "James Calder", "Guillaume Cordier", "Francesco Della Villa", "Arianna Gianakos",
 "Cesc Malagelada", "Maiti M&uuml;nchgesang", "Anthony Perera", "Robbie Ray",
 "Ioan Tudur Jones", "Pim van Dijk", "Cinthya Vargas", "Pierre-Henri Vermorel",
 "Enric Vila",
]

# pre-meeting skills lab, from ESSKA_Slide7_SkillsLab_A4.pdf
SKILLS_MODULES = [
 ("Syndesmosis evaluation and testing", "Clinical exam, intra-operative assessment"),
 ("Syndesmosis repair and augmentation", "Anatomical repair, suture-tape reinforcement"),
 ("Suture button fixation", "Placement, tensioning, pitfalls"),
 ("Deltoid ligament repair", "Anchors, augmentation techniques"),
 ("Lateral ligament repair", "Brostr&ouml;m, InternalBrace-style constructs"),
]
SKILLS_FACULTY = [
 ("Mette Andersen", "Chair"),
 ("Pieter D&rsquo;Hooghe", "Co-Chair"),
 ("Guillaume Cordier", "ESSKA Foot and Ankle Section"),
 ("James Calder", "Local faculty, London"),
 ("Robbie Ray", "Local faculty, London"),
 ("Cesc Malagelada", "Local faculty, London"),
 ("Ioan Tudur Jones", "Local faculty, London"),
]
