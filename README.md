# VANYCS Compliance Auditor

## Executive Summary
A dual-mode AI-powered compliance auditing tool built with Python and the
Gemini API, simulating compliance workflows for the fictional Virginia-New
York Consulting Service (VANYCS):

1. **Password Policy Audit** — validates a password against a corporate
   access control policy (length, character composition, prohibited
   content, reuse rules).
2. **AI Governance Audit** — evaluates a free-text description of an AI
   system or use case against three major AI governance frameworks:
   - **NIST AI Risk Management Framework** (Govern / Map / Measure / Manage)
   - **EU AI Act** (risk-tier classification and applicable obligations)
   - **ISO/IEC 42001** (AI management system alignment and gaps)

Both modes return structured, explainable output rather than a pass/fail
black box — every result includes a rationale and remediation guidance,
which mirrors how compliance findings are documented in practice.

## Architectural Highlights
- **Modular design**: business logic (`dashboard.py`) is separated from
  AI/infrastructure logic (`audit_logic.py`, `ai_governance_logic.py`),
  keeping the system easy to extend with additional audit types.
- **Cost-optimized**: the password mode uses local Python-side context
  (the policy file) and reserves the Gemini API for the semantic
  judgment calls that actually require it.
- **Auditability & explainability**: both modes generate structured JSON
  output with remediation rationale, reflecting enterprise audit trail
  requirements.

## Key Risk Mitigation
- **Secret management**: credentials are read from environment variables /
  Streamlit secrets and excluded from version control.
- **Prompt resilience**: structured system prompts constrain model output
  to a fixed JSON schema to reduce manipulation risk.

## Usage
1. Clone the repository.
2. Install dependencies:
