### PLAN.md
## Project OverView
**Title:** Prompt Injection Attacks and Defenses in LLM Applications
**Author:** Gunther Gerlach
**Date:** 4/27/2026

### Description
A security analysis of prompt injection vulnerabilities in structured LLM pipelines. The project tests how malicious attacks within automated invoice processing can hijack simulated agentic functions (e.g. unauthorized wire transfers). It establishes a baseline invoice model and evaluates the efficacy of a multi-layered defense architecture. The defenses span prompt-level techniques (XML Spotlighting, Instruction Hierarchy), Dual-LLM/CaMel privilege separation, and Thought Trace Evaluation.

### Objectives
-	Evaluating the vulnerability of Gemini 2.5 to targeted data manipulation within unstructured output constraints.
-	Implement schema enforcement, dual llms, and delimiter based defenses from recent AI security research.
-	Quantify the Attack Success Rate drop across base vs defended llm to provide statistically significant insights using McNemar's test. Providing insights into both the independant and combined efficacy of the different defenses for secure data engineering.

## Tasks
### Phase 1-Gather Dataset, conduct research, and baseline pipeline construction.
-  [ ] Get invoice dataset from kaggle https://www.kaggle.com/datasets/pradumn203/payment-date-prediction-for-invoices-dataset
-  [ ] Select a subset of invoices and write a Python script to convert the tabular rows into text-based "Invoice Documents" (like pdfs) to simulate realistic, semi-structured LLM inputs.
-  [ ] Set up API connections for the Gemini 2.5 models.

### Phase 2-Create the base invoice model, the prompt injections for it, and recording initial metrics.
- [ ] Build the baseline invoice extraction pipeline.
- [ ] Create mock agentic tools like initiate_wire_transfer(vendor_name, routing_number, amount) that appends to a local transfer_ledger list. Mock Agent should be able to read invoices, initiate wire transfer, or request wire transfers.
- [ ] Design and inject custom prompt attacks with varying locations and instruction syntax into the invoice subset.
- [ ] Attack the baseline pipeline and record the initial metrics , specifically measuring Attack Success Rate (succesful attacks / total attacks), False Positive Rate, and Cost/Latency.

### Phase 3-Engineer the dual llm, delimiters, and other defenses.
- [ ] Implement XML delimiters as a spotlighting technique to strictly separate raw invoice data from system instructions.
- [ ] Implement Instruction Hierarchy, Restructure the prompt template so user input is bounded at the top, and critical system instructions are placed at the absolute bottom as the final authoritative command.
- [ ] Engineer the CaMel defense architecture by separating the workflow into a quarantined LLM for reading untrusted data and a privileged LLM for executing API tools.
- [ ] Thought Trace Evaluation: Require a mandatory thought_trace from the executing LLM. Introduce a lightweight Evaluator LLM to scan this trace for anomalous reasoning or override compliance.
- [ ] Schema Validation Enforce a strict predefined JSON schema to filter out malicious code or weird conversational outputs.

### Phase 4-Final evaluation, data analysis, and report drafting.
- [ ] Defended Pipeline Evaluation: Re-run the attack dataset against the pipeline with all defenses active. Conduct McNemar's test for analysis to validate the statistical significance of the drop in Attack Success Rate between the baseline and defended systems. Log the final ASR, FPR (False Positive Rate), Cost, and Latency.
- [ ] Compile all metrics and draft a comprehensive academic report detailing findings on the utilized prompt injections.
- [ ] Prepare the final project deliverables which include: Drafting the academic report detailing the methodology, defense layering efficacy, and final metrics. Finalize the GitHub repository with a reproducible dataset and live exploit/defense demo script.

### Tech Stack
-	Language: Python 3.10+
-	LLM Provider: Google Gemini API (Models: gemini-2.5-flash, gemini-2.5-flash-lite)
-	Agent Framework: LangChain / LangGraph (create_agent, @tool decorators)
-	Data Manipulation: pandas
