# PantoMart Luxury Lifestyle Platform

> [!CAUTION]
> **Not for Production or Actual Work**
> This codebase is strictly for a start-up proof of concept. Nobody should use this codebase in a real-world scenario or deploy it for actual work.

PantoMart is a premium lifestyle e-commerce platform offering carefully curated products across multiple lifestyle segments. 

## Overview
The platform provides a modern and immersive shopping experience featuring high-end aesthetics, semantic architectures, and dynamic product management. Built primarily using HTML, JavaScript, and TailwindCSS (as evidenced by `tailwind.config.js`).

## Project Structure
This project follows a strict semantic asset architecture:
- `/assets/`: Contains modular CSS, JS, and Images.
- **Category Folders**: Folders such as `/care`, `/style`, etc., contain dynamic SEO-friendly product pages.
- **Core Pages**: Pages like `/about`, `/profile`, `index.html`, `cart.html`, and others are hosted at the root level.
- **Scripts**: Various Python scripts (e.g., `build_all_products.py`, `update_products.py`) are used for building, patching, checking data integrity, and managing the dynamic backend content.

## Setup and Development
To install dependencies and start the local development server:
```bash
npm install
npm start # or equivalent depending on package.json scripts
```

Ensure you have run the appropriate python build scripts if you are making changes to product configurations or category templates.

## Licensing
Please see the `LICENSE` file for more details regarding the rights and limitations of using this source code.
