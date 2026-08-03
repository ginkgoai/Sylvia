import { cn } from "../../lib/cn";

export interface BrandHeaderProps {
  eyebrow?: string;
  title?: string;
  subtitle?: string;
  logoSrc?: string;
  className?: string;
}

export function BrandHeader({
  eyebrow,
  title = "LEAF",
  subtitle = "by Ginkgo",
  logoSrc,
  className,
}: BrandHeaderProps) {
  return (
    <header className={cn("flex items-center justify-between gap-6", className)}>
      <div className="flex items-center gap-3">
        {logoSrc ? (
          <img src={logoSrc} alt="LEAF by Ginkgo" className="h-11 w-11 object-contain" />
        ) : (
          <div aria-hidden className="grid h-11 w-11 grid-cols-2 gap-1">
            <span className="rounded-tl-xl rounded-br-md bg-[var(--leaf-primary)]" />
            <span className="rounded-tr-xl rounded-bl-md bg-[var(--leaf-primary)]" />
            <span className="rounded-bl-xl rounded-tr-md bg-[var(--leaf-primary)]" />
            <span className="rounded-br-xl rounded-tl-md bg-[var(--leaf-primary)]" />
          </div>
        )}
        <div>
          <div className="leaf-display text-2xl font-semibold tracking-[0.18em]">{title}</div>
          <div className="text-xs text-[var(--leaf-text-muted)]">{subtitle}</div>
        </div>
      </div>
      {eyebrow ? (
        <span className="leaf-mono rounded-full border border-[var(--leaf-border)] px-4 py-2 text-[11px] uppercase tracking-[0.16em] text-[var(--leaf-gold)]">
          {eyebrow}
        </span>
      ) : null}
    </header>
  );
}
