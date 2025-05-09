import type { BaseLayoutProps } from 'fumadocs-ui/layouts/shared';
import { NotepadText } from 'lucide-react';
import siteIcon from '../public/images/icon.png';
import Image from 'next/image';
/**
 * Shared layout configurations
 *
 * you can customise layouts individually from:
 * Home Layout: app/(home)/layout.tsx
 * Docs Layout: app/docs/layout.tsx
 */
export const baseOptions: BaseLayoutProps = {
  nav: {
    title: (
      <>
        <Image 
          src={siteIcon} 
          alt="context icon logo" 
          width={40} 
          height={40} 
          className="rounded-md"
          priority 
        />
        <span className="site-title">context</span>
      </>
    )
  },
  links: [
    {
      icon: <NotepadText aria-hidden="true" />,
      text: 'Docs',
      url: '/docs',
      active: 'nested-url',
      secondary: false
    },
  ],
  githubUrl: 'https://github.com/wyattowalsh/context'
};

export const config = {
  name: "context",
  description: "context is a system for efficiently generating LLM-ready knowledge files from web, file, and github data sources",
  githubUrl: "https://github.com/wyattowalsh/context",
  docsRepositoryBase: "https://github.com/wyattowalsh/context/tree/main/docs",
  socialLinks: {
    twitter: "https://twitter.com/wyattowalsh",
    github: "https://github.com/wyattowalsh/context",
  },
  navigation: [
    {
      title: "Introduction",
      links: [
        { title: "Getting Started", href: "/docs" },
        { title: "Installation", href: "/docs/installation" },
        { title: "Configuration", href: "/docs/configuration" },
      ],
    },
    {
      title: "Core Concepts",
      links: [
        { title: "Context", href: "/docs/context" },
        { title: "Tools", href: "/docs/tools" },
        { title: "Authentication", href: "/docs/authentication" },
      ],
    },
    {
      title: "API Reference",
      links: [
        { title: "Overview", href: "/docs/api" },
        { title: "Client", href: "/docs/api/client" },
        { title: "Server", href: "/docs/api/server" },
      ],
    },
  ],
};
