# Essay Guide

Every new essay must be placed in `src/content/blog/` as a `.mdx` file. 

## Minimal Draft Template

```markdown
---
title: "The Latent Manifold"
description: "Exploring the geometry of representations in high-dimensional neural spaces."
date: 2026-05-24
tags: ["representation-learning", "epistemology"]
kicker: "On machine knowledge & philosophical loss"
subtitle: "An inquiry into the coordinates of machine experience"
draft: true
---

import ScrollReveal from '../../components/ScrollReveal.astro';
import SectionLabel from '../../components/SectionLabel.astro';
import Philosophy from '../../components/Philosophy.astro';

<ScrollReveal>
We start with a question: what does a neural representation point to?
</ScrollReveal>
```

---

## 1. Frontmatter Requirements
Every essay's YAML frontmatter must contain these fields:
* `title`: The main essay title (wrapped in double quotes).
* `description`: Under 160 characters (critical for SEO).
* `date`: In `YYYY-MM-DD` format.
* `tags`: Array of lowercased, topic-specific strings focusing on precise technical/philosophical details rather than broad generalizations (e.g. `["causal-inference", "epistemology", "representation-learning"]` instead of generic `["ml", "philosophy"]`).
* `kicker`: Uppercase topic statement displayed at the very top.
* `subtitle`: Secondary title in italics.
* `draft`: Defaults to `true` for new drafts to prevent premature live deployment.

---

## 2. MDX Components and Markup Rules

To maintain the blog's dark-academic design and mobile-readiness, structure your Markdown elements as follows:

### A. Spacing & Scroll Reveal
* Wrap content blocks inside `<ScrollReveal>` tags to enable the staggered fade-in animations on load.
* Use `<SectionLabel label="I" />` (with Roman numerals) above each `## Heading` to mark major sections.

### B. Philosophy Blocks
* Place reflections, conceptual transitions, or philosophical quotes inside `<Philosophy>` wrappers. This renders them as elegant italicized blockquotes with a left border.

### C. Mathematics (KaTeX)
* **Inline math**: Use single dollar signs (e.g. `$P(Y \mid \text{do}(X))$`).
* **Block math**: Use double dollar signs (e.g. `$$ \Sigma_A \approx \dots $$`).
* *Note*: Keep equations brief so they do not break boundaries on small viewports.

### D. Comparison Tables
* Wrap Markdown tables in a `<div class="spectrum-container">` block to style column headers and enable horizontal scrolling on small screens.
  ```html
  <div class="spectrum-container">

  | Variable | World A | World B |
  | :--- | :--- | :--- |
  | $X \rightarrow Y$ | Direct Causal | Reverse Causal |

  </div>
  ```

### E. Code Windows
* Standard Markdown fenced code blocks (e.g., ` ```python `) are automatically processed by a global script and wrapped in `.code-window` containers complete with OS control dots, language badges, and a clipboard copy button.

### F. Glossary Tooltips (`<Term>`)
* Use the `<Term>` component to provide inline glossary tooltips for domain-specific vocabulary.
* **Import statement**:
  ```mdx
  import Term from '../../components/Term.astro';
  ```
* **Usage**:
  ```mdx
  the <Term id="duhem-quine">Duhem-Quine thesis</Term> states that...
  ```
* **Definitions Registry**: Edit `src/data/glossary.ts` to add definitions (must be under 120 characters).

---

## 3. Build & Deployment
Before committing and deploying:
1. Run local development server:
   ```bash
   npm run dev
   ```
2. Run production compiler to test static generation and Pagefind search indexing:
   ```bash
   npm run build
   ```
3. Commit and push:
   ```bash
   git add .
   git commit -m "Add new essay draft: [Name]"
   git push origin main
   ```
