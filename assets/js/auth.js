/* ===== GLOBAL AUTH STATE ===== */
document.addEventListener('DOMContentLoaded', () => {
  const userStr = localStorage.getItem('pantoUser');
  if (userStr && userStr !== 'undefined' && userStr !== 'null') {
    // User is logged in, rewrite profile links to point directly to dashboard
    const profileIcon = document.querySelector('.nav-icon[title="Profile"]');
    if (profileIcon && profileIcon.getAttribute('href')) {
      profileIcon.href = profileIcon.getAttribute('href').replace('login/', 'profile/');
    }
  }
});
