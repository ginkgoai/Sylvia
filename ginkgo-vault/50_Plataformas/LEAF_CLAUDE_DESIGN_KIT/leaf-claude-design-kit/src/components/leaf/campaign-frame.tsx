import type { ReactNode } from "react";
import { cn } from "../../lib/cn";

export interface CampaignFrameProps {
  children: ReactNode;
  format?: "feed" | "square" | "story";
  className?: string;
}

const ratios = {
  feed: "aspect-[4/5]",
  square: "aspect-square",
  story: "aspect-[9/16]",
};

export function CampaignFrame({ children, format = "feed", className }: CampaignFrameProps) {
  return (
    <section
      className={cn(
        "leaf-canvas relative isolate w-full overflow-hidden rounded-[28px] border border-[var(--leaf-border)] p-[7%]",
        ratios[format],
        className,
      )}
    >
      <div aria-hidden className="absolute inset-0 -z-10 opacity-50 [background-image:radial-gradient(rgba(143,230,162,.12)_1px,transparent_1px)] [background-size:24px_24px]" />
      {children}
    </section>
  );
}
