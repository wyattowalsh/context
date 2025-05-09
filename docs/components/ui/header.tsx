import Link from "next/link";
import { ThemeToggle } from "./theme-toggle";
import { cn } from "./utils";
import { Button } from "./button";
import { Github } from "lucide-react";
import { config } from "../../app/layout.config";
import siteIcon from "../../public/images/icon.png";
import Image from "next/image";
import { Separator } from "./separator";
import { TbFileSmile } from "react-icons/tb";
import { AiOutlineExperiment } from "react-icons/ai";
import { GrInstall } from "react-icons/gr";
import { GitPullRequestCreateArrow } from "lucide-react";

export function Header() {
  return (
    <header className="sticky top-0 z-40 w-full border-b border-border/40 bg-background/80 backdrop-blur-md">
      <div className="container flex h-16 items-center justify-between">
        <div className="flex items-center gap-6">
          <Link href="/" className="site-title flex flex-row items-center gap-2">
          <Image src={siteIcon} alt="context icon logo" width={60} height={60} />
          <div className="context-text text-3xl">{config.name}</div>
          </Link>
          <nav className="hidden md:flex">
            <ul className="flex items-center gap-5">
              <li>
                <Link
                  href="/docs"
                  className="text-muted-foreground transition-colors hover:text-foreground flex flex-row items-center gap-1"
                >
                  <TbFileSmile className="h-6 w-6" /> Get Started
                </Link>
              </li>
              <Separator orientation="vertical" />
              <li>
                <Link
                  href="/docs/examples"
                  className="text-muted-foreground transition-colors hover:text-foreground flex flex-row items-center gap-1"
                >
                  <GrInstall className="h-6 w-6" /> Installation
                </Link>
              </li>
              <Separator orientation="vertical" />
              <li>
                <Link
                  href="/docs/examples"
                  className="text-muted-foreground transition-colors hover:text-foreground flex flex-row items-center gap-1"
                >
                  <AiOutlineExperiment className="h-6 w-6" /> Examples
                </Link>
              </li>
              <Separator orientation="vertical" />
              <li>
                <Link
                  href="/docs/examples"
                  className="text-muted-foreground transition-colors hover:text-foreground flex flex-row items-center gap-1"
                >
                  <GitPullRequestCreateArrow className="h-6 w-6" /> Contributing
                </Link>
              </li>
            </ul>
          </nav>
        </div>
        
        <div className="flex items-center gap-2">
          <Button variant="ghost" size="icon" asChild>
            <Link
              href="https://github.com/wyattowalsh/context"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="GitHub"
            >
              <Github className="h-5 w-5" />
            </Link>
          </Button>
          <ThemeToggle />
        </div>
      </div>
    </header>
  );
} 