import { source } from '@/lib/source';
import {
  DocsPage,
  DocsBody,
  DocsDescription,
  DocsTitle,
} from 'fumadocs-ui/page';
import { notFound } from 'next/navigation';
import { createRelativeLink } from 'fumadocs-ui/mdx';
import { getMDXComponents } from '@/mdx-components';
import type { Metadata } from 'next';

export default async function Page(props: {
  params: Promise<{ slug?: string[] }>;
}) {
  const params = await props.params;
  const page = source.getPage(params.slug);
  if (!page) notFound();

  const MDXContent = page.data.body;

  return (
    <DocsPage toc={page.data.toc} full={page.data.full}>
      <DocsTitle>{page.data.title}</DocsTitle>
      <DocsDescription>{page.data.description}</DocsDescription>
      <DocsBody>
        <MDXContent
          components={getMDXComponents({
            // this allows you to link to other pages with relative file paths
            a: createRelativeLink(source, page),
          })}
        />
      </DocsBody>
    </DocsPage>
  );
}

export async function generateStaticParams() {
  return source.generateParams();
}

export async function generateMetadata(props: {
  params: Promise<{ slug?: string[] }>;
}): Promise<Metadata> {
  const params = await props.params;
  const page = source.getPage(params.slug);
  if (!page) notFound();

  // Extract keywords from frontmatter if available
  const keywords = page.data.keywords || [];

  return {
    title: page.data.title ? `${page.data.title} - Context` : 'Context Docs',
    description: page.data.description || 'Context documentation',
    keywords: [
      'context management', 
      'AI', 
      'LLM', 
      'documentation',
      ...keywords
    ],
    authors: [{ name: 'Wyatt Walsh', url: 'https://github.com/wyattowalsh' }],
    creator: 'Context Team',
    publisher: 'Context',
    openGraph: {
      type: 'article',
      title: page.data.title,
      description: page.data.description,
      url: `https://www.promptcontext.xyz/docs/${params.slug?.join('/') || ''}`,
      images: [
        {
          url: page.data.image || '/images/hero.png', // Use custom image if available
          width: 1200,
          height: 630,
          alt: page.data.title,
        },
      ],
    },
    twitter: {
      card: 'summary_large_image',
      title: page.data.title,
      description: page.data.description,
      images: [page.data.image || '/images/hero.png'],
    },
    alternates: {
      canonical: `https://www.promptcontext.xyz/docs/${params.slug?.join('/') || ''}`,
    },
    metadataBase: new URL('https://www.promptcontext.xyz'),
  };
}
