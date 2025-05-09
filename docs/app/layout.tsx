import './global.css';
import { Metadata } from 'next';
import { Handjet as FontHandjet } from 'next/font/google';
import { cn } from '../components/ui/utils';
import LayoutProvider from './layout.provider';
import { config } from './layout.config';

const fontHandjet = FontHandjet({
  subsets: ['latin'],
  variable: '--font-handjet',
});

export const metadata: Metadata = {
  title: {
    template: '%s | %s',
    default: config.name,
  },
  description: config.description,
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={cn(
          'min-h-screen bg-background antialiased',
          fontHandjet.variable
        )}
      >
        {/* Skip to content link for keyboard users */}
        <a 
          href="#main-content" 
          className="sr-only focus:not-sr-only focus:absolute focus:z-50 focus:p-4 focus:bg-background focus:text-foreground focus:top-0 focus:left-0"
        >
          Skip to content
        </a>
        
        {/* Background effects */}
        <div className="fixed inset-0 -z-10 h-full w-full select-none overflow-hidden">
          <div className="absolute left-[20%] top-[15%] h-56 w-56 rounded-full bg-primary/5 blur-3xl" />
          <div className="absolute right-[15%] bottom-[20%] h-64 w-64 rounded-full bg-accent/5 blur-3xl" />
        </div>
        
        <div id="main-content">
          <LayoutProvider>{children}</LayoutProvider>
        </div>
      </body>
    </html>
  );
}
