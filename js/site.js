(function () {
  // Mobile menu
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('site-nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) {
        nav.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
        btn.focus();
      }
    });
  }

  // Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // Contact form -> opens the visitor's email app addressed to Reborn Ready
  var form = document.getElementById('contact-form');
  if (form) {
    var key = new URLSearchParams(location.search).get('reason');
    if (key) {
      var opt = form.querySelector('option[data-key="' + key + '"]');
      if (opt) { opt.selected = true; var nm = form.elements['name']; if (nm) nm.focus({preventScroll: true}); }
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var err = document.getElementById('form-error');
      var name = form.elements['name'].value.trim();
      var reason = form.elements['reason'].value;
      var msg = form.elements['message'].value.trim();
      var phone = form.elements['phone'].value.trim();
      var email = form.elements['email'].value.trim();
      if (!name || !msg || (!phone && !email)) {
        err.textContent = 'Please add your name, a message, and a phone number or email so we can get back to you.';
        err.classList.add('show');
        return;
      }
      err.classList.remove('show');
      var body = 'Name: ' + name + '\n' +
        (phone ? 'Phone: ' + phone + '\n' : '') +
        (email ? 'Email: ' + email + '\n' : '') +
        'Reason: ' + reason + '\n\n' + msg;
      var subject = 'Website message: ' + reason;
      window.location.href = 'mailto:info@rebornreadyhousing.org?subject=' +
        encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    });
  }
})();
