# Style Guide

This guide defines the visual identity, typography system, color tokens, and layout guidelines for **Gradient and Reason**.

## 1. Typography
We use three custom Google fonts preloaded in the header:
* **EB Garamond**: Primarily for headers, section indicators, blockquotes, and footer links. Used to evoke academic and classical styling.
* **Literata**: Used for body prose to ensure high readability and comfortable tracking on both desktop and mobile screens.
* **JetBrains Mono**: Used for all code blocks, monospace tokens, search results metadata, and citation codes.

### Helper Classes
* `.type-display`: Large header text for titles (`font-garamond`, large size).
* `.type-h2`: Section titles in italics (`font-garamond`, italicized, moderate size).
* `.type-kicker`: Small uppercase taglines at the top of pages/essays (`font-garamond`, uppercase, wide tracking).
* `.type-label`: Small metadata, button, and column labels (`font-garamond`, tracking `0.2em`).

---

## 2. Color Palette (Dark Academic Theme)
Colors are defined as CSS custom variables in `src/styles/global.css`.

| Variable | Dark Mode (Default) | Light Mode | Description |
| :--- | :--- | :--- | :--- |
| `--bg` | `#0e0d0b` (Deep Slate Black) | `#f5f0e8` (Paper White) | Background canvas |
| `--surface` | `#141311` (Chalk Coal) | `#ebe5d9` (Warm Parchment) | Cards and panels |
| `--surface-raised` | `#1d1b19` (Elevated Chalk) | `#e0d9cb` (Darker Parchment) | Elevated inputs/buttons |
| `--ink` | `#c8bfaa` (Bone Ivory) | `#3d372e` (Ink Black) | Primary body text |
| `--ink-strong` | `#e6e2de` (Bright Cream) | `#1a1714` (Deep Charcoal) | Headings and titles |
| `--ink-dim` | `#6b6358` (Muted Grey) | `#8a7f70` (Subdued Grey) | Meta labels and descriptors |
| `--accent` | `#8b7355` (Amber Bronze) | `#6b5a3e` (Deep Olive Bronze) | Dynamic elements & highlights |

---

## 3. Layout Constraints for Mobile
To maintain responsiveness and prevent horizontal layout breakages:
1. **Flex Width Overrides**: Always use `w-full` and `min-w-0` on columns containing text blocks or code blocks. This forces wide children to wrap or scroll rather than stretching the main container grid.
2. **Text Bleeding**: Keep equations (`.katex-display`) and tables (`.spectrum-container`) set with `max-width: 100%` and `overflow-x: auto` so that mobile viewports scroll their contents natively.
3. **Word Breaks**: Long words or mathematical sequences should utilize `overflow-wrap: break-word` and `word-break: break-word` (configured globally on the `body` element).
