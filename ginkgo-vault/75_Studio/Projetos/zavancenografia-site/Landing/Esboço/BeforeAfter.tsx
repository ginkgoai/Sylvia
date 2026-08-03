export function BeforeAfter() {
  return (
    <section aria-label="Antes e depois" className="py-32 px-6 md:px-10 bg-zinc-50 border-b border-border">
      <div className="max-w-7xl mx-auto">
        <div className="flex flex-col md:flex-row md:items-end md:justify-between gap-6 mb-14">
          <div className="max-w-xl">
            <span className="font-mono text-[10px] uppercase tracking-[0.35em] text-muted-foreground block mb-4">
              Cases
            </span>
            <h2 className="font-display italic text-4xl md:text-5xl tracking-tight">
              Antes &amp; depois.
            </h2>
          </div>
          <p className="text-muted-foreground max-w-sm text-pretty">
            Em breve — a curadoria de transformações completas, do briefing inicial à instalação final.
          </p>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {[0, 1].map((n) => (
            <div key={n} className="aspect-[16/10] border border-dashed border-border flex items-center justify-center bg-background">
              <span className="font-mono text-[10px] uppercase tracking-[0.35em] text-muted-foreground">
                Case {String(n + 1).padStart(2, "0")} · em breve
              </span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
