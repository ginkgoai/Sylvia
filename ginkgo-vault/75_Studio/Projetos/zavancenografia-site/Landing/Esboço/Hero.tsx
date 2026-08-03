import { useEffect, useState } from "react";
import useEmblaCarousel from "embla-carousel-react";
import { motion } from "framer-motion";
import { heroSlides } from "@/data/portfolio";

export function Hero() {
  const [emblaRef, emblaApi] = useEmblaCarousel({ loop: true, duration: 40 });
  const [idx, setIdx] = useState(0);

  useEffect(() => {
    if (!emblaApi) return;
    const id = setInterval(() => emblaApi.scrollNext(), 5000);
    const onSel = () => setIdx(emblaApi.selectedScrollSnap());
    emblaApi.on("select", onSel);
    return () => {
      clearInterval(id);
      emblaApi.off("select", onSel);
    };
  }, [emblaApi]);

  return (
    <section id="top" className="min-h-screen flex flex-col items-center justify-center px-6 text-center pt-28 pb-20">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.9, ease: [0.16, 1, 0.3, 1] }}
        className="max-w-5xl"
      >
        <span className="font-mono text-[10px] uppercase tracking-[0.35em] text-muted-foreground mb-8 block">
          Curadoria de Espaços · Fabricação Cenográfica
        </span>
        <h1 className="font-display italic text-5xl md:text-7xl lg:text-8xl text-balance leading-[0.9] tracking-tight mb-10">
          Cenografia que transforma <br className="hidden md:block" />
          ideias em <span className="not-italic font-normal">experiências</span> inesquecíveis.
        </h1>
        <p className="text-base md:text-lg text-muted-foreground max-w-2xl mx-auto mb-12 text-pretty leading-relaxed">
          Projetamos, fabricamos e entregamos cenografias, esculturas e ambientações personalizadas
          para marcas, eventos e espaços comerciais em todo o Brasil.
        </p>
        <div className="flex flex-col sm:flex-row gap-3 justify-center items-center">
          <a
            href="#contato"
            className="px-8 py-4 bg-foreground text-background text-[10px] uppercase tracking-[0.25em] font-medium hover:bg-zinc-800 transition-colors"
          >
            Solicitar Orçamento
          </a>
          <a
            href="#portfolio"
            className="px-8 py-4 border border-border text-[10px] uppercase tracking-[0.25em] font-medium hover:border-foreground transition-colors"
          >
            Ver Portfólio
          </a>
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1, delay: 0.25, ease: [0.16, 1, 0.3, 1] }}
        className="mt-20 w-full max-w-6xl"
      >
        <div className="overflow-hidden aspect-[21/9] bg-zinc-100" ref={emblaRef}>
          <div className="flex h-full">
            {heroSlides.map((src, i) => (
              <div key={i} className="min-w-0 flex-[0_0_100%] h-full">
                <img
                  src={src}
                  alt="Projeto do portfólio Zavan Cenografia"
                  loading={i === 0 ? "eager" : "lazy"}
                  decoding="async"
                  className="w-full h-full object-cover"
                />
              </div>
            ))}
          </div>
        </div>
        <div className="flex items-center justify-between mt-4 font-mono text-[10px] uppercase tracking-[0.25em] text-muted-foreground">
          <span>Escala · Matéria · Precisão</span>
          <span>
            {String(idx + 1).padStart(2, "0")} / {String(heroSlides.length).padStart(2, "0")}
          </span>
        </div>
      </motion.div>
    </section>
  );
}
