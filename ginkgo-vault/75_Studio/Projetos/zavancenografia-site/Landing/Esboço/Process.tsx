import { motion } from "framer-motion";
import { process } from "@/data/site";

export function Process() {
  return (
    <section id="processo" className="py-32 px-6 md:px-10 bg-zinc-950 text-white">
      <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-12">
        <div className="md:col-span-1">
          <span className="font-mono text-[10px] uppercase tracking-[0.35em] text-white/40 block mb-4">
            Processo
          </span>
          <h2 className="font-display italic text-3xl md:text-4xl leading-tight">
            Do bloco bruto <br />à experiência.
          </h2>
          <p className="mt-6 text-sm text-white/50 leading-relaxed max-w-xs">
            O rigor da indústria encontra a sensibilidade do artista em oito etapas de precisão.
          </p>
        </div>
        <div className="md:col-span-3 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-y-14 gap-x-8">
          {process.map((p, i) => (
            <motion.div
              key={p.n}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.4 }}
              transition={{ duration: 0.55, delay: (i % 4) * 0.05, ease: [0.16, 1, 0.3, 1] }}
              className="border-l border-white/15 pl-5"
            >
              <span className="font-mono text-[10px] text-white/40 block mb-4 tracking-[0.25em]">
                {p.n} — {p.title}
              </span>
              <p className="text-sm text-white/75 leading-relaxed">{p.desc}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
