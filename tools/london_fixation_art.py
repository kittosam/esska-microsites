# -*- coding: utf-8 -*-
"""Builds the SVG behind London's "Unstable injuries" card (suture-button fixation, rendered
style). Usage: python3 tools/london_fixation_art.py out.svg, screenshot it at 800x900 in
headless Chrome, tone it violet (CIFalseColor #16102A to #E2DCF4, 70%) and crop 680x740 at
(120,100) to assets/img/card-fixation-render.jpg (new filename on every change)."""
import random, pathlib, sys
random.seed(7)
W,H=800,900
TIB="M235 -20H545C548 140 556 280 590 370C606 412 616 452 612 500C560 486 420 488 358 512C350 560 340 610 318 642C300 668 262 666 248 636C224 584 206 490 212 420C218 330 240 160 235 -20Z"
FIB="M650 -20H700C700 170 706 330 724 430C742 520 744 600 720 660C700 706 654 704 640 664C626 624 628 546 630 470C634 360 648 180 650 -20Z"
TAL="M362 528C420 494 560 492 606 520C630 536 636 590 626 632C608 694 552 736 482 738C410 740 366 702 350 652C338 612 344 546 362 528Z"
def pores(path_id, box, n):
    x0,y0,x1,y1=box; out=[]
    for _ in range(n):
        x=random.uniform(x0,x1); y=y1-abs(random.gauss(0,(y1-y0)*.45)); r=random.uniform(1,2.6)
        out.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{r:.1f}" ry="{r*random.uniform(.6,1):.1f}" opacity="{random.uniform(.22,.55):.2f}"/>')
    return f'<g clip-path="url(#c-{path_id})" fill="#6d6280">{"".join(out)}</g>'
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
 <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d6d1e0"/><stop offset=".55" stop-color="#9f97b4"/><stop offset="1" stop-color="#554c6e"/></linearGradient>
 <radialGradient id="boneG" cx="35%" cy="30%" r="80%"><stop offset="0" stop-color="#ffffff"/><stop offset=".5" stop-color="#ebe6e2"/><stop offset="1" stop-color="#9b91a9"/></radialGradient>
 <radialGradient id="talG" cx="40%" cy="30%" r="75%"><stop offset="0" stop-color="#fbf9f7"/><stop offset=".6" stop-color="#e0dada"/><stop offset="1" stop-color="#958ca4"/></radialGradient>
 <linearGradient id="metal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f7f7fb"/><stop offset=".45" stop-color="#b9bccb"/><stop offset=".55" stop-color="#8f93a6"/><stop offset="1" stop-color="#e3e5ee"/></linearGradient>
 <filter id="tex" x="0" y="0" width="100%" height="100%">
  <feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="3" seed="4" result="n"/>
  <feDiffuseLighting in="n" surfaceScale="1.6" lighting-color="#ffffff" result="l"><feDistantLight azimuth="230" elevation="58"/></feDiffuseLighting>
  <feComposite in="l" in2="SourceGraphic" operator="in" result="t"/>
  <feBlend in="SourceGraphic" in2="t" mode="multiply"/>
 </filter>
 <filter id="inner" x="-10%" y="-10%" width="120%" height="120%">
  <feGaussianBlur in="SourceAlpha" stdDeviation="30" result="b"/>
  <feComposite in="SourceAlpha" in2="b" operator="arithmetic" k2="1" k3="-1" result="edge"/>
  <feFlood flood-color="#4a4160" flood-opacity=".85"/><feComposite in2="edge" operator="in" result="sh"/>
  <feMerge><feMergeNode in="SourceGraphic"/><feMergeNode in="sh"/></feMerge>
 </filter>
 <filter id="soft"><feGaussianBlur stdDeviation="18"/></filter>
 <filter id="drop"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#3a3150" flood-opacity=".35"/></filter>
 <clipPath id="c-tib"><path d="{TIB}"/></clipPath><clipPath id="c-fib"><path d="{FIB}"/></clipPath><clipPath id="c-tal"><path d="{TAL}"/></clipPath>
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<radialGradient id="vig" cx="40%" cy="35%" r="85%"><stop offset=".4" stop-color="#231c36" stop-opacity="0"/><stop offset="1" stop-color="#231c36" stop-opacity=".7"/></radialGradient>
<rect width="{W}" height="{H}" fill="url(#vig)"/>
<!-- translucent soft tissue, like the ghosted skin in the renders -->
<path d="M110 -20H790V760C700 860 520 900 380 880C240 860 150 780 120 660C96 560 120 300 110 -20Z" fill="#ffffff" opacity=".16" filter="url(#soft)"/>
<path d="M150 -20H770V720C690 820 520 856 390 840C260 824 180 752 158 650C140 560 160 300 150 -20Z" fill="none" stroke="#ffffff" stroke-opacity=".35" stroke-width="3" filter="url(#soft)"/>
<g filter="url(#drop)">
 <path d="{TAL}" fill="url(#talG)" filter="url(#inner)"/>
 <path d="{TIB}" fill="url(#boneG)" filter="url(#inner)"/>
 <path d="{FIB}" fill="url(#boneG)" filter="url(#inner)"/>
</g>
<g opacity=".7" style="mix-blend-mode:multiply"><path d="{TIB}" fill="#ffffff" filter="url(#tex)"/><path d="{FIB}" fill="#ffffff" filter="url(#tex)"/><path d="{TAL}" fill="#ffffff" filter="url(#tex)"/></g>
<g filter="url(#soft)" opacity=".7"><path d="M300 -20C300 120 296 250 318 340" stroke="#ffffff" stroke-width="40" fill="none"/><path d="M668 -20C668 150 670 330 684 440" stroke="#ffffff" stroke-width="18" fill="none"/><ellipse cx="450" cy="560" rx="80" ry="26" fill="#ffffff"/></g>
{pores("tib",(180,0,610,640),230)}{pores("fib",(625,0,735,700),60)}{pores("tal",(340,500,640,740),60)}
<path d="M486 520C482 580 480 650 484 720" stroke="#6d6280" stroke-opacity=".12" stroke-width="14" fill="none" filter="url(#soft)"/>
<!-- the syndesmotic ligament, repaired: fibres between tibia and fibula below the fixation -->
<g stroke="#f3eef6" stroke-width="2.2" stroke-linecap="round" opacity=".85">
{"".join(f'<path d="M{600+random.uniform(-3,3):.0f} {420+i*7} C{614:.0f} {416+i*7} {626:.0f} {428+i*7} {640+random.uniform(-3,3):.0f} {432+i*7}"/>' for i in range(9))}
</g>
<!-- suture-button fixation: a cord through a tunnel across both bones, a button on each cortex -->
<path d="M214 372L748 372" stroke="#e9e4f0" stroke-width="7" stroke-linecap="round" opacity=".9"/>
<path d="M214 368L748 368" stroke="#ffffff" stroke-width="2" opacity=".8"/>
<g filter="url(#drop)">
 <rect x="196" y="338" width="22" height="70" rx="10" fill="url(#metal)"/>
 <rect x="744" y="340" width="22" height="66" rx="10" fill="url(#metal)"/>
</g>
<circle cx="207" cy="354" r="3" fill="#6f7388"/><circle cx="207" cy="392" r="3" fill="#6f7388"/>
<circle cx="755" cy="356" r="3" fill="#6f7388"/><circle cx="755" cy="390" r="3" fill="#6f7388"/>
</svg>'''
pathlib.Path(sys.argv[1]).write_text(svg)
