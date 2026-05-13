### PLAN_V2.md
## Project Overview
**Title:** Prompt Injection Attacks and Defenses in LLM Applications (Version 2)
**Author:** Gunther Gerlach
**Date:** 4/27/2026

### Description
A security analysis of prompt injection vulnerabilities in structured LLM pipelines. This capstone project tests how malicious attacks within automated invoice processing can hijack simulated agentic functions (e.g., unauthorized wire transfers). It establishes a vulnerable baseline using the `gemini-3.1-flash-lite-preview` model and evaluates the efficacy of a multi-layered defense architecture. 


### Objectives
- Evaluate the vulnerability of the Gemini 3.1 model to targeted data manipulation and prompt injections within automated Accounts Payable constraints.
- Implement four distinct defense mechanisms (XML, Hierarchy, CaMel, CoT Monitoring) and combine them into a comprehensive, layered architecture.
- Quantify the efficacy of standalone defenses versus the layered defense to provide new insights into secure AI data engineering.
- Achieve the target enterprise viability threshold: Reducing the Attack Success Rate (ASR) to < 5% while strictly maintaining a False Positive Rate (FPR) of < 2%.

## Evaluation Metrics & Tests
- **Security Metrics:** The primary error metric is the Attack Success Rate (ASR), representing the percentage of malicious payloads that successfully bypassed the simulated three-way match. McNemar’s Test will be used to determine the statistical significance of the ASR reduction between the baseline and the defended models.
- **Operational Metrics:** To ensure the defenses are viable for enterprise use, the False Positive Rate (FPR)—the rate at which clean invoices are flagged—will be measured. Execution latency is recorded to quantify the computational "security tax" added by the defenses. The Wilcoxon Signed-Rank Test will assess the statistical significance of this added latency across the 300-invoice dataset.
- **Viability Analysis:** An F1-Score will be calculated to identify the optimal mathematical balance between maximizing security (precision) and maintaining enterprise throughput (minimizing false positives).

## Tasks
### Phase 1 - Gather Dataset, conduct research, and baseline pipeline construction.
- [x] Get invoice dataset from kaggle.https://www.kaggle.com/datasets/pradumn203/payment-date-prediction-for-invoices-dataset
- [x] Select a subset of 300 invoices and write a Python script to convert tabular rows into text-based "Invoice Documents" to simulate realistic LLM inputs.
- [x] Set up API connections for the `gemini-3.1-flash-lite-preview` model.

### Phase 2 - Create the base invoice model, prompt injections, and record initial metrics.
- [x] Build the baseline invoice extraction pipeline.
- [x] Create mock agentic tools and a Three-Way Match Verification Suite (e.g., `initiate_wire_transfer`, `get_purchase_order`, `verify_vendor_routing`). Mock Agent should be able to read invoices, initiate wire transfer, or request wire transfers.
- [x] Design and inject 10 custom prompt attacks with varying locations and instruction syntax.
- [ ] Attack the baseline pipeline and record initial metrics (ASR, FPR, Latency). 

### Phase 3 - Engineer standalone defenses and the unified layered defense architecture.
- [ ] **Structural Isolation (XML Spotlighting):** Demarcate untrusted external data within specific XML tags to strictly separate raw invoice data from system instructions.
- [ ] **Instruction Hierarchy:** Restructure the prompt to place system guardrails in the privileged, final position of the context window. User input is bounded at the top, and critical system instructions are placed at the absolute bottom as the final authoritative command.
- [ ] **Privilege Separation (CaMel Architecture):** Implement a dual-LLM approach utilizing a "Quarantined LLM" for raw data parsing and a "Privileged LLM" for secure tool execution.
- [ ] **Chain-of-Thought (CoT) Monitoring:** Assign an evaluator LLM model to scan the primary agent's reasoning traces for compliance anomalies.
- [ ] **Layered Integration:** Combine the above techniques to test their synergistic effects against the attack library.

### Phase 4 - Final evaluation, data analysis, and report drafting.
- [ ] **Defended Pipeline Evaluation:** Re-run the 300-invoice dataset against the pipeline for each standalone defense and then the final layered defense. 
- [ ] **Statistical Analysis:** Calculate the final ASR, FPR, and Latency. Run McNemar's Test for ASR reduction significance and the Wilcoxon Signed-Rank Test for the latency "security tax". Generate the final F1-scores.
- [ ] **Draft Report:** Compile all metrics and draft a comprehensive academic capstone report detailing methodology, independent vs. layered defense efficacy, and statistical findings.
- [ ] **Final Deliverables:** Finalize the GitHub repository with a reproducible dataset, live exploit/defense demo script, and the completed academic report.

### Tech Stack
- Language: Python 3.10+
- LLM Provider: Google Gemini API (Model: `gemini-3.1-flash-lite-preview`)
- Agent Framework: LangChain / LangGraph (create_react_agent, @tool decorators)
- Data Analysis & Stats: pandas, statsmodels, scipy
