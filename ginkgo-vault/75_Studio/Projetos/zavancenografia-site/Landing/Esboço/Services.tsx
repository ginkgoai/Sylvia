import { motion } from "framer-motion";
import { services } from "@/data/site";

export function Services() {
  return (
    <section id="servicos" className="py-32 px-6 md:px-10 bg-zinc-50 border-y border-border">
      <div className="max-w-7xl mx-auto">
        <div className="flex flex-col md:flex-row md:items-end md:justify-between gap-6 mb-16">
          <div className="max-w-xl">
            <span className="font-mono text-[10px] uppercase tracking-[0.35em] text-muted-foreground block mb-4">
              Capacidades
            </span>
            <h2 className="font-display italic text-4xl md:text-5xl tracking-tight">
              Fabricação verticalizada, da modelagem ao acabamento.
            </h2>
          </div>
          <p className="text-muted-foreground max-w-md text-pretty">
            Nove frentes de produção que se combinam em cada projeto — soluções completas para
            marcas que precisam sair do papel com escala, precisão e presença física.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-px bg-border">
          {services.map((s, i) => (
            <motion.article
              key={s.title}
              initial={{ opacity: 0, y: 16 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.3 }}
              transition={{ duration: 0.55, delay: (i % 3) * 0.06, ease: [0.16, 1, 0.3, 1] }}
              className="bg-zinc-50 p-8 md:p-10 group hover:bg-background transition-colors"
            >
              <s.icon className="size-6 stroke-[1.25]" aria-hidden />
              <h3 className="mt-8 font-display italic text-xl tracking-tight">{s.title}</h3>
              <p className="mt-3 text-sm text-muted-foreground leading-relaxed">{s.desc}</p>
            </motion.article>
          ))}
        </div>
      </div>
    </section>
  );
}
