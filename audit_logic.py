import os
from google import genai
from google.genai import types

def analyze_password(password, policy):

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

system_prompt = """
    You are an expert Cyber Risk Auditor. Evaluate the provided password
    against the company policy. Respond ONLY in valid JSON.
    Format: {"compliant": bool, "violations": list, "risk_score": int, "remediation": str}
    """

prompt = f"Policy:\n{policy}\n\nPassword to audit:\n{password}"

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
        response_mime_type="application/json",
        temperature=0.1
    ),
)
return response.txt
