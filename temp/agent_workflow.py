"""
DPR Agent Workflow using LangGraph
Phase 1: Basic text generation (Executive Summary + Cluster Profile)
"""

from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from datetime import datetime

from models import UserInput, ValidationResult
from prompts import get_executive_summary_prompt, get_cluster_profile_prompt
from gemini_service import get_gemini_service


# ============================================
# State Definition
# ============================================

class DPRState(TypedDict):
    """State that flows through the workflow"""
    user_input: dict
    validation_passed: bool
    validation_errors: list
    executive_summary: str
    cluster_profile: str
    execution_time: float


# ============================================
# Node Functions
# ============================================

def initialize_state(state: DPRState) -> DPRState:
    """Initialize state with defaults"""
    return {
        "user_input": state.get("user_input", {}),
        "validation_passed": False,
        "validation_errors": [],
        "executive_summary": "",
        "cluster_profile": "",
        "execution_time": 0.0
    }


def validate_input(state: DPRState) -> DPRState:
    """Validate user input"""
    print("\n" + "="*60)
    print("NODE 1: VALIDATING INPUT")
    print("="*60)
    
    errors = []
    
    try:
        # Validate using Pydantic
        user_input_obj = UserInput(**state["user_input"])
        state["validation_passed"] = True
        print("✓ Input validation PASSED")
        
    except Exception as e:
        errors.append(str(e))
        state["validation_passed"] = False
        state["validation_errors"] = errors
        print(f"✗ Input validation FAILED: {errors}")
    
    return state


def generate_executive_summary(state: DPRState) -> DPRState:
    """Generate executive summary using Gemini"""
    print("\n" + "="*60)
    print("NODE 2: GENERATING EXECUTIVE SUMMARY")
    print("="*60)
    
    if not state["validation_passed"]:
        print("⊘ Skipping due to validation failure")
        return state
    
    try:
        gemini = get_gemini_service()
        prompt = get_executive_summary_prompt(state["user_input"])
        
        print("Calling Gemini API...")
        summary = gemini.generate(prompt)
        
        state["executive_summary"] = summary
        print(f"✓ Executive Summary generated ({len(summary)} characters)")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        state["executive_summary"] = f"[ERROR: {e}]"
    
    return state


def generate_cluster_profile(state: DPRState) -> DPRState:
    """Generate cluster profile using Gemini"""
    print("\n" + "="*60)
    print("NODE 3: GENERATING CLUSTER PROFILE")
    print("="*60)
    
    if not state["validation_passed"]:
        print("⊘ Skipping due to validation failure")
        return state
    
    try:
        gemini = get_gemini_service()
        prompt = get_cluster_profile_prompt(state["user_input"])
        
        print("Calling Gemini API...")
        profile = gemini.generate(prompt)
        
        state["cluster_profile"] = profile
        print(f"✓ Cluster Profile generated ({len(profile)} characters)")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        state["cluster_profile"] = f"[ERROR: {e}]"
    
    return state


# ============================================
# Build Graph
# ============================================

def build_dpr_graph():
    """Build the DPR workflow graph"""
    
    builder = StateGraph(DPRState)
    
    # Add nodes
    builder.add_node("INITIALIZE", initialize_state)
    builder.add_node("VALIDATE", validate_input)
    builder.add_node("EXEC_SUMMARY", generate_executive_summary)
    builder.add_node("CLUSTER_PROFILE", generate_cluster_profile)
    
    # Add edges
    builder.add_edge(START, "INITIALIZE")
    builder.add_edge("INITIALIZE", "VALIDATE")
    builder.add_edge("VALIDATE", "EXEC_SUMMARY")
    builder.add_edge("EXEC_SUMMARY", "CLUSTER_PROFILE")
    builder.add_edge("CLUSTER_PROFILE", END)
    
    # Compile
    graph = builder.compile()
    
    print("✓ DPR Graph built successfully")
    
    return graph


# ============================================
# Create Agent
# ============================================

def create_agent():
    """Create DPR agent"""
    return build_dpr_graph()
