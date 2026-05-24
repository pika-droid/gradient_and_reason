# Codebase Structure

This guide explains the directory map and layout structure of the **Gradient and Reason** repository.

```
├── .astro/                 # Astro build cache and type definitions
├── public/                 # Static public assets (fonts, icons, robots.txt)
├── src/
│   ├── assets/             # Raw image assets (placeholders, hero images)
│   ├── components/         # Reusable UI component blocks
│   │   ├── BaseHead.astro  # Unused baseline head definitions
│   │   ├── CitationModal.astro # Custom modal generating APA/Chicago/BibTeX citations
│   │   ├── EssayCard.astro # Essay card displaying brief info and read times
│   │   ├── Footer.astro    # Persistent page footer with dynamic links
│   │   ├── Header.astro    # Site header containing navigation, theme switches, and search triggers
│   │   ├── HeroSection.astro # Header block on landing page
│   │   ├── Philosophy.astro # Styled mdx italic blockquotes
│   │   ├── ReadingNote.astro # Live quote box displaying random philosophical reflections
│   │   └── SearchModal.astro # Pagefind UI integration for search modals
│   ├── content/
│   │   ├── blog/           # MDX essay collection source files
│   │   └── config.ts       # Content schema validators
│   ├── data/
│   │   ├── glossary.ts     # Data registry for inline tooltips
│   │   └── quotes.ts       # Data registry for landing page quotes
│   ├── layouts/
│   │   ├── BaseLayout.astro # Global HTML document template (includes footer/header/modals)
│   │   └── BlogPost.astro   # Wrapper for rendering single essay structures
│   ├── pages/
│   │   ├── about.astro     # The mission and author about page
│   │   ├── essays/         # Year-sorted collection of all essays
│   │   ├── tags/           # Tag taxonomies and filtered archives
│   │   ├── index.astro     # Main landing page
│   │   └── rss.xml.ts      # Endpoint generating the dynamic feed
│   └── styles/
│       └── global.css      # Tailwinds imports, font preloads, and custom typography classes
├── astro.config.mjs        # Core Astro build configurations
├── tailwind.config.cjs     # Tailwind styling rules and breakpoints
└── vercel.json             # Frame guard headers and framework deployment settings
```

## Layout Nesting Model
* All content pages (`src/pages/*.astro`) render inside `<BaseLayout>`.
* Single essay pages (`src/content/blog/*.mdx`) are automatically fed into `<BlogPost>` which mounts inside `<BaseLayout>` to provide table of contents sidebars, reading progression bars, and tag clouds.
