## Project OverView
**Title:** Prompt Injection Attacks and Defenses in LLM Applications
**Author:** Gunther Gerlach
**Date:** 4/27/2026

###Description
A security analysis of prompt injection vulnerabilities in structured LLM pipelines. The project tests how malicious attacks  embedded into automated invoice processing can hijack simulated agentic functions, and evaluates the efficacy of using things like dual llm (CaMel) as a defense as well as implementing layered defenses like schema validation and spotlighting on top of dual llm defenses.  

### Objectives
•	Evaluating the vulnerability of Gemini 2.5 to targeted data manipulation within structured output constraints.
•	Implement schema enforcement, dual llms, and delimiter based defenses from recent AI security research.
•	Quantify the drop in Attack Success Rate when defenses are active, providing insights for secure data engineering.

## Tasks
### Phase 1-Gather Dataset, conduct research, and baseline pipeline construction.
-  [ ] Get invoice dataset from kaggle
-  [ ] Select a subset of invoices, preprocess the data using Excel to create a clean baseline dataset
-  [ ] Set up API connections for the Gemini 1.5 or 2.5 models.

### Phase 2-Create the base invoice model, the prompt injections for it, and recording initial metrics.
- [ ] Build the baseline data extraction pipeline.
- [ ] Create mock agentic tools , such as a simulated Python function like initiate_wire_transfer()
- [ ] Design and inject custom prompt attacks with varying locations and instruction syntax into the invoice subset.
- [ ] Attack the baseline pipeline and record the initial metrics , specifically measuring Attack Success Rate, False Positive Rate, and Latency.

### Phase 3-Engineer the dual llm, delimiters, and other defenses.
- [ ] Implement XML delimiters as a spotlighting technique to strictly separate raw invoice data from system instructions.
- [ ] Engineer the CaMel defense architecture by separating the workflow into a quarantined LLM for reading untrusted data and a privileged LLM for executing API tools.
- [ ] Enforce a strict predefined Pydantic or JSON schema to filter out malicious code or weird conversational outputs.
- [ ] 

### Phase 4-Final evaluation, data analysis, and report drafting.
- [ ] Conduct McNemar's test for analysis to validate the statistical significance of the drop in Attack Success Rate between the baseline and defended systems.
- [ ] Re-evaluate the defended pipelines against the attack dataset.
- [ ] Compile all metrics and draft a comprehensive academic report detailing findings on the utilized prompt injections.
- [ ] Prepare the final project deliverables , which include a GitHub repository, a reproducible evaluation dataset, and a capstone presentation with a live exploit and defense demo
       
