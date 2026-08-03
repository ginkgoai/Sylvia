import { ArrowRight, Star } from "lucide-react";
import { cn } from "../../lib/cn";

export interface QualificationField {
  label: string;
  value: string;
}

export interface LeadQualificationCardProps {
  title?: string;
  fields: QualificationField[];
  status?: string;
  className?: string;
}

export function LeadQualificationCard({
  title = "Lead qualificado",
  fields,
  status = "Encaminhado para atendimento",
  className,
}: LeadQualificationCardProps) {
  return (
    <article className={cn("leaf-card leaf-active p-5", className)}>
      <div className="flex items-center gap-2 text-[var(--leaf-primary-bright)]">
        <Star className="h-4 w-4 fill-current" />
        <h3 className="font-semibold">{title}</h3>
      </div>
      <dl className="mt-4 space-y-2">
        {fields.map((field) => (
          <div key={field.label} className="flex items-start justify-between gap-4 text-sm">
            <dt className="text-[var(--leaf-text-muted)]">{field.label}</dt>
            <dd className="text-right font-medium">{field.value}</dd>
          </div>
        ))}
      </dl>
      <div className="mt-5 flex items-center justify-between rounded-xl bg-[rgba(101,199,122,.10)] px-4 py-3 text-xs text-[var(--leaf-primary-bright)]">
        <span>{status}</span>
        <ArrowRight className="h-4 w-4" />
      </div>
    </article>
  );
}
