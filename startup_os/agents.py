import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_agent(prompt: str, idea: str) -> str:
    full_prompt = f"{prompt}\n\nStartup Idea: {idea}"
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.7,
        max_tokens=1500,
    )
    return response.choices[0].message.content

def analyze_startup(idea: str) -> dict:

    print("🔍 Market Researcher analyzing...")
    market = run_agent(
        """You are an expert market research analyst.
        Analyze this startup idea and provide:
        - Total Addressable Market (TAM) size and growth rate
        - Top 3 competitors and their weaknesses
        - Target customer segments
        - Key market trends supporting this idea
        - Top 3 market risks
        Be specific with numbers. Use clear headers.""",
        idea
    )

    print("💼 Business Model Analyst analyzing...")
    business = run_agent(
        """You are an expert business model strategist.
        Analyze this startup idea and design:
        - Revenue streams with specific pricing
        - Customer acquisition strategy
        - Key partnerships needed
        - Cost structure breakdown
        - Path to profitability timeline
        Be specific and realistic. Use clear headers.""",
        idea
    )

    print("🎤 Pitch Writer analyzing...")
    pitch = run_agent(
        """You are an expert startup pitch writer who has helped raise $500M+.
        Write an investor pitch covering:
        - A powerful one-liner
        - The problem being solved
        - The solution
        - Why now (market timing)
        - Key traction points
        - The funding ask and why
        Make it compelling. Use clear headers.""",
        idea
    )

    print("💰 Financial Modeler analyzing...")
    financial = run_agent(
        """You are a startup CFO and financial modeling expert.
        Produce a financial overview:
        - Year 1, 2, 3 revenue projections
        - Key assumptions
        - Burn rate estimate
        - Break-even point
        - Funding requirements (Pre-seed, Seed, Series A)
        - Key metrics: CAC, LTV, Gross Margin
        Use realistic numbers. Use clear headers.""",
        idea
    )

    print("⚖️ Legal Risk Scanner analyzing...")
    legal = run_agent(
        """You are a startup lawyer and risk expert.
        Identify for this startup:
        - Top 3 legal risks and how to mitigate them
        - Required licenses or permits
        - IP strategy
        - Data privacy considerations
        - Recommended business structure
        - Regulatory hurdles
        Be practical. Use clear headers.""",
        idea
    )

    print("🧠 Director synthesizing everything...")
    synthesis_prompt = f"""You are a world-class startup advisor and VC.
    You have received analysis from 5 specialist agents on this startup idea:
    "{idea}"
    
    Here are their reports:
    
    === MARKET RESEARCH ===
    {market}
    
    === BUSINESS MODEL ===
    {business}
    
    === INVESTOR PITCH ===
    {pitch}
    
    === FINANCIAL PROJECTIONS ===
    {financial}
    
    === LEGAL & RISK ===
    {legal}
    
    Now synthesize everything into one cohesive investor-ready startup package with these sections:
    1. EXECUTIVE SUMMARY
    2. MARKET OPPORTUNITY
    3. BUSINESS MODEL
    4. FINANCIAL PROJECTIONS
    5. LEGAL & RISK OVERVIEW
    6. INVESTOR PITCH
    7. OVERALL VERDICT & SCORE (out of 10)
    
    Make it exceptional and compelling."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": synthesis_prompt}
        ],
        temperature=0.7,
        max_tokens=3000,
    )

    return {
        "market_research": market,
        "business_model": business,
        "pitch": pitch,
        "financial": financial,
        "legal": legal,
        "final_synthesis": response.choices[0].message.content
    }