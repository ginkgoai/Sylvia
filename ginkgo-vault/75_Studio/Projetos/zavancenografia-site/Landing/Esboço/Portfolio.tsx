import { useEffect, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { X, ChevronLeft, ChevronRight } from "lucide-react";
import { portfolio, categories, type PortfolioItem, type Category } from "@/data/portfolio";

const spanClass: Record<PortfolioItem["span"], string> = {
  sm: "md:col-span-3 aspect-square",
  md: "md:col-span-4 aspect-[4/5]",
  lg: "md:col-span-6 aspect-[4/3]",
  tall: "md:col-span-3 aspect-[3/4]",
  wide: "md:col-span-8 aspect-[16/9]",
};

export function Portfolio() {
  const [cat, setCat] = useState<Category>("Todos");
  const [openIdx, setOpenIdx] = useState<number | null>(null);

  const items = cat === "Todos" ? portfolio : portfolio.filter((p) => p.category === cat);

  useEffect(() => {
    if (openIdx === null) return;
    const onKey = (e: KeyboardEvent) => {
      if (e.key === "Escape") setOpenIdx(null);
      if (e.key === "ArrowRight") setOpenIdx((i) => (i === null ? null : (i + 1) % items.length));
      if (e.key === "ArrowLeft") setOpenIdx((i) => (i === null ? null : (i - 1 + items.length) % items.length));
    };
    window.addEventListener("keydown", onKey);
    document.body.style.overflow = "hidden";
    return () => {
      window.removeEventListener("keydown", onKey);
      document.body.style.overflow = "";
    };
  }, [openIdx, items.length]);

  return (
    <section id="portfolio" className="py-32 px-6 md:px-10">
      <div className="max-w-7xl mx-auto">
        <div className="flex flex-col md:flex-row md:items-end md:justify-between gap-8 mb-16">
          <div className="max-w-xl">
            <span className="font-mono text-[10px] uppercase tracking-[0.35em] text-muted-foreground block mb-4">
              Portfólio
            </span>
            <h2 className="font-display italic text-4xl md:text-5xl tracking-tight mb-4">
              Projetos selecionados
            </h2>
            <p className="text-muted-foreground text-pretty max-w-md">
              Obras que atravessam escalas — da escultura de detalhe ao cenário monumental.
              Cada peça é modelada, produzida e finalizada em ateliê próprio.
            </p>
          </div>
          <div className="flex flex-wrap gap-x-5 gap-y-2 font-mono text-[10px] uppercase tracking-[0.25em]">
            {categories.map((c) => (
              <button
                key={c}
                onClick={() => setCat(c)}
                className={`pb-1 border-b transition-colors ${
                  cat === c
                    ? "text-foreground border-foreground"
                    : "text-muted-foreground border-transparent hover:text-foreground"
                }`}
              >
                {c}
              </button>
            ))}
          </div>
        </div>

        <motion.div layout className="grid grid-cols-2 md:grid-cols-12 gap-4 md:gap-6">
          <AnimatePresence mode="popLayout">
            {items.map((p, i) => (
              <motion.button
                type="button"
                layout
                key={p.id}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: 10 }}
                transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
                onClick={() => setOpenIdx(i)}
                className={`group text-left ${spanClass[p.span]} col-span-2 relative overflow-hidden bg-zinc-100`}
                aria-label={`Ampliar: ${p.title}`}
              >
                <img
                  src={p.url}
                  alt={p.alt}
                  loading="lazy"
                  decoding="async"
                  className="w-full h-full object-cover transition-transform duration-[900ms] group-hover:scale-[1.03]"
                />
                <div className="absolute inset-x-0 bottom-0 p-4 md:p-5 bg-gradient-to-t from-black/70 via-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity">
                  <div className="flex justify-between items-end text-white">
                    <h3 className="font-display italic text-lg md:text-xl">{p.title}</h3>
                    <span className="font-mono text-[10px] uppercase tracking-[0.25em] opacity-80">
                      {p.year}
                    </span>
                  </div>
                </div>
              </motion.button>
            ))}
          </AnimatePresence>
        </motion.div>
      </div>

      <AnimatePresence>
        {openIdx !== null && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-[100] bg-black/95 flex items-center justify-center p-4"
            onClick={() => setOpenIdx(null)}
          >
            <button
              aria-label="Fechar"
              className="absolute top-5 right-5 text-white/70 hover:text-white z-10"
              onClick={() => setOpenIdx(null)}
            >
              <X className="size-6" />
            </button>
            <button
              aria-label="Anterior"
              className="absolute left-4 md:left-8 text-white/70 hover:text-white z-10"
              onClick={(e) => {
                e.stopPropagation();
                setOpenIdx((i) => (i === null ? null : (i - 1 + items.length) % items.length));
              }}
            >
              <ChevronLeft className="size-8" />
            </button>
            <button
              aria-label="Próxima"
              className="absolute right-4 md:right-8 text-white/70 hover:text-white z-10"
              onClick={(e) => {
                e.stopPropagation();
                setOpenIdx((i) => (i === null ? null : (i + 1) % items.length));
              }}
            >
              <ChevronRight className="size-8" />
            </button>
            <motion.div
              key={items[openIdx].id}
              initial={{ opacity: 0, scale: 0.98 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.35, ease: [0.16, 1, 0.3, 1] }}
              className="max-w-6xl max-h-[85vh] flex flex-col items-center"
              onClick={(e) => e.stopPropagation()}
            >
              <img
                src={items[openIdx].url}
                alt={items[openIdx].alt}
                className="max-w-full max-h-[75vh] object-contain"
              />
              <div className="mt-5 text-center text-white">
                <h3 className="font-display italic text-2xl">{items[openIdx].title}</h3>
                <p className="mt-1 font-mono text-[10px] uppercase tracking-[0.25em] text-white/60">
                  {items[openIdx].year}
                </p>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
}
