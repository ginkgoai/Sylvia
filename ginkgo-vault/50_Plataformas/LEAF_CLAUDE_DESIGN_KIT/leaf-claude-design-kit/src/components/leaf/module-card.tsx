import type { LucideIcon } from "lucide-react";
import { Plus } from "lucide-react";
import { cn } from "../../lib/cn";

export interface ModuleCardProps {
  name: string;
  description: string;
  icon?: LucideIcon;
  state?: "included" | "optional" | "active";
  className?: string;
}

export function ModuleCard({ name, description, icon: Icon, state = "optional", className }: ModuleCardProps) {
  return (
    <article className={cn("leaf-card flex items-start gap-4 p-5", state === "active" && "leaf-active", className)}>
      <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl border border-[var(--leaf-border)] bg-[rgba(101,199,122,.08)]">
        {Icon ? <Icon className="h-5 w-5 text-[var(--leaf-primary)]" /> : null}
      </div>
      <div className="min-w-0 flex-1">
        <div className="flex items-center justify-between gap-3">
          <h3 className="font-semibold">{name}</h3>
          <span className="leaf-mono text-[10px] uppercase tracking-[0.14em] text-[var(--leaf-gold)]">{state}</span>
        </div>
        <p className="mt-1 text-sm leading-relaxed text-[var(--leaf-text-muted)]">{description}</p>
      </div>
      {state === "optional" ? <Plus className="mt-1 h-4 w-4 text-[var(--leaf-primary)]" /> : null}
    </article>
  );
}
