import { motion } from "framer-motion";
import { differentiators } from "@/data/site";

export function Differentiators() {
  return (
    <section aria-label="Diferenciais" className="py-32 px-6 md:px-10 border-b border-border">
      <div className="max-w-7xl mx-auto">
        <div className="max-w-xl mb-16">
          <span className="font-mono text-[10px] uppercase tracking-[0.35em] text-muted-foreground block mb-4">
            Diferenciais
          </span>
          <h2 className="font-display italic text-4xl md:text-5xl tracking-tight">
            O que nos torna diferentes.
          </h2>
        </div>
        <ul className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-x-6 gap-y-10">
          {differentiators.map((d, i) => (
            <motion.li
              key={d}
              initial={{ opacity: 0, y: 12 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true, amount: 0.5 }}
              transition={{ duration: 0.5, delay: (i % 4) * 0.05 }}
              className="border-t border-foreground pt-5"
            >
              <span className="font-mono text-[10px] uppercase tracking-[0.25em] text-muted-foreground block mb-2">
                {String(i + 1).padStart(2, "0")}
              </span>
              <p className="font-display italic text-xl md:text-2xl leading-tight">{d}</p>
            </motion.li>
          ))}
        </ul>
      </div>
    </section>
  );
}
