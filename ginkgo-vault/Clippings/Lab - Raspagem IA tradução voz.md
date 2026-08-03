---
title: "Lab - Raspagem IA tradução voz"
source: "https://chatgpt.com/g/g-p-6920bddfbb548191ac06d937cdb0b5c0/c/68f2cdb5-ffe8-8326-a943-9d1cc7c60b78"
author:
published:
created: 2026-07-19
description: "O ChatGPT é seu assistente de IA para uso diário. Converse com a IA mais avançada para explorar ideias, resolver problemas e aprender mais rápido."
tags:
  - "clippings"
---
sex., 17 de out. às 20:14

Seguinte quero te passar uma tarefa minuciosa, uma raspagem completa dos avanços da CHINA na aplicação de IA para tradução de voz simultânea e chamadas de voz ou vídeos ao vivo e integração com serviços de chamada e livre, use pesquisa em mandarim e traduza em um super relatório detalhado de maneiras e aplicações de uso.

perfeito, Gabriel — vamos varrer a China inteira (tecnologicamente falando) e condensar num dossiê prático. Abaixo está um relatório de campo, em português claro, com termos-chave em mandarim para você rastrear fontes originais. Foquei em aplicações de tradução de voz simultânea (同声传译), chamadas de voz/vídeo ao vivo (语音/视频通话), e integrações com serviços de reunião/streaming. No fim, deixo arquiteturas de integração que você pode copiar na Ginkgo LiveLingo.

## Visão geral — onde a China está puxando a fila

- A China empurrou tradução simultânea de “demo” para “produto” em reuniões, lives e hardware de consumo. Três trilhas se destacam:
	1. **SaaS de reunião** (Tencent Meeting 腾讯会议, Feishu/飞书, DingTalk/钉钉, Huawei Cloud Meeting/华为云会议), já com modos nativos de *simultaneous interpreting* e/ou legendas multilíngues. [Huawei Cloud Support+7meeting.tencent.com+7meeting.tencent.com+7](https://meeting.tencent.com/news/17zyyfysj20240822.html?utm_source=chatgpt.com)
		2. **Nuvens & APIs** (Alibaba 通义听悟/Tongyi Tingwu, Baidu 实时语音翻译, ByteDance/Volcengine 火山引擎 “豆包语音” + veRTC) para montar pipelines WebRTC/RTMP com baixa latência. [volcengine.com+7tingwu.aliyun.com+7tongyi.aliyun.com+7](https://tingwu.aliyun.com/?utm_source=chatgpt.com)
		3. **Hardware/consumer** com *earbuds* e *translators* (iFlytek/科大讯飞, Timekettle/时空壶, Xiaomi) trazendo *simulcast* de 40–60 idiomas e features como “voz clonada” (声音复刻) no próprio fone. [Sina Finance+5Sina Finance+5ITHome+5](https://finance.sina.com.cn/tech/it/2025-10-14/doc-inftwhpk2770596.shtml?cre=tianyi&loc=15&mod=pchp&r=0&rfunc=64&tj=cxvertical_pc_hp&tr=12&utm_source=chatgpt.com)

## Jogadores-chave, capacidades e onde usar

## 1) iFlytek 科大讯飞 — “AI 同传” de ponta + fone tradutor

- **Estado-da-arte comercial** em *simultaneous interpreting* com resposta inicial média de ~2 s (中英同传首字响应≈2秒) e dicionários profissionais 80–100k termos (médico/financeiro/jurídico). Agora com **voz do próprio usuário** para ler a tradução (声音复刻). Ideal para conferências, keynotes e atendimento “premium”. [Sina Finance+2品玩+2](https://finance.sina.com.cn/tech/shenji/2025-10-15/doc-inftxuqs2173268.shtml?cre=tianyi&loc=5&mod=pchp&r=0&rfunc=83&tj=cxvertical_pc_hp&tr=12&utm_source=chatgpt.com)
- **Stack de produtos**: 讯飞同传 (plataforma de conferência/legendagem), app 讯飞翻译/听见, **AI翻译耳机** (60 línguas, “dual channel” p/ 2 pessoas usando um par). Bom para *face-to-face*, chamadas telefônicas/vídeo e “旁听同传” (escuta lateral em palestras). [iFlyrec+2Sina Finance+2](https://tongchuan.iflyrec.com/?utm_source=chatgpt.com)

**Cenários de uso**

- Palestras internacionais com *overlay* bilíngue no telão e *audio-feed* por canal.
- *Line-of-business* (médico, legal, finanças) com glossário forçado.

## 2) Alibaba Cloud — 通义听悟 (Tongyi Tingwu) + FunASR/Paraformer

- **通义听悟**: “copiloto” de áudio/vídeo com **realtime STT + tradução** e **resumo/ata** pós-reunião; atende a *meeting minutes* e longas gravações. Pode operar via API e **implantação privada** (ponto forte para compliance). [tingwu.aliyun.com+2tongyi.aliyun.com+2](https://tingwu.aliyun.com/?utm_source=chatgpt.com)
- **FunASR + Paraformer** (达摩院): base industrial *open-source* para **ASR streaming** de baixa latência (não-autoregressivo) e *hotword boosting*; muito usada para montar **pipelines próprios de SimulST** e *captioning* com latências <1s por bloco de 480–900 ms. [ModelScope+3Aliyun Developer Community+3Aliyun Developer Community+3](https://developer.aliyun.com/article/1335528?utm_source=chatgpt.com)

**Cenários de uso**

- **Live shopping** transfronteiriço com OBS+WebSocket e inserção de legendas multilíngues.
- **Chamada B2B** com política de dados on-prem.

## 3) Tencent Meeting 腾讯会议 — modo multilíngue “ligou, traduziu”

- Suporta **17 idiomas** com tradução nas **legendas em tempo real** e na **gravação pós-call**; tem **dial-in** telefônico (mix fixo + VoIP). Em *enterprise tiers* há controles de canais de interpretação (传译频道). Boa base para clientes que “já usam Tencent”. [meeting.tencent.com+1](https://meeting.tencent.com/news/17zyyfysj20240822.html?utm_source=chatgpt.com)

## 4) Baidu — 实时语音翻译 API (WebSocket)

- API “pronta para batalha” com **ASR+MT+TTS** em **45 idiomas**, inteligente em pontuação/segmentação e **broadcast** de resultados parciais — excelente para **overlay** em lives (RTMP/OBS) e *speaker coach*. [ai.baidu.com](https://ai.baidu.com/tech/mt/realtime_speech_trans?utm_source=chatgpt.com)

## 5) ByteDance / Volcengine 火山引擎 — “豆包语音” + veRTC

- Oferece **Realtime API** de voz-para-voz, **ASR/TTS de grande modelo**, *voice cloning* e **veRTC** para **salas em WebRTC** com *routing* de áudio/vídeo de baixíssima latência. É a rota mais “ *developer-friendly* ” para **conversação simultânea** e **tradução em chamadas 1:1 ou 1:N** web/mobile. [volcengine.com+2volcengine.com+2](https://www.volcengine.com/docs/6561/1594356?utm_source=chatgpt.com)

## 6) Feishu/飞书 (Lark), DingTalk/钉钉, Huawei Cloud Meeting

- **Feishu**: recursos de **字幕+翻译** e **modo 同声传译** (versões recentes). [feishu.cn+1](https://www.feishu.cn/hc/zh-CN/articles/360049067870-%E4%BD%BF%E7%94%A8%E5%90%8C%E5%A3%B0%E4%BC%A0%E8%AF%91%E5%8A%9F%E8%83%BD?utm_source=chatgpt.com)
- **DingTalk Rooms**: *simul-interpreting* para eventos híbridos; nova linha “DingTalk A1” integra **tradução + ata inteligente**. [alidocs.dingtalk.com+1](https://alidocs.dingtalk.com/i/p/Y7kmbokZp3pgGLq2/docs/N7dx2rn0JbZ943aOuxX59M64JMGjLRb3?utm_source=chatgpt.com)
- **Huawei Cloud Meeting**: canais de **同传** e demonstrações com **盘古/Pangu** + “数字人” fazendo **labial sincronizado** em idioma alvo — forte narrativa de *mother-tongue experience*. [Huawei Cloud Community+2Huawei Cloud+2](https://bbs.huaweicloud.com/blogs/429855?utm_source=chatgpt.com)

## 7) Hardware consumidor — “tradução no ouvido”

- **iFlytek AI 翻译耳机**: 60 línguas, *dual channel*, **voz clonada**; pensado para **chamada telefônica/vídeo** e **reuniões**. [Sina Finance+1](https://finance.sina.com.cn/tech/it/2025-10-14/doc-inftwhpk2770596.shtml?cre=tianyi&loc=15&mod=pchp&r=0&rfunc=64&tj=cxvertical_pc_hp&tr=12&utm_source=chatgpt.com)
- **Timekettle WT2 Edge/W3** (Shenzhen): *true bi-directional simultaneous* com ~0,5 s alegados; útil para atendimento presencial e feiras. [Timekettle+2Timekettle+2](https://www.timekettle.co/zh-hans-ar/products/wt2-edge-starter-set?utm_source=chatgpt.com)
- **Xiaomi** (Buds/phones): *AI captions* e **tradução ao vivo** integradas ao sistema (澎湃OS2/AI 字幕). [Sina Finance+1](https://finance.sina.com.cn/tech/roll/2024-10-29/doc-incufqps1796817.shtml?utm_source=chatgpt.com)

## Aplicações reais (China → mundo)

- **Conferências globais**: WAIC 2025 com **讯飞同传** servindo como “invisible comms officer”; demos de latência curta e melhor *prosody*. [品玩](https://www.pingwest.com/a/306645?utm_source=chatgpt.com)
- **Eventos/governo/turismo**: “北信源” levou **大模型语音翻译** a feiras internacionais (IASP, Tokyo meetups) e lançou app **AItran**. [Stcn](https://www.stcn.com/article/detail/3346258.html?utm_source=chatgpt.com)
- **Live streaming/TikTok**: ecossistema chinês padronizou *stack* **OBS + STT plugin + Translation API + subtitle overlay** para *lives* multilíngues. [Ipdodo](https://www.ipdodo.com/news/12745/?utm_source=chatgpt.com)

## Pesquisa & modelos que importam para baixa latência

- **Paraformer (Alibaba 达摩院)**: ASR **não-autoregressivo** industrial, 5–10× mais eficiente que S2S autoregressivo típico; versões *online* operam em janelas 480–900 ms. Base de muitos pipelines SimulST open-source. [Aliyun Developer Community+1](https://developer.aliyun.com/article/1210192?utm_source=chatgpt.com)
- **FunASR**: *toolkit* que integra VAD→ASR→PUNC→(MT/TTS) com **streaming** e *hotwords*. [Zhuanlan+1](https://zhuanlan.zhihu.com/p/1939029320631813876?utm_source=chatgpt.com)
- **FireRedTTS-1S (2025)**: TTS *streamable* com **<150 ms** de latência de geração; útil para *speech-to-speech* natural. [arXiv](https://arxiv.org/abs/2503.20499?utm_source=chatgpt.com)

## Regras & compliance (para ir ao ar sem surpresas)

- **深度合成管理规定** (CAC, 2023/01/10): exige controles, veracidade e **marcação** quando houver “deep synthesis” (inclui **voz clonada**). [Governo da China](https://www.gov.cn/zhengce/zhengceku/2022-12/12/content_5731431.htm?utm_source=chatgpt.com)
- **生成式AI 暂行办法** (2023/07/13): base regulatória para serviços de GenAI na China (texto, **áudio**, vídeo). [Supervisão de Mercados+1](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm?utm_source=chatgpt.com)
- **合成内容标识办法** (2025/09/01 em vigor): obriga **rótulos explícitos/implícitos** em conteúdo gerado (texto-imagem- **áudio** -vídeo). Para *speech-to-speech* com voz clonada, **marcação é mandatória**. [Supervisão de Mercados+2Supervisão de Mercados+2](https://www.cac.gov.cn/2025-03/14/c_1743654685899683.htm?utm_source=chatgpt.com)
- **Telecom/VoIP**: chamadas públicas exigem licenças (电信条例); para *gateway* SIP/RTC em território chinês, faça via provedores licenciados ou *clouds* locais. [Governo da China](https://www.gov.cn/gongbao/content/2016/content_5139478.htm?utm_source=chatgpt.com)

## Como integrar — três arquiteturas copiáveis para a LiveLingo

## A) “Meeting overlay” universal (Zoom/Meet/Voov/Feishu)

1. **Captura de áudio** (NDI/virtual mic) → **ASR streaming** (FunASR/Paraformer *self-hosted* ou **Baidu Realtime** via WebSocket).
2. **MT** (通义/自建 NMT) → **subtitle render** em **OBS** (Text source) e **canal TTS** opcional em *monitor mix*.
3. **Retorno aos participantes**:
	- **Legendas** integradas quando a plataforma suporta (Tencent Meeting, Huawei Meeting).
		- **Canal de interpretação** separado (interpretation channel). [ai.baidu.com+1](https://ai.baidu.com/tech/mt/realtime_speech_trans?utm_source=chatgpt.com)

## B) “WebRTC bidirecional” (site/app LiveLingo)

- **veRTC (Volcengine)** faz roteamento de áudio/vídeo; *workers* aplicam **ASR→MT→TTS** *on the fly* (豆包语音 APIs).
- **Modo *speech-to-speech*** com **voz clonada** opcional (marcada conforme CAC).
- **Latência**: sub-segundo percepção se você *chunkar* 300–600 ms e sintetizar *incremental TTS*. [volcengine.com+1](https://www.volcengine.com/product/veRTC/ConversationalAI?utm_source=chatgpt.com)

## C) “Live commerce multilíngue” (TikTok/Douyin/YouTube)

- **OBS** + plugin STT (Whisper/Live Captions) → **translate API** (Baidu/Volcengine) → **overlay** com estilos pré-prontos; *fallback*: *dual-sub* para VOD. [Ipdodo](https://www.ipdodo.com/news/12745/?utm_source=chatgpt.com)

## Tabela rápida — quando usar cada um

- **Quer “ligar e usar” em corp**: Tencent Meeting / Feishu / DingTalk / Huawei Meeting (modo 同传 nativo). [meeting.tencent.com+2feishu.cn+2](https://meeting.tencent.com/news/17zyyfysj20240822.html?utm_source=chatgpt.com)
- **Quer API componível/privada**: Alibaba 通义听悟 + FunASR/Paraformer; Baidu 实时语音翻译; Volcengine (ASR/TTS + veRTC). [volcengine.com+3tongyi.aliyun.com+3Aliyun Developer Community+3](https://tongyi.aliyun.com/tingwu?utm_source=chatgpt.com)
- **Quer hardware “no bolso”**: iFlytek AI 翻译耳机; Timekettle WT2 Edge; fones Xiaomi mais novos. [Sina Finance+2Timekettle+2](https://finance.sina.com.cn/tech/it/2025-10-14/doc-inftwhpk2770596.shtml?cre=tianyi&loc=15&mod=pchp&r=0&rfunc=64&tj=cxvertical_pc_hp&tr=12&utm_source=chatgpt.com)

## Métricas que importam (observadas nas fontes)

- **First token/word**: iFlytek reporta **≈2 s** em CH↔EN *simul* (terceira grande atualização do modelo). [Sina Finance](https://finance.sina.com.cn/tech/shenji/2025-10-15/doc-inftxuqs2173268.shtml?cre=tianyi&loc=5&mod=pchp&r=0&rfunc=83&tj=cxvertical_pc_hp&tr=12&utm_source=chatgpt.com)
- **Idiomas**: Tencent Meeting **17 línguas**; Baidu API **≈45 línguas**; iFlytek fone **60 línguas**. [meeting.tencent.com+2ai.baidu.com+2](https://meeting.tencent.com/news/17zyyfysj20240822.html?utm_source=chatgpt.com)
- **Pipeline open-source**: FunASR/Paraformer com janelas **480–900 ms**, hotwords e eficiência 5–10× (S2S). [Aliyun Developer Community+1](https://developer.aliyun.com/article/1335528?utm_source=chatgpt.com)
- **TTS streaming**: FireRedTTS-1S com **<150 ms** de latência de síntese incremental (paper 2025). [arXiv](https://arxiv.org/abs/2503.20499?utm_source=chatgpt.com)

## Padrões de implementação (com pitadas práticas)

- **Glossário forçado**: use *hotword boosting* no FunASR e dicionários dinâmicos em iFlytek/Baidu para *brands/jargões*. [Zhuanlan](https://zhuanlan.zhihu.com/p/1939029320631813876?utm_source=chatgpt.com)
- **Segmentação inteligente**: aceite *partial hypotheses* (ASR parcial) e re-emita *stabilized segments* para reduzir “pula-pula” de legenda. Baidu e Alibaba já entregam isso. [ai.baidu.com+1](https://ai.baidu.com/tech/mt/realtime_speech_trans?utm_source=chatgpt.com)
- **Canal de áudio dedicado**: em plataformas com “同传频道”, publique o TTS alvo como **interpretação** (não sobreponha ao *floor audio*). [meeting.tencent.com](https://meeting.tencent.com/support-version-detail/427/index.html?utm_source=chatgpt.com)
- **WebRTC io**: em chamadas 1:1, faça **barge-in handling** (detectar interrupção) e **AEC/NS** (Acoustic Echo Cancelation/Noise Suppression) do SDK RTC — Volcengine já traz *building blocks*. [volcengine.com](https://www.volcengine.com/product/veRTC/ConversationalAI?utm_source=chatgpt.com)
- **Compliance**: se usar **voz clonada do falante** (iFlytek “声音复刻”), aplique **marcação explícita** no UI/áudio conforme a **CAC 2025**. [Supervisão de Mercados](https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm?utm_source=chatgpt.com)

## Pontos de atenção (para produto global)

- **Licenças de telecom** (中国电信条例): evite intermediar tráfego telefônico “como operadora” em solo chinês; use *dial-in* oficial das plataformas ou *clouds* licenciadas. [Governo da China](https://www.gov.cn/gongbao/content/2016/content_5139478.htm?utm_source=chatgpt.com)
- **Algoritmo/Deep Synthesis备案**: serviços com “capacidade de mobilização social” precisam de **algoritmo备案** (algumas categorias). [Supervisão de Mercados](https://www.cac.gov.cn/2025-07/14/c_1754207718303963.htm?utm_source=chatgpt.com)
- **Marcações de conteúdo**: *speech-to-speech* com *voice cloning* precisa de rotulagem; configure *watermark* / *earcon* em TTS como camada adicional de transparência. [Supervisão de Mercados](https://www.cac.gov.cn/2025-03/14/c_1743654685899683.htm?utm_source=chatgpt.com)

## Roadmap sugerido para a Ginkgo LiveLingo (pronto para execução)

1. **MVP WebRTC** (web + Android):
	- **veRTC** p/ sala 1:1/1:N → **豆包ASR** (stream) → **MT** (EN↔PT↔ZH) → **TTS stream** (voz neutra; “voz clonada” sob opt-in + rótulo). [volcengine.com+1](https://www.volcengine.com/product/veRTC/ConversationalAI?utm_source=chatgpt.com)
2. **Modo Reunião conectável**:
	- *Adapter* para **Tencent Meeting/Feishu/DingTalk**: injete legendas via *screen overlay* e/ou publique TTS no **canal de interpretação** quando disponível. [meeting.tencent.com](https://meeting.tencent.com/support-version-detail/427/index.html?utm_source=chatgpt.com)
3. **Live commerce**:
	- *Preset* OBS com **Baidu Realtime** (WS) → *overlay* bilíngue; *macro* de glossário por produto. [ai.baidu.com](https://ai.baidu.com/tech/mt/realtime_speech_trans?utm_source=chatgpt.com)
4. **On-prem corporativo (China/LatAm)**:
	- **通义听悟** + **FunASR/Paraformer** *self-hosted* para compliance, com gateway LiveKit/Janus se preferir infra própria. [AlibabaCloud+1](https://www.aliyun.com/activity/intelligent/nsl/tingwu?utm_source=chatgpt.com)
5. **Qualidade percebida**:
	- *A/B* de latência: **chunks 320–600 ms**, *endpointer* agressivo + TTS incremental (ex.: FireRedTTS-like). [arXiv](https://arxiv.org/abs/2503.20499?utm_source=chatgpt.com)
6. **Compliance UX**:
	- *Badge* “AI 语音合成/AI Voice” + *earcon* curto em cada início de fala sintetizada, atendendo **标识办法(2025)**. [Supervisão de Mercados](https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm?utm_source=chatgpt.com)

—

Quer que eu transforme isso em um **plano técnico passo-a-passo** (com endpoints, exemplos de WebSocket, e um *boilerplate* WebRTC para Android/Web) já alinhado ao seu stack Ginkgo (n8n + Evolution API + Flowise)? Posso entregar já com *glossary injection* e presets de OBS/RTMP.

Sim.

perfeito — aqui vai o “kit de montagem” do LiveLingo do zero ao operacional, já encaixado no teu stack (n8n + Evolution API + Flowise). Trago duas trilhas (cloud chinesa e self-host), exemplos de WebSocket ponta-a-ponta, boilerplate WebRTC Web/Android, esquema de glossário, presets de OBS e o fio de compliance. Copia/cola com pequenas trocas de chaves.

## Arquitetura em 2 sabores

**Sabor A — Cloud chinesa, latência mínima (recomendado para MVP)**

- **veRTC (ByteDance/Volcengine)** para salas WebRTC 1:1/1:N.
- **ASR/TTS Realtime** da própria Volcengine ou Baidu Realtime (WS).
- **MT** (tradução) via Volcengine/Alibaba (qualquer REST/WS).
- **n8n** como orquestrador (glossário, logs, billing, webhooks).
- **Flowise** como “consciência” (contexto, instruções dinâmicas).
- **Evolution API** para ponte com WhatsApp quando a “chamada” for voz via WhatsApp (push de transcrições/legendas/áudio TTS).

**Sabor B — Self-host/privado (compliance e controle de custo)**

- **FunASR + Paraformer (streaming)** em Docker para ASR.
- **NMT** (tradução) via servidor próprio (por ex. Marian/Opus+ dicionário) ou API externa.
- **TTS streaming** (por ex. FireRed-like/Kokoro stream) com síntese incremental.
- **LiveKit/Janus** para RTC próprio ou manter veRTC só para roteamento.

> Dá para começar no **Sabor A** (MVP em dias) e evoluir para **B** por cliente/região.

---

## 1) Boilerplate WebRTC (Web) — captura, envio e reprodução TTS

### Front-end (Browser, JS/TS)

```markdown
<!doctype html>
<html>
  <body>
    <button id="join">Entrar</button>
    <select id="lang-in"><option value="zh">ZH</option><option value="en">EN</option><option value="pt">PT</option></select>
    <select id="lang-out"><option value="en">EN</option><option value="pt">PT</option><option value="zh">ZH</option></select>
    <div id="subs"></div>
    <audio id="tts" autoplay playsinline></audio>
    <script type="module">
      const ws = new WebSocket("wss://SEU_BACKEND/realtime"); // servidor Node (abaixo)
      const ttsEl = document.getElementById('tts');
      const subsEl = document.getElementById('subs');
      let mediaStream, mediaRecorder;

      async function start() {
        mediaStream = await navigator.mediaDevices.getUserMedia({ audio: { echoCancellation: true, noiseSuppression: true }, video: false });
        const audioCtx = new AudioContext();
        const source = audioCtx.createMediaStreamSource(mediaStream);
        // grava em chunks ~320ms para latência baixa
        const dest = audioCtx.createMediaStreamDestination();
        source.connect(dest);
        const mime = MediaRecorder.isTypeSupported('audio/webm;codecs=opus') ? 'audio/webm;codecs=opus' : 'audio/webm';
        mediaRecorder = new MediaRecorder(dest.stream, { mimeType: mime, audioBitsPerSecond: 32000 });
        mediaRecorder.ondataavailable = (e) => { if (e.data.size > 0 && ws.readyState === 1) ws.send(e.data); };
        mediaRecorder.start(320);

        ws.onopen = () => {
          ws.send(JSON.stringify({ type: 'config', lang_in: document.getElementById('lang-in').value, lang_out: document.getElementById('lang-out').value, partials: true }));
        };
        ws.onmessage = (ev) => {
          if (typeof ev.data !== 'string') {
            // binário = chunk de TTS
            ev.data.arrayBuffer().then(buf => {
              const blob = new Blob([buf], { type: 'audio/mpeg' }); // ou audio/ogg
              const url = URL.createObjectURL(blob);
              ttsEl.src = url; // reprodução incremental
            });
            return;
          }
          const msg = JSON.parse(ev.data);
          if (msg.type === 'subtitle') {
            subsEl.textContent = msg.text;
          }
        };
      }
      document.getElementById('join').onclick = start;
    </script>
  </body>
</html>
```

### Backend (Node.js, WS proxy “tudo-em-um”)

- Recebe áudio **Opus/WebM** → envia para **ASR streaming** (WS) → recebe **parciais** → passa em **MT** → devolve `subtitle` e **solicita TTS incremental**, devolvendo **binário** ao browser.
- Substitua os stubs `ASR_WS_URL`, `TTS_WS_URL` e `MT_URL` pelos provedores (Volc/Baidu/Alibaba) ou pelos teus serviços self-host.
```markdown
// server.js
import express from "express";
import { WebSocketServer } from "ws";
import fetch from "node-fetch";
import WebSocket from "ws";

const app = express();
const wss = new WebSocketServer({ noServer: true });

const ASR_WS_URL = "wss://ASR-PROVEDOR/realtime";
const TTS_WS_URL = "wss://TTS-PROVEDOR/stream";
const MT_URL     = "https://MT-PROVEDOR/translate";

function translateText(text, src, tgt, glossary=[]) {
  return fetch(MT_URL, {
    method: "POST",
    headers: { "content-type": "application/json", "authorization": \`Bearer ${process.env.MT_KEY}\` },
    body: JSON.stringify({ text, source: src, target: tgt, glossary })
  }).then(r => r.json()).then(j => j.translation);
}

wss.on("connection", (client) => {
  let cfg = { lang_in: "zh", lang_out: "pt", partials: true, glossary: [] };

  // 1) ASR socket para upstream
  const asr = new WebSocket(ASR_WS_URL, { headers: { Authorization: \`Bearer ${process.env.ASR_KEY}\` } });
  const tts = new WebSocket(TTS_WS_URL, { headers: { Authorization: \`Bearer ${process.env.TTS_KEY}\` } });

  client.on("message", async (data) => {
    if (typeof data === "string") {
      const msg = JSON.parse(data);
      if (msg.type === "config") { cfg = { ...cfg, ...msg }; return; }
      return;
    }
    // binário do microfone -> ASR
    if (asr.readyState === 1) asr.send(data);
  });

  asr.on("message", async (raw) => {
    const msg = JSON.parse(raw.toString());
    if (msg.type === "partial" || msg.type === "final") {
      const tr = await translateText(msg.text, cfg.lang_in, cfg.lang_out, cfg.glossary);
      client.send(JSON.stringify({ type: "subtitle", text: tr, stability: msg.type }));

      // Solicita TTS incremental (envie texto curto por curto)
      if (tts.readyState === 1) tts.send(JSON.stringify({ text: tr, voice: "neutral", stream: true }));
    }
  });

  // Retorna áudio TTS (binário) ao browser
  tts.on("message", (audioChunk) => { client.send(audioChunk); });

  client.on("close", () => { try { asr.close(); tts.close(); } catch(e){} });
});

const server = app.listen(process.env.PORT || 8080);
server.on("upgrade", (req, socket, head) => {
  if (req.url === "/realtime") wss.handleUpgrade(req, socket, head, (ws) => wss.emit("connection", ws, req));
  else socket.destroy();
});
```

> **Latência prática**: mande *chunks* de 320–600 ms; aceite parciais do ASR; re-emita traduções curtas; TTS **streaming** com *buffer* mínimo de ~150–300 ms por pedaço.

---

## 2) Android (Kotlin) — captura e envio por WebSocket

```markdown
// build.gradle: implementation("org.java-websocket:Java-WebSocket:1.5.4")
val url = "wss://SEU_BACKEND/realtime"
val ws = object : WebSocketClient(URI(url)) {
    override fun onOpen(handshakedata: ServerHandshake?) {
        val cfg = """{"type":"config","lang_in":"zh","lang_out":"pt","partials":true}"""
        send(cfg)
        startRecordingAndStream()
    }
    override fun onMessage(message: String?) {
        // legendas
        // atualizar UI com JSONObject(message)["text"]
    }
    override fun onMessage(bytes: ByteBuffer?) {
        // áudio TTS: tocar com AudioTrack (STREAM_MUSIC, 16k/24k conforme codec)
    }
}
ws.connect()

fun startRecordingAndStream() {
    val sr = 16000
    val minBuf = AudioRecord.getMinBufferSize(sr, AudioFormat.CHANNEL_IN_MONO, AudioFormat.ENCODING_PCM_16BIT)
    val recorder = AudioRecord(MediaRecorder.AudioSource.MIC, sr, AudioFormat.CHANNEL_IN_MONO, AudioFormat.ENCODING_PCM_16BIT, minBuf)
    recorder.startRecording()
    thread(start=true) {
        val buf = ByteArray(640) // ~20ms @16k 16bit mono
        while(true){
            val n = recorder.read(buf, 0, buf.size)
            if (n > 0 && ws.isOpen) ws.send(ByteBuffer.wrap(buf, 0, n))
        }
    }
}
```

> Em produção, use **WebRTC SDK** (veRTC) para captura, AEC/NS embutidos e envio de trilhas; o WebSocket acima é o “modo simples” direto-no-fio.

---

## 3) n8n — orquestração e “cola” (glossário, logs, webhooks, WhatsApp)

**Fluxo “LL-ORCH-REALTIME” (esqueleto):**

1. **Webhook** (POST `/glossary`): recebe termos do cliente ⇒ grava em **Supabase**.
2. **Cron** (cada minuto): puxa termos ativos por sala (Supabase → `SELECT * FROM glossary WHERE room_id=?`).
3. **Function**: normaliza para formato `{ source:'zh', target:'pt', pairs:[['科大讯飞','iFlytek'], ...] }`.
4. **HTTP Request**: envia glossário para o **Node backend** (`/rooms/:id/glossary`).
5. **Webhook** (POST `/meeting-log`): backend envia blocos (ASR/MT/latência) ⇒ **Insert** em Supabase (tabela `realtime_logs`).
6. **If** (canal WhatsApp configurado?):
	- **Function**: compõe resumo parcial (a cada 2–5 min).
		- **HTTP Request** (Evolution API): envia **mensagem de texto** com os highlights.
		- **(Opcional)** **HTTP Request** (Kokoro TTS): gera áudio e envia **áudio** pelo Evolution.

**Tabelas Supabase (DDL básico):**

```markdown
create table glossary (
  id uuid primary key default gen_random_uuid(),
  room_id text not null,
  source_lang text not null,
  target_lang text not null,
  term_source text not null,
  term_target text not null,
  weight numeric default 1,
  created_at timestamptz default now()
);

create table realtime_logs (
  id bigint generated always as identity primary key,
  room_id text,
  lang_in text, lang_out text,
  asr_partial text, mt_partial text,
  latency_ms int,
  stability text, -- partial|final
  created_at timestamptz default now()
);
```

---

## 4) Flowise — “Consciência” plugável

- **Papel**: ajustar estilo de tradução, formalidade, e decidir **quando** ligar “voz clonada” (consentimento), além de gerar **resumos** / **atas** pós-reunião.
- **Ferramenta**: crie um **Tool** HTTP no Flowise que recebe `transcripts[]` e retorna:
	- *Resumo estruturado* (bullets + decisões + tarefas).
		- *Dicionário* detectado automaticamente (novos termos → volta para n8n gravar).
- **Prompt-base sugerido (trecho)**:
	```markdown
	Você é o controlador de estilo do LiveLingo. Parâmetros:
	- formalidade: neutro
	- pontuação: frases curtas
	- números próprios: não traduzir nomes de marca
	- glossário: aplicar sempre; se não encontrado, sugerir candidato em "glossary_suggestion"
	Output JSON:
	{ "subtitle_style": "...", "minutes": {...}, "glossary_suggestion":[...] }
	```

---

## 5) OBS/Live (YouTube, Douyin/TikTok, Instagram Live)

- **Fonte de legenda**: crie endpoint `/overlay?room_id=...` no **Node backend** que emite **Server-Sent Events (SSE)** com o último `subtitle`. Página HTML simples com `EventSource` + `<div>` full-width, fundo semi-transparente.
- **Preset**:
	- Cena 1: vídeo da câmera.
		- Texto: browser source apontando para `/overlay?...`.
		- Cena 2 (backup): “dual-sub” (origem / traduzido) com duas áreas configuráveis.
- **Latência**: usar “Low-Latency” RTMP, desativar filtros pesados; chunk pequeno no ASR.

---

## 6) Glossário — injeção e UI

- **Modelo**: `[{src:"科大讯飞", tgt:"iFlytek", weight: 2}, ...]`
- **Aplicação**:
	- No **ASR** (hotword boosting): enviar lista para o engine (quando suportado).
		- No **MT**: *pre-replace* (regex seguro) e/ou dicionário do provedor.
- **UI**: painel simples (React/Tailwind) por sala com:
	- Input “src” / “tgt”, idioma, *weight*.
		- Live preview de como a legenda sai.
		- Botão “Aplicar em tempo real” (POST n8n webhook).

---

## 7) Integração WhatsApp (Evolution API)

**Enviar legenda “viva”** para um contato/grupo:

```markdown
curl -X POST https://EVOLUTION_HOST/message/text \
  -H "Authorization: Bearer $EVOLUTION_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "number": "55XXXXXXXXXXX",
    "text": "*LiveLingo* (ZH→PT)\nAgora: '$(printf %q "texto atual")'"
  }'
```

**Enviar áudio TTS (arquivo mp3/ogg gerado):**

```markdown
curl -X POST https://EVOLUTION_HOST/message/audio \
  -H "Authorization: Bearer $EVOLUTION_KEY" \
  -F "number=55XXXXXXXXXXX" \
  -F "audio=@/path/tts-chunk-001.mp3"
```

> Para “ouvir a tradução” no WhatsApp enquanto a call rola em outra plataforma, dispare **clips curtos** (5–8 s).

---

## 8) Self-host (opcional/avançado)

**Docker Compose rascunho (FunASR + NMT + TTS):**

```markdown
version: "3.8"
services:
  funasr:
    image: funasr/runtime:latest
    ports: ["9000:9000"]   # WS/HTTP streaming
    environment:
      - MODEL=paraformer-online
  nmt:
    image: ghcr.io/seuorg/nmt-server:latest
    ports: ["9100:9100"]
  tts:
    image: ghcr.io/seuorg/tts-stream:latest
    ports: ["9200:9200"]
  gateway:
    build: ./gateway   # teu Node server (server.js)
    environment:
      - ASR_WS_URL=ws://funasr:9000/ws
      - MT_URL=http://nmt:9100/translate
      - TTS_WS_URL=ws://tts:9200/stream
    ports: ["8080:8080"]
```

> **Caminho de evolução**: começa com provedores (Volc/Baidu); quando o custo por minuto subir, migra ASR/TTS para o cluster e mantém só MT externo se for melhor.

---

## 9) Segurança & Compliance (UX honesta, sem drama)

- **Rotulagem**: quando usar **voz clonada** (voz do falante no idioma alvo), tocar *earcon* curtíssimo (50–100 ms) no início e exibir “AI Voice” no UI.
- **Consentimento**: “Ativar voz clonada?” **off por padrão**; salvar consent logs (Supabase `consents`).
- **Privacidade**: endpoint `/redact` em n8n que apaga metadados sensíveis da ata antes do envio.

---

## 10) Testes de qualidade (rápido e objetivo)

- **Métricas**: `first_token_ms`, `WER parcial`, `BLEU/COMET` em amostras, `MOS` subjetivo TTS.
- **Procedimento**:
	1. 10 frases curtas e 10 longas CH↔PT.
		2. Medir latência **captura→legenda** e **captura→áudio TTS**.
		3. Testar **overlap** (interrupções) e *barge-in* (corta TTS ao detectar voz local).

---

## 11) Roteiro de deploy (passo-a-passo)

1. **Provisionar**: VPS/VM com Node 20+, Docker, domínio `livelingo.seudominio`.
2. **Subir gateway**: `server.js` + **Nginx** com `wss` em `/realtime`.
3. **Configurar provedores** (Sabor A): chaves **ASR**, **TTS**, **MT** em variáveis de ambiente.
4. **n8n**: importar fluxo `LL-ORCH-REALTIME` (webhooks, cron, Supabase, Evolution).
5. **Supabase**: criar tabelas (`glossary`, `realtime_logs`, `consents`).
6. **Flowise**: criar Tool HTTP e *chain* “Minutes + Glossary Suggestion”.
7. **Front**: página web “/room/:id” com UI de legenda e botões “Join”, “Voz clonada (beta)”.
8. **OBS preset**: cena com **Browser Source** apontando para `/overlay?room_id=:id`.
9. **Android demo**: app lightweight com botão “Join room” (WebSocket) e “Enviar para WhatsApp” (Evolution).
10. **Teste fechado**: 3 sessões de 15 min ZH↔PT, com e sem glossário; latência alvo: **<800 ms** legenda percebida, **<1200 ms** áudio TTS.

---

## 12) Checklists de produção

**Env vars (gateway)**

```markdown
ASR_WS_URL=
ASR_KEY=
TTS_WS_URL=
TTS_KEY=
MT_URL=
MT_KEY=
SUPABASE_URL=
SUPABASE_KEY=
EVOLUTION_URL=
EVOLUTION_KEY=
FLOWISE_TOOL_URL=
FLOWISE_KEY=
```

**Portas (padrão)**

- `443` (Nginx TLS), `8080` (gateway WS/HTTP), `8000–9200` (serviços internos conforme stack).

**Observabilidade**

- Logs por sala (`realtime_logs`).
- Painel Grafana simple (latência, tokens, custo por minuto).
- Alarmes (n8n + Telegram/WhatsApp) se `first_token_ms > 1500` por > 30 s.

---

### Próximo passo

Se quiser, já te entrego:

- um **repositório** (gateway Node + front Web + overlay + docker compose self-host),
- o **fluxo n8n** `.json` (LL-ORCH-REALTIME),
- e um **preset OBS** `.json` com duas cenas (single-sub e dual-sub).

Também posso adaptar a ponte para **WhatsApp call-in** (quando a reunião for “só WhatsApp”), mandando **legenda por texto** e **respostas TTS curtas** como áudio na conversa — útil para triagem e suporte multilíngue.