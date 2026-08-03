import type { ReactNode } from "react";
import { CheckCheck, FileText } from "lucide-react";
import { cn } from "../../lib/cn";

export type ChatSender = "agent" | "customer" | "system";

export interface ChatAttachment {
  type: "pdf" | "image" | "catalog";
  name: string;
  meta?: string;
}

export interface ChatBubbleProps {
  sender: ChatSender;
  message: string;
  time?: string;
  read?: boolean;
  attachment?: ChatAttachment;
  className?: string;
}

export function ChatBubble({ sender, message, time, read, attachment, className }: ChatBubbleProps) {
  const isCustomer = sender === "customer";
  const isSystem = sender === "system";

  return (
    <div className={cn("flex", isCustomer ? "justify-end" : "justify-start", className)}>
      <div
        className={cn(
          "max-w-[86%] rounded-2xl border px-4 py-3 text-sm leading-relaxed",
          isCustomer && "border-[var(--leaf-border-strong)] bg-[rgba(31,174,103,.20)]",
          sender === "agent" && "border-white/5 bg-white/[0.055]",
          isSystem && "border-[var(--leaf-border)] bg-[rgba(101,199,122,.08)]",
        )}
      >
        <p>{message}</p>
        {attachment ? (
          <div className="mt-3 flex items-center gap-3 rounded-xl border border-white/8 bg-black/20 p-3">
            <FileText className="h-5 w-5 text-[var(--leaf-primary)]" />
            <div className="min-w-0">
              <div className="truncate text-xs font-semibold">{attachment.name}</div>
              {attachment.meta ? <div className="text-[10px] text-[var(--leaf-text-muted)]">{attachment.meta}</div> : null}
            </div>
          </div>
        ) : null}
        {time ? (
          <div className="mt-1 flex items-center justify-end gap-1 text-[10px] text-[var(--leaf-text-muted)]">
            <span>{time}</span>
            {read ? <CheckCheck className="h-3 w-3 text-[var(--leaf-primary-bright)]" /> : null}
          </div>
        ) : null}
      </div>
    </div>
  );
}

export interface ChatWindowProps {
  children: ReactNode;
  title?: string;
  status?: string;
  className?: string;
}

export function ChatWindow({ children, title = "LEAF by Ginkgo", status = "online", className }: ChatWindowProps) {
  return (
    <div className={cn("leaf-card overflow-hidden", className)}>
      <div className="flex items-center gap-3 border-b border-white/6 px-5 py-4">
        <div className="h-9 w-9 rounded-full bg-[var(--leaf-primary)]/15 ring-1 ring-[var(--leaf-border)]" />
        <div>
          <div className="text-sm font-semibold">{title}</div>
          <div className="text-[11px] text-[var(--leaf-primary)]">{status}</div>
        </div>
      </div>
      <div className="space-y-3 p-5">{children}</div>
    </div>
  );
}
