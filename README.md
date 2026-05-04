# Prompt Injection Attacks and Defenses in LLM Applications

## 📌 Project Overview
A security analysis of prompt injection vulnerabilities in structured LLM pipelines. This project tests how malicious attacks within automated invoice processing can hijack agentic functions like unauthorized wire transfers. It evaluates a multi-layered defense architecture against a vulnerable baseline.

## 🎯 Objectives
- Quantify the vulnerability of Gemini 2.5 to prompt injection in financial workflows.
- Implement and evaluate a multi-layered defense (XML Spotlighting, Instruction Hierarchy, CaMel Architecture, Thought Trace Evaluation).
- Statistically validate defense efficacy using McNemar's test.

## 🧰 Tech Stack
- **LLM:** Google Gemini 2.5 (Flash/Flash-Lite)
- **Framework:** LangChain / LangGraph
- **Language:** Python 3.10+
- **Analysis:** pandas, statsmodels

## 🚀 Project Structure
- `generate_invoices.py`: Phase 1 - Converts CSV data to text invoices.
- `attack_library.py`: Phase 2 - Contains prompt injection payloads.
- `agent_tools.py`: Phase 2 - Mock financial tools (Wire Transfer, etc.).
- `baseline_agent.py`: Phase 2 - The vulnerable ReAct agent.
- `defenses.py`: Phase 3 - Delimiter and verification logic.
- `defended_agent.py`: Phase 3 - The secure pipeline (CaMel Architecture).
- `evaluate_baseline.py`: Phase 2 - Measures baseline ASR.
- `final_evaluation.py`: Phase 4 - Comparative analysis.
- `stats_analysis.py`: Phase 4 - Statistical significance testing.

## 🛠️ How to Run

### 1. Install Dependencies
```bash
make install
```

### 2. Set API Key
```bash
$env:GOOGLE_API_KEY='your_api_key_here'
```

### 3. Generate Dataset
```bash
make generate-invoices
```

### 4. Run Baseline Evaluation
```bash
make evaluate-baseline
```

### 5. Run Final Comparison
```bash
make evaluate-final
```

### 6. Perform Statistical Analysis
```bash
make stats-analysis
```

## 👥 Authors
Gunther Gerlach

## 📅 Date
April 2026
