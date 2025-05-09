import * as React from "react"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "../ui/utils"

const cardVariants = cva(
  "feature-card group relative overflow-hidden rounded-2xl border border-border bg-card text-card-foreground transition-all duration-300",
  {
    variants: {
      variant: {
        default: "",
        gradient: "bg-gradient-to-br from-card to-background",
        outline: "border-2 bg-transparent",
        glass: "bg-card/80 backdrop-blur-md",
      },
      size: {
        default: "p-6",
        sm: "p-4",
        lg: "p-8",
      },
      interactive: {
        true: "hover:-translate-y-1 hover:shadow-lg hover:shadow-primary/10 hover:border-primary/50 cursor-pointer",
        false: "",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
      interactive: false,
    },
  }
)

const cardHeaderVariants = cva("flex flex-col space-y-1.5", {
  variants: {
    align: {
      default: "",
      center: "items-center text-center",
      left: "items-start text-left",
      right: "items-end text-right",
    },
  },
  defaultVariants: {
    align: "left",
  },
})

const cardTitleVariants = cva("text-2xl font-semibold tracking-tight", {
  variants: {
    gradient: {
      true: "hero-text-gradient",
      false: "",
    },
  },
  defaultVariants: {
    gradient: false,
  },
})

const cardDescriptionVariants = cva("text-muted-foreground", {
  variants: {
    size: {
      default: "text-sm",
      sm: "text-xs",
      lg: "text-base",
    },
  },
  defaultVariants: {
    size: "default",
  },
})

const cardContentVariants = cva("", {
  variants: {
    spacing: {
      default: "pt-4",
      none: "",
      sm: "pt-2",
      lg: "pt-6",
    },
  },
  defaultVariants: {
    spacing: "default",
  },
})

const cardFooterVariants = cva("flex items-center", {
  variants: {
    align: {
      default: "",
      center: "justify-center",
      left: "justify-start",
      right: "justify-end",
      between: "justify-between",
    },
    spacing: {
      default: "pt-4",
      none: "",
      sm: "pt-2",
      lg: "pt-6",
    },
  },
  defaultVariants: {
    align: "left",
    spacing: "default",
  },
})

export interface CardProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof cardVariants> {}

const Card = React.forwardRef<HTMLDivElement, CardProps>(
  ({ className, variant, size, interactive, ...props }, ref) => (
    <div
      ref={ref}
      className={cn(cardVariants({ variant, size, interactive, className }))}
      {...props}
    />
  )
)
Card.displayName = "Card"

export interface CardHeaderProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof cardHeaderVariants> {}

const CardHeader = React.forwardRef<HTMLDivElement, CardHeaderProps>(
  ({ className, align, ...props }, ref) => (
    <div
      ref={ref}
      className={cn(cardHeaderVariants({ align, className }))}
      {...props}
    />
  )
)
CardHeader.displayName = "CardHeader"

export interface CardTitleProps
  extends React.HTMLAttributes<HTMLHeadingElement>,
    VariantProps<typeof cardTitleVariants> {}

const CardTitle = React.forwardRef<HTMLParagraphElement, CardTitleProps>(
  ({ className, gradient, ...props }, ref) => (
    <h3
      ref={ref}
      className={cn(cardTitleVariants({ gradient, className }))}
      {...props}
    />
  )
)
CardTitle.displayName = "CardTitle"

export interface CardDescriptionProps
  extends React.HTMLAttributes<HTMLParagraphElement>,
    VariantProps<typeof cardDescriptionVariants> {}

const CardDescription = React.forwardRef<
  HTMLParagraphElement,
  CardDescriptionProps
>(({ className, size, ...props }, ref) => (
  <p
    ref={ref}
    className={cn(cardDescriptionVariants({ size, className }))}
    {...props}
  />
))
CardDescription.displayName = "CardDescription"

export interface CardContentProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof cardContentVariants> {}

const CardContent = React.forwardRef<HTMLDivElement, CardContentProps>(
  ({ className, spacing, ...props }, ref) => (
    <div
      ref={ref}
      className={cn(cardContentVariants({ spacing, className }))}
      {...props}
    />
  )
)
CardContent.displayName = "CardContent"

export interface CardFooterProps
  extends React.HTMLAttributes<HTMLDivElement>,
    VariantProps<typeof cardFooterVariants> {}

const CardFooter = React.forwardRef<HTMLDivElement, CardFooterProps>(
  ({ className, align, spacing, ...props }, ref) => (
    <div
      ref={ref}
      className={cn(cardFooterVariants({ align, spacing, className }))}
      {...props}
    />
  )
)
CardFooter.displayName = "CardFooter"

export {
  Card,
  CardHeader,
  CardFooter,
  CardTitle,
  CardDescription,
  CardContent,
}
