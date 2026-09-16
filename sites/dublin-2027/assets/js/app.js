const PAGES=["welcome","programme","venue","registration","industry","contacts"];
const io=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}})},{threshold:.1,rootMargin:"0px 0px -6% 0px"});
function obs(r){(r||document).querySelectorAll(".rv:not(.in)").forEach(el=>{el.classList.add("pre");io.observe(el)})}
obs();
function go(id){
  const t=document.getElementById(id);
  PAGES.forEach(p=>{if(p!==id)document.getElementById(p).hidden=true});
  t.hidden=false; t.classList.remove("pg"); void t.offsetWidth; t.classList.add("pg");
  document.querySelectorAll('.nav a[data-go]').forEach(a=>a.classList.toggle('on',a.dataset.go===id));
  scrollTo({top:0,behavior:"auto"}); obs(t);
}
document.addEventListener("click",e=>{const l=e.target.closest("[data-go]");if(!l)return;e.preventDefault();go(l.dataset.go)});
const nav=document.getElementById("nav"),stick=document.getElementById("stick");
function darkCheck(){
  const bar=document.getElementById("stick"); if(!bar) return;
  const r=bar.getBoundingClientRect(); const y=r.top+r.height/2;
  let over=false;
  document.querySelectorAll(".bleed:not([hidden]) , footer").forEach(el=>{
    if(el.closest("main") && el.closest("main").hidden) return;
    const b=el.getBoundingClientRect();
    if(b.top < y && b.bottom > y) over=true;
  });
  bar.classList.toggle("onlight", over);
}
addEventListener("scroll",()=>{document.body.classList.toggle("scrolled",scrollY>40);darkCheck();nav.classList.toggle("stuck",scrollY>10);stick.classList.toggle("show",scrollY>260)},{passive:true});
const cio=new IntersectionObserver(es=>{es.forEach(e=>{
  if(!e.isIntersecting)return;
  const el=e.target, end=+el.dataset.to; let t0=null;
  requestAnimationFrame(function step(ts){
    if(!t0)t0=ts;
    const k=Math.min((ts-t0)/1300,1);
    el.textContent=Math.round(end*(1-Math.pow(1-k,3)));
    if(k<1)requestAnimationFrame(step);
  });
  cio.unobserve(el);
})},{threshold:.6});
document.querySelectorAll("[data-to]").forEach(el=>cio.observe(el));

/* Dublin: 6-7 May 2027 (from the ESSKA banner). The start time is not confirmed,
   so 09:00 Dublin time (+01:00, Irish summer time) is assumed, as on Rome.
   The early-rate deadline is not confirmed: leave EARLY_RATE as null until ESSKA
   supplies it, and the fee countdown hides and shows TBC instead. Set it in Dublin
   time, e.g. EARLY_RATE="2027-MM-DDT23:59:59+01:00" (or +00:00 before 28 March 2027). */
const MEETING_START="2027-05-06T09:00:00+01:00";
const EARLY_RATE=null;

if(MEETING_START){
  const MEET=new Date(MEETING_START).getTime();
  const meetTick=()=>{
    const d=document.getElementById("uD"); if(!d) return;
    let m=MEET-Date.now(); if(m<0) m=0;
    const s=Math.floor(m/1000);
    d.textContent=Math.floor(s/86400);
    document.getElementById("uH").textContent=String(Math.floor(s%86400/3600)).padStart(2,"0");
    document.getElementById("uM").textContent=String(Math.floor(s%3600/60)).padStart(2,"0");
    const d2=document.getElementById("uD2"); if(d2) d2.textContent=Math.floor(s/86400);
  };
  meetTick(); setInterval(meetTick,20000);
}else{
  document.getElementById("cd").hidden=true;
  document.getElementById("cdTba").hidden=false;
}

if(EARLY_RATE){
  const DL=new Date(EARLY_RATE).getTime(), pad=n=>String(n).padStart(2,"0");
  const txt=new Date(EARLY_RATE).toLocaleDateString("en-GB",{day:"numeric",month:"long",year:"numeric"});
  /* the header tab and the sticky bar give the early-rate date as "until …" */
  const erOpts={day:"numeric",month:"long"};
  document.querySelectorAll(".er-until-short").forEach(el=>el.textContent="until "+new Date(EARLY_RATE).toLocaleDateString("en-GB",erOpts));
  document.querySelectorAll(".er-until").forEach(el=>el.textContent="until "+new Date(EARLY_RATE).toLocaleDateString("en-GB",{...erOpts,year:"numeric"}));
  ["erDate","erDate2","erDate3"].forEach(id=>{const el=document.getElementById(id); if(el) el.textContent=txt;});
  const tick=()=>{let m=DL-Date.now();if(m<0)m=0;const s=Math.floor(m/1000);
    cD.textContent=Math.floor(s/86400);cH.textContent=pad(Math.floor(s%86400/3600));
    cM.textContent=pad(Math.floor(s%3600/60));cS.textContent=pad(s%60)};
  tick();setInterval(tick,1000);
}else{
  ["erCount","erNote"].forEach(id=>{const el=document.getElementById(id); if(el) el.hidden=true;});
}

/* hero artwork follows the pointer a little. Skipped for reduced motion and on
   stacked layouts, where the artwork is a banner rather than a side panel. */
(function(){
  const hero=document.querySelector(".hero"), art=document.querySelector(".hero .art");
  if(!hero||!art) return;
  if(matchMedia("(prefers-reduced-motion:reduce)").matches) return;
  if(!matchMedia("(min-width:1081px)").matches) return;
  hero.addEventListener("pointermove",e=>{
    const r=hero.getBoundingClientRect();
    const x=(e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
    art.style.setProperty("--px",(x*-24).toFixed(1)+"px");
    art.style.setProperty("--py",(y*-14).toFixed(1)+"px");
  },{passive:true});
  hero.addEventListener("pointerleave",()=>{
    art.style.setProperty("--px","0px"); art.style.setProperty("--py","0px");
  });
})();





/* ---------------------------------------------------------------------------
   Programme: one day at a time, live search, and blocks that open on click.
   The whole header row is the button, so there is no separate show/hide link.
   --------------------------------------------------------------------------- */
(function(){
  const days = document.getElementById("progDays");
  if(!days) return;
  const q = document.getElementById("progQ");
  const empty = document.getElementById("progEmpty");
  const chips = [...document.querySelectorAll(".pchip")];
  let term = "", activeDay = "1";

  const rows = [...days.querySelectorAll(".prow")];
  rows.forEach(r => r.querySelectorAll(".ptitle,.ptx,.psp,.psub:not(.psub-note),.pnote-t").forEach(
    el => el.dataset.raw = el.textContent));

  const esc = t => t.replace(/[&<>]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));
  const paint = (el, t) => {
    const raw = el.dataset.raw;
    if(!t){ el.textContent = raw; return false; }
    const i = raw.toLowerCase().indexOf(t);
    if(i < 0){ el.textContent = raw; return false; }
    el.innerHTML = esc(raw.slice(0,i)) + "<mark>" + esc(raw.slice(i,i+t.length)) +
                   "</mark>" + esc(raw.slice(i+t.length));
    return true;
  };

  const setOpen = (row, open) => {
    const btn = row.querySelector(".prow-btn");
    if(!btn) return;
    row.classList.toggle("is-open", open);
    btn.setAttribute("aria-expanded", open ? "true" : "false");
    row.querySelector(".ptalks-wrap").hidden = !open;
  };

  function apply(){
    let shown = 0;
    days.querySelectorAll(".pday").forEach(d => d.hidden = d.dataset.day !== activeDay);
    rows.forEach(row => {
      if(row.dataset.day !== activeDay) return;
      const isBreak = row.classList.contains("break");
      let hit = false;
      row.querySelectorAll(".ptitle,.ptx,.psp,.psub:not(.psub-note),.pnote-t").forEach(el => { if(paint(el, term)) hit = true; });
      const visible = isBreak ? !term : (!term || hit);
      row.hidden = !visible;
      if(visible && !isBreak) shown++;
      if(visible && term){
        setOpen(row, true);          /* a search result opens itself */
      }
    });
    empty.hidden = shown > 0;
  }

  q.addEventListener("input", e => { term = e.target.value.trim().toLowerCase(); apply(); });
  chips.forEach(c => c.addEventListener("click", () => {
    activeDay = c.dataset.filter;
    chips.forEach(x => x.setAttribute("aria-pressed", x === c ? "true" : "false"));
    apply();
  }));
  document.getElementById("progClear").addEventListener("click", () => {
    term = ""; q.value = ""; apply(); q.focus();
  });

  days.addEventListener("click", e => {
    const btn = e.target.closest(".prow-btn");
    if(btn){
      const row = btn.closest(".prow");
      setOpen(row, btn.getAttribute("aria-expanded") !== "true");
      return;
    }
    const c = e.target.closest(".pcollapse");
    if(c){
      const expand = c.textContent.trim() === "Expand all";
      c.closest(".pday").querySelectorAll(".prow").forEach(r => setOpen(r, expand));
      c.textContent = expand ? "Collapse all" : "Expand all";
    }
  });

  apply();
})();

/* The hero fills the screen below the utility bar and nav, so the section
   underneath only appears once you scroll. Their combined height changes when
   the nav wraps, so it is measured rather than hard-coded. Skipped while
   scrolled, because the utility bar collapses then and the hero is already
   out of view. */
(function(){
  const util = document.getElementById("util"), nav = document.getElementById("nav");
  if(!util || !nav) return;
  const setChrome = () => {
    if(document.body.classList.contains("scrolled")) return;
    document.documentElement.style.setProperty(
      "--chrome", (util.offsetHeight + nav.offsetHeight) + "px");
  };
  setChrome();
  /* the nav grows a little once Onest has loaded, so measure again then:
     otherwise the hero is sized against the fallback font and overshoots */
  if(document.fonts && document.fonts.ready) document.fonts.ready.then(setChrome);
  addEventListener("resize", setChrome, {passive:true});
})();

/* Registration: mark the fee period that applies today, or the first one
   still to come, in both the period cards and the fee table columns. */
(function(){
  const periods=[...document.querySelectorAll(".fee-period")];
  if(!periods.length) return;
  const now=Date.now();
  let key=null, live=false;
  for(const p of periods){
    const s=new Date(p.dataset.start).getTime(), e=new Date(p.dataset.end).getTime();
    if(now>=s && now<=e){ key=p.dataset.period; live=true; break; }
    if(now<s && !key) key=p.dataset.period;
  }
  if(!key) return;
  document.querySelectorAll('[data-period="'+key+'"]').forEach(el=>el.classList.add(live?"is-now":"is-next"));
  const tag=document.querySelector('.fee-period[data-period="'+key+'"] .fp-tag');
  if(tag){ tag.textContent=live?"Current rate":"Opens first"; tag.hidden=false; }
})();
