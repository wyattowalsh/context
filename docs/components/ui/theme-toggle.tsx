"use client";

import * as React from "react";
import { useTheme } from "next-themes";
import { Moon, Sun, Laptop } from "lucide-react";
import { Button } from "./button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "./dropdown-menu";

export function ThemeToggle() {
  const { setTheme, theme } = useTheme();

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button
          variant="ghost"
          size="icon"
          className="relative h-9 w-9 overflow-hidden rounded-full"
          aria-label="Select theme"
        >
          <Sun className="h-5 w-5 rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
          <Moon className="absolute h-5 w-5 rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
          <Laptop className="absolute h-5 w-5 scale-0 transition-all [.system &]:scale-100" />
          <span className="sr-only">Toggle theme</span>
        </Button>
      </DropdownMenuTrigger>
      <DropdownMenuContent align="end" className="w-40 overflow-hidden rounded-xl p-1">
        <DropdownMenuItem 
          className="flex cursor-pointer items-center gap-2 rounded-lg px-3 py-2.5 hover:bg-accent focus:bg-accent"
          onClick={() => setTheme("light")}
        >
          <Sun className="h-4 w-4" />
          <span className="font-medium">Light</span>
        </DropdownMenuItem>
        <DropdownMenuItem 
          className="flex cursor-pointer items-center gap-2 rounded-lg px-3 py-2.5 hover:bg-accent focus:bg-accent"
          onClick={() => setTheme("dark")}
        >
          <Moon className="h-4 w-4" />
          <span className="font-medium">Dark</span>
        </DropdownMenuItem>
        <DropdownMenuItem 
          className="flex cursor-pointer items-center gap-2 rounded-lg px-3 py-2.5 hover:bg-accent focus:bg-accent"
          onClick={() => setTheme("system")}
        >
          <Laptop className="h-4 w-4" />
          <span className="font-medium">System</span>
        </DropdownMenuItem>
      </DropdownMenuContent>
    </DropdownMenu>
  );
} 