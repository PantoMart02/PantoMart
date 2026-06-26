// This file is the replacement for initFixedBackground — injected by patch_fixedbg2.py
function initFixedBackground(image) {
  // Remove previous instance
  var old = document.getElementById('product-fixed-bg');
  if (old) old.remove();
  var oldOverlay = document.getElementById('product-fixed-bg-overlay');
  if (oldOverlay) oldOverlay.remove();
  var oldStyle = document.getElementById('product-fixed-bg-style');
  if (oldStyle) oldStyle.remove();

  // Fixed background: raw product image
  var bg = document.createElement('div');
  bg.id = 'product-fixed-bg';
  bg.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:-2;background-image:url(' + JSON.stringify(image) + ');background-size:cover;background-position:center 30%;pointer-events:none;transform:scale(1.08);transition:opacity 1s ease';
  document.body.appendChild(bg);

  // Dark cinematic overlay + blur
  var ov = document.createElement('div');
  ov.id = 'product-fixed-bg-overlay';
  ov.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;z-index:-1;background:rgba(6,4,3,0.68);backdrop-filter:blur(4px);-webkit-backdrop-filter:blur(4px);pointer-events:none';
  document.body.appendChild(ov);

  // Body dark so gaps between sections look cinematic
  document.body.style.background = '#080604';

  // Inject gap + z-index CSS for all category pages
  var st = document.createElement('style');
  st.id = 'product-fixed-bg-style';
  st.textContent = 'body{background:#080604!important}#product-container{position:relative;z-index:1}.fit-strip,.fit-motion,.fit-why,.fit-eng,.fit-outcome,.fit-howto,.fit-social,.fit-final{margin-top:8px}.sp{padding-bottom:40px!important}#product-container>div>section+section{margin-top:8px}#product-container>div>div+section{margin-top:8px}#product-container>div>div+div{margin-top:8px}.fashion-page>section+section,.fashion-page>div+div{margin-top:8px}';
  document.head.appendChild(st);
}
