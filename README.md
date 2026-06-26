# 🛒 PantoMart Luxury Lifestyle Platform

> [!CAUTION]
> **Not for Production or Actual Work**
> This codebase is strictly for a start-up proof of concept. Nobody should use this codebase in a real-world scenario or deploy it for actual work.

Welcome to **PantoMart**, a premium lifestyle e-commerce platform offering carefully curated products across multiple lifestyle segments. Designed with high-end aesthetics and an immersive user experience, PantoMart categorizes luxury products intuitively, making shopping seamless.

## ✨ Key Features
- **Dynamic Product Pages:** Built to be highly SEO-friendly and dynamically managed per lifestyle segment (e.g., `care`, `style`, `fit`, `pet`, `space`).
- **Responsive & Premium UI:** Crafted using Tailwind CSS with beautiful interactions and animations.
- **Robust Python Tooling:** A suite of custom Python scripts designed to automate asset generation, validate data structures, patch HTML, and verify data integrity.
- **Modular Asset Architecture:** Organized asset handling to separate logic, styling, and media for scalability and clarity.
- **Dedicated Backend:** Local Node.js environment configured for product seeding and mock APIs.

## 🛠️ Technology Stack
- **Frontend:** HTML5, JavaScript (Vanilla/ES6)
- **Styling:** Tailwind CSS (v3), custom CSS properties
- **Animations & DOM manipulation:** Framer Motion, JSDOM
- **Build Tools & Utilities:** Python 3 (custom scripts), Node.js, npm

## 📂 Project Structure

```text
PantoMart/
├── assets/             # Modular CSS, JS, and product images
├── backend/            # Local Node server scripts, database seeds, and APIs
├── login/              # User authentication flows
├── contact/            # Support and contact interfaces
├── index.html          # Main landing page
├── cart.html           # Shopping cart interface
├── category.html       # Dynamic category templates
├── product.html        # Individual product view
├── profile.html        # User account management
├── track.html          # Order tracking interface
└── package.json        # NPM dependencies and project scripts
```

### ⚙️ Automation Scripts
The repository is bundled with a powerful set of Python utilities for ongoing maintenance and content management:
- `build_all_products.py`: Regenerates product data and builds HTML views.
- `update_products.py`: Batch updates to product listings.
- `patch_*.py`: Component-specific patching utilities (e.g., `patch_style.py`, `patch_care.py`, `patch_space.py`).
- `check_*.py`: Diagnostic scripts to verify API keys, data structures, review formats, and image integrity (e.g., `check_images.py`, `check_api_keys.py`).

## 🚀 Setup & Installation

### Prerequisites
- [Node.js](https://nodejs.org/en/) (v16 or higher recommended)
- [Python 3.x](https://www.python.org/downloads/) (for running utility scripts)

### Installation Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/PantoMart02/PantoMart.git
   cd PantoMart
   ```

2. **Install Node dependencies:**
   ```bash
   npm install
   ```

3. **Build Tailwind CSS:**
   ```bash
   npm run build:css
   ```
   *(To watch for CSS changes during development, run: `npm run watch:css`)*

4. **Serve the project:**
   You can use any local web server (such as Live Server in VS Code, or Python's `http.server`) to serve the root directory.
   ```bash
   python -m http.server 8000
   ```
   Navigate to `http://localhost:8000/` in your web browser.

## 📜 License
Please refer to the `LICENSE` file at the root of the project for distribution terms and limitations.

---
*Document formally created on June 26, 2026.*
