import { MessageCircle } from "lucide-react";
import { contact } from "@/data/contact";

export function WhatsAppFab() {
  return (
    <a
      href={contact.whatsappUrl()}
      target="_blank"
      rel="noopener noreferrer"
      aria-label="Falar no WhatsApp"
      className="fixed bottom-6 right-6 z-40 size-14 bg-emerald-500 text-black rounded-full shadow-xl flex items-center justify-center hover:scale-110 transition-transform"
    >
      <MessageCircle className="size-6 stroke-[1.75]" />
    </a>
  );
}
