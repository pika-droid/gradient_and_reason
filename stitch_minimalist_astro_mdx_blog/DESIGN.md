---
name: Empirical Archive
colors:
  surface: '#141311'
  surface-dim: '#141311'
  surface-bright: '#3b3936'
  surface-container-lowest: '#0f0e0c'
  surface-container-low: '#1d1b19'
  surface-container: '#211f1d'
  surface-container-high: '#2b2a27'
  surface-container-highest: '#363432'
  on-surface: '#e6e2de'
  on-surface-variant: '#ccc6ba'
  inverse-surface: '#e6e2de'
  inverse-on-surface: '#32302e'
  outline: '#959086'
  outline-variant: '#4a463e'
  surface-tint: '#cfc6b1'
  primary: '#e4dbc5'
  on-primary: '#353021'
  primary-container: '#c8bfaa'
  on-primary-container: '#534e3d'
  inverse-primary: '#645e4d'
  secondary: '#dfc29f'
  on-secondary: '#3f2d15'
  secondary-container: '#5a452b'
  on-secondary-container: '#d0b492'
  tertiary: '#ded9e7'
  on-tertiary: '#312f3a'
  tertiary-container: '#c2bdcb'
  on-tertiary-container: '#4f4c58'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ece2cc'
  primary-fixed-dim: '#cfc6b1'
  on-primary-fixed: '#201b0e'
  on-primary-fixed-variant: '#4c4636'
  secondary-fixed: '#fcdeba'
  secondary-fixed-dim: '#dfc29f'
  on-secondary-fixed: '#281903'
  on-secondary-fixed-variant: '#574329'
  tertiary-fixed: '#e6e0ef'
  tertiary-fixed-dim: '#c9c4d2'
  on-tertiary-fixed: '#1c1a24'
  on-tertiary-fixed-variant: '#484551'
  background: '#141311'
  on-background: '#e6e2de'
  surface-variant: '#363432'
  bg-paper: '#141310'
  ink-dim: '#6b6358'
  ink-faint: '#2a2823'
  accent-pale: '#4a3f2f'
  code-bg: '#151412'
  code-keyword: '#569cd6'
  code-fn: '#dcdcaa'
  code-str: '#ce9178'
  code-comment: '#6a9955'
  code-num: '#b5cea8'
  code-type: '#4ec9b0'
typography:
  display-h1:
    fontFamily: ebGaramond
    fontSize: 3.8rem
    fontWeight: '300'
    lineHeight: '1.12'
    letterSpacing: -0.01em
  display-h1-mobile:
    fontFamily: ebGaramond
    fontSize: 2.6rem
    fontWeight: '300'
    lineHeight: '1.15'
  section-h2:
    fontFamily: ebGaramond
    fontSize: 1.8rem
    fontWeight: '300'
    lineHeight: '1.3'
  body-main:
    fontFamily: literata
    fontSize: 18px
    fontWeight: '300'
    lineHeight: '1.9'
  blockquote:
    fontFamily: ebGaramond
    fontSize: 1.25rem
    fontWeight: '300'
    lineHeight: '1.6'
  kicker:
    fontFamily: ebGaramond
    fontSize: 0.72rem
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.22em
  label-numeral:
    fontFamily: ebGaramond
    fontSize: 0.68rem
    fontWeight: '400'
    lineHeight: '1'
    letterSpacing: 0.2em
  code-block:
    fontFamily: jetbrainsMono
    fontSize: 0.82rem
    fontWeight: '400'
    lineHeight: '1.65'
spacing:
  container-max: 740px
  section-gap: 6.5rem
  paragraph-bottom: 1.7rem
  gutter-desktop: 2rem
  gutter-mobile: 1.25rem
---

## Brand & Style
The design system is built for the "Dark Academic" aesthetic—a digital sanctuary for high-density philosophical and technical discourse. It evokes the feeling of a late-night study session in a private library, where classical intellectual heritage meets modern computational precision.

The style is **Minimalist and Editorial**, characterized by:
- **Atmospheric Depth:** Utilizing a persistent grain texture overlay (0.04 opacity) to simulate the tactile quality of physical parchment or film stock.
- **Academic Rigor:** Heavy reliance on serif-on-serif typography to create an "empirical essay" atmosphere.
- **Structured Density:** A focused, single-column layout that prioritizes deep reading and mathematical clarity over rapid scanning.
- **Melancholic Precision:** A dark, muted palette that reduces eye strain while maintaining high enough contrast for technical code blocks.

## Colors
The palette is rooted in the "Dark Academic" spectrum, moving away from pure blacks toward deep, organic charcoals and warm, ink-stained neutrals.

- **Primary (Ink):** Used for all main narrative text and primary headings. It is an antique off-white that prevents the "vibration" common in high-contrast dark modes.
- **Secondary (Wood/Parchment):** An architectural accent used for structural labels, section headers, and metadata.
- **Backgrounds:** The primary background is a deep charcoal, while the `bg-paper` variant provides subtle surface differentiation for cards or code containers.
- **Code Syntax:** A custom-tuned "Dark+" theme that maintains high legibility within the muted environment, using desaturated jewel tones for syntax highlighting.

## Typography
This system utilizes a **Serif-on-Serif** pairing. **EB Garamond** (acting as the stand-in for Cormorant Garamond) provides the decorative, academic display weight, while **Literata** (acting as the stand-in for Crimson Pro) offers the robust legibility required for long-form narrative.

- **The Display Face:** Used for all structural elements including titles, section headers, and pull quotes. It should lean into its elegant, high-contrast strokes.
- **The Body Face:** Set with a generous line height (1.9) to allow the "eye to breathe" during dense philosophical or technical reading.
- **Hierarchy:** Use the "Kicker" and "Label" styles for metadata to create a rhythmic separation between the essay content and its structural framework.

## Layout & Spacing
The layout follows a **Fixed-Width Editorial** model. To maintain the "golden line length" for readability, the primary text container never exceeds 740px.

- **Vertical Rhythm:** Major narrative shifts are separated by aggressive whitespace (6rem+) to signify a change in thought or topic.
- **Breathability:** Paragraphs are spaced widely to prevent the "wall of text" effect common in academic writing.
- **Breakpoints:**
  - **Desktop (1024px+):** Centered 740px column with generous side margins.
  - **Tablet (768px):** The column fills the screen with 4rem side padding.
  - **Mobile (480px):** Typography scales (see H1-mobile) and side padding reduces to 1.25rem.

## Elevation & Depth
Depth is conveyed through **Tonal Layers** rather than shadows. The system is intentionally flat to mimic the nature of ink on paper.

- **Surface Tiers:** The base background is the darkest layer. Code blocks and mathematical notation containers sit on a slightly lighter "Paper" surface (`#141310`).
- **Dividers:** Use 1px solid rules in `accent-pale` or `ink-faint` to define sections. Avoid shadows entirely.
- **Grain Overlay:** A global SVG turbulence filter is applied to the entire viewport. This provides a "micro-elevation" texture that unifies all elements under a single tactile aesthetic.

## Shapes
The shape language is **Sharp and Rigid**. 
- All standard containers, code blocks, and buttons utilize 0px border-radius to maintain the formal, institutional feel.
- **Exceptions:** Mathematical matrix brackets should use a minimal 4px radius on the corner tips to properly emulate traditional typesetting of linear algebra.

## Components
- **Code Blocks:** Styled with a distinct background (`code-bg`) and a 1px border (`ink-faint`). They must include a "kicker" label indicating the language (e.g., PYTHON) in the top-right or top-left corner.
- **Mathematical Matrices:** Use `inline-flex` containers. Brackets are constructed via `::before` and `::after` pseudo-elements with 1.5px solid borders and specific 4px rounding on the outer corners.
- **Blockquotes:** Indented 2rem from the left, featuring a 1.5px vertical rule in `accent-pale`. Text should be entirely italicized EB Garamond.
- **Horizontal Rules:** Use a centered 1px rule that doesn't span the full width, often punctuated by a small ornamental glyph or a section label.
- **Interactive Elements:** Links should be underlined with a 1px offset line in `secondary_color`. Hover states should transition the underline color to the primary ink color, rather than changing the text color itself.