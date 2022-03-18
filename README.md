# barcode-sheet-generator
Generate CODE39 labels for product SKUs formatted as a pdf for printing onto label paper.
# Usage Guide
To use, put SKUs separated by line breaks in input.txt file. To generate N labels for the same SKU, append \*N to the end of the respective SKU line.
Then simply run python main.py.

# Installation
Pull the repo, then run
python3 -m venv
source /bin/activate
python -m pip install -r requirements.txt
