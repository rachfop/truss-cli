# Truss Chains Custom Image Example

Minimal reproduction of the “Truss Chains” tab from `docs/index.mdx`. The sample
relies on a light-weight `truss_chains` stub so it can run offline.

## Running the example

1. Create a virtual environment and install the local requirements (no external
   packages needed):
   ```bash
   python -m venv .venv
   ./.venv/bin/pip install -r requirements.txt
   ```
2. Execute the chainlet:
   ```bash
   ./.venv/bin/python chainlet.py
   ```
   Expected output: `HELLO, WORLD!`
