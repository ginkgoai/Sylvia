import { CalendarDays, MessageCircle, Route, Users } from "lucide-react";
import {
  BrandHeader,
  CampaignFrame,
  ChatBubble,
  ChatWindow,
  FeatureChip,
  LeadQualificationCard,
  PrimaryCTA,
} from "../components/leaf";

export function CampaignShowcase() {
  return (
    <CampaignFrame format="feed" className="grid grid-cols-[1.02fr_.98fr] gap-10">
      <div className="flex min-w-0 flex-col">
        <BrandHeader eyebrow="Campanha 1 • Awareness" />
        <div className="mt-16">
          <h1 className="leaf-display text-[clamp(2.8rem,5vw,5.6rem)] font-extrabold leading-[.96]">
            Seu WhatsApp fecha.
            <span className="mt-2 block text-[var(--leaf-primary)]">Seus clientes não.</span>
          </h1>
          <p className="mt-8 max-w-xl text-lg leading-relaxed text-[var(--leaf-text-muted)]">
            Atendimento 24/7 com respostas humanizadas, qualificação de leads e encaminhamento inteligente.
          </p>
        </div>
        <div className="mt-10 grid gap-3">
          <FeatureChip icon={MessageCircle} label="WhatsApp 24/7" />
          <FeatureChip icon={Users} label="Qualifica oportunidades" tone="gold" />
          <FeatureChip icon={Route} label="Encaminha para atendente" />
        </div>
        <PrimaryCTA className="mt-auto self-start" />
      </div>
      <div className="flex min-w-0 flex-col justify-center gap-5">
        <ChatWindow>
          <ChatBubble sender="agent" message="Olá! Sou o LEAF. Como posso ajudar você hoje?" time="09:41" />
          <ChatBubble sender="customer" message="Quero conhecer o plano ideal para minha equipe." time="09:42" read />
          <ChatBubble sender="agent" message="Posso fazer algumas perguntas rápidas para entender sua necessidade?" time="09:42" />
        </ChatWindow>
        <LeadQualificationCard
          fields={[
            { label: "Interesse", value: "Plano profissional" },
            { label: "Equipe", value: "6 a 20 pessoas" },
            { label: "Próxima etapa", value: "Demonstração" },
          ]}
        />
        <FeatureChip icon={CalendarDays} label="Interface demonstrativa; substituir por captura real quando disponível" tone="neutral" />
      </div>
    </CampaignFrame>
  );
}
