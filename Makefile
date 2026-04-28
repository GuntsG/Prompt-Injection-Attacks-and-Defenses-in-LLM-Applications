.PHONY: help install run clean

# Default target
help:
	@echo "Available commands:"
	@echo "  make install  - Install required Python dependencies"
	@echo "  make run      - Execute the Jupyter notebook from the command line"
	@echo "  make clean    - Remove cached files and executed notebooks"

# Install dependencies needed for the notebook
install:
	pip install pandas langchain-core langchain-google-genai langgraph jupyter

# Run the notebook headlessly and save the output
run:
	jupyter nbconvert --to notebook --execute paper_3_demo.ipynb --output executed_paper_3_demo.ipynb

# Clean up Jupyter checkpoints and cache
clean:
	rm -rf .ipynb_checkpoints
	rm -f executed_paper_3_demo.ipynb
	find . -type d -name "__pycache__" -exec rm -rf {} +
