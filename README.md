# Gradient and Reason

> **On machine knowledge & philosophical loss.**
> Computational essays integrating machine learning, analytics, and epistemology.

**Gradient and Reason** is a technical philosophy blog operating at the intersection of empirical rigor (Machine Learning, analytics) and philosophical inquiry (epistemology, cognitive science, memory, and structural representations).

Built with **Astro**, **MDX**, and **TailwindCSS**, this repository implements a tailored dark-academic, minimalist aesthetic optimized for readability, typesetting quality, and high performance (100/100 Lighthouse score).

---

## 🎨 Design & Aesthetic Principles

- **Typography**: Elegant Serif fonts ([Playfair Display](https://fonts.google.com/specimen/Playfair+Display) / [Garamond](https://fonts.google.com/specimen/EB+Garamond) and [Literata](https://fonts.google.com/specimen/Literata)) paired with clean, minimalist Sans-Serif system typography for meta-information and navigation.
- **Visual Staggering**: Smooth page load intersection observers wrapped in `<ScrollReveal />` to present text dynamically as the reader scrolls.
- **Dark & Light Themes**: Accessible high-contrast dark-mode and light-mode configurations via a tailwind-integrated `<ThemeToggle />` component.
- **Responsive Layout**: Designed to render flawlessly on mobile, tablet, and desktop screens with custom code blocks, tables, and math equations that support internal horizontal scrolling instead of causing layout overflow.

---

## 📁 Repository Structure

```text
├── .astro/                 # Auto-generated Astro files & runtime cache
├── public/                 # Static assets (images, fonts, sitemaps, global assets)
├── src/
│   ├── assets/             # Internal assets processed/optimized by Astro
│   ├── components/         # Premium, reusable UI elements
│   │   ├── BaseHead.astro       # Metadata, SEO tags, Fonts, and search script loading
│   │   ├── EssayCard.astro      # Card layout for displaying individual post snippets
│   │   ├── Experiment.astro     # Interactive code/math playground component
│   │   ├── Footer.astro         # Site footer with brand details & layout links
│   │   ├── FormattedDate.astro  # Component to format date objects cleanly
│   │   ├── Header.astro         # Navigation header containing the brand monogram & search trigger
│   │   ├── HeaderLink.astro     # Link component indicating the active route state
│   │   ├── HeroSection.astro    # Bold landing page intro banner
│   │   ├── Philosophy.astro     # Stylized blockquotes for conceptual transitions/philosophical reflections
│   │   ├── ReadingNote.astro    # Quote-highlighting blocks for citations
│   │   ├── ReadingProgress.astro# Scroll indicator bar showing remaining reading time
│   │   ├── ScrollReveal.astro   # Wrapper implementing scroll fade-in animations
│   │   ├── SearchModal.astro    # Modal container and script loading for client-side search
│   │   ├── SectionLabel.astro   # Sub-heading dividers featuring Roman numerals
│   │   ├── TableOfContents.astro# Sidebar navigation mapping headings inside long posts
│   │   └── ThemeToggle.astro    # Interactive theme switcher
│   ├── consts.ts           # Site-wide configurations (SITE_TITLE, SITE_DESCRIPTION)
│   ├── content.config.ts   # Definition of schemas and validation schemas for content collections
│   ├── content/
│   │   └── blog/           # Source MDX/MD files containing the essays
│   ├── layouts/
│   │   ├── BaseLayout.astro     # Main application layout frame
│   │   └── BlogPost.astro       # Specific layout optimized for writing essays (contains reading progress & TOC)
│   ├── pages/
│   │   ├── about.astro     # Static page describing the project
│   │   ├── essays/         # Pages for listing all essays and rendering individual post slugs
│   │   ├── index.astro     # Blog landing page featuring recent posts and selected citations
│   │   ├── rss.xml.ts      # Automated generator for site RSS feeds
│   │   └── tags/           # Pages tracking tags and grouped posts
│   ├── styles/
│   │   └── global.css      # Core styles (typography, HSL palettes, KaTeX styling, custom scrollbars)
│   └── utils/
│       └── remark-reading-time.mjs  # remark plugin injecting estimated reading time into post frontmatter
├── astro.config.mjs        # Astro configuration (integrations, Markdown plugins, KaTeX configuration)
├── package.json            # Script definitions and package dependencies
├── tailwind.config.cjs     # Tailwind configuration (custom fonts, themes, borders)
└── tsconfig.json           # TypeScript configuration
```

---

## 🛠️ Tech Stack & Core Integrations

- **Astro v6**: Modern static site generator optimized for low-latency delivery.
- **MDX**: Combines standard markdown with custom Astro components directly inside your essays.
- **TailwindCSS**: Utilitarian styling framework configured with custom dark-academic themes.
- **Pagefind**: Fast, static, full-text search indexer. It generates index data during `postbuild` and searches locally on the client without external queries.
- **KaTeX (remark-math / rehype-katex)**: Type-set scientific and mathematical equations with zero performance overhead during build-time.
- **Reading Time Estimator**: Automatically calculates reading duration for each essay and binds it to the metadata.

---

## ⚙️ Development Workflow & Commands

Run all command lines from the project root directory:

| Command | Action | Description |
| :--- | :--- | :--- |
| `npm install` | Install Dependencies | Sets up development packages and assets locally. |
| `npm run dev` | Dev Server | Launches the dev server at `http://localhost:4321` with hot module replacement (HMR). |
| `npm run build` | Production Build | Builds pages into static files and triggers the **Pagefind** indexer on the built `dist/` directory. |
| `npm run preview` | Preview Site | Serves the generated static files from `/dist` to test production assets locally. |

---

## ✍️ Essay Authoring & Writing Guide

To add a new essay, create an `.mdx` file inside the `src/content/blog/` directory.

### 1. Frontmatter Requirements
All draft files must include the following metadata:
```yaml
---
title: "Your Essay Title"
description: "A summary of the essay under 160 characters (important for search indexing & SEO)."
date: YYYY-MM-DD
tags: ["ml", "philosophy"]
kicker: "THE TOPIC OVERVIEW STATEMENT"
subtitle: "A subtitle/secondary title displayed in italics"
draft: true # Default to true. Change to false only when ready to publish.
---
```

### 2. Layout Structure & Components
*   **Animations**: Wrap your essay blocks inside `<ScrollReveal>` tags to enable staggered fade-in animations on load. Avoid nesting `<ScrollReveal>` elements.
*   **Sections**: Use `<SectionLabel label="I. Title" />` (using Roman numerals) above your main `## Headings` to separate major arguments.
*   **Philosophical Quotes**: Wrap conceptual transitions or citations inside `<Philosophy>` tags.
*   **Math Equations**: Use standard LaTeX syntax:
    - Inline equations: `$P(Y \mid \text{do}(X))$`
    - Block equations: `$$ \Sigma_A \approx \dots $$`
*   **Data Tables**: Make sure all markdown tables are wrapped in a `<div class="spectrum-container">` container to apply styling and prevent mobile layout overflow:
    ```html
    <div class="spectrum-container">

    | Header 1 | Header 2 |
    | :--- | :--- |
    | Row 1 | Row 2 |

    </div>
    ```
*   **Code Blocks**: Fenced code blocks (e.g. ` ```python `) are automatically stylized with visual control dots and a clipboard copy button using global markdown decorators.

---

## 📱 Mobile Layout Constraints

To prevent layout breakages on viewports down to $320\text{px}$:
1. **Min-Width Refets**: Any flexible container holding user-written text or code windows must use Tailwind's `w-full min-w-0` to let flex elements shrink as needed.
2. **Width Caps**: The `.code-window`, `.katex-display`, and `.spectrum-container` classes restrict their max-width to `100%` and force internal overflow-scrolling.
3. **Monogram collapsing**: The website header automatically collapses to the monogram `G & R` on mobile breakpoints ($< 640\text{px}$).
