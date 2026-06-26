// ── PantoMart Theme Toggle ──
// Applies saved theme immediately to prevent flash of wrong theme
(function () {
  const saved = localStorage.getItem('pantoTheme');
  // Always toggle on <html>, never on body (body gets product-page classes)
  if (saved === 'dark') document.documentElement.classList.add('dark');
  else document.documentElement.classList.remove('dark');
})();

function applyThemeIcons() {
  const isDark = document.documentElement.classList.contains('dark');
  document.querySelectorAll('[data-theme-toggle]').forEach(btn => {
    const sun  = btn.querySelector('[data-sun]');
    const moon = btn.querySelector('[data-moon]');
    if (sun)  sun.style.display  = isDark ? 'none' : 'inline';
    if (moon) moon.style.display = isDark ? 'inline' : 'none';
  });
}

function toggleTheme() {
  const isDark = document.documentElement.classList.toggle('dark');
  localStorage.setItem('pantoTheme', isDark ? 'dark' : 'light');
  applyThemeIcons();
}

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[data-theme-toggle]').forEach(btn => {
    btn.addEventListener('click', toggleTheme);
  });
  applyThemeIcons();
});
