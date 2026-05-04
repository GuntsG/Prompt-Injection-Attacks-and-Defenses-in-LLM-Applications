# Project Report: Prompt Injection Attacks and Defenses in LLM Applications

**Author:** Gunther Gerlach  
**Date:** April 2026

## 1. Executive Summary
This project analyzes the vulnerability of LLM-based automated Accounts Payable (AP) agents to prompt injection attacks and evaluates the effectiveness of a multi-layered defense architecture.

## 2. Methodology
### 2.1 Dataset
- **Source:** Kaggle Payment Date Prediction for Invoices.
- **Samples:** 300 invoices converted from tabular CSV data to semi-structured text documents.
- **Modifications:** Added mock routing numbers to simulate realistic financial data.

### 2.2 Attack Library
Three types of prompt injection attacks were designed:
1. **Direct Override:** Explicit system-style command to ignore original data.
2. **Social Engineering:** Narrative-based attempt to deceive the agent.
3. **Hidden Instruction:** Large whitespace padding followed by a "confidential" override.

### 2.3 Defense Architecture (CaMel & Multi-Layered)
The defended pipeline incorporates:
- **XML Spotlighting:** Wrapping untrusted data in `<invoice_data>` tags.
- **Instruction Hierarchy:** Placing authoritative system commands at the bottom of the prompt.
- **Schema Enforcement:** Using Pydantic for structured JSON output to filter conversational noise.
- **CaMel Architecture:** Separating the workflow into a **Quarantined LLM** (extraction only) and a **Privileged LLM** (execution only).
- **Thought Trace Evaluation:** A secondary **Evaluator LLM** scans the extraction logic for malicious reasoning.

## 3. Results (Placeholders)
| Metric | Baseline (Vulnerable) | Defended Agent |
| :--- | :--- | :--- |
| **Attack Success Rate (ASR)** | TBD | TBD |
| **False Positive Rate (FPR)** | 0% | TBD |
| **Average Latency** | TBD | TBD |
| **McNemar's P-Value** | N/A | TBD |

## 4. Analysis
[To be completed after evaluation]

## 5. Conclusion
[To be completed after evaluation]
