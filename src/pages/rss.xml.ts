import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { SITE_TITLE, SITE_DESCRIPTION } from '../consts';

export async function GET(context: any) {
  const posts = await getCollection('blog');
  const nonDraftPosts = posts.filter(post => !post.data.draft);

  return rss({
    title: SITE_TITLE,
    description: SITE_DESCRIPTION,
    site: 'https://gradient-and-reason.vercel.app',
    items: nonDraftPosts.map((post) => ({
      title: post.data.title,
      pubDate: post.data.date,
      description: post.data.description,
      link: `/essays/${post.id}/`,
    })),
  });
}
