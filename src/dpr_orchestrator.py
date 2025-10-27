# dpr_orchestrator.py
"""
DPR Orchestrator Agent - Stage 3: Financial Modeling Integration
Orchestrator with modular agent integration
"""
from typing import TypedDict, Annotated
from termcolor import cprint

from langchain_core.messages import BaseMessage, HumanMessage, AIMessage
from langchain_google_vertexai import ChatVertexAI
from langgraph.graph import START, END, StateGraph
from langgraph.graph.message import add_messages

from lg_utility import save_graph_as_png
from config import LLM_MODEL

# Import agents
from data_collection_agent import data_collection_agent
from financial_agent import financial_modeling_agent


# ============================================================================
# STATE DEFINITION
# ============================================================================

class DPRState(TypedDict):
    """
    State for DPR generation workflow
    """
    # Conversation messages
    messages: Annotated[list[BaseMessage], add_messages]
    
    # Project data collected from user
    project_data: dict
    
    # Validation results
    validation: dict
    
    # Generated DPR sections
    dpr_sections: dict
    
    # Current processing stage
    current_stage: str


# ============================================================================
# DUMMY NODE FUNCTIONS
# ============================================================================

def orchestrator_init(state: DPRState) -> DPRState:
    """
    Node 1: Initialize the orchestrator
    """
    print()
    cprint(f"{'NODE: orchestrator_init':-^80}", 'cyan')
    
    messages = state.get("messages", [])
    if messages:
        print(f"Input: {messages[-1].content[:100]}...")
    
    # Initialize empty structures if not present
    if "project_data" not in state:
        state["project_data"] = {}
    
    if "dpr_sections" not in state:
        state["dpr_sections"] = {}
    
    if "validation" not in state:
        state["validation"] = {}
    
    state["current_stage"] = "initialized"
    
    print(f"Status: ✅ Initialized")
    return state


def coordinator_agent(state: DPRState) -> DPRState:
    """
    Node 4: Main coordinator agent
    Uses collected project data and financial metrics to coordinate workflow
    """
    print()
    cprint(f"{'NODE: coordinator_agent':-^80}", 'green')
    
    messages = state.get("messages", [])
    project_data = state.get("project_data", {})
    validation = state.get("validation", {})
    dpr_sections = state.get("dpr_sections", {})
    
    # Check if we have valid project data
    if validation.get("valid"):
        cluster = project_data.get('cluster_type', 'Unknown')
        response_text = f"✅ Project data validated. Coordinating agents for {cluster} cluster."
        print(f"📊 Cluster: {project_data.get('cluster_type', 'N/A')}")
        print(f"📍 Location: {project_data.get('location', 'N/A')}")
        print(f"👥 Members: {project_data.get('members', 'N/A')}")
        
        # Check if financial modeling is done
        if "financial" in dpr_sections:
            financial = dpr_sections["financial"]
            compliance = financial.get("mse_cdp_compliance", {}).get("status", "UNKNOWN")
            print(f"💰 Financial Status: {compliance}")
            response_text += f" Financial modeling complete: {compliance}."
    else:
        response_text = "⚠️ Project data incomplete. May need additional information."
        print(f"⚠️  Missing fields: {validation.get('missing_fields', [])}")
    
    response = AIMessage(content=response_text)
    
    print(f"\nResponse: {response_text}")
    
    state["messages"].append(response)
    state["current_stage"] = "coordinated"
    
    print(f"Status: ✅ Coordination complete")
    return state


def workflow_planner(state: DPRState) -> DPRState:
    """
    Node 5: Plan the workflow (dummy for now)
    """
    print()
    cprint(f"{'NODE: workflow_planner':-^80}", 'yellow')
    
    # Dummy plan
    plan = {
        "stage": "Stage 1",
        "next_agents": ["Data Collection (Stage 2)", "Financial (Stage 3)", "Document Gen (Stage 4)"]
    }
    
    state["project_data"]["workflow_plan"] = plan
    state["current_stage"] = "planned"
    
    print(f"Plan: {plan}")
    print(f"Status: ✅ Workflow planned")
    return state


def output_formatter(state: DPRState) -> DPRState:
    """
    Node 6: Format final output
    Includes collected project data and financial metrics
    """
    print()
    cprint(f"{'NODE: output_formatter':-^80}", 'magenta')
    
    project_data = state.get("project_data", {})
    validation = state.get("validation", {})
    dpr_sections = state.get("dpr_sections", {})
    
    # Build output
    output = {
        "status": "Stage 3 Complete",
        "orchestrator": "✅ Functional",
        "data_collection": "✅ Integrated",
        "financial_modeling": "✅ Integrated",
        "project_data_collected": len(project_data),
        "validation": "✅ Passed" if validation.get("valid") else "⚠️ Has Issues",
        "next_step": "Stage 4 - Add Document Generation Agent"
    }
    
    # Add project summary if data is valid
    if validation.get("valid"):
        output["project_summary"] = {
            "cluster": project_data.get("cluster_type"),
            "location": project_data.get("location"),
            "members": project_data.get("members"),
            "cost": project_data.get("project_cost")
        }
    
    # Add financial summary if available
    if "financial" in dpr_sections:
        financial = dpr_sections["financial"]
        metrics = financial.get("metrics", {})
        compliance = financial.get("mse_cdp_compliance", {})
        
        output["financial_summary"] = {
            "npv": metrics.get("npv"),
            "irr": metrics.get("irr"),
            "dscr": metrics.get("dscr"),
            "breakeven": metrics.get("breakeven_percentage"),
            "compliance": compliance.get("status"),
            "note": "⚠️ Using simulated calculations"
        }
    
    import json
    output_str = json.dumps(output, indent=2)
    
    print(f"Final Output:\n{output_str}")
    
    final_message = AIMessage(content=output_str)
    state["messages"].append(final_message)
    state["current_stage"] = "complete"
    
    print(f"Status: ✅ Output formatted")
    return state


# ============================================================================
# GRAPH BUILDER
# ============================================================================

def build_orchestrator_agent():
    """
    Build the orchestrator graph with data collection and financial modeling agents
    Stage 3: Integrated financial modeling
    """
    print("\n" + "="*80)
    print("🏗️  BUILDING DPR ORCHESTRATOR GRAPH - STAGE 3")
    print("="*80)
    
    # Create state graph
    builder = StateGraph(DPRState)
    
    # Add nodes
    builder.add_node("ORCHESTRATOR_INIT", orchestrator_init)
    builder.add_node("DATA_COLLECTION_AGENT", data_collection_agent)
    builder.add_node("FINANCIAL_MODELING_AGENT", financial_modeling_agent)  # NEW!
    builder.add_node("COORDINATOR_AGENT", coordinator_agent)
    builder.add_node("WORKFLOW_PLANNER", workflow_planner)
    builder.add_node("OUTPUT_FORMATTER", output_formatter)
    
    # Add edges - Updated flow with financial modeling
    builder.add_edge(START, "ORCHESTRATOR_INIT")
    builder.add_edge("ORCHESTRATOR_INIT", "DATA_COLLECTION_AGENT")
    builder.add_edge("DATA_COLLECTION_AGENT", "FINANCIAL_MODELING_AGENT")  # NEW!
    builder.add_edge("FINANCIAL_MODELING_AGENT", "COORDINATOR_AGENT")  # NEW!
    builder.add_edge("COORDINATOR_AGENT", "WORKFLOW_PLANNER")
    builder.add_edge("WORKFLOW_PLANNER", "OUTPUT_FORMATTER")
    builder.add_edge("OUTPUT_FORMATTER", END)
    
    # Compile graph
    graph = builder.compile()
    
    # Save visualization
    save_graph_as_png(graph, __file__)
    
    print("\n✅ Orchestrator graph built successfully! (Stage 3)")
    print("="*80 + "\n")
    
    return graph


# ============================================================================
# BUILD GRAPH ON MODULE IMPORT
# ============================================================================

orchestrator_graph = build_orchestrator_agent()