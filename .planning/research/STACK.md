# Technology Stack: OpenClaw Go-To-Market Research

**Project:** Gonka Tokenomics v1.3 -- OpenClaw GTM Strategy
**Researched:** 2026-04-01
**Overall Confidence:** HIGH (OpenClaw ecosystem), MEDIUM (GTM tooling)

---

## Context: What This Stack Is For

v1.3 is a **research and strategy milestone**, not an engineering milestone. The "stack" here means: what tools, data sources, platforms, and technical knowledge are needed to research and write a go-to-market strategy for convincing OpenClaw developers and agents to use Gonka.ai as their inference provider.

This is NOT about building software. It is about understanding the OpenClaw ecosystem deeply enough to produce actionable GTM documents.

---

## 1. OpenClaw Technical Architecture (What We Need to Know)

### Overview

OpenClaw is the fastest-growing open-source project in GitHub history: 250K+ stars in ~4 months, 1,075 contributors, 124K LOC. It is a self-hosted AI agent gateway that bridges messaging apps (WhatsApp, Telegram, Discord, Slack, iMessage, etc.) to LLM inference providers. Users deploy a Gateway process on their machine that routes messages to AI agents backed by configurable model providers.

**Confidence:** HIGH -- verified across official docs, GitHub, and multiple sources.

### How Agents Select Inference Providers

This is the critical GTM question. OpenClaw uses a **declarative configuration model** in `~/.openclaw/openclaw.json`:

```json5
{
  models: {
    providers: {
      "gonka": {
        baseUrl: "https://api.gonka.ai/v1",
        apiKey: "${GONKA_API_KEY}",
        api: "openai-completions",
        models: [
          {
            id: "kimi-k2.5",
            name: "Kimi K2.5",
            contextWindow: 131072,
            maxTokens: 8192,
            cost: { input: 0.50, output: 1.50 }
          }
        ]
      }
    }
  },
  agents: {
    defaults: {
      models: {
        "gonka/kimi-k2.5": { alias: "k2.5" }
      }
    }
  }
}
```

**Provider selection is a TWO-STEP process:**

1. **Provider definition** -- `models.providers` block with `baseUrl`, `apiKey`, `api` type, and model list
2. **Model allowlisting** -- `agents.defaults.models` must include fully-qualified `provider/model` names

Missing either step causes silent failure. This is a known gotcha in the OpenClaw community.

**Key rotation and failover:**
- Keys checked in priority order: `OPENCLAW_LIVE_<PROVIDER>_KEY` > `<PROVIDER>_API_KEYS` > `<PROVIDER>_API_KEY` > `<PROVIDER>_API_KEY_*`
- Retry with next key ONLY on rate-limit responses (429, quota_exceeded)
- Non-rate-limit errors fail immediately (no fallback)

**API compatibility requirement:** OpenClaw requires either `openai-completions` or `anthropic-messages` API format. Gonka.ai already implements OpenAI-compatible `/v1/chat/completions` -- this is table stakes and already shipped in v1.2.

**Confidence:** HIGH -- verified against official docs at docs.openclaw.ai and GitHub source.

### Built-In vs Custom Providers

OpenClaw ships with ~20 built-in provider plugins:
- **API key providers:** OpenAI, Anthropic, Google Gemini, Mistral, OpenRouter, Together, Groq, Cerebras, NVIDIA, MiniMax, Moonshot, Kimi Coding, Qianfan
- **OAuth providers:** GitHub Copilot, OpenAI Codex, Google Vertex
- **Local/self-hosted:** Ollama, vLLM, SGLang

**Gonka is NOT a built-in provider.** This means every Gonka user must manually configure `openclaw.json`. This is both a GTM challenge (friction) and opportunity (becoming a built-in provider via PR to openclaw/openclaw would be a major win).

**Confidence:** HIGH -- verified from official model-providers documentation.

### Plugin Architecture

OpenClaw supports two extension types:
- **Plugins** -- TypeScript modules loaded at runtime via jiti. Can register providers, tools, hooks, channels, CLI commands, background services. Run in-process with Gateway (trusted code).
- **Skills** -- Markdown-based agent capability definitions (SKILL.md). 5,700+ skills in ClawHub marketplace. Skills are injected into system prompts based on context.

A **Gonka provider plugin** could be distributed via npm and installed by users, reducing configuration to `npm install openclaw-gonka-plugin` + API key. This is a high-value GTM engineering task.

**Confidence:** HIGH -- verified from OpenClaw plugin docs and DeepWiki analysis.

### vLLM Integration Details

OpenClaw has first-class vLLM support as a bundled provider. Critical gotchas for vLLM-backed providers:
- vLLM must be started with `--enable-auto-tool-choice` and `--tool-call-parser` flags for tool calling
- After config change, run `openclaw models scan` to populate tool capability metadata
- Without `toolUse: true` metadata, agents silently fail (stopReason: "stop" instead of tool invocation)

**Gonka.ai already runs vLLM** (shipped in v1.2). The GTM strategy must document that Gonka handles these vLLM gotchas server-side so OpenClaw users don't have to.

**Confidence:** HIGH -- verified from multiple sources including official docs and community tutorials.

---

## 2. Competitive Intelligence Sources

### Direct Competitors to Track

| Competitor | What to Track | Data Source | Update Frequency |
|------------|--------------|-------------|------------------|
| **OpenRouter** | Pricing, model catalog, 5.5% fee changes, free tier limits | openrouter.ai/pricing, openrouter.ai/models | Weekly |
| **OpenAI** | API pricing, rate limits, new model launches | platform.openai.com/docs | On announcement |
| **Anthropic** | Claude pricing, context window pricing, batch API | docs.anthropic.com/en/docs/pricing | On announcement |
| **Google** | Gemini API pricing, free tier generosity | ai.google.dev/pricing | On announcement |
| **Together AI** | Open-model pricing (Llama, Mixtral) | together.ai/pricing | Monthly |
| **Groq** | Speed-optimized inference pricing | groq.com/pricing | Monthly |
| **DeepSeek** | Ultra-low-cost pricing ($0.55/$2.19 per M tokens) | platform.deepseek.com | Monthly |

### Pricing Tracking Approach

Use a lightweight manual tracking spreadsheet (openpyxl, naturally) rather than paying $25K+/yr for Crayon/Klue. The competitive landscape moves fast enough that automated scraping becomes stale quickly anyway.

**Key metrics to track per competitor:**
- Input token price per 1M tokens
- Output token price per 1M tokens
- Context window sizes
- Rate limits (RPM, TPM)
- Free tier availability and limits
- Tool/function calling support
- Streaming support quality
- Uptime/reliability (community reports)

**Current benchmark pricing (April 2026):**

| Provider | Model | Input/1M | Output/1M | Context |
|----------|-------|----------|-----------|---------|
| OpenRouter (pass-through) | GPT-5.4 | $2.50 | $15.00 | 1M |
| OpenRouter | Gemini 3.1 Flash Lite | $0.25 | $1.50 | -- |
| OpenAI direct | GPT-4o | $5.00 | $15.00 | 128K |
| Anthropic direct | Claude Opus | $15.00 | $75.00 | 200K |
| DeepSeek | V3.2 | $0.55 | $2.19 | 128K |
| **Gonka target** | Kimi K2.5 | **TBD** | **TBD** | 131K |

Gonka's pricing advantage comes from decentralized compute (50-70% lower cost than centralized clouds per Gonka's own claims). The GTM research must validate this claim against actual provider pricing.

**Confidence:** MEDIUM -- pricing data from search results; exact numbers shift frequently.

---

## 3. OpenClaw Community Channels

### Where OpenClaw Developers Congregate

| Channel | Type | Reach | GTM Relevance |
|---------|------|-------|---------------|
| **GitHub openclaw/openclaw** | Code + Issues + Discussions | 250K+ stars, 9,574 open issues | HIGH -- PRs for built-in provider, issue engagement |
| **OpenClaw Discord** | Community chat | Thousands of active members | HIGH -- #help, #models, #users-helping-users channels |
| **GitHub openclaw/community** | Discord policies, community docs | -- | MEDIUM -- understand community norms |
| **X/Twitter** | Social | Viral lobster memes, organic growth | HIGH -- developer word-of-mouth |
| **Medium / dev.to** | Blog posts | Heavy tutorial ecosystem | HIGH -- publish integration guides |
| **Weibo / Zhihu** | Chinese community | Massive (lobster culture viral) | MEDIUM -- if targeting Chinese devs |
| **YouTube** | Video tutorials | Growing | MEDIUM -- demo videos |
| **ClawHub Skills Marketplace** | Skill registry | 5,700+ skills | HIGH -- publish Gonka skill |

### Community Engagement Strategy Sources

The OpenClaw community grew entirely organically -- no Product Hunt, no VC-funded growth team. Word of mouth + GitHub trending + social sharing. This means:
- **Authentic technical content wins** over marketing speak
- **Contributing upstream** (PRs, plugins, skills) earns credibility
- **Tutorial content** on dev.to/Medium gets discovered by new users

**Confidence:** HIGH -- verified from multiple sources.

---

## 4. Research & Analysis Tooling

### What v1.3 Needs to Produce GTM Research Documents

Since v1.3 is a research milestone (like v1.0), the primary output is **documents**, not code. The stack is:

| Tool | Purpose | Why |
|------|---------|-----|
| **Markdown** | Primary document format | All research files, strategy docs. Matches repo convention. |
| **openpyxl 3.1.5** | Competitive pricing comparison workbook | Reuse existing stack from v1.1. One workbook tracking competitor pricing over time. |
| **Python 3.10+** | Data processing if needed | Existing stack. May be needed for pricing analysis scripts. |

### No New Dependencies Needed

v1.3 does not require new libraries, frameworks, or tools. The research output is markdown documents and potentially one Excel workbook for competitive pricing tracking. Everything needed is already installed.

---

## 5. GTM Engineering Artifacts to Research (Not Build in v1.3)

The GTM research should identify and spec these engineering deliverables for a future milestone:

| Artifact | What It Is | OpenClaw Integration Point |
|----------|-----------|---------------------------|
| **Gonka provider plugin** | npm package (`openclaw-plugin-gonka`) | `models.providers` auto-configuration |
| **Gonka OpenClaw skill** | SKILL.md for ClawHub | System prompt injection for Gonka-aware agents |
| **One-line onboarding** | `openclaw onboard --auth-choice gonka` | CLI provider setup flow |
| **openclaw.json template** | Pre-configured JSON for copy-paste | Eliminates manual config errors |
| **Integration guide** | dev.to / Medium tutorial | Community discovery |
| **Quickstart repo** | GitHub template with working OpenClaw + Gonka setup | Reduces time-to-first-inference |

These are **not in scope for v1.3** but the GTM research must document what they are, why they matter, and prioritize them.

---

## 6. Key Technical Facts for GTM Positioning

### What Gonka.ai Already Has (v1.2 shipped)

| Capability | Status | OpenClaw Compatibility |
|------------|--------|----------------------|
| OpenAI-compatible `/v1/chat/completions` | Shipped | Direct compatibility |
| API key authentication | Shipped | Maps to `apiKey` in provider config |
| Rate limiting | Shipped | Handles OpenClaw's key rotation retry on 429 |
| Usage metering | Shipped | Foundation for per-token billing |
| Model routing / tiering | Shipped | Can serve cheap + strong models for OpenClaw's intent classification + planning steps |
| Session persistence | Shipped | Unique differentiator (no competitor offers this at provider level) |
| Memory API | Shipped | Unique differentiator for stateful agents |
| Webhooks | Shipped | Enables event-driven agent patterns |
| Tool calling (vLLM) | Shipped | Critical for OpenClaw agent tool execution |

### What Gonka.ai Does NOT Have Yet (gaps to address)

| Gap | Why It Matters for OpenClaw | Priority |
|-----|---------------------------|----------|
| **Not a built-in OpenClaw provider** | Users must manually configure JSON | CRITICAL |
| **No npm plugin package** | Cannot `npm install` to add Gonka | HIGH |
| **No ClawHub skill** | Agents don't know Gonka exists | HIGH |
| **No public pricing page** | Can't compare against OpenRouter | HIGH |
| **No uptime/status page** | Developers need reliability signals | MEDIUM |
| **TF-IDF search (not vector)** | Memory API less useful without good retrieval | MEDIUM |
| **In-memory sessions** | Production reliability concern | MEDIUM |
| **JSON key storage** | Security concern for enterprise | LOW (for early GTM) |

---

## Alternatives Considered

### Research Approach Alternatives

| Category | Recommended | Alternative | Why Not |
|----------|-------------|-------------|---------|
| Competitive tracking | Manual spreadsheet (openpyxl) | Crayon/Klue ($25K+/yr) | Overkill for 7 competitors; pricing changes are easy to track manually |
| Community research | Direct observation (GitHub, Discord, X) | Social listening tools (Brandwatch, etc.) | OpenClaw community is concentrated in few channels; tools add cost without value |
| Developer surveys | N/A for v1.3 | Typeform/SurveyMonkey | No community presence yet; survey without trust = low response rate |
| Pricing analysis | Excel workbook | SaaS pricing intelligence | Manual is sufficient at this scale |

### GTM Delivery Format Alternatives

| Category | Recommended | Alternative | Why Not |
|----------|-------------|-------------|---------|
| Strategy docs | Markdown in repo | Google Docs / Notion | Repo is the single source of truth; leadership can review via GitHub |
| Pricing comparison | openpyxl workbook | Google Sheets | Consistency with v1.1 tooling; portable .xlsx |
| Competitive matrix | Markdown tables | Spreadsheet | Simple enough for markdown; no formulas needed |

---

## OpenClaw Ecosystem Key Numbers

| Metric | Value | Source | Confidence |
|--------|-------|--------|------------|
| GitHub stars | 250K+ | GitHub, multiple sources | HIGH |
| Contributors | 1,075 | GitHub | HIGH |
| Lines of code | 124K | Community reports | MEDIUM |
| Skills in marketplace | 5,700+ | ClawHub, community reports | MEDIUM |
| Built-in providers | ~20 | Official docs | HIGH |
| Custom provider API formats | 2 (openai-completions, anthropic-messages) | Official docs | HIGH |
| Time since public launch | ~3 months (Jan 25, 2026) | Multiple sources | HIGH |
| GitHub forks | 48K+ | GitHub | HIGH |
| Messaging channels supported | 50+ | Official docs | HIGH |
| NemoClaw (Nvidia security addon) | Released Mar 16, 2026 | News reports | MEDIUM |

---

## Sources

### HIGH Confidence (Official Documentation)
- [OpenClaw Model Providers -- Official Docs](https://docs.openclaw.ai/concepts/model-providers)
- [OpenClaw Model Providers -- GitHub Source](https://github.com/openclaw/openclaw/blob/main/docs/concepts/model-providers.md)
- [OpenClaw Plugin System -- Official Docs](https://docs.openclaw.ai/tools/plugin)
- [OpenClaw GitHub Repository](https://github.com/openclaw/openclaw)
- [OpenClaw AGENTS.md](https://github.com/openclaw/openclaw/blob/main/AGENTS.md)
- [OpenClaw Community Repository](https://github.com/openclaw/community)
- [OpenRouter Pricing](https://openrouter.ai/pricing)
- [OpenRouter Models](https://openrouter.ai/models)

### MEDIUM Confidence (Verified with Multiple Sources)
- [OpenClaw 250K Stars Milestone -- OpenClaw Blog](https://openclaws.io/blog/openclaw-250k-stars-milestone)
- [Custom LLM Provider Setup Guide -- haimaker.ai](https://haimaker.ai/blog/integrating-custom-llm-providers-with-clawdbot/)
- [vLLM Self-Hosting with OpenClaw -- DeepWiki](https://deepwiki.com/gensecaihq/Wazuh-Openclaw-Autopilot/7.3-vllm-self-hosting)
- [OpenClaw vLLM Custom Endpoints -- Stanza](https://www.stanza.dev/courses/openclaw-production/local-models/openclaw-production-vllm-custom-endpoints)
- [OpenClaw Extensions Architecture -- DeepWiki](https://deepwiki.com/openclaw/openclaw/5-extensions)
- [Awesome OpenClaw Skills -- VoltAgent](https://github.com/VoltAgent/awesome-openclaw-skills)
- [OpenRouter Pricing Calculator -- CostGoat](https://costgoat.com/pricing/openrouter)
- [Gonka Network -- MEXC Analysis](https://www.mexc.com/news/734910)
- [Gonka Whitepaper](https://gonka.ai/whitepaper.pdf)
- [OpenClaw Architecture Guide -- Milvus Blog](https://milvus.io/blog/openclaw-formerly-clawdbot-moltbot-explained-a-complete-guide-to-the-autonomous-ai-agent.md)

### LOW Confidence (Single Source / Community)
- OpenClaw Discord server size and activity levels (inferred from docs, not directly measured)
- Gonka compute cost advantage of 50-70% (Gonka's own marketing claims, not independently verified)
- DeepSeek V3.2 achieving "~90% of GPT-5.4 performance" (community benchmark claims)
