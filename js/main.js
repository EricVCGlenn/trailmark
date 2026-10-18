/* Trailmark Insurance Advisors — nav + callbar */
(function(){
  var toggle=document.querySelector('.nav-toggle');
  var nav=document.querySelector('.nav');
  var close=document.querySelector('.nav-close');
  if(toggle&&nav){
    toggle.addEventListener('click',function(){
      nav.classList.add('open');toggle.setAttribute('aria-expanded','true');
    });
  }
  if(close&&nav){
    close.addEventListener('click',function(){
      nav.classList.remove('open');toggle&&toggle.setAttribute('aria-expanded','false');
    });
  }
  // close menu when a link is tapped (mobile)
  nav&&nav.querySelectorAll('a').forEach(function(a){
    a.addEventListener('click',function(){
      if(window.innerWidth<=720){nav.classList.remove('open');toggle&&toggle.setAttribute('aria-expanded','false');}
    });
  });
  // bottom callbar reveal on scroll (mobile)
  var bar=document.querySelector('.callbar');
  if(bar){
    var onScroll=function(){
      if(window.pageYOffset>300)bar.classList.add('show');else bar.classList.remove('show');
    };
    window.addEventListener('scroll',onScroll,{passive:true});onScroll();
  }
})();
