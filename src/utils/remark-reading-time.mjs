import { toString } from 'mdast-util-to-string';
import getReadingTime from 'reading-time';

export function remarkReadingTime() {
  return function (tree, { data }) {
    const text = toString(tree);
    const readingTime = getReadingTime(text);
    // Inject readingTime text (e.g. "5 min read") into the Astro frontmatter
    data.astro.frontmatter.readingTime = readingTime.text;
  };
}
