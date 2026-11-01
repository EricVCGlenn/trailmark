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

  // File picker: show chosen file names, support drag and drop
  document.querySelectorAll('.file-input').forEach(function (inp) {
    var drop = document.querySelector('label.file-drop[for="' + inp.id + '"]');
    if (!drop) return;
    var txt = drop.querySelector('.file-text'), orig = txt.innerHTML;
    function show() {
      var n = Array.prototype.map.call(inp.files, function (f) { return f.name; });
      txt.innerHTML = n.length ? '<strong>' + n.length + ' file' + (n.length > 1 ? 's' : '') + ' attached</strong><small>' + n.join(', ') + '</small>' : orig;
    }
    inp.addEventListener('change', show);
    ['dragenter', 'dragover'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.add('drag'); }); });
    ['dragleave', 'drop'].forEach(function (ev) { drop.addEventListener(ev, function (e) { e.preventDefault(); drop.classList.remove('drag'); }); });
    drop.addEventListener('drop', function (e) { if (e.dataTransfer && e.dataTransfer.files.length) { inp.files = e.dataTransfer.files; show(); } });
  });

  // Contact forms -> Formspree. If an attachment is rejected, resend without it.
  document.querySelectorAll('form.quote-form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var fd = new FormData(form);
      var cov = fd.getAll('coverage').join(', ') || 'Not specified';
      fd.delete('coverage'); fd.append('coverage', cov);
      var files = form.querySelector('.file-input'), hasFiles = files && files.files.length > 0;
      var b = form.querySelector('button[type=submit]'), label = b.textContent;
      b.disabled = true; b.textContent = 'Sending…';
      function send(data) { return fetch(form.getAttribute('data-endpoint'), { method: 'POST', body: data, headers: { Accept: 'application/json' } }); }
      function done(note) {
        form.style.display = 'none';
        var ok = form.parentNode.querySelector('.form-success');
        if (note) ok.querySelector('.ok-msg').textContent = note;
        ok.style.display = 'block';
      }
      function fail() {
        b.disabled = false; b.textContent = label;
        alert('Sorry, something went wrong. Please call (214) 531-7932 or email eric@texastrailmark.com.');
      }
      send(fd).then(function (r) {
        if (r.ok) return done();
        if (!hasFiles) throw new Error('bad');
        fd.delete('attachment');
        fd.append('attachment_note', 'Visitor tried to attach a file, but it could not be uploaded.');
        return send(fd).then(function (r2) {
          if (!r2.ok) throw new Error('bad');
          done('Eric received your message, but your file could not be uploaded. Please email your policy to eric@texastrailmark.com and he\'ll take a look.');
        });
      }).catch(fail);
    });
  });
})();
