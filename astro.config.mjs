import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import tailwind from '@astrojs/tailwind';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { remarkReadingTime } from './src/utils/remark-reading-time.mjs';

// https://astro.build/config
export default defineConfig({
	site: 'https://gradient-and-reason.vercel.app',
	integrations: [
		mdx(),
		sitemap(),
		tailwind(),
	],
	markdown: {
		remarkPlugins: [remarkMath, remarkReadingTime],
		rehypePlugins: [rehypeKatex],
		shikiConfig: {
			theme: 'one-dark-pro',
			wrap: true,
		},
	},
});
