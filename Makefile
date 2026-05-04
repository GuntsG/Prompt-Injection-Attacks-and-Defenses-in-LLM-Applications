.PHONY: help install generate-invoices evaluate-baseline evaluate-final stats-analysis smoke-test clean

# Default target
help:
	@echo "Available commands:"
	@echo "  make install           - Install required Python dependencies"
	@echo "  make generate-invoices - Generate 300 text-based invoices"
	@echo "  make smoke-test        - Run a minimal (1-sample) test to verify code (~8 API calls)"
	@echo "  make evaluate-baseline - Run baseline evaluation (vulnerable agent)"
	@echo "  make evaluate-final    - Run final comparison (Baseline vs Defended)"
	@echo "  make stats-analysis    - Perform McNemar's test on final results"
	@echo "  make clean             - Remove cached files and logs"

# Smoke Test: Verify code logic with minimal API cost
smoke-test:
	python smoke_test.py

# Install dependencies
install:
	pip install pandas langchain-core langchain-google-genai langgraph jupyter statsmodels pydantic

# Phase 1: Generate dataset
generate-invoices:
	python generate_invoices.py

# Phase 2: Evaluate baseline
evaluate-baseline:
	python evaluate_baseline.py

# Phase 4: Final evaluation
evaluate-final:
	python final_evaluation.py

# Phase 4: Statistical analysis
stats-analysis:
	python stats_analysis.py

# Clean up
clean:
	rm -rf .ipynb_checkpoints
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -f baseline_metrics.csv final_comparison_results.csv
