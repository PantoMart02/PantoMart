// ======================
// 🌐 API BASE URL
// ======================
const API_BASE_URL =
  window.location.hostname === 'localhost' ||
  window.location.hostname === '127.0.0.1' ||
  window.location.protocol === 'file:' ||
  window.location.hostname === ''
    ? 'http://localhost:5000'
    : 'http://localhost:5000'; // Fallback to localhost if no real backend is provided

// ======================
// 🔐 GENERIC API REQUEST
// ======================
async function apiRequest(endpoint, options = {}) {
  try {
    console.log('Fetching:', API_BASE_URL + endpoint);
    const res = await fetch(`${API_BASE_URL}${endpoint}`, options);
    if (!res.ok) throw new Error(`API Error: ${res.status}`);
    const data = await res.json();
    console.log('API Response:', data);
    return data;
  } catch (err) {
    console.error('API Request Failed:', err);
    return null;
  }
}

// ======================
// 📦 FETCH FUNCTIONS
// ======================
async function fetchProducts() {
  return await apiRequest('/products');
}

async function fetchProductById(id) {
  if (!id) return null;
  return await apiRequest(`/products/${id}`);
}

async function fetchProductsByCategory(category) {
  if (!category) return [];
  const result = await apiRequest(`/products/category/${category}`);
  return Array.isArray(result) ? result : [];
}

// ======================
// 🖼️ IMAGE URL HELPER
// ======================
function getImageUrl(path) {
  if (!path) return './assets/images/placeholder.jpg';
  if (path.startsWith('http')) return path;
  // Remove leading slash if present to make it relative
  const cleanPath = path.startsWith('/') ? '.' + path : './' + path;
  return cleanPath;
}

window.addEventListener('error', (e) => {
  console.error('GLOBAL JS ERROR:', e.message, 'at', e.filename, 'line', e.lineno);
  // Optional: alert for the user to report back
  // alert('Error: ' + e.message);
});

// ======================
// 🚀 SINGLE GLOBAL INIT
// ======================
document.addEventListener('DOMContentLoaded', () => {
  console.log('--- PANTO MART INIT ---');
  if (typeof initHome === 'function') { console.log('Init Home'); initHome(); }
  if (typeof initCategory === 'function') { console.log('Init Category'); initCategory(); }
  if (typeof initProduct === 'function') { console.log('Init Product'); initProduct(); }
  if (typeof initCart === 'function') { console.log('Init Cart'); initCart(); }
});