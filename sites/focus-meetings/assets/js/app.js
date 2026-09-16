/* The hub is one static page: the only behaviour is the same reveal-on-scroll the
   six event sites use. Elements with .rv fade up once, when they first appear. */
const io=new IntersectionObserver(es=>{es.forEach(e=>{
  if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target)}
})},{threshold:.1,rootMargin:"0px 0px -6% 0px"});
document.querySelectorAll(".rv").forEach(el=>{el.classList.add("pre");io.observe(el)});
