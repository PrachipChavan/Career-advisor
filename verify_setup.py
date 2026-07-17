import sys

print("Verifying Python packages for Groq version...")
try:
    import streamlit
    print("SUCCESS: Streamlit imported successfully.")
except ImportError as e:
    print(f"FAILED: Failed to import streamlit: {e}")

try:
    import groq
    print("SUCCESS: groq imported successfully.")
except ImportError as e:
    print(f"FAILED: Failed to import groq: {e}")

try:
    import plotly
    print("SUCCESS: Plotly imported successfully.")
except ImportError as e:
    print(f"FAILED: Failed to import plotly: {e}")

try:
    import pdfplumber
    print("SUCCESS: pdfplumber imported successfully.")
except ImportError as e:
    print(f"FAILED: Failed to import pdfplumber: {e}")

print("Verification complete.")
