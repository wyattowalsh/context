import { DocsLayout, DocsLayoutProps } from 'fumadocs-ui/layouts/docs';
import type { ReactNode } from 'react';
import { baseOptions } from '@/app/layout.config';
import { source } from '@/lib/source';
import { Banner } from 'fumadocs-ui/components/banner';
import { GiSpellBook } from "react-icons/gi";
import { GithubInfo } from 'fumadocs-ui/components/github-info';

const docsOptions: DocsLayoutProps = {
    ...baseOptions,
    tree: source.pageTree,
    links: [
      {
        type: 'custom',
        children: (
          <GithubInfo owner="wyattowalsh" repo="context" className="lg:-mx-2" />
        ),
      },
    ],
    tabs: {
      transform: (option) => ({
        ...option,
        icon: <GiSpellBook />,
      })
    },
    collapsible: true,
    defaultOpenLevel: 1,
    githubUrl: "https://github.com/wyattowalsh/context"
  }


export default function Layout({ children }: { children: ReactNode }) {
  return (
    <DocsLayout {...docsOptions}>
      {children}
      </DocsLayout>
  );
}