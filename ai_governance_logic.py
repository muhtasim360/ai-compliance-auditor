import os
import streamlit as st
from google import genai
from google.genai import types


GOVERNANCE_SYSTEM_PROMPT = """
You are an expert AI Governance and Regulatory Compliance Auditor.

You will be given a description of an AI system or AI use case. Evaluate it
against three frameworks:

1. NIST AI Risk Management Framework (AI RMF) — assess across the four core
   functions: Govern, Map, Measure, Manage.
2. EU AI Act — classify the system's likely risk tier (Unacceptable, High,
   Limited, Minimal) and note which obligations would apply at that tier.
3. ISO/IEC 42001 — assess against AI management system expectations
   (policy, roles/accountability, risk assessment, monitoring, continual
   improvement).

Respond ONLY in valid JSON using this exact structure:
{
  "system_summary": str,
  "nist_ai_rmf": {
    "govern": str,
    "map": str,
    "measure": str,
    "manage": str
  },
  "eu_ai_act": {
    "risk_tier": str,
    "rationale": str,
    "key_obligations": list
  },
  "iso_42001": {
    "alignment_summary": str,
    "gaps": list
  },
  "overall_risk_score": int,
  "remediation_priorities": list
}

overall_risk_score is an integer from 1 (low risk) to 10 (high risk).
Be specific and reference the actual content of the system description —
do not give generic boilerplate answers.
"""


def analyze_ai_system(system_description: str) -> str:
    """
    Audits a free-text description of an AI system or use case against
    NIST AI RMF, EU AI Act risk tiers, and ISO/IEC 42001 AI management
    system controls. Returns a structured JSON string.
    """
    api_key = st.secrets.get("GEMINI_API_KEY") or os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    prompt = f"AI system / use case description:\n{system_description}"

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=GOVERNANCE_SYSTEM_PROMPT,
            response_mime_type="application/json",
            temperature=0.1,
        ),
    )
    return response.text
