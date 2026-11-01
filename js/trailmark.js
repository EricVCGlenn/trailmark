/* Trailmark Insurance Advisors - shared scripts */
(function () {
  // Sticky header shadow
  var hdr = document.querySelector('header.site');
  addEventListener('scroll', function () { if (hdr) hdr.classList.toggle('scrolled', scrollY > 10); }, { passive: true });

  // Mobile menu
  var btn = document.querySelector('.menu-btn'), links = document.getElementById('navlinks');
  if (btn && links) {
    btn.addEventListener('click', function () {
      var o = links.classList.toggle('open');
      btn.setAttribute('aria-expanded', o);
    });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { links.classList.remove('open'); btn.setAttribute('aria-expanded', false); });
    });
  }

  // "Our Products" dropdown
  document.querySelectorAll('.dd-toggle').forEach(function (t) {
    t.addEventListener('click', function (e) {
      e.stopPropagation();
      var dd = t.closest('.dd'), o = dd.classList.toggle('open');
      t.setAttribute('aria-expanded', o);
    });
  });
  document.addEventListener('click', function (e) {
    document.querySelectorAll('.dd.open').forEach(function (dd) {
      if (!dd.contains(e.target)) { dd.classList.remove('open'); dd.querySelector('.dd-toggle').setAttribute('aria-expanded', false); }
    });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') document.querySelectorAll('.dd.open').forEach(function (dd) { dd.classList.remove('open'); });
  });

  // Scroll reveal
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }

  // Pre-select coverage: from links with data-cov, or ?coverage=Auto in the URL
  function check(v) {
    var cb = document.querySelector('.chips input[value="' + v + '"]');
    if (cb) cb.checked = true;
  }
  document.querySelectorAll('[data-cov]').forEach(function (a) {
    a.addEventListener('click', function () { check(a.getAttribute('data-cov')); });
  });
  try {
    var q = new URLSearchParams(location.search).get('coverage');
    if (q) q.split(',').forEach(check);
  } catch (e) {}

  // Footer year
  document.querySelectorAll('.yr').forEach(function (y) { y.textContent = new Date().getFullYear(); });

  // Quote forms -> Formspree
  document.querySelectorAll('form.quote-form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var fd = new FormData(form);
      var cov = fd.getAll('coverage').join(', ') || 'Not specified';
      fd.delete('coverage'); fd.append('coverage', cov);
      var b = form.querySelector('button[type=submit]'), label = b.textContent;
      b.disabled = true; b.textContent = 'Sending…';
      fetch(form.getAttribute('data-endpoint'), { method: 'POST', body: fd, headers: { Accept: 'application/json' } })
        .then(function (r) {
          if (!r.ok) throw new Error('bad');
          form.style.display = 'none';
          form.parentNode.querySelector('.form-success').style.display = 'block';
        })
        .catch(function () {
          b.disabled = false; b.textContent = label;
          alert('Sorry, something went wrong. Please call (214) 531-7932 or email eric@texastrailmark.com.');
        });
    });
  });
})();
