import { Instagram, Facebook, Linkedin, Mail } from "lucide-react";
import { contact } from "@/data/contact";

export function Footer() {
  return (
    <footer className="border-t border-border">
      <div className="max-w-7xl mx-auto px-6 md:px-10 py-20 grid grid-cols-1 md:grid-cols-12 gap-12">
        <div className="md:col-span-5">
          <span className="font-mono text-xs tracking-[0.35em] uppercase block mb-4">
            Zavan <span className="opacity-60">/ Scenography</span>
          </span>
          <p className="text-sm text-muted-foreground leading-relaxed max-w-sm">
            Fabricação verticalizada de cenografia, esculturas e ambientações personalizadas.
            Do briefing à instalação, com atendimento em todo o Brasil.
          </p>
          <div className="mt-8 flex gap-4">
            <a aria-label="Instagram" href={contact.instagram} target="_blank" rel="noopener noreferrer" className="hover:opacity-60 transition-opacity">
              <Instagram className="size-5 stroke-[1.25]" />
            </a>
            <a aria-label="Facebook" href={contact.facebook} target="_blank" rel="noopener noreferrer" className="hover:opacity-60 transition-opacity">
              <Facebook className="size-5 stroke-[1.25]" />
            </a>
            <a aria-label="LinkedIn" href={contact.linkedin} target="_blank" rel="noopener noreferrer" className="hover:opacity-60 transition-opacity">
              <Linkedin className="size-5 stroke-[1.25]" />
            </a>
            <a aria-label="E-mail" href={`mailto:${contact.email}`} className="hover:opacity-60 transition-opacity">
              <Mail className="size-5 stroke-[1.25]" />
            </a>
          </div>
        </div>

        <div className="md:col-span-3">
          <span className="font-mono text-[10px] uppercase tracking-[0.25em] text-muted-foreground block mb-4">Contato</span>
          <ul className="text-sm space-y-2">
            <li><a href={contact.whatsappUrl()} target="_blank" rel="noopener noreferrer" className="hover:underline">{contact.whatsappDisplay}</a></li>
            <li><a href={`mailto:${contact.email}`} className="hover:underline">{contact.email}</a></li>
            <li className="text-muted-foreground">{contact.city}</li>
          </ul>
        </div>

        <div className="md:col-span-4">
          <span className="font-mono text-[10px] uppercase tracking-[0.25em] text-muted-foreground block mb-4">Localização</span>
          <div className="aspect-[4/3] bg-zinc-100 overflow-hidden">
            <iframe
              title="Localização Zavan Cenografia"
              src={contact.mapEmbed}
              loading="lazy"
              referrerPolicy="no-referrer-when-downgrade"
              className="w-full h-full border-0 grayscale"
            />
          </div>
        </div>
      </div>

      <div className="border-t border-border">
        <div className="max-w-7xl mx-auto px-6 md:px-10 py-6 flex flex-col md:flex-row justify-between items-center gap-3 font-mono text-[10px] uppercase tracking-[0.25em] text-muted-foreground">
          <span>© {new Date().getFullYear()} Zavan Cenografia. Todos os direitos reservados.</span>
          <span>Built for immersion.</span>
        </div>
      </div>
    </footer>
  );
}
