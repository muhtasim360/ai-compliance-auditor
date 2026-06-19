import os
import streamlit as st
from groq import Groq


def analyze_password(password, policy):
    api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
    client = Groq(api_key=api_key)

    system_prompt = """
    You are an expert Cyber Risk Auditor. Evaluate the provided password
    against the company policy. Respond ONLY in valid JSON, with no markdown
    formatting or code fences.
    Format: {"compliant": bool, "violations": list, "risk_score": int, "remediation": str}
    """
    prompt = f"Policy:\n{policy}\n\nPassword to audit:\n{password}"

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=0.1,
        response_format={"type": "json_object"},
    )
    return response.choices[0].message.content
