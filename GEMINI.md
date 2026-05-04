# Gemini Project Context: Prompt Injection Attacks and Defenses

## 🎯 Current Status
We are in the transition between **Phase 2 (Baseline Evaluation)** and **Phase 4 (Final Evaluation)**. 

### Completed
- [x] Dataset generation (300 invoices).
- [x] Mock financial tools implementation.
- [x] Attack library with 3 injection types (Direct, Social Engineering, Hidden).
- [x] Defense implementations (XML, Hierarchy, CaMel, Thought Trace, Schema).

### ⚠️ Blockers / Issues
- **Rate Limiting:** `baseline_metrics.csv` shows frequent `RESOURCE_EXHAUSTED` errors from the Gemini API. Evaluation runs need to be more resilient or paced slower to complete.
- **Incomplete Baseline:** The baseline ASR is not yet quantified due to the API errors.

### 🔜 Immediate Next Steps
1. **Rerun/Complete Baseline Evaluation:** Ensure we have a full set of metrics for the vulnerable agent.
2. **Run Final Evaluation:** Execute `final_evaluation.py` to compare Baseline vs. Defended.
3. **Statistical Analysis:** Run `stats_analysis.py` once data is collected.
4. **Finalize Report:** Update `REPORT.md` with TBD metrics.

## 🛠️ Project Conventions
- **Models:** Uses `gemini-2.5-flash` and `gemini-2.5-flash-lite`.
- **Metrics:** ASR (Attack Success Rate), FPR (False Positive Rate), Latency.
- **Key Files:** 
    - `defended_agent.py`: Implementation of the CaMel architecture.
    - `attack_library.py`: The source of malicious payloads.
    - `Makefile`: Centralized command runner.
