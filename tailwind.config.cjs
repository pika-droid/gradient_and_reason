/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        garamond: ['"EB Garamond"', 'Georgia', 'serif'],
        literata: ['"Literata"', 'Georgia', 'serif'],
        mono: ['"JetBrains Mono"', 'Consolas', 'monospace']
      },
      maxWidth: {
        prose: '740px'
      },
      spacing: {
        'section': '6.5rem'
      },
      colors: {
        bg: 'var(--bg)',
        surface: 'var(--surface)',
        'surface-raised': 'var(--surface-raised)',
        ink: 'var(--ink)',
        'ink-strong': 'var(--ink-strong)',
        'ink-dim': 'var(--ink-dim)',
        'ink-faint': 'var(--ink-faint)',
        accent: 'var(--accent)',
        'accent-pale': 'var(--accent-pale)',
        'code-bg': 'var(--code-bg)',
        'code-border': 'var(--code-border)',
        'code-txt': 'var(--code-txt)'
      }
    }
  },
  plugins: [],
}
