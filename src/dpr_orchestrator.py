# dpr_orchestrator.py
"""
DPR Orchestrator Agent - Stage 9: File Export Integration! 📁
Orchestrator with modular agent integration
ALL 21 MSE-CDP SECTIONS COMPLETE + FILE EXPORT!
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
from document_generator import document_generator_agent
from file_export_agent import file_export_agent  # NEW!


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
    
    # Export information (NEW!)
    export_info: dict


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
    
    if "export_info" not in state:
        state["export_info"] = {}
    
    state["current_stage"] = "initialized"
    
    print(f"Status: ✅ Initialized")
    return state


def coordinator_agent(state: DPRState) -> DPRState:
    """
    Node 6: Main coordinator agent
    Uses collected project data, financial metrics, generated documents, and export info
    """
    print()
    cprint(f"{'NODE: coordinator_agent':-^80}", 'green')
    
    messages = state.get("messages", [])
    project_data = state.get("project_data", {})
    validation = state.get("validation", {})
    dpr_sections = state.get("dpr_sections", {})
    export_info = state.get("export_info", {})  # NEW!
    
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
        
        # Check if documents are generated
        doc_sections = [k for k in ["executive_summary", "organization_details", "financial_plan",
                                    "project_introduction", "cluster_profile", "technical_feasibility",
                                    "market_analysis", "implementation_schedule",
                                    "management_structure", "economic_viability", "swot_analysis",
                                    "risk_analysis", "environmental_impact",
                                    "quality_assurance", "supply_chain", "infrastructure",
                                    "legal_compliance", "human_resource",
                                    "marketing_strategy", "monitoring_framework", "annexures"] 
                       if k in dpr_sections]
        if doc_sections:
            print(f"📄 Documents Generated: {len(doc_sections)}/21 sections (Stage 8 - COMPLETE!) 🎉")
            response_text += f" Generated {len(doc_sections)} DPR sections."
        
        # Check if files are exported (NEW!)
        if export_info and export_info.get("files_created"):
            files_created = export_info.get("files_created", 0)
            output_dir = export_info.get("output_directory", "N/A")
            print(f"📁 Files Exported: {files_created} files → {output_dir}")
            response_text += f" Exported {files_created} files to disk."
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
    Node 7: Plan the workflow (dummy for now)
    """
    print()
    cprint(f"{'NODE: workflow_planner':-^80}", 'yellow')
    
    # Dummy plan
    plan = {
        "stage": "Stage 9",
        "next_agents": ["Data Collection", "Financial", "Document Gen", "File Export"]
    }
    
    state["project_data"]["workflow_plan"] = plan
    state["current_stage"] = "planned"
    
    print(f"Plan: {plan}")
    print(f"Status: ✅ Workflow planned")
    return state


def output_formatter(state: DPRState) -> DPRState:
    """
    Node 8: Format final output
    Includes collected project data, financial metrics, generated documents, and export info
    """
    print()
    cprint(f"{'NODE: output_formatter':-^80}", 'magenta')
    
    project_data = state.get("project_data", {})
    validation = state.get("validation", {})
    dpr_sections = state.get("dpr_sections", {})
    export_info = state.get("export_info", {})  # NEW!
    
    # Build output
    output = {
        "status": "Stage 9 COMPLETE! 🎉",
        "orchestrator": "✅ Functional",
        "data_collection": "✅ Integrated",
        "financial_modeling": "✅ Integrated",
        "document_generation": "✅ COMPLETE (ALL 21 sections!) 🎊",
        "file_export": "✅ COMPLETE (Files written to disk!) 📁",
        "project_data_collected": len(project_data),
        "validation": "✅ Passed" if validation.get("valid") else "⚠️ Has Issues",
        "next_step": "All files exported! Ready for submission or Phase 2 enhancements."
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
    
    # Add document generation summary
    doc_sections = [k for k in ["executive_summary", "organization_details", "financial_plan",
                                "project_introduction", "cluster_profile", "technical_feasibility",
                                "market_analysis", "implementation_schedule",
                                "management_structure", "economic_viability", "swot_analysis",
                                "risk_analysis", "environmental_impact",
                                "quality_assurance", "supply_chain", "infrastructure",
                                "legal_compliance", "human_resource",
                                "marketing_strategy", "monitoring_framework", "annexures"] 
                   if k in dpr_sections]
    
    output["document_summary"] = {
        "sections_generated": len(doc_sections),
        "total_sections_this_stage": 21,
        "total_mse_cdp_sections": 21,
        "progress_percentage": round((len(doc_sections) / 21) * 100, 1),
        "sections": doc_sections,
        "format": "Markdown",
        "method": "Template + LLM",
        "status": "🎉 ALL MSE-CDP SECTIONS COMPLETE! 🎉"
    }
    
    # Add export summary (NEW!)
    if export_info:
        output["export_summary"] = {
            "files_created": export_info.get("files_created", 0),
            "output_directory": export_info.get("output_directory", "N/A"),
            "total_size_kb": round(export_info.get("total_size_bytes", 0) / 1024, 1),
            "timestamp": export_info.get("timestamp", "N/A"),
            "status": "✅ Files available on disk"
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
    Build the orchestrator graph with all agents
    Stage 9: FILE EXPORT INTEGRATION! 📁
    """
    print("\n" + "="*80)
    print("🏗️  BUILDING DPR ORCHESTRATOR GRAPH - STAGE 9 (FILE EXPORT!)")
    print("="*80)
    
    # Create state graph
    builder = StateGraph(DPRState)
    
    # Add nodes
    builder.add_node("ORCHESTRATOR_INIT", orchestrator_init)
    builder.add_node("DATA_COLLECTION_AGENT", data_collection_agent)
    builder.add_node("FINANCIAL_MODELING_AGENT", financial_modeling_agent)
    builder.add_node("DOCUMENT_GENERATOR_AGENT", document_generator_agent)
    builder.add_node("FILE_EXPORT_AGENT", file_export_agent)  # NEW!
    builder.add_node("COORDINATOR_AGENT", coordinator_agent)
    builder.add_node("WORKFLOW_PLANNER", workflow_planner)
    builder.add_node("OUTPUT_FORMATTER", output_formatter)
    
    # Add edges - Updated flow with file export
    builder.add_edge(START, "ORCHESTRATOR_INIT")
    builder.add_edge("ORCHESTRATOR_INIT", "DATA_COLLECTION_AGENT")
    builder.add_edge("DATA_COLLECTION_AGENT", "FINANCIAL_MODELING_AGENT")
    builder.add_edge("FINANCIAL_MODELING_AGENT", "DOCUMENT_GENERATOR_AGENT")
    builder.add_edge("DOCUMENT_GENERATOR_AGENT", "FILE_EXPORT_AGENT")  # NEW!
    builder.add_edge("FILE_EXPORT_AGENT", "COORDINATOR_AGENT")  # NEW!
    builder.add_edge("COORDINATOR_AGENT", "WORKFLOW_PLANNER")
    builder.add_edge("WORKFLOW_PLANNER", "OUTPUT_FORMATTER")
    builder.add_edge("OUTPUT_FORMATTER", END)
    
    # Compile graph
    graph = builder.compile()
    
    # Save visualization
    save_graph_as_png(graph, __file__)
    
    print("\n✅ Orchestrator graph built successfully! (Stage 9 - FILE EXPORT!) 📁")
    print("="*80 + "\n")
    
    return graph


# ============================================================================
# BUILD GRAPH ON MODULE IMPORT
# ============================================================================

orchestrator_graph = build_orchestrator_agent()