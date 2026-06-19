import streamlit as st
import json
from audit_logic import analyze_password
from ai_governance_logic import analyze_ai_system

st.set_page_config(page_title="VANYCS Compliance Auditor", page_icon="🛡️", layout="centered")

st.title("🛡️ VANYCS Compliance Auditor")
st.write(
    "A dual-mode compliance auditing tool: validate passwords against "
    "internal policy, or evaluate an AI system/use case against the "
    "NIST AI RMF, EU AI Act, and ISO/IEC 42001."
)

mode = st.radio(
    "Select audit mode",
    ["Password Policy Audit", "AI Governance Audit"],
    horizontal=True,
)

st.divider()

if mode == "Password Policy Audit":
    st.subheader("Password Policy Audit")
    st.write("Enter a password below to audit it against the VANYCS access control policy.")

    with st.expander("View policy requirements"):
        st.markdown(
            """
            - **Minimum length:** 14 characters
            - **Character composition:** must include at least 3 of the following 4 categories — uppercase, lowercase, numbers, special characters
            - **Prohibited content:** cannot contain your username/name, corporate terms (e.g. "VNYCS"), sequential strings (e.g. "123456", "abcdef"), or common dictionary/breached passwords
            - **No reuse** of the last 5 passwords
            """
        )

    password = st.text_input("Enter password", type="password")
    if st.button("Run Audit", key="password_audit"):
        if password:
            with open("policy.txt", "r") as f:
                policy = f.read()

            with st.spinner("Auditing..."):
                result = analyze_password(password, policy)
                data = json.loads(result)

            if data["compliant"]:
                st.success("✅ Password is compliant!")
            else:
                st.error("❌ Password failed compliance.")

            st.write("### Audit Details")
            st.json(data)
        else:
            st.warning("Please enter a password first.")

else:
    st.subheader("AI Governance Audit")
    st.write(
        "Describe an AI system or use case to evaluate it against the "
        "NIST AI Risk Management Framework, EU AI Act risk tiers, and "
        "ISO/IEC 42001 AI management system controls."
    )

    with st.expander("What makes a good description"):
        st.markdown(
            """
            For the most accurate audit, include:
            - **What the system does** (e.g. answers billing questions, screens resumes)
            - **What data it accesses** (e.g. account balances, PII, health records)
            - **Who reviews its outputs** before they reach a person or decision (if anyone)
            - **How broadly it's deployed** (e.g. internal pilot, company-wide, customer-facing)
            """
        )

    example = (
        "A customer service chatbot that uses an LLM to answer billing "
        "questions and can access account balance and payment history. "
        "It is deployed company-wide with no human review of responses "
        "before they reach the customer."
    )

    system_description = st.text_area(
        "Describe the AI system or use case",
        placeholder=example,
        height=140,
    )

    if st.button("Run Governance Audit", key="ai_audit"):
        if system_description:
            with st.spinner("Auditing against NIST AI RMF, EU AI Act, and ISO 42001..."):
                result = analyze_ai_system(system_description)
                data = json.loads(result)

            st.write("### System Summary")
            st.write(data["system_summary"])

            risk = data["overall_risk_score"]
            if risk <= 3:
                st.success(f"Overall Risk Score: {risk}/10 (Low)")
            elif risk <= 6:
                st.warning(f"Overall Risk Score: {risk}/10 (Moderate)")
            else:
                st.error(f"Overall Risk Score: {risk}/10 (High)")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.write("**NIST AI RMF**")
                st.json(data["nist_ai_rmf"])

            with col2:
                st.write("**EU AI Act**")
                st.json(data["eu_ai_act"])

            with col3:
                st.write("**ISO/IEC 42001**")
                st.json(data["iso_42001"])

            st.write("### Remediation Priorities")
            for item in data["remediation_priorities"]:
                st.write(f"- {item}")
        else:
            st.warning("Please describe an AI system or use case first.")
