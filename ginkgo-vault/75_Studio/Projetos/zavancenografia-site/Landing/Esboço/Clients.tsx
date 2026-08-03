export function Clients() {
  const slots = ["Marca 01", "Marca 02", "Marca 03", "Marca 04", "Marca 05", "Marca 06"];
  return (
    <section aria-label="Clientes" className="py-20 border-y border-border px-6 md:px-10 overflow-hidden">
      <p className="text-center font-mono text-[10px] uppercase tracking-[0.35em] text-muted-foreground mb-10">
        Empresas que confiaram em nosso trabalho
      </p>
      <div className="flex flex-wrap justify-center items-center gap-x-16 gap-y-8 opacity-40">
        {slots.map((s) => (
          <span key={s} className="font-mono text-sm italic tracking-tight">
            {s}
          </span>
        ))}
      </div>
    </section>
  );
}
