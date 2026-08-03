import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import { faqs } from "@/data/site";

export function Faq() {
  return (
    <section id="faq" className="py-32 px-6 md:px-10">
      <div className="max-w-4xl mx-auto">
        <div className="mb-14 text-center">
          <span className="font-mono text-[10px] uppercase tracking-[0.35em] text-muted-foreground block mb-4">
            Perguntas frequentes
          </span>
          <h2 className="font-display italic text-4xl md:text-5xl tracking-tight">
            Dúvidas comuns.
          </h2>
        </div>
        <Accordion type="single" collapsible className="w-full">
          {faqs.map((f, i) => (
            <AccordionItem key={i} value={`item-${i}`} className="border-border">
              <AccordionTrigger className="text-left text-base md:text-lg font-display italic tracking-tight hover:no-underline py-6">
                {f.q}
              </AccordionTrigger>
              <AccordionContent className="text-muted-foreground text-base leading-relaxed pb-6">
                {f.a}
              </AccordionContent>
            </AccordionItem>
          ))}
        </Accordion>
      </div>
    </section>
  );
}
