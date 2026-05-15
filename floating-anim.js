/* floating-anim.js — EUSTAQUIA Floating Classroom Symbols
 * Include this ONCE in pages that use grammar-shared.css
 * Adds: <canvas id="floating-canvas"></canvas> + animation
 */
(function () {
  /* Only inject once per page */
  if (document.getElementById('floating-canvas')) return;
  if (document.getElementById('bg-canvas')) return; // skip if original animation already present

  var canvas = document.createElement('canvas');
  canvas.id = 'floating-canvas';
  document.body.prepend(canvas);

  var c = document.getElementById('floating-canvas');
  var x = c.getContext('2d');
  var w, h, particles = [];

  /* Theme-aware emoji sets */
  var isDark = getComputedStyle(document.body).backgroundColor !== 'rgb(255, 255, 255)' &&
               getComputedStyle(document.body).backgroundColor !== 'rgb(240, 245, 255)';

  /* Grammar / dark pages: academic + nature emojis */
  var E_DARK = [
    '📚', '📖', '📝', '✏️', '🔤', '🖊️', '📕', '📗', '📘', '📙',
    '🏛️', '🧠', '💡', '🎯', '⭐', '🌿', '🌱', '⚡', '🔬', '🧪',
    '📐', '📏', '🧮', '🔢', '📊', '📈', '🌍', '🎓', '✂️', '🖇️',
    '💎', '🔮', '🪶', '🌙', '⭐', '🔔'
  ];

  /* Light pages: playful + nature emojis */
  var E_LIGHT = [
    '📐', '📏', '✏️', '📖', '📝', '🔢', '🧮', '🌍', '🧪', '⚡',
    '📚', '🎯', '⭐', '💡', '🔤', '🏛️', '🌿', '✂️', '🌟', '📕',
    '🦋', '🌸', '🌻', '🍀', '🌈', '☀️', '🌙', '⭐', '🐝', '🪻'
  ];

  var E = isDark ? E_DARK : E_LIGHT;

  function resize() {
    w = c.width = window.innerWidth;
    h = c.height = window.innerHeight;
  }

  function spawn() {
    if (particles.length > 30) return;
    particles.push({
      emoji: E[Math.random() * E.length | 0],
      x: Math.random() * w,
      y: h + 30,
      size: 20 + Math.random() * 26,
      vy: -(0.12 + Math.random() * 0.38),
      vx: (Math.random() - 0.5) * 0.28,
      rotation: Math.random() * 360,
      rotSpeed: (Math.random() - 0.5) * 0.45,
      alpha: 0.06 + Math.random() * 0.13
    });
  }

  function draw() {
    x.clearRect(0, 0, w, h);
    particles.forEach(function (p, i) {
      p.x += p.vx;
      p.y += p.vy;
      p.rotation += p.rotSpeed;
      /* Gentle horizontal sway */
      p.x += Math.sin(p.y * 0.008) * 0.3;

      if (p.y < -70 || p.x < -70 || p.x > w + 70) {
        particles.splice(i, 1);
        return;
      }
      x.save();
      x.globalAlpha = p.alpha;
      x.translate(p.x, p.y);
      x.rotate(p.rotation * Math.PI / 180);
      x.font = p.size + 'px serif';
      x.textAlign = 'center';
      x.fillText(p.emoji, 0, 0);
      x.restore();
    });
    while (particles.length < 18) spawn();
    requestAnimationFrame(draw);
  }

  resize();
  /* Initial populate spread across screen */
  for (var i = 0; i < 20; i++) {
    spawn();
    particles[particles.length - 1].y = Math.random() * h;
  }
  window.addEventListener('resize', resize);
  draw();
})();
