/* Demosh Designs site script: header, menu, videos, reveal, gallery, WhatsApp quote builder */
(function () {
  var WA = '254704121852';
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var small = window.matchMedia('(max-width: 700px)').matches;
  var conn = navigator.connection || {};
  var saveData = !!conn.saveData;

  // Header turns solid after scrolling (always solid on pages without a dark hero)
  var hdr = document.querySelector('.hdr');
  var hero = document.querySelector('.hero');
  function onScroll() {
    if (!hdr) return;
    var limit = hero ? Math.min(hero.offsetHeight - 80, 120) : -1;
    hdr.classList.toggle('solid', window.scrollY > limit);
  }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Mobile menu
  var menu = document.querySelector('.mnav');
  var openBtn = document.querySelector('.menu-btn');
  var closeBtn = document.querySelector('.mnav-close');
  function setMenu(open) {
    if (!menu) return;
    menu.classList.toggle('open', open);
    menu.setAttribute('aria-hidden', open ? 'false' : 'true');
    openBtn && openBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.style.overflow = open ? 'hidden' : '';
    if (open && closeBtn) closeBtn.focus();
  }
  openBtn && openBtn.addEventListener('click', function () { setMenu(true); });
  closeBtn && closeBtn.addEventListener('click', function () { setMenu(false); openBtn.focus(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { setMenu(false); closeLb(); } });

  // Videos: Mixkit clips (free licence). A local copy in assets/media/<name>.mp4 is used first when it exists.
  function mixkit(id) {
    var q = small ? '360' : '720';
    return 'https://assets.mixkit.co/videos/' + id + '/' + id + '-' + q + '.mp4';
  }
  function loadVideo(v) {
    if (v.dataset.loaded) return;
    v.dataset.loaded = '1';
    if (v.dataset.local) {
      var s1 = document.createElement('source'); s1.src = v.dataset.local; s1.type = 'video/mp4'; v.appendChild(s1);
    }
    var s2 = document.createElement('source'); s2.src = mixkit(v.dataset.mx); s2.type = 'video/mp4'; v.appendChild(s2);
    v.muted = true; v.loop = true; v.playsInline = true;
    v.setAttribute('muted', ''); v.setAttribute('playsinline', '');
    v.addEventListener('playing', function () { v.classList.add('on'); }, { once: true });
    v.load();
    var p = v.play(); if (p && p.catch) p.catch(function () {});
  }
  var vids = Array.prototype.slice.call(document.querySelectorAll('video[data-mx]'));
  if (!reduce && !saveData) {
    if ('IntersectionObserver' in window) {
      var vo = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          var v = en.target;
          if (en.isIntersecting) { loadVideo(v); if (v.paused) { var p = v.play(); if (p && p.catch) p.catch(function () {}); } }
          else if (v.dataset.loaded) { v.pause(); }
        });
      }, { rootMargin: '250px 0px' });
      vids.forEach(function (v) { vo.observe(v); });
    } else { vids.forEach(loadVideo); }
  }

  // Rotating word in the home hero
  var swap = document.querySelector('[data-swap]');
  if (swap && !reduce) {
    var words = swap.dataset.swap.split('|'), i = 0;
    setInterval(function () {
      i = (i + 1) % words.length;
      swap.animate ? swap.animate([{ opacity: 1, transform: 'none' }, { opacity: 0, transform: 'translateY(-14px)' }], { duration: 220, fill: 'forwards' }).onfinish = function () {
        swap.textContent = words[i];
        swap.animate([{ opacity: 0, transform: 'translateY(14px)' }, { opacity: 1, transform: 'none' }], { duration: 260, fill: 'forwards' });
      } : (swap.textContent = words[i]);
    }, 2400);
  }

  // Reveal on scroll
  var rv = document.querySelectorAll('.rv');
  if ('IntersectionObserver' in window && !reduce) {
    var ro = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); ro.unobserve(en.target); } });
    }, { threshold: 0.12 });
    rv.forEach(function (el) { ro.observe(el); });
  } else { rv.forEach(function (el) { el.classList.add('in'); }); }

  // Year
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });

  /* ---------- Gallery ---------- */
  var gal = document.getElementById('gallery');
  var lb = document.querySelector('.lb');
  function closeLb() { if (lb && lb.classList.contains('open')) { lb.classList.remove('open'); document.body.style.overflow = ''; } }
  if (gal && window.DEMOSH_GALLERY) {
    var items = window.DEMOSH_GALLERY;
    items.forEach(function (it, idx) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'g-item rv';
      b.dataset.cat = it.cat;
      var art = it.img ? '<img src="' + it.img + '" alt="' + it.title.replace(/"/g, '&quot;') + '" loading="lazy">' : window.demoshMock(it);
      b.innerHTML = '<span class="art">' + art + '</span><span class="cap"><span>' + it.title + '</span><small>' + it.cat + '</small></span>';
      b.addEventListener('click', function () {
        if (!lb) return;
        lb.querySelector('.art').innerHTML = art;
        lb.querySelector('.t').textContent = it.title;
        var msg = 'Hi Demosh Designs, I saw "' + it.title + '" on your website and I would like something similar.';
        lb.querySelector('a').href = 'https://wa.me/' + WA + '?text=' + encodeURIComponent(msg);
        lb.classList.add('open'); document.body.style.overflow = 'hidden';
        lb.querySelector('.lb-close').focus();
      });
      gal.appendChild(b);
      if ('IntersectionObserver' in window && !reduce) ro.observe(b); else b.classList.add('in');
    });
    document.querySelectorAll('.filters button').forEach(function (btn) {
      btn.addEventListener('click', function () {
        document.querySelectorAll('.filters button').forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
        btn.setAttribute('aria-pressed', 'true');
        var f = btn.dataset.f;
        gal.querySelectorAll('.g-item').forEach(function (g) { g.classList.toggle('hide', f !== 'all' && g.dataset.cat !== f); g.classList.add('in'); });
      });
    });
    if (lb) {
      lb.addEventListener('click', function (e) { if (e.target === lb) closeLb(); });
      lb.querySelector('.lb-close').addEventListener('click', closeLb);
    }
  }

  /* ---------- WhatsApp quote builder ---------- */
  var form = document.getElementById('quote');
  if (form) {
    var pre = new URLSearchParams(location.search).get('service');
    if (pre) {
      var box = form.querySelector('input[name=service][value="' + pre + '"]');
      if (box) box.checked = true;
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form);
      var services = d.getAll('service');
      var lines = ['Hi Demosh Designs, I would like a quote.'];
      if (d.get('name')) lines.push('Name: ' + d.get('name'));
      if (services.length) lines.push('Service: ' + services.join(', '));
      if (d.get('item')) lines.push('Item: ' + d.get('item'));
      if (d.get('qty')) lines.push('Quantity: ' + d.get('qty'));
      if (d.get('date')) lines.push('Needed by: ' + d.get('date'));
      if (d.get('details')) lines.push('Details: ' + d.get('details'));
      lines.push('I can share my logo or design here on WhatsApp.');
      window.open('https://wa.me/' + WA + '?text=' + encodeURIComponent(lines.join('\n')), '_blank', 'noopener');
    });
  }
})();
