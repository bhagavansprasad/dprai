# data_collection_agent.py
"""
Data Collection Agent - Stage 2
Extracts and validates project data from user input
"""
import json
import re
from typing import Dict, Any
from termcolor import cprint

from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_google_vertexai import ChatVertexAI
from config import LLM_MODEL


def extract_json_from_string(text: str) -> Dict[str, Any]:
    """
    Extract JSON from LLM response text
    """
    if isinstance(text, dict):
        return text
    
    # Try to find JSON in the response
    match = re.search(r'\{.*?\}', text, re.DOTALL)
    if match:
        json_str = match.group(0)
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            pass
    
    return {}


def validate_project_data(project_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Validate required fields and return validation result
    
    Returns:
        {
            "valid": bool,
            "missing_fields": list,
            "warnings": list
        }
    """
    # Required fields for DPR
    required_fields = [
        "cluster_type",
        "location", 
        "members",
        "project_cost",
        "facility_type",
        "grant_scheme"
    ]
    
    missing_fields = []
    warnings = []
    
    # Check required fields
    for field in required_fields:
        if field not in project_data or not project_data[field]:
            missing_fields.append(field)
    
    # Validate data types and ranges
    if "members" in project_data:
        try:
            members = int(project_data["members"])
            if members < 1:
                warnings.append("Number of members should be at least 1")
        except (ValueError, TypeError):
            warnings.append("Number of members should be a valid number")
    
    if "project_cost" in project_data:
        try:
            cost = float(project_data["project_cost"])
            if cost <= 0:
                warnings.append("Project cost should be greater than 0")
        except (ValueError, TypeError):
            warnings.append("Project cost should be a valid number")
    
    validation_result = {
        "valid": len(missing_fields) == 0,
        "missing_fields": missing_fields,
        "warnings": warnings
    }
    
    return validation_result


def data_collection_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract structured project data from user input using LLM
    """
    print()
    cprint(f"{'NODE: data_collection_agent':-^80}", 'blue', attrs=['bold'])
    
    messages = state.get("messages", [])
    if not messages:
        print("⚠️  No messages found in state")
        return state
    
    # Get user input
    user_input = messages[-1].content if messages else ""
    print(f"\n📥 Extracting project data from user input...")
    
    # System prompt for data extraction
    system_prompt = """You are a Data Extraction Agent for DPR (Detailed Project Report) generation.

Your task is to extract structured project information from the user's input.

Extract the following fields and return as JSON:
- cluster_type: Type of industry/cluster (e.g., "Printing Industry", "Textile", "Food Processing")
- location: Full location (city, state)
- members: Number of units/members in the cluster (as integer)
- project_cost: Total project cost in rupees (as number, remove currency symbols)
- facility_type: Type of Common Facility Centre (e.g., "Digital Printing Equipment")
- grant_scheme: Government scheme name (e.g., "MSE-CDP", "PMEGP", "SFURTI")
- subsidy_range: Subsidy percentage or range (e.g., "60-80%")

Additional optional fields:
- turnover: Average turnover if mentioned
- address: Delivery address if mentioned
- sector: Industry sector

CRITICAL: Return ONLY valid JSON, no additional text.

Example output:
{
  "cluster_type": "Printing Industry",
  "location": "Tirupati, Andhra Pradesh",
  "members": 50,
  "project_cost": 82000000,
  "facility_type": "Digital Printing Equipment",
  "grant_scheme": "MSE-CDP",
  "subsidy_range": "60-80%"
}"""

    sys_msg = SystemMessage(content=system_prompt)
    human_msg = HumanMessage(content=user_input)
    
    # Initialize LLM
    llm = ChatVertexAI(model_name=LLM_MODEL, temperature=0)
    
    # Get structured data
    prompt = [sys_msg, human_msg]
    response = llm.invoke(prompt)
    
    # Extract JSON from response
    project_data = extract_json_from_string(response.content)
    
    if not project_data:
        print("⚠️  Could not extract structured data from user input")
        project_data = {"error": "Failed to parse project data"}
    
    # Validate the extracted data
    validation = validate_project_data(project_data)
    
    # Display extracted data
    print(f"\n✅ Extracted Project Data:")
    print(json.dumps(project_data, indent=2))
    
    # Display validation results
    print(f"\n🔍 Validation Results:")
    if validation["valid"]:
        print("  ✅ All required fields present")
    else:
        print(f"  ⚠️  Missing fields: {', '.join(validation['missing_fields'])}")
    
    if validation["warnings"]:
        print(f"  ⚠️  Warnings:")
        for warning in validation["warnings"]:
            print(f"     - {warning}")
    
    # Store in state
    state["project_data"] = project_data
    state["validation"] = validation
    
    # Add data collection message to conversation
    data_msg = AIMessage(
        content=f"Project data collected and validated. Found {len(project_data)} fields."
    )
    state["messages"].append(data_msg)
    
    print(f"\n✅ Data collection complete")
    return state
