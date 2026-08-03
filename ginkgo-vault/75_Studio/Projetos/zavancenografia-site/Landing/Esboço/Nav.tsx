import { useEffect, useState } from "react";

export function Nav() {
  const [scrolled, setScrolled] = useState(false);
  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 40);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <nav
      aria-label="Navegação principal"
      className={`fixed top-0 w-full z-50 px-6 md:px-10 py-5 flex justify-between items-center transition-[background,backdrop-filter] duration-500 ${
        scrolled ? "bg-background/70 backdrop-blur-md" : ""
      } ${scrolled ? "text-foreground" : "mix-blend-difference text-white"}`}
    >
      <a href="#top" className="font-mono text-xs tracking-[0.3em] uppercase">
        Zavan <span className="opacity-60">/ Scenography</span>
      </a>
      <div className="hidden md:flex gap-10 text-[10px] tracking-[0.25em] uppercase font-medium">
        <a href="#portfolio" className="hover:opacity-50 transition-opacity">Portfólio</a>
        <a href="#servicos" className="hover:opacity-50 transition-opacity">Serviços</a>
        <a href="#processo" className="hover:opacity-50 transition-opacity">Processo</a>
        <a href="#contato" className="hover:opacity-50 transition-opacity">Contato</a>
      </div>
      <a
        href="#contato"
        className="hidden md:inline-block text-[10px] tracking-[0.25em] uppercase font-medium border border-current px-4 py-2 hover:opacity-70 transition-opacity"
      >
        Orçamento
      </a>
    </nav>
  );
}
