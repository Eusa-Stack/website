/* ══════════════════════════════════════
   FOOTER INJECTOR — loads shared footer
   Usage: <link rel="stylesheet" href="footer.css">
          <div id="shared-footer-placeholder"></div>
          <script src="footer-inject.js"></script>
   ══════════════════════════════════════ */

(function() {
  // Shared footer HTML — injected into #shared-footer-placeholder
  var FOOTER_HTML = '<footer id="shared-footer">' +
    '<p>© <span class="ft">EUSTAQUIA</span> — Global Educator</p>' +
    '<p style="margin-top:4px">' +
      '<a href="classroom.html">Classroom</a> · ' +
      '<a href="https://www.youtube.com/@Eusell77" target="_blank">YouTube</a> · ' +
      '<a href="#">Privacy</a>' +
      '<span class="ft-sep">·</span>' +
      '<a href="https://tech-ant.fi" target="_blank" class="ft-brand">tech-ant</a>' +
      '<span class="ft-dash">—</span>' +
      '<a href="https://tech-ant.fi" target="_blank" class="ft-url">tech-ant.fi</a>' +
    '</p>' +
  '</footer>';

  function injectFooter() {
    var placeholder = document.getElementById('shared-footer-placeholder');
    if (placeholder) {
      placeholder.insertAdjacentHTML('beforebegin', FOOTER_HTML);
      placeholder.remove();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectFooter);
  } else {
    injectFooter();
  }
})();