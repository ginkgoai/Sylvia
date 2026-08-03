import type { LucideIcon } from "lucide-react";
import { cn } from "../../lib/cn";

export interface FeatureChipProps {
  label: string;
  icon?: LucideIcon;
  tone?: "green" | "gold" | "neutral";
  className?: string;
}

export function FeatureChip({ label, icon: Icon, tone = "green", className }: FeatureChipProps) {
  return (
    <div
      className={cn(
        "flex min-h-12 items-center gap-3 rounded-2xl border px-4 text-sm font-semibold",
        tone === "green" && "border-[var(--leaf-border)] bg-[rgba(101,199,122,.06)]",
        tone === "gold" && "border-[rgba(200,169,107,.22)] bg-[rgba(200,169,107,.06)]",
        tone === "neutral" && "border-white/8 bg-white/[0.035]",
        className,
      )}
    >
      {Icon ? <Icon className="h-5 w-5 text-[var(--leaf-primary)]" /> : null}
      <span>{label}</span>
    </div>
  );
}
