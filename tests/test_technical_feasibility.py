# test_technical_feasibility.py
"""
Quick test file to regenerate Technical Feasibility section
Used for rapid iteration during validation development
"""
import sys
sys.path.insert(0, '/home/bhagavan/aura/dprai/src')

from document_generator import generate_technical_feasibility
from langchain_google_vertexai import ChatVertexAI
from config import LLM_MODEL

# Project data
project_data = {
    "cluster_type": "Printing Industry",
    "location": "Tirupati, Andhra Pradesh",
    "members": 50,
    "project_cost": 82000000,
    "facility_type": "Digital Printing Equipment",
    "grant_scheme": "MSE-CDP"
}

print("\n" + "="*80)
print("🔧 REGENERATING: Technical Feasibility Section")
print("="*80)

# Initialize LLM
llm = ChatVertexAI(model_name=LLM_MODEL, temperature=0)

# Generate document (only 2 arguments: project_data, llm)
print("\n📝 Calling document generator...")
result = generate_technical_feasibility(project_data, llm)

# Save to file
output_path = '../output/Printing_Industry_Tirupati/06_technical_feasibility.md'
print(f"\n💾 Saving to: {output_path}")

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(result)

print(f"✅ Technical Feasibility regenerated ({len(result)} characters)")
print("\n" + "="*80)
print("🎯 Next Step: Run validation")
print("   cd /home/bhagavan/aura/dprai/src")
print("   python validate_standalone.py --source real --path ../output/Printing_Industry_Tirupati/ --section technical")
print("="*80 + "\n")
