'use client';

import React from 'react';
import { ThemeProvider as NextThemeProvider } from 'next-themes';
import { RootProvider } from 'fumadocs-ui/provider';

export default function LayoutProvider({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <NextThemeProvider attribute="class" defaultTheme="system" enableSystem disableTransitionOnChange>
      <RootProvider
        search={{
          options: {
            type: 'static',
          },
        }}
      >
        <div className="flex min-h-screen flex-col">
          {children}
        </div>
      </RootProvider>
    </NextThemeProvider>
  );
} 