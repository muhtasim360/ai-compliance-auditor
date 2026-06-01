# AI-Powered Password Compliance Auditor (VANYCS Simulation)

## Executive Summary
This project automates the auditing of password policies against unstructured corporate documents. It bridges the gap between static policy and dynamic risk assessment using a hybrid Python/Gemini API architecture, designed to simulate compliance workflows for the fictional **Virginia-New York Consulting Service (VANYCS)**.

## Architectural Highlights
* **Modular Design:** The project separates business logic (`tracker.py`) from infrastructure/AI logic (`audit_logic.py`), ensuring scalability and ease of maintenance.
* **Cost-Optimized Latency:** Utilizes local Python logic for baseline character checks to minimize unnecessary API calls, reserving the Gemini API for complex semantic analysis.
* **Auditability & Explainability:** The system generates structured JSON audit logs, ensuring every compliance decision includes a remediation rationale for the end-user—a critical requirement for enterprise audit trails.

## Key Risk Mitigation
* **Secret Management:** Sensitive credentials are managed via environment variables (`.env`) and explicitly excluded from version control.
* **Resilience:** Built with structured system prompts to minimize model manipulation and potential prompt injection.

## Usage
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install google-genai python-dotenv
