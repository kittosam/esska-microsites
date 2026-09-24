# -*- coding: utf-8 -*-
# Programme and faculty, transcribed from
# "ESSKA Shoulder Focus Meeting 2027_Programme.docx" (preliminary, 2026-09-25).
# Rows are (time range, duration, title, [talks], note, is_break). A talk may carry
# its speaker in <i>...</i>. A range of "TBC" renders as a row without a time.

DAY1 = ("1", "Friday, 10 September 2027", "08:30&ndash;18:30", [
 ("08:30&ndash;10:30","120 min","Anterosuperior tears &middot; Repairable massive tears",
  ["Open versus arthroscopic repair: selecting the appropriate approach",
   "&ldquo;Relive&rdquo; surgical video: How I repair it",
   "Augmentation techniques",
   "Management of the pseudoparetic shoulder",
   "Case-based discussion: two clinical cases"],
  "Format|Expert presentations, a &ldquo;Relive&rdquo; surgical video and case-based discussion", False),
 ("10:30&ndash;11:00","30 min","Coffee break", [], "", True),
 ("11:00&ndash;13:00","120 min","Anterosuperior tears &middot; Irreparable tears",
  ["Expert debate: Which tendon transfer?",
   "Tendon transfer selection: evidence-based indications and outcomes",
   "&ldquo;Relive&rdquo; surgical video: Pectoralis minor transfer",
   "&ldquo;Relive&rdquo; surgical video: Pectoralis major transfer",
   "&ldquo;Relive&rdquo; surgical video: Latissimus dorsi transfer",
   "Case-based discussion: two clinical cases"],
  "Format|An expert debate, three &ldquo;Relive&rdquo; surgical videos and case-based discussion", False),
 ("13:00&ndash;14:00","60 min","Lunch break", [], "", True),
 ("14:00&ndash;16:00","120 min","Posterosuperior tears &middot; Repairable massive tears",
  ["Evidence-based treatment algorithm",
   "Biological augmentation techniques: footprint preservation, growth factors and stem cells",
   "Biceps augmentation: techniques and outcomes",
   "Patch augmentation: technique and outcomes",
   "Case-based discussion: two clinical cases"],
  "Format|Expert presentations and case-based discussion", False),
 ("16:00&ndash;16:30","30 min","Coffee break", [], "", True),
 ("16:30&ndash;18:30","120 min","Posterosuperior tears &middot; Irreparable tears: techniques and outcomes",
  ["Functional repair",
   "Superior capsular reconstruction using the long head of the biceps",
   "Superior capsular reconstruction using fascia lata autograft",
   "Tendon transfers: latissimus dorsi versus lower trapezius",
   "Case-based discussion: two clinical cases"],
  "Format|Expert presentations and case-based discussion", False),
])

DAY2 = ("2", "Saturday, 11 September 2027", "08:30&ndash;13:00", [
 ("08:30&ndash;10:30","120 min","Session I &middot; When arthroscopy is no longer enough",
  ["Indications and patient selection: massive tears, retears and pseudoparalysis",
   "Biomechanics: the influence of the residual rotator cuff",
   "From preoperative planning to virtual reality",
   "Indications for tendon transfer",
   "Complications"],
  "Discussion|Five presentations, followed by 30 minutes of open discussion", False),
 ("10:30&ndash;11:00","30 min","Coffee break", [], "", True),
 ("11:00&ndash;13:00","120 min","Session II &middot; Complex clinical cases", [],
  "Format|An interactive discussion of four complex clinical cases, with 30 minutes for each case. Case details to be announced.", False),
 ("TBC","","Grand finale debate",
  ["Superior capsular reconstruction <i>Teruhisa Mihata</i>",
   "Lower trapezius transfer <i>Bassem Elhassan</i>",
   "Functional (partial) repair <i>Emilio Calvo</i>",
   "Reverse shoulder arthroplasty <i>Felix Savoie III</i>"],
  "Chairs|Emmanouil Brilakis and Maristella Saccomanno &middot; What is the best treatment for the 60-year-old active patient with an irreparable posterosuperior rotator cuff tear? Proposed panel, participation to be confirmed.", False),
 ("TBC","","Keynote lectures",
  ["The Future of Rotator Cuff Reconstruction <i>Speaker to be confirmed</i>",
   "Massive Rotator Cuff Tears: Repair, Reconstruct, Transfer or Replace? <i>Emilio Calvo, proposed</i>"],
  "Scheduling|Dates and times to be confirmed", False),
])

# name, role or country ("" when ESSKA has not given one)
CHAIRS = [("Emmanouil Brilakis","ESSKA Shoulder Section Chair"),
          ("Maristella Francesca Saccomanno","Scientific Co-Chair"),
          ("Alfonso Maria Romano","Scientific Chair"),
          ("Bar&#305;&#351; Kocao&#287;lu","Local Chair"),
          ("Nezih Ziroglu","Local Chair"),
          ("Kerem Bilsel","Local Chair")]

PROPOSED = [("Teruhisa Mihata",""),("Bassem Elhassan",""),
            ("Emilio Calvo","Spain"),("Felix Savoie III","")]
