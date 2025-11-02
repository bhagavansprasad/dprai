# test_executive_summary.py
import sys
sys.path.insert(0, '/home/bhagavan/aura/dprai/src')

from document_generator import generate_executive_summary
from langchain_google_vertexai import ChatVertexAI
from config import LLM_MODEL

project_data = {
    "cluster_type": "Printing Industry",
    "location": "Tirupati, Andhra Pradesh",
    "members": 50,
    "project_cost": 82000000,
    "facility_type": "Digital Printing Equipment",
    "grant_scheme": "MSE-CDP"
}

financial_data = {
    "metrics": {"npv": 28700000, "irr": 15.5, "dscr": 2.67, "breakeven_percentage": 80},
    "mse_cdp_compliance": {"status": "COMPLIANT"}
}

llm = ChatVertexAI(model_name=LLM_MODEL, temperature=0)
result = generate_executive_summary(project_data, financial_data, llm)

# Save to file
with open('../output/Printing_Industry_Tirupati/01_executive_summary.md', 'w') as f:
    f.write(result)

print("✅ Executive Summary regenerated")
