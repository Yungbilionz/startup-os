# 🚀 StartupOS — AI Co-Founder Swarm

> **5 AI agents. 1 startup idea. A complete investor package in 90 seconds.**

![StartupOS](https://img.shields.io/badge/StartupOS-AI%20Co--Founder%20Swarm-dc2626?style=for-the-badge&logo=rocket)
![Swarms](https://img.shields.io/badge/Powered%20By-Swarms-black?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Groq](https://img.shields.io/badge/LLM-Groq%20LLaMA%203.3-orange?style=for-the-badge)
![Flask](https://img.shields.io/badge/Backend-Flask-lightgrey?style=for-the-badge&logo=flask)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 💥 The Problem

Every year, **600,000+ startups launch in Africa alone** — and most fail.

Not because the ideas are bad. But because founders lack access to:
- Expert market research
- Solid financial modeling
- Investor-ready pitch writing
- Legal risk assessment
- A coherent business strategy

Hiring experts for all of this costs **$10,000–$50,000** and takes **weeks**.

**StartupOS does it in 90 seconds. For free.**

---

## 🧠 What is StartupOS?

**StartupOS** is an AI co-founder swarm built on the **Swarms Framework**. It deploys 5 specialized AI agents concurrently — each a domain expert — then a Director Agent synthesizes their outputs into one cohesive, investor-ready startup package complete with a score out of 10.

No single AI. No generic output. A **true multi-agent swarm** working in parallel.

---

## 🤖 The Agent Swarm

| Agent | Expertise | Delivers |
|-------|-----------|---------|
| 🔍 **Market Researcher** | Market sizing, competitive analysis | TAM, competitor weaknesses, trends, risks |
| 💼 **Business Analyst** | Revenue models, go-to-market strategy | Pricing, CAC, partnerships, profitability path |
| 🎤 **Pitch Writer** | Investor storytelling, fundraising | One-liner, problem, solution, funding ask |
| 💰 **Financial Modeler** | Startup finance, projections | 3-year revenue, burn rate, LTV, CAC, margins |
| ⚖️ **Legal Scanner** | Startup law, risk management | Legal risks, licenses, IP strategy, compliance |
| 🧠 **Director Agent** | Synthesis, venture capital perspective | Complete investor package + score out of 10 |

---

## ⚡ Why Swarms?

StartupOS is built specifically to showcase the power of the **Swarms Framework**:

- **MixtureOfAgents Pattern** — 5 specialist agents run concurrently, maximizing speed and depth
- **Aggregator Agent** — A Director Agent synthesizes all 5 outputs into one cohesive package
- **Agent Specialization** — Each agent has a deeply crafted system prompt making it a genuine domain expert
- **Scalability** — The swarm can be extended with more agents without changing the core architecture
- **Production Ready** — Wrapped in a Flask REST API with a full frontend dashboard

> This is not a demo. This is Swarms in production.

---

## 🏗️ Detailed Workflow

Here is exactly what happens from the moment you submit a startup idea:

Step 1 — User submits idea via the web dashboard

↓

Step 2 — Flask API receives the POST /analyze request

↓

Step 3 — 5 agents are initialized with specialized system prompts

↓

Step 4 — All 5 agents run concurrently (parallel execution)

┌──────────────────────────────────────────────┐

│  🔍 Market Researcher   → market analysis    │

│  💼 Business Analyst    → business model     │

│  🎤 Pitch Writer        → investor pitch     │

│  💰 Financial Modeler   → financial plan     │

│  ⚖️ Legal Scanner       → risk assessment    │

└──────────────────────────────────────────────┘

↓

Step 5 — All 5 outputs passed to the Director Agent

↓

Step 6 — Director Agent synthesizes everything into
one investor-ready package with score/10

↓

Step 7 — Results returned to frontend dashboard

↓

Step 8 — User sees full analysis in beautiful UI
with each agent's report + final synthesis

**Total time: 60–90 seconds**

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Multi-Agent Framework | [Swarms](https://github.com/kyegomez/swarms) | Agent orchestration |
| LLM Provider | Groq — LLaMA 3.3 70B | Fast free inference |
| Backend | Python + Flask | REST API server |
| Frontend | HTML + CSS + JavaScript | Web dashboard |
| Agent Pattern | MixtureOfAgents | Concurrent execution |
| Environment | python-dotenv | Secure key management |

---

## 📋 Prerequisites

Before running StartupOS, make sure you have:

- Python 3.10 or higher installed
- A free **Groq API key** — get one at [console.groq.com](https://console.groq.com)
- A free **Swarms API key** — get one at [swarms.world/platform/api-keys](https://swarms.world/platform/api-keys)
- Git installed on your machine

---

## 🔑 API Keys Setup

StartupOS requires 2 API keys. Both are completely free.

### 1. Groq API Key (powers the AI agents)
1. Go to [https://console.groq.com](https://console.groq.com)
2. Sign up for a free account
3. Click **"API Keys"** in the left sidebar
4. Click **"Create API Key"**
5. Copy and save the key

### 2. Swarms API Key (connects to Swarms ecosystem)
1. Go to [https://swarms.world/platform/api-keys](https://swarms.world/platform/api-keys)
2. Sign up for a free account
3. Click **"Create API Key"**
4. Copy and save the key

### 3. Create your .env file
In the `startup_os` folder, create a file called `.env` and add:

GROQ_API_KEY=your_groq_api_key_here

SWARMS_API_KEY=your_swarms_api_key_here

> ⚠️ Never commit your `.env` file to GitHub. It is already in `.gitignore` for your protection.

---

## 🚀 Quick Start

**1. Clone the repo**
```bash
git clone https://github.com/Yungbilionz/startup-os.git
cd startup-os
```

**2. Install all dependencies**
```bash
pip install swarms flask flask-cors groq python-dotenv google-genai
```

**3. Set up your API keys**
```bash
cd startup_os
# Create .env file and add your keys as shown above
```

**4. Run the backend server**
```bash
python main.py
```

**5. Open the app in your browser**

http://localhost:5000

**6. Enter any startup idea and click Analyze!**

---

## 📁 Project Structure

startup-os/
├── startup_os/

│   ├── main.py              # Flask API server + all routes

│   ├── agents.py            # All 6 swarm agent definitions

│   ├── templates/

│   │   └── index.html       # Full frontend dashboard

│   ├── requirements.txt     # Python dependencies

│   └── .env                 # Your API keys (never committed)

├── .gitignore               # Protects sensitive files

├── requirements.txt         # Project dependencies

└── README.md                # project info

---

## 🔌 API Reference

StartupOS exposes a simple REST API:

### POST /analyze
Analyzes a startup idea using the full agent swarm.

**Request:**
```json
{
  "idea": "Your startup idea description here"
}
```

**Response:**
```json
{
  "success": true,
  "idea": "Your startup idea",
  "analysis": {
    "market_research": "Full market analysis...",
    "business_model": "Complete business model...",
    "pitch": "Investor pitch content...",
    "financial": "Financial projections...",
    "legal": "Legal risk assessment...",
    "final_synthesis": "Complete investor package + score/10"
  }
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Error description"
}
```

---

## 🎯 Example Output

**Input:**
> *"An app that connects African farmers directly to city buyers, cutting out middlemen and increasing farmer profits by 40%"*

**Output in 90 seconds:**
- 📊 **Market**: $56B TAM, 5% annual growth, top 3 competitors analyzed
- 💼 **Business Model**: 5% transaction fee, premium tier at $10/month
- 🎤 **Pitch**: Seeking $2M Series A with compelling narrative
- 💰 **Financials**: Year 3 revenue $5M, break-even at 12-18 months
- ⚖️ **Legal**: 3 key risks identified with full mitigation strategies
- ⭐ **Overall Score: 8.5/10**

---

## 🧪 Testing

To test the API directly without the frontend, run:

```bash
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"idea": "A subscription box service delivering African artisan products to diaspora communities worldwide"}'
```

---

## 🌍 Impact

StartupOS is built for the **next billion founders** — entrepreneurs in emerging markets who have world-changing ideas but no access to $500/hour consultants, VCs, or startup advisors.

With StartupOS, any founder anywhere can get a complete market analysis, solid business model, investor-ready pitch, financial projections, and legal risk assessment — all in 90 seconds, all for free.

---

## 🔮 Future Roadmap

- [ ] Add PDF export of full investor package
- [ ] Swarms Marketplace integration to publish agents publicly
- [ ] Add competitor deep-dive agent
- [ ] Add SEO and growth hacking agent
- [ ] Multi-language support for African languages
- [ ] Email delivery of analysis report

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open issues for bugs or feature requests
- Submit pull requests
- Share feedback on the Swarms Discord

---

## 🏆 Hackathon Submission

**Swarms Hackathon 2026**

Built by: [@Yungbilionz](https://github.com/Yungbilionz)

Framework: [@swarms_corp](https://x.com/swarms_corp) — [github.com/kyegomez/swarms](https://github.com/kyegomez/swarms)

Key Swarms features demonstrated:
- `MixtureOfAgents` — concurrent multi-agent execution
- `Agent` — specialized domain expert agents with custom system prompts
- Aggregator pattern — director agent synthesis
- Production deployment — real REST API + web frontend

---

## 📄 License

MIT — free to use, modify, and distribute.

---

<p align="center">
  Built with ❤️ using <a href="https://github.com/kyegomez/swarms">Swarms Framework</a> ·
  <a href="https://x.com/swarms_corp">@swarms_corp</a> ·
  <a href="https://swarms.world">swarms.world</a>
</p>
