import { useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import { z } from "zod";
import { toast } from "sonner";
import { contact } from "@/data/contact";

const schema = z.object({
  nome: z.string().min(2, "Informe seu nome"),
  empresa: z.string().min(2, "Informe sua empresa"),
  email: z.string().email("E-mail inválido"),
  whatsapp: z.string().min(8, "Informe um WhatsApp válido"),
  tipo: z.string().min(1, "Escolha o tipo de projeto"),
  mensagem: z.string().min(10, "Conte um pouco mais sobre o projeto"),
});
type FormData = z.infer<typeof schema>;

export function QuoteCta() {
  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting },
  } = useForm<FormData>({ resolver: zodResolver(schema) });

  async function onSubmit(data: FormData) {
    // TODO: plug CRM / GA4 / Meta Pixel here
    console.log("[Zavan][Lead]", data);
    await new Promise((r) => setTimeout(r, 700));
    toast.success("Recebemos seu pedido — retornamos em até 48h úteis.");
    reset();
  }

  const inputCls =
    "w-full bg-transparent border-b border-white/20 py-3 text-sm text-white placeholder:text-white/40 focus:outline-none focus:border-white transition-colors";

  return (
    <section id="contato" className="py-32 px-6 md:px-10 bg-zinc-950 text-white">
      <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24 items-start">
        <div>
          <span className="font-mono text-[10px] uppercase tracking-[0.35em] text-white/40 block mb-6">
            Contato · Orçamento
          </span>
          <h2 className="font-display italic text-4xl md:text-6xl leading-[0.95] tracking-tight mb-8">
            Seu projeto merece <br />sair do papel.
          </h2>
          <p className="text-white/60 max-w-md leading-relaxed mb-10 text-pretty">
            Envie seu briefing, uma referência ou apenas uma ideia. Nossa equipe retorna com
            proposta técnica e comercial em até 48 horas úteis.
          </p>
          <a
            href={contact.whatsappUrl()}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-3 px-8 py-4 bg-emerald-500 text-black text-[10px] uppercase tracking-[0.25em] font-medium hover:bg-emerald-400 transition-colors"
          >
            Falar no WhatsApp
            <span aria-hidden>→</span>
          </a>
        </div>

        <form onSubmit={handleSubmit(onSubmit)} className="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div className="sm:col-span-1">
            <label className="font-mono text-[10px] uppercase tracking-[0.25em] text-white/40 block mb-1">Nome</label>
            <input {...register("nome")} className={inputCls} placeholder="Seu nome" />
            {errors.nome && <p className="mt-1 text-[10px] text-red-400">{errors.nome.message}</p>}
          </div>
          <div className="sm:col-span-1">
            <label className="font-mono text-[10px] uppercase tracking-[0.25em] text-white/40 block mb-1">Empresa</label>
            <input {...register("empresa")} className={inputCls} placeholder="Empresa / Agência" />
            {errors.empresa && <p className="mt-1 text-[10px] text-red-400">{errors.empresa.message}</p>}
          </div>
          <div className="sm:col-span-1">
            <label className="font-mono text-[10px] uppercase tracking-[0.25em] text-white/40 block mb-1">E-mail</label>
            <input type="email" {...register("email")} className={inputCls} placeholder="voce@empresa.com" />
            {errors.email && <p className="mt-1 text-[10px] text-red-400">{errors.email.message}</p>}
          </div>
          <div className="sm:col-span-1">
            <label className="font-mono text-[10px] uppercase tracking-[0.25em] text-white/40 block mb-1">WhatsApp</label>
            <input {...register("whatsapp")} className={inputCls} placeholder="(11) 99999-9999" />
            {errors.whatsapp && <p className="mt-1 text-[10px] text-red-400">{errors.whatsapp.message}</p>}
          </div>
          <div className="sm:col-span-2">
            <label className="font-mono text-[10px] uppercase tracking-[0.25em] text-white/40 block mb-1">Tipo de projeto</label>
            <select {...register("tipo")} className={`${inputCls} appearance-none`} defaultValue="">
              <option value="" disabled className="bg-zinc-950">Selecione…</option>
              <option className="bg-zinc-950">Escultura em EPS</option>
              <option className="bg-zinc-950">Personagem gigante</option>
              <option className="bg-zinc-950">Cenografia corporativa</option>
              <option className="bg-zinc-950">Ambientação temática</option>
              <option className="bg-zinc-950">Fachada cenográfica</option>
              <option className="bg-zinc-950">Display / painel instagramável</option>
              <option className="bg-zinc-950">Cenário de evento</option>
              <option className="bg-zinc-950">Natal / Páscoa sazonal</option>
              <option className="bg-zinc-950">Projeto especial</option>
            </select>
            {errors.tipo && <p className="mt-1 text-[10px] text-red-400">{errors.tipo.message}</p>}
          </div>
          <div className="sm:col-span-2">
            <label className="font-mono text-[10px] uppercase tracking-[0.25em] text-white/40 block mb-1">Mensagem</label>
            <textarea {...register("mensagem")} rows={4} className={`${inputCls} resize-none`} placeholder="Descreva o projeto, escala aproximada, prazo…" />
            {errors.mensagem && <p className="mt-1 text-[10px] text-red-400">{errors.mensagem.message}</p>}
          </div>
          <div className="sm:col-span-2 pt-2">
            <button
              type="submit"
              disabled={isSubmitting}
              className="w-full sm:w-auto px-10 py-4 bg-white text-black text-[10px] uppercase tracking-[0.25em] font-medium hover:bg-white/90 transition-colors disabled:opacity-50"
            >
              {isSubmitting ? "Enviando…" : "Enviar Pedido de Orçamento"}
            </button>
          </div>
        </form>
      </div>
    </section>
  );
}
