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
document.querySelectorAll(".tabs button").forEach(b=>b.addEventListener("click",()=>{
  const d=b.dataset.day;
  document.querySelectorAll(".tabs button").forEach(x=>x.setAttribute("aria-selected",x===b?"true":"false"));
  const s=document.getElementById("day"+d),h=document.getElementById("day"+(d==="1"?"2":"1"));
  h.hidden=true;s.hidden=false;s.classList.remove("pg");void s.offsetWidth;s.classList.add("pg");
}));
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
/* meeting start; change this one line if the date moves */
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

const MEETING_START="2027-10-08T09:00:00+02:00";
const MEET=new Date(MEETING_START).getTime();
function meetTick(){
  const d=document.getElementById("uD"); if(!d) return;
  let m=MEET-Date.now(); if(m<0) m=0;
  const s=Math.floor(m/1000);
  d.textContent=Math.floor(s/86400);
  document.getElementById("uH").textContent=String(Math.floor(s%86400/3600)).padStart(2,"0");
  document.getElementById("uM").textContent=String(Math.floor(s%3600/60)).padStart(2,"0");
  const d2=document.getElementById("uD2"); if(d2) d2.textContent=Math.floor(s/86400);
}
meetTick(); setInterval(meetTick,20000);
/* early rate deadline; placeholder until ESSKA confirms it */
const EARLY_RATE="2027-06-30T23:59:59+02:00";
const DL=new Date(EARLY_RATE).getTime(), pad=n=>String(n).padStart(2,"0");
(function(){const el=document.getElementById("erDate");
  if(el) el.textContent=new Date(EARLY_RATE).toLocaleDateString("en-GB",
    {day:"numeric",month:"long",year:"numeric"});})();
function tick(){let m=DL-Date.now();if(m<0)m=0;const s=Math.floor(m/1000);
  cD.textContent=Math.floor(s/86400);cH.textContent=pad(Math.floor(s%86400/3600));
  cM.textContent=pad(Math.floor(s%3600/60));cS.textContent=pad(s%60)}
tick();setInterval(tick,1000);
