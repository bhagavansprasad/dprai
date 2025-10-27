# document_generator.py
"""
Document Generation Agent - Stage 4
Generates DPR sections in Markdown format using real collected data

Sections generated (Phase 1 - 3 sections):
1. Executive Summary
2. Organization Details
3. Financial Plan

Uses: Template structure + LLM content enhancement
Format: Markdown
Content: Real data from collected project_data and financial metrics
"""
import json
from typing import Dict, Any
from termcolor import cprint

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_vertexai import ChatVertexAI
from config import LLM_MODEL


# ============================================================================
# SECTION TEMPLATES
# ============================================================================

def get_executive_summary_template() -> str:
    """
    Template for Executive Summary section
    Structure is predefined, content filled by LLM
    """
    template = """# EXECUTIVE SUMMARY

## Project Overview
{project_overview}

## Cluster Profile
{cluster_profile}

## Financial Highlights
{financial_highlights}

## Expected Impact
{expected_impact}

## Recommendation
{recommendation}
"""
    return template


def get_organization_details_template() -> str:
    """
    Template for Organization Details section
    """
    template = """# ORGANIZATION DETAILS

## Cluster Information
{cluster_info}

## Membership Structure
{membership_structure}

## Common Facility Centre
{cfc_details}

## Geographic Coverage
{geographic_coverage}

## Governance Structure
{governance_structure}
"""
    return template


def get_financial_plan_template() -> str:
    """
    Template for Financial Plan section
    Uses calculated financial metrics
    """
    template = """# FINANCIAL PLAN

## Project Cost Breakdown
{cost_breakdown}

## Funding Structure
{funding_structure}

## Financial Viability Metrics
{financial_metrics}

## Revenue Projections
{revenue_projections}

## Debt Service Analysis
{debt_service_analysis}

## Financial Feasibility Assessment
{feasibility_assessment}
"""
    return template


# ============================================================================
# CONTENT GENERATORS (Template + LLM)
# ============================================================================

def generate_executive_summary(project_data: Dict, financial_data: Dict, llm) -> str:
    """
    Generate Executive Summary using Template + LLM
    """
    print("  📝 Generating: Executive Summary")
    print("     🔧 [DEBUG] Using Template + LLM approach")
    
    # Prepare data for LLM
    cluster_type = project_data.get("cluster_type", "N/A")
    location = project_data.get("location", "N/A")
    members = project_data.get("members", 0)
    cost = project_data.get("project_cost", 0)
    grant_scheme = project_data.get("grant_scheme", "N/A")
    
    metrics = financial_data.get("metrics", {})
    compliance = financial_data.get("mse_cdp_compliance", {})
    
    # LLM prompt for content generation
    system_prompt = """You are a professional DPR writer specializing in MSME cluster development projects.
Generate clear, professional content for the Executive Summary section.
Use the provided data to create compelling, factual content.
Write in formal business language suitable for government submissions.
Keep content concise but comprehensive."""

    user_prompt = f"""Generate content for an Executive Summary with these subsections:

PROJECT DATA:
- Cluster Type: {cluster_type}
- Location: {location}
- Members: {members} units
- Project Cost: ₹{cost:,}
- Grant Scheme: {grant_scheme}

FINANCIAL METRICS:
- NPV: ₹{metrics.get('npv', 0):,.2f}
- IRR: {metrics.get('irr', 0):.2f}%
- DSCR: {metrics.get('dscr', 0):.2f}
- Break-even: {metrics.get('breakeven_percentage', 0):.1f}%
- Compliance: {compliance.get('status', 'UNKNOWN')}

Generate 4-5 paragraphs covering:
1. PROJECT OVERVIEW - Brief introduction to the cluster and proposed CFC
2. CLUSTER PROFILE - Key characteristics and current challenges
3. FINANCIAL HIGHLIGHTS - Summary of financial viability metrics
4. EXPECTED IMPACT - Benefits to cluster members and local economy
5. RECOMMENDATION - Clear statement on project viability

Write in professional, formal tone. Be factual and specific."""

    sys_msg = SystemMessage(content=system_prompt)
    user_msg = HumanMessage(content=user_prompt)
    
    print("     🤖 [DEBUG] Invoking LLM for content generation...")
    response = llm.invoke([sys_msg, user_msg])
    content = response.content
    
    print("     ✅ [DEBUG] Executive Summary generated")
    
    # Use template structure with LLM content
    # For simplicity, we'll use the LLM content directly
    # In production, you'd parse and insert into template placeholders
    return f"# EXECUTIVE SUMMARY\n\n{content}"


def generate_organization_details(project_data: Dict, llm) -> str:
    """
    Generate Organization Details using Template + LLM
    """
    print("  📝 Generating: Organization Details")
    print("     🔧 [DEBUG] Using Template + LLM approach")
    
    cluster_type = project_data.get("cluster_type", "N/A")
    location = project_data.get("location", "N/A")
    members = project_data.get("members", 0)
    facility_type = project_data.get("facility_type", "N/A")
    
    system_prompt = """You are a professional DPR writer specializing in MSME cluster development.
Generate clear, detailed content for the Organization Details section.
Focus on structure, governance, and operational details.
Write in formal business language."""

    user_prompt = f"""Generate content for Organization Details section:

PROJECT DATA:
- Cluster Type: {cluster_type}
- Location: {location}
- Number of Members: {members} units
- Facility Type: {facility_type}

Generate detailed content covering:
1. CLUSTER INFORMATION - History, current status, key characteristics
2. MEMBERSHIP STRUCTURE - Member profiles, size distribution, specializations
3. COMMON FACILITY CENTRE - Detailed description of proposed facility
4. GEOGRAPHIC COVERAGE - Area covered, accessibility, infrastructure
5. GOVERNANCE STRUCTURE - Proposed SPV structure, management, decision-making

Write 5-6 paragraphs with specific details. Be professional and comprehensive."""

    sys_msg = SystemMessage(content=system_prompt)
    user_msg = HumanMessage(content=user_prompt)
    
    print("     🤖 [DEBUG] Invoking LLM for content generation...")
    response = llm.invoke([sys_msg, user_msg])
    content = response.content
    
    print("     ✅ [DEBUG] Organization Details generated")
    
    return f"# ORGANIZATION DETAILS\n\n{content}"


def generate_financial_plan(project_data: Dict, financial_data: Dict, llm) -> str:
    """
    Generate Financial Plan using Template + LLM + Real Metrics
    """
    print("  📝 Generating: Financial Plan")
    print("     🔧 [DEBUG] Using Template + LLM + Real Financial Metrics")
    
    cost = project_data.get("project_cost", 0)
    metrics = financial_data.get("metrics", {})
    loan_details = financial_data.get("loan_details", {})
    compliance = financial_data.get("mse_cdp_compliance", {})
    projections = financial_data.get("projections", {})
    
    # Build detailed financial metrics text
    financial_metrics_text = f"""
## Financial Viability Metrics

Based on detailed financial modeling, the project demonstrates the following key metrics:

**Net Present Value (NPV):** ₹{metrics.get('npv', 0):,.2f}
- Status: {'✅ PASS' if metrics.get('npv', 0) > 0 else '❌ FAIL'} (Requirement: > 0)
- Indicates positive return on investment over project lifetime

**Internal Rate of Return (IRR):** {metrics.get('irr', 0):.2f}%
- Status: {'✅ PASS' if metrics.get('irr', 0) > 10 else '❌ FAIL'} (Requirement: > 10%)
- Demonstrates attractive return compared to alternative investments

**Debt Service Coverage Ratio (DSCR):** {metrics.get('dscr', 0):.2f}
- Status: {'✅ PASS' if metrics.get('dscr', 0) > 3.0 else '❌ FAIL'} (MSE-CDP Requirement: > 3:1)
- Indicates {'strong' if metrics.get('dscr', 0) > 3.0 else 'needs improvement in'} debt servicing capacity

**Break-even Point:** {metrics.get('breakeven_percentage', 0):.1f}%
- Status: {'✅ PASS' if metrics.get('breakeven_percentage', 0) < 60 else '❌ FAIL'} (MSE-CDP Requirement: < 60%)
- Project reaches break-even at {metrics.get('breakeven_percentage', 0):.1f}% capacity utilization

**Payback Period:** {metrics.get('payback_period_years', 0):.1f} years
- Investment will be recovered in {metrics.get('payback_period_years', 0):.1f} years

**MSE-CDP Compliance Status:** {compliance.get('status', 'UNKNOWN')}
"""

    system_prompt = """You are a financial analyst specializing in MSME project financing.
Generate professional content for the Financial Plan section of a DPR.
Use the provided financial data and metrics.
Explain financial viability clearly for both technical and non-technical readers.
Write in formal, professional tone."""

    user_prompt = f"""Generate content for Financial Plan section:

PROJECT COST: ₹{cost:,}

FUNDING STRUCTURE:
- Grant Amount: ₹{loan_details.get('grant_amount', 0):,.2f} ({loan_details.get('grant_percentage', 0):.0f}%)
- Loan Amount: ₹{loan_details.get('loan_amount', 0):,.2f}

FINANCIAL METRICS (already formatted above)

PROJECTIONS: {projections.get('duration_years', 10)}-year projections available

Generate content covering:
1. PROJECT COST BREAKDOWN - Detailed cost components
2. FUNDING STRUCTURE - Grant and loan details, terms
3. REVENUE PROJECTIONS - Expected income streams over time
4. DEBT SERVICE ANALYSIS - Loan repayment schedule and capacity
5. FINANCIAL FEASIBILITY ASSESSMENT - Overall viability conclusion

Write 4-5 paragraphs. Integrate the metrics provided. Be specific and data-driven.

NOTE: The financial metrics section is already formatted above, include it in your response."""

    sys_msg = SystemMessage(content=system_prompt)
    user_msg = HumanMessage(content=user_prompt)
    
    print("     🤖 [DEBUG] Invoking LLM for content generation...")
    response = llm.invoke([sys_msg, user_msg])
    content = response.content
    
    print("     ✅ [DEBUG] Financial Plan generated")
    
    # Combine LLM content with real metrics
    full_content = f"# FINANCIAL PLAN\n\n{content}\n\n{financial_metrics_text}"
    
    return full_content


# ============================================================================
# MAIN AGENT FUNCTION
# ============================================================================

def document_generator_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Document Generation Agent - Generates 3 DPR sections in Markdown format
    
    Sections generated:
    1. Executive Summary
    2. Organization Details
    3. Financial Plan
    
    Uses: Real data from state, Template + LLM approach
    Format: Markdown
    """
    print()
    cprint(f"{'NODE: document_generator_agent':-^80}", 'yellow', attrs=['bold'])
    
    project_data = state.get("project_data", {})
    dpr_sections = state.get("dpr_sections", {})
    financial_data = dpr_sections.get("financial", {})
    
    if not project_data:
        print("⚠️  No project data available for document generation")
        return state
    
    if not financial_data:
        print("⚠️  No financial data available for document generation")
        return state
    
    print(f"\n📄 Generating DPR sections for {project_data.get('cluster_type', 'project')}...")
    print(f"   Format: Markdown")
    print(f"   Method: Template + LLM")
    print(f"   Content: Real data\n")
    
    # Initialize LLM
    llm = ChatVertexAI(model_name=LLM_MODEL, temperature=0.3)
    
    print("🔄 Generating 3 sections:")
    print("="*50)
    
    # Generate Section 1: Executive Summary
    try:
        executive_summary = generate_executive_summary(project_data, financial_data, llm)
        state["dpr_sections"]["executive_summary"] = executive_summary
        print("  ✅ Executive Summary complete")
    except Exception as e:
        print(f"  ❌ Error generating Executive Summary: {e}")
        state["dpr_sections"]["executive_summary"] = "# EXECUTIVE SUMMARY\n\nError generating content."
    
    print()
    
    # Generate Section 2: Organization Details
    try:
        organization_details = generate_organization_details(project_data, llm)
        state["dpr_sections"]["organization_details"] = organization_details
        print("  ✅ Organization Details complete")
    except Exception as e:
        print(f"  ❌ Error generating Organization Details: {e}")
        state["dpr_sections"]["organization_details"] = "# ORGANIZATION DETAILS\n\nError generating content."
    
    print()
    
    # Generate Section 3: Financial Plan
    try:
        financial_plan = generate_financial_plan(project_data, financial_data, llm)
        state["dpr_sections"]["financial_plan"] = financial_plan
        print("  ✅ Financial Plan complete")
    except Exception as e:
        print(f"  ❌ Error generating Financial Plan: {e}")
        state["dpr_sections"]["financial_plan"] = "# FINANCIAL PLAN\n\nError generating content."
    
    print("="*50)
    print()
    
    # Summary
    sections_generated = len([k for k in ["executive_summary", "organization_details", "financial_plan"] 
                              if k in state["dpr_sections"]])
    
    print(f"✅ Document generation complete")
    print(f"   Sections generated: {sections_generated}/3")
    print(f"   Storage: state['dpr_sections'][section_name]")
    print(f"   Format: Markdown")
    print()
    
    return state