/* The hub is one static page: the only behaviour is the same reveal-on-scroll the
   six event sites use. Elements with .rv fade up once, when they first appear. */
const io=new IntersectionObserver(es=>{es.forEach(e=>{
  if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}
})},{threshold:.1,rootMargin:"0px 0px -6% 0px"});
document.querySelectorAll(".rv").forEach(el=>{el.classList.add("pre");io.observe(el)});

/* The opening block (kicker, heading, copy and the four facts) starts on the same left
   edge as the words "Focus Meetings" in the header. The header and the page use
   different widths, so the edge is measured rather than fixed. Phones keep the normal
   page gutter. */
(function(){
  const bn=document.querySelector(".brand .bn"), wrap=document.querySelector(".hero > .wrap");
  if(!bn||!wrap) return;
  const set=()=>{
    if(innerWidth<=760){ wrap.style.removeProperty("--hero-left"); return; }
    wrap.style.setProperty("--hero-left", Math.round(bn.getBoundingClientRect().left)+"px");
  };
  set();
  if(document.fonts && document.fonts.ready) document.fonts.ready.then(set);
  addEventListener("load", set);
  addEventListener("resize", set, {passive:true});
})();
