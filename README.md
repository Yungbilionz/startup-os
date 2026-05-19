# 🚀 StartupOS — AI Co-Founder Swarm

> Built for the Swarms Hackathon · Powered by [Swarms Framework](https://github.com/kyegomez/swarms)

![StartupOS](https://img.shields.io/badge/StartupOS-AI%20Co--Founder%20Swarm-dc2626?style=for-the-badge&logo=rocket)
![Swarms](https://img.shields.io/badge/Powered%20By-Swarms-black?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)

---

## 🧠 What is StartupOS?

**StartupOS** is an AI-powered co-founder swarm that takes any startup idea and autonomously produces a complete investor-ready business package in under 90 seconds.

Instead of one AI doing everything, StartupOS deploys **5 specialized agents working concurrently**, each an expert in their domain — then a **Director Agent** synthesizes everything into one cohesive package scored out of 10.

---

## 🤖 The Agent Swarm

| Agent | Role | Output |
|-------|------|--------|
| 🔍 Market Researcher | Analyzes market size, competitors, trends | TAM, competitor weaknesses, market risks |
| 💼 Business Analyst | Designs revenue model and go-to-market | Pricing, CAC, partnerships, profitability |
| 🎤 Pitch Writer | Crafts compelling investor narrative | One-liner, problem, solution, funding ask |
| 💰 Financial Modeler | Projects financials and funding needs | 3-year projections, burn rate, LTV, CAC |
| ⚖️ Legal Scanner | Identifies risks and compliance needs | Legal risks, licenses, IP strategy |
| 🧠 Director Agent | Synthesizes all outputs into final package | Complete investor deck + score out of 10 |

---

## 🛠️ Tech Stack

- **Framework**: Swarms — Multi-agent orchestration
- **LLM**: Groq LLaMA 3.3 70B — Fast, free inference
- **Backend**: Python + Flask REST API
- **Frontend**: Vanilla HTML/CSS/JS — Sleek dark dashboard
- **Pattern**: MixtureOfAgents — Concurrent agents + aggregator director

---

## 🚀 Quick Start

1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/startup-os.git
cd startup-os
```

2. Install dependencies
```bash
pip install swarms flask flask-cors groq python-dotenv
```

3. Add your API keys to a `.env` file