import type { ButtonHTMLAttributes } from "react";
import { ArrowRight } from "lucide-react";
import { cn } from "../../lib/cn";

export interface PrimaryCTAProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  label?: string;
}

export function PrimaryCTA({ label = "Solicitar demonstração", className, ...props }: PrimaryCTAProps) {
  return (
    <button
      type="button"
      className={cn(
        "inline-flex min-h-12 items-center justify-center gap-3 rounded-2xl bg-[linear-gradient(135deg,var(--leaf-primary-bright),var(--leaf-primary))] px-6 font-bold text-[#061009] shadow-[0_12px_40px_rgba(101,199,122,.20)] transition-transform hover:-translate-y-0.5 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[var(--leaf-primary-bright)] focus-visible:ring-offset-2 focus-visible:ring-offset-[var(--leaf-background)]",
        className,
      )}
      {...props}
    >
      <span>{label}</span>
      <ArrowRight className="h-5 w-5" />
    </button>
  );
}
