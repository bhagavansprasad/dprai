# test_financial_plan.py
import sys
sys.path.insert(0, '/home/bhagavan/aura/dprai/src')

from document_generator import generate_financial_plan
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
    "metrics": {
        "npv": 28700000,
        "irr": 15.5,
        "dscr": 3.5,
        "breakeven_percentage": 55,
        "payback_period_years": 4.5
    },
    "loan_details": {
        "grant_amount": 57400000,
        "grant_percentage": 70,
        "loan_amount": 24600000
    },
    "mse_cdp_compliance": {
        "status": "COMPLIANT"
    },
    "projections": {
        "duration_years": 10
    }
}

llm = ChatVertexAI(model_name=LLM_MODEL, temperature=0)
result = generate_financial_plan(project_data, financial_data, llm)

# Save to file
with open('../output/Printing_Industry_Tirupati/03_financial_plan.md', 'w') as f:
    f.write(result)

print("✅ Financial Plan regenerated")