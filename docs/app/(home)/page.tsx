import Link from 'next/link';
import Image from 'next/image';
import { ArrowRight, GitFork, Star, ExternalLink, MessageSquare, CheckCircle2, Database, Code, FileText, Globe } from "lucide-react";
import { Button } from "../../components/ui/button";
import { Separator } from "../../components/ui/separator";
import { FaGithubAlt } from "react-icons/fa";
import { type Metadata } from 'next';

const Features = [
  {
    name: 'Multi-Document Support',
    description: 'Seamlessly process multiple documents with smart chunking and prioritization.',
  },
  {
    name: 'Semantic Chunking',
    description: 'Intelligently break down content to preserve context and meaning.',
  },
  {
    name: 'Smart Prioritization',
    description: 'Automatically prioritize the most relevant context for your AI interactions.',
  },
  {
    name: 'Developer-Friendly',
    description: 'Simple API designed for easy integration into any AI workflow.',
  },
]

// Add comprehensive metadata
export const metadata: Metadata = {
  title: 'Context - Advanced Context Management for AI',
  description: 'Build multi-document aware AI apps with semantic chunking and prioritization. Context is a powerful open-source library for managing context in AI applications.',
  keywords: ['context management', 'AI', 'LLM', 'document chunking', 'context window', 'NLP', 'natural language processing', 'semantic search'],
  authors: [{ name: 'Wyatt Walsh', url: 'https://github.com/wyattowalsh' }],
  creator: 'Context Team',
  publisher: 'Context',
  openGraph: {
    type: 'website',
    locale: 'en_US',
    url: 'https://www.promptcontext.xyz',
    title: 'Context - Advanced Context Management for AI',
    description: 'Build multi-document aware AI apps with semantic chunking and prioritization. Context helps you manage complex data for AI applications.',
    siteName: 'Context',
    images: [
      {
        url: '/images/hero.png', // Using existing hero image
        width: 1200,
        height: 630,
        alt: 'Context - Advanced Context Management for AI',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Context - Advanced Context Management for AI',
    description: 'Build multi-document aware AI apps with semantic chunking and prioritization.',
    creator: '@contextlib', // Replace with actual Twitter handle if available
    images: ['/images/hero.png'], // Using existing hero image
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  alternates: {
    canonical: 'https://www.promptcontext.xyz',
  },
  metadataBase: new URL('https://www.promptcontext.xyz'),
  category: 'Technology',
  applicationName: 'Context',
  other: {
    'google-site-verification': '', // Add verification code if needed
  },
};

export default function Page() {
  return (
    <div className="flex flex-col items-center justify-around flex-start">
      {/* Hero Section with Gradient Background */}
      <div className="relative flex w-full max-w-4xl flex-col items-center justify-around pt-12 md:pt-20">
        {/* Gradient Background Effects */}
        <div className="absolute inset-0 -z-10">
          <div className="absolute left-1/4 top-1/4 h-72 w-72 rounded-full bg-primary/15 blur-3xl animate-pulse" 
            style={{ animationDuration: '6s' }} />
          <div className="absolute right-1/4 bottom-1/4 h-72 w-72 rounded-full bg-accent/15 blur-3xl animate-pulse" 
            style={{ animationDelay: '2s', animationDuration: '8s' }} />
        </div>
        
        {/* Hero Content with improved spacing and animations */}
        <div className="flex flex-col items-center justify-start text-center">
          <div className="mb-8 relative w-36 h-36 drop-shadow-lg">
            <Image 
              src="/images/icon.png" 
              alt="Context Project Logo" 
              fill
              priority
              className="animate-float"
              style={{ animationDuration: '6s' }}
            />
          </div>
          
          <div className="inline-flex items-center rounded-full border border-border/60 bg-background/80 backdrop-blur-md px-4 py-1.5 text-sm mb-8 shadow-sm hover:shadow-md transition-all duration-300 animate-fadeIn">
            
            <Link
              href="./docs/examples/mcp" 
              target="_blank" 
              rel="noopener noreferrer" 
              className="mx-1.5 text-primary hover:text-primary/80 font-semibold underline-offset-2 hover:underline transition-colors flex items-center"
            >
              <span className="mr-2 animate-pulse text-lg">🚀</span> 
              <span className="font-medium">Try the MCP server!</span>
              <ExternalLink className="h-3 w-3 inline" />
            </Link>
            <span className="font-medium mr-2"></span>
            <a href="https://modelcontextprotocol.io/" target="_blank" rel="noopener noreferrer">
              <div className="relative group">
                <Image 
                  src="/images/mcp.svg" 
                  width={35} 
                  height={35} 
                  alt="Model Context Protocol (MCP) logo"
                  className="transition-transform hover:scale-110" 
                />
                <span className="absolute -top-8 left-1/2 -translate-x-1/2 bg-background/90 px-2 py-1 rounded text-xs opacity-0 group-hover:opacity-100 transition-opacity pointer-events-none whitespace-nowrap shadow-sm">
                  MCP Logo
                </span>
              </div>
            </a>
          </div>
          <div className="context-text">
          <h1 className="mb-8 text-5xl font-bold sm:text-6xl md:text-7xl">
            context
          </h1>
          </div>
          <h5 className="max-w-xl text-base text-foreground/90 md:text-xl mb-14">
            Generate LLM-ready prompt <div className="context-text">context</div> with ease
          </h5>
          
          {/* Improved CTA Buttons */}
          <div className="flex flex-wrap items-center justify-start gap-4">
            <Button asChild size="lg" className="gap-2 px-6 rounded-full shadow-md transition-all duration-200 hover:shadow-lg hover:translate-y-[-2px] active:translate-y-0 active:shadow-md">
              <Link href="/docs" className="flex flex-row items-center">
                Get Started &nbsp; <ArrowRight className="h-6 w-6" />
              </Link>
            </Button>
            <Button asChild variant="outline" size="lg" className="gap-2 px-6 rounded-full border-border/60 shadow-sm hover:border-primary/40 transition-all duration-200 hover:shadow-md hover:translate-y-[-2px] active:translate-y-0 active:shadow-sm">
              <a href="https://github.com/wyattowalsh/context" target="_blank" rel="noopener noreferrer" className="flex flex-row items-center">
                View on GitHub &nbsp; <FaGithubAlt className="h-6 w-6" />
              </a>
            </Button>
          </div>
        </div>
      </div>

      <Separator orientation="horizontal" className="w-full my-18" />

      {/* Features Section */}
      <div className="w-full max-w-4xl flex flex-col items-center justify-start gap-4">
        <div className="text-center mb-4">
          <h2 className="text-3xl font-bold tracking-tight sm:text-4xl">
            Key Features
          </h2>
          <p className="mt-3 text-base text-muted-foreground md:text-lg">
          <u>Transform web, file, and GitHub data</u> into <b><i>optimized-for-LLM knowledge files</i></b>
          </p>
        </div>

        <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 mb-6">
          {/* Feature 1 */}
          <div className="group relative rounded-xl bg-background/60 p-7 shadow-md ring-1 ring-border transition-all duration-300 hover:shadow-lg hover:ring-primary/30 focus-within:ring-primary/40 h-full">
            <div className="absolute right-6 top-6 opacity-10 text-primary">
              <Code className="h-16 w-16" />
            </div>
            <div className="mb-5 rounded-full bg-primary/10 p-3 w-fit">
              <Code className="h-6 w-6 text-primary" />
            </div>
            <h3 className="mb-3 text-lg font-semibold">Web Processing</h3>
            <p className="text-muted-foreground text-sm leading-relaxed">
              Smart crawling and extraction of web content with route trees, sitemap parsing, and content filtering.
            </p>
          </div>

          {/* Feature 2 */}
          <div className="group relative rounded-xl bg-background/60 p-7 shadow-md ring-1 ring-border transition-all duration-300 hover:shadow-lg hover:ring-primary/30 focus-within:ring-primary/40 h-full">
            <div className="absolute right-6 top-6 opacity-10 text-primary">
              <FileText className="h-16 w-16" />
            </div>
            <div className="mb-5 rounded-full bg-primary/10 p-3 w-fit">
              <FileText className="h-6 w-6 text-primary" />
            </div>
            <h3 className="mb-3 text-lg font-semibold">File Processing</h3>
            <p className="text-muted-foreground text-sm leading-relaxed">
              Advanced document conversion with OCR, formula understanding, and rich content extraction for various file formats.
            </p>
          </div>

          <div className="group relative rounded-xl bg-background/60 p-7 shadow-md ring-1 ring-border transition-all duration-300 hover:shadow-lg hover:ring-primary/30 focus-within:ring-primary/40 h-full">
            <div className="absolute right-6 top-6 opacity-10 text-primary">
              <FileText className="h-16 w-16" />
            </div>
            <div className="mb-5 rounded-full bg-primary/10 p-3 w-fit">
              <FileText className="h-6 w-6 text-primary" />
            </div>
            <h3 className="mb-3 text-lg font-semibold">GitHub Integration</h3>
            <p className="text-muted-foreground text-sm leading-relaxed">
              Effortlessly process GitHub repositories with customizable path filters and intelligent content selection.
            </p>
          </div>
        </div>
      </div>

      {/* CTA Section */}
      <div className="w-full max-w-4xl mb-6">
        <div className="overflow-hidden rounded-xl bg-gradient-to-br from-background to-background relative shadow-lg ring-1 ring-border">
          {/* Background decorative elements */}
          <div className="absolute inset-0 overflow-hidden">
            <div className="absolute -left-10 -top-10 h-64 w-64 rounded-full bg-primary/10 blur-3xl"></div>
            <div className="absolute -bottom-10 -right-10 h-64 w-64 rounded-full bg-accent/10 blur-3xl"></div>
          </div>
          
          {/* Content with improved contrast */}
          <div className="relative p-8 md:p-10">
            <div className="flex flex-col items-center text-center">
              <h2 className="text-2xl font-bold tracking-tight sm:text-3xl relative">
                <span className="bg-gradient-to-r from-primary to-accent bg-clip-text text-transparent">Ready to generate some <div className="context-text text-4xl"><b>context</b></div> ?</span>
              </h2>
              <p className="mt-4 max-w-2xl text-base text-foreground/90 md:text-lg">
                Web, files, or GitHub -- you name it, it can be <div className="context-text"><b>context</b></div>
              </p>
              <Button asChild size="lg" className="mt-8 px-8 py-6 rounded-full shadow-md transition-all duration-200 gap-2 hover:shadow-lg hover:translate-y-[-2px] active:translate-y-0 active:shadow-md flex flex-row items-center">
                <Link href="/docs">
                  Explore Documentation <ArrowRight className="h-4 w-4 ml-1" />
                </Link>
              </Button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
