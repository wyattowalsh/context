import {
  defineConfig,
  defineDocs,
  frontmatterSchema,
  metaSchema,
} from 'fumadocs-mdx/config';
import { remarkAutoTypeTable, createGenerator } from 'fumadocs-typescript';
import { rehypeToc, remarkAdmonition, remarkStructure } from 'fumadocs-core/mdx-plugins';
import rehypeAutolinkHeadings from 'rehype-autolink-headings';
import rehypeExternalLinks from 'rehype-external-links';
import rehypeImageCaption from 'rehype-image-caption';
import rehypeMeta from 'rehype-meta';
import { z } from 'zod';

const generator = createGenerator();

// You can customise Zod schemas for frontmatter and `meta.json` here
// see https://fumadocs.vercel.app/docs/mdx/collections#define-docs
export const docs = defineDocs({
  docs: {
    schema: frontmatterSchema.extend({
      // Add additional frontmatter properties for better SEO metadata
      description: z.string().optional(),
      keywords: z.array(z.string()).optional(),
      author: z.string().optional(),
      image: z.string().optional(),
    }),
  },
  meta: {
    schema: metaSchema,
  },
});

export default defineConfig({
  mdxOptions: {
    // MDX options
    rehypeCodeOptions: undefined,
    remarkImageOptions: undefined,
    remarkHeadingOptions: undefined,
    remarkPlugins: [[remarkAutoTypeTable, { generator }], remarkAdmonition, remarkStructure],
    rehypePlugins: [
      rehypeToc, 
      rehypeExternalLinks, 
      rehypeImageCaption, 
      [rehypeMeta, {
        // Configure rehype-meta with default metadata for all pages
        og: true, // Enable Open Graph metadata
        twitter: true, // Enable Twitter Card metadata
        copyright: 'Context Project',
        color: '#3B82F6', // Primary color
        author: 'Context Team',
        image: '/images/og-image.png', // Default image
        name: 'Context',
        description: 'Advanced context management for AI applications',
      }]
    ]
  },
});
