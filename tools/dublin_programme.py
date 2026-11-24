# -*- coding: utf-8 -*-
# Programme first transcribed from "ACL_Focus_Meeting_Programme_Readable.docx" (2026-09-27),
# updated from the speaker allocation document (2026-11-12).
# Rows are (time range, duration, title, [talks], note, is_break[, chair and faculty]).

# Session chairs and faculty from "ACL Focus_Course - Dublin - Speaker Allocation.doc"
# (Brian Devitt, 12 November 2026). The industry partner names that followed each Re-live 1
# speaker were removed on 24 November 2026; co() now adds nothing.
TBC = '<abbr class="tbc" title="To be confirmed">TBC</abbr>'
AW, CS, NB, TW = "Andy Williams", "Ciara Stevenson", "Nicolas Bouguennec", "Tim Whitehead"
MV, JR, EK = "Mihai Vioreanu", "James Robinson", "Enda King"
BD, MS, SS = "Brian Devitt", "Martyn Snow", "Sven Scheffler"
def who(chair, *faculty): return {"Chair": chair, "Faculty": faculty}
def co(name): return ""

DAY1 = ("1", "Friday, 14 May 2027", "08:00&ndash;17:00", [
 ("08:00&ndash;08:30","30 min","Registration and coffee", [], "", True),
 ("08:30&ndash;08:45","15 min","Welcome, introduction and meeting objectives", [], "", False),
 ("08:45&ndash;10:15","90 min","The ACL Clinic &middot; Live patient assessment workshop", [],
  "Format|Live assessment of acute and chronic ACL injuries: Lachman testing, pivot shift examination, hyperlaxity assessment, clinical assessment of peripheral laxity, patient expectations and audience polling on treatment strategy.", False,
  who(BD, AW, CS, TW)),
 ("10:15&ndash;10:45","30 min","Coffee break", [], "", True),
 ("10:45&ndash;12:30","105 min","MRI interpretation and surgical decision-making", [],
  "Format|A systematic review of MRI scans and X-rays, identifying surgical risk factors, with graft selection algorithms and patient-specific operative planning.", False,
  who(MS, MV, NB, JR)),
 ("12:30&ndash;13:30","60 min","Lunch", [], "", True),
 ("13:30&ndash;14:15","45 min","Choosing the right graft &middot; Interactive case-based discussion", [],
  "Format|A faculty-led discussion comparing hamstring, quadriceps, BPTB, peroneus longus and rectus femoris autografts, using real-world cases.", False,
  who(SS, EK, AW, MV)),
 ("14:15&ndash;17:00","165 min","Re-live surgery 1 &middot; Graft harvest and preparation",
  [f"Patellar tendon <i>{AW}{co('Innovate Orthopaedics')}</i>", f"Hamstring <i>{MV}{co('Signature Orthopaedics')}</i>",
   f"Quadriceps <i>{TW}{co('Medacta')}</i>", f"Rectus femoris <i>{NB}{co('SBM')}</i>", f"Peroneus longus <i>{SS}{co(TBC)}</i>"],
  "Format|Five short video sessions: hamstring harvest, quadriceps harvest, BPTB harvest, peroneus longus split and rectus femoris harvest, with the emphasis on surgical workflow, graft preparation, avoiding complications and technical pearls.", False,
  who(CS)),
 ("17:00&ndash;17:05","5 min","Close of day one", [], "", True),
])

DAY2 = ("2", "Saturday, 15 May 2027", "08:00&ndash;17:00", [
 ("08:00&ndash;08:15","15 min","Review of day one", [], "", False),
 ("08:15&ndash;11:00","165 min","Re-live surgery 2 &middot; Building the perfect ACL reconstruction", [],
  "Format|Surgical flow: femoral and tibial tunnel positioning, graft passage and fixation strategies, with expert commentary and discussion.", False,
  who(MS, JR, TW, CS)),
 ("11:00&ndash;11:15","15 min","Coffee break", [], "", True),
 ("11:15&ndash;13:00","105 min","Re-live surgery 3 &middot; Surgical pearls, pitfalls and performance", [],
  "Format|Complications, including arthrogenic muscle inhibition, arthrofibrosis, persistent inflammation and cyclops lesions; common technical errors, troubleshooting, workflow optimisation, efficiency and performance enhancement for ACL surgeons.", False,
  who(BD, AW, NB, MV)),
 ("13:00&ndash;14:00","60 min","Lunch", [], "", True),
 ("14:00&ndash;14:45","45 min","Thinking outside the notch &middot; Rotational laxity in the primary ACL patient", [],
  "Format|A case-based discussion of rotational laxity, the high-grade pivot shift, hyperlax athletes and the indications for peripheral augmentation and reconstruction.", False,
  who(SS, JR, NB, CS, EK)),
 ("14:45&ndash;16:00","75 min","Re-live surgery 4 &middot; Peripheral procedures for rotational laxity", [],
  "Format|Modified Lemaire tenodesis, the Ellison procedure, anterolateral ligament reconstruction and (antero)medial reconstruction techniques: pearls, indications, fixation and avoiding complications.", False,
  who(MS, MV, TW, AW, NB)),
 ("16:00&ndash;17:00","60 min","Practical rehabilitation workshop &middot; Getting rehabilitation right first time", [],
  "Format|A fully interactive surgeon and physiotherapist session on extension restoration, swelling control, quadriceps activation, gait recovery, rehabilitation algorithms and difficult early rehabilitation cases.", False,
  who(AW, EK)),
 ("17:00&ndash;17:05","5 min","Closing remarks and key take-home messages", [], "", False),
])

# what the course sets out to do, shown above the day tabs
PHILOSOPHY = [
 "Live patient assessment and clinical examination workshops.",
 "Interactive MRI interpretation and surgical decision-making algorithms.",
 "Re-live surgery sessions with expert faculty commentary.",
 "Comprehensive management of rotational laxity.",
 "A practical rehabilitation workshop led by surgeons and specialist physiotherapists.",
]
OBJECTIVES = [
 "Assess the ACL-injured patient using a structured clinical approach.",
 "Interpret MRI findings and integrate them into surgical decision-making.",
 "Select the most appropriate graft for individual patients.",
 "Optimise graft harvest, tunnel placement, graft passage and fixation.",
 "Identify patients at risk of residual rotational laxity.",
 "Understand the indications and techniques for additional peripheral procedures.",
 "Understand the indications and techniques for treating additional injuries associated with ACL rupture.",
 "Manage common early rehabilitation challenges after ACL reconstruction.",
 "Use the meeting app to pose questions before each session and to highlight the key learning points afterwards.",
]
# "Potential Faculty Discussion Topics" in the document, shown as the third course tab
TOPICS = [
 "What graft for which patient?",
 "When is ACL reconstruction alone enough?",
 "Managing rotational laxity in young athletes.",
 "Managing ACL reconstruction in patients with open growth plates.",
 "Top ten technical errors in ACL reconstruction.",
 "How to optimise rehabilitation after surgery.",
]
AUDIENCE = ("Orthopaedic surgeons, fellows, senior trainees, physiotherapists and members of "
            "the multidisciplinary ACL team.")

CHAIRS = [("Brian Devitt","Co-Chair &middot; Ireland"),("Martyn Snow","Co-Chair &middot; UK"),("Sven Scheffler","Scientific Coordinator &middot; Germany")]
FACULTY = [(n,"") for n in (AW, CS, NB, TW, MV, JR, EK)]
# the same portraits as the welcome letter
CHAIR_PHOTOS = {"Brian Devitt":"chair-devitt.jpg","Martyn Snow":"chair-snow.jpg","Sven Scheffler":"chair-scheffler.jpg"}
