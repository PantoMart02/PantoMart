/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",
  content: [
    "./index.html",
    "./category.html",
    "./product.html",
    "./profile.html",
    "./cart.html",
    "./track.html",
    "./assets/js/**/*.js",
    "./about/**/*.html",
    "./contact/**/*.html",
    "./login/**/*.html",
    "./order/**/*.html",
    "./privacy-policy/**/*.html",
    "./terms/**/*.html"
  ],
  theme: {
    extend: {
      "colors": {
        // ── CSS Variable Colors (support dark mode + opacity modifiers) ──
        "primary":                    "rgb(var(--color-primary) / <alpha-value>)",
        "on-primary":                 "rgb(var(--color-on-primary) / <alpha-value>)",
        "primary-container":          "rgb(var(--color-primary-container) / <alpha-value>)",
        "on-primary-container":       "rgb(var(--color-on-primary-container) / <alpha-value>)",
        "secondary":                  "rgb(var(--color-secondary) / <alpha-value>)",
        "on-secondary":               "rgb(var(--color-on-secondary) / <alpha-value>)",
        "secondary-container":        "rgb(var(--color-secondary-container) / <alpha-value>)",
        "on-secondary-container":     "rgb(var(--color-on-secondary-container) / <alpha-value>)",
        "surface":                    "rgb(var(--color-surface) / <alpha-value>)",
        "on-surface":                 "rgb(var(--color-on-surface) / <alpha-value>)",
        "surface-variant":            "rgb(var(--color-surface-variant) / <alpha-value>)",
        "on-surface-variant":         "rgb(var(--color-on-surface-variant) / <alpha-value>)",
        "surface-container-lowest":   "rgb(var(--color-surface-container-lowest) / <alpha-value>)",
        "surface-container-low":      "rgb(var(--color-surface-container-low) / <alpha-value>)",
        "surface-container":          "rgb(var(--color-surface-container) / <alpha-value>)",
        "surface-container-high":     "rgb(var(--color-surface-container-high) / <alpha-value>)",
        "surface-container-highest":  "rgb(var(--color-surface-container-highest) / <alpha-value>)",
        "surface-dim":                "rgb(var(--color-surface-dim) / <alpha-value>)",
        "surface-bright":             "rgb(var(--color-surface-bright) / <alpha-value>)",
        "background":                 "rgb(var(--color-background) / <alpha-value>)",
        "on-background":              "rgb(var(--color-on-background) / <alpha-value>)",
        "outline":                    "rgb(var(--color-outline) / <alpha-value>)",
        "outline-variant":            "rgb(var(--color-outline-variant) / <alpha-value>)",
        "inverse-surface":            "rgb(var(--color-inverse-surface) / <alpha-value>)",
        "inverse-on-surface":         "rgb(var(--color-inverse-on-surface) / <alpha-value>)",
        // ── Static Colors (less common, no dark variant needed) ──
        "tertiary":                   "#000000",
        "on-tertiary":                "#ffffff",
        "tertiary-container":         "#1e1c14",
        "on-tertiary-container":      "#888379",
        "tertiary-fixed":             "#e8e2d6",
        "tertiary-fixed-dim":         "#cbc6ba",
        "on-tertiary-fixed":          "#1e1c14",
        "on-tertiary-fixed-variant":  "#4a473e",
        "primary-fixed":              "#e5e2e1",
        "primary-fixed-dim":          "#c8c6c5",
        "on-primary-fixed":           "#1c1b1b",
        "on-primary-fixed-variant":   "#474746",
        "secondary-fixed":            "#e3e3de",
        "secondary-fixed-dim":        "#c7c7c2",
        "on-secondary-fixed":         "#1b1c19",
        "on-secondary-fixed-variant": "#464744",
        "inverse-primary":            "#c8c6c5",
        "surface-tint":               "#5f5e5e",
        "error":                      "#ba1a1a",
        "on-error":                   "#ffffff",
        "error-container":            "#ffdad6",
        "on-error-container":         "#93000a",
        "accent-gold":                "#C5A059"
      },
      "borderRadius": {
        "DEFAULT": "0.25rem",
        "lg": "0.5rem",
        "xl": "0.75rem",
        "full": "9999px"
      },
      "spacing": {
        "margin-page": "48px",
        "gutter": "24px",
        "unit-base": "8px",
        "container-max": "1280px",
        "section-padding": "80px"
      },
      "fontFamily": {
        "headline-lg": ["Noto Serif"],
        "body-md": ["Manrope"],
        "display-xl": ["Noto Serif"],
        "label-sm": ["Manrope"],
        "body-lg": ["Manrope"],
        "headline-md": ["Noto Serif"]
      },
      "fontSize": {
        "headline-lg": ["32px", {"lineHeight": "1.3", "fontWeight": "400"}],
        "body-md": ["16px", {"lineHeight": "1.6", "fontWeight": "400"}],
        "display-xl": ["48px", {"lineHeight": "1.2", "letterSpacing": "-0.02em", "fontWeight": "400"}],
        "label-sm": ["12px", {"lineHeight": "1", "letterSpacing": "0.05em", "fontWeight": "600"}],
        "body-lg": ["18px", {"lineHeight": "1.6", "fontWeight": "400"}],
        "headline-md": ["24px", {"lineHeight": "1.4", "fontWeight": "500"}]
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/container-queries'),
  ],
}
