# document_generator.py
"""
Document Generation Agent - Stage 6
Generates DPR sections in Markdown format using real collected data

Sections generated (Phase 3 - 13 sections total):
Stage 4 (3 sections):
1. Executive Summary
2. Organization Details
3. Financial Plan

Stage 5 (5 sections):
4. Project Introduction & Background
5. Cluster Profile Analysis
6. Technical Feasibility Study
7. Market Analysis & Demand Assessment
8. Implementation Schedule & Timeline

Stage 6 (5 NEW sections):
9. Management & Organizational Structure
10. Economic & Commercial Viability
11. SWOT Analysis
12. Risk Analysis & Mitigation
13. Environmental & Social Impact Assessment

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
# STAGE 5: NEW SECTION TEMPLATES
# ============================================================================

def get_project_introduction_template() -> str:
    """
    Template for Project Introduction & Background section
    """
    template = """# PROJECT INTRODUCTION & BACKGROUND

## Project Genesis
{project_genesis}

## Problem Statement
{problem_statement}

## Project Objectives
{project_objectives}

## Expected Outcomes
{expected_outcomes}

## Project Scope
{project_scope}
"""
    return template


def get_cluster_profile_template() -> str:
    """
    Template for Cluster Profile Analysis section
    """
    template = """# CLUSTER PROFILE ANALYSIS

## Cluster Overview
{cluster_overview}

## Industry Characteristics
{industry_characteristics}

## Current Challenges
{current_challenges}

## Competitive Advantages
{competitive_advantages}

## Growth Potential
{growth_potential}
"""
    return template


def get_technical_feasibility_template() -> str:
    """
    Template for Technical Feasibility Study section
    """
    template = """# TECHNICAL FEASIBILITY STUDY

## Technology Overview
{technology_overview}

## Equipment & Machinery
{equipment_machinery}

## Production Process
{production_process}

## Capacity Analysis
{capacity_analysis}

## Technical Specifications
{technical_specifications}

## Technology Transfer & Training
{technology_training}
"""
    return template


def get_market_analysis_template() -> str:
    """
    Template for Market Analysis & Demand Assessment section
    """
    template = """# MARKET ANALYSIS & DEMAND ASSESSMENT

## Market Size & Trends
{market_size_trends}

## Target Market Segments
{target_segments}

## Competition Analysis
{competition_analysis}

## Demand Projections
{demand_projections}

## Market Entry Strategy
{market_entry}
"""
    return template


def get_implementation_schedule_template() -> str:
    """
    Template for Implementation Schedule & Timeline section
    """
    template = """# IMPLEMENTATION SCHEDULE & TIMELINE

## Project Phases
{project_phases}

## Timeline & Milestones
{timeline_milestones}

## Critical Path Activities
{critical_path}

## Resource Deployment Plan
{resource_deployment}

## Monitoring Checkpoints
{monitoring_checkpoints}
"""
    return template


# ============================================================================
# STAGE 6: NEW SECTION TEMPLATES
# ============================================================================

def get_management_structure_template() -> str:
    """
    Template for Management & Organizational Structure section
    """
    template = """# MANAGEMENT & ORGANIZATIONAL STRUCTURE

## Organizational Framework
{organizational_framework}

## Management Team
{management_team}

## Roles & Responsibilities
{roles_responsibilities}

## Governance Structure
{governance_structure}

## Decision-Making Process
{decision_making}
"""
    return template


def get_economic_viability_template() -> str:
    """
    Template for Economic & Commercial Viability section
    """
    template = """# ECONOMIC & COMMERCIAL VIABILITY

## Economic Impact Analysis
{economic_impact}

## Commercial Feasibility
{commercial_feasibility}

## Cost-Benefit Analysis
{cost_benefit}

## Revenue Model
{revenue_model}

## Sustainability Assessment
{sustainability_assessment}
"""
    return template


def get_swot_analysis_template() -> str:
    """
    Template for SWOT Analysis section
    """
    template = """# SWOT ANALYSIS

## Strengths
{strengths}

## Weaknesses
{weaknesses}

## Opportunities
{opportunities}

## Threats
{threats}

## Strategic Implications
{strategic_implications}
"""
    return template


def get_risk_analysis_template() -> str:
    """
    Template for Risk Analysis & Mitigation section
    """
    template = """# RISK ANALYSIS & MITIGATION

## Risk Identification
{risk_identification}

## Risk Assessment
{risk_assessment}

## Mitigation Strategies
{mitigation_strategies}

## Contingency Plans
{contingency_plans}

## Risk Monitoring
{risk_monitoring}
"""
    return template


def get_environmental_impact_template() -> str:
    """
    Template for Environmental & Social Impact Assessment section
    """
    template = """# ENVIRONMENTAL & SOCIAL IMPACT ASSESSMENT

## Environmental Impact
{environmental_impact}

## Social Impact
{social_impact}

## Sustainability Measures
{sustainability_measures}

## Compliance Requirements
{compliance_requirements}

## CSR Initiatives
{csr_initiatives}
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
# STAGE 5: NEW CONTENT GENERATORS
# ============================================================================

def generate_project_introduction(project_data: Dict, llm) -> str:
    """
    Generate Project Introduction & Background using Template + LLM
    """
    print("  📝 Generating: Project Introduction & Background")
    print("     🔧 [DEBUG] Using Template + LLM approach")
    
    cluster_type = project_data.get("cluster_type", "N/A")
    location = project_data.get("location", "N/A")
    members = project_data.get("members", 0)
    facility_type = project_data.get("facility_type", "N/A")
    cost = project_data.get("project_cost", 0)
    
    system_prompt = """You are a professional DPR writer specializing in MSME cluster development.
Generate clear, compelling content for the Project Introduction & Background section.
Focus on the rationale, context, and strategic importance of the project.
Write in formal business language suitable for government submissions."""

    user_prompt = f"""Generate content for Project Introduction & Background section:

PROJECT DATA:
- Cluster Type: {cluster_type}
- Location: {location}
- Members: {members} units
- Facility Type: {facility_type}
- Project Cost: ₹{cost:,}

Generate detailed content covering:
1. PROJECT GENESIS - How the project idea originated, stakeholder consultations
2. PROBLEM STATEMENT - Current challenges faced by cluster members
3. PROJECT OBJECTIVES - Clear, measurable objectives for the CFC
4. EXPECTED OUTCOMES - Tangible benefits and impact expected
5. PROJECT SCOPE - Boundaries and coverage of the project

Write 5-6 comprehensive paragraphs. Be specific and strategic."""

    sys_msg = SystemMessage(content=system_prompt)
    user_msg = HumanMessage(content=user_prompt)
    
    print("     🤖 [DEBUG] Invoking LLM for content generation...")
    response = llm.invoke([sys_msg, user_msg])
    content = response.content
    
    print("     ✅ [DEBUG] Project Introduction & Background generated")
    
    return f"# PROJECT INTRODUCTION & BACKGROUND\n\n{content}"


def generate_cluster_profile(project_data: Dict, llm) -> str:
    """
    Generate Cluster Profile Analysis using Template + LLM
    """
    print("  📝 Generating: Cluster Profile Analysis")
    print("     🔧 [DEBUG] Using Template + LLM approach")
    
    cluster_type = project_data.get("cluster_type", "N/A")
    location = project_data.get("location", "N/A")
    members = project_data.get("members", 0)
    
    system_prompt = """You are an industry analyst specializing in MSME clusters.
Generate detailed, analytical content for the Cluster Profile Analysis section.
Include industry-specific insights and competitive dynamics.
Write professionally with data-driven insights."""

    user_prompt = f"""Generate content for Cluster Profile Analysis:

CLUSTER DATA:
- Type: {cluster_type}
- Location: {location}
- Number of Units: {members}

Generate comprehensive analysis covering:
1. CLUSTER OVERVIEW - History, evolution, current state
2. INDUSTRY CHARACTERISTICS - Specific to {cluster_type}
3. CURRENT CHALLENGES - Infrastructure gaps, technology limitations, market access issues
4. COMPETITIVE ADVANTAGES - Unique strengths of this cluster
5. GROWTH POTENTIAL - Future opportunities and expansion possibilities

Write 5-6 detailed paragraphs with industry-specific insights."""

    sys_msg = SystemMessage(content=system_prompt)
    user_msg = HumanMessage(content=user_prompt)
    
    print("     🤖 [DEBUG] Invoking LLM for content generation...")
    response = llm.invoke([sys_msg, user_msg])
    content = response.content
    
    print("     ✅ [DEBUG] Cluster Profile Analysis generated")
    
    return f"# CLUSTER PROFILE ANALYSIS\n\n{content}"


def generate_technical_feasibility(project_data: Dict, llm) -> str:
    """
    Generate Technical Feasibility Study using Template + LLM
    """
    print("  📝 Generating: Technical Feasibility Study")
    print("     🔧 [DEBUG] Using Template + LLM approach")
    
    cluster_type = project_data.get("cluster_type", "N/A")
    facility_type = project_data.get("facility_type", "N/A")
    members = project_data.get("members", 0)
    
    system_prompt = """You are a technical consultant specializing in manufacturing and production facilities.
Generate detailed technical content for the Technical Feasibility Study section.
Include specific equipment, processes, and technical specifications.
Write with technical accuracy and practical implementation focus."""

    user_prompt = f"""Generate content for Technical Feasibility Study:

PROJECT DATA:
- Cluster Type: {cluster_type}
- Facility Type: {facility_type}
- Serving: {members} member units

Generate technical analysis covering:
1. TECHNOLOGY OVERVIEW - Modern technologies suitable for {facility_type}
2. EQUIPMENT & MACHINERY - Specific equipment required, specifications
3. PRODUCTION PROCESS - Step-by-step workflow and operations
4. CAPACITY ANALYSIS - Production capacity, utilization projections
5. TECHNICAL SPECIFICATIONS - Quality standards, technical parameters
6. TECHNOLOGY TRANSFER & TRAINING - Training needs and skill development

Write 6-7 paragraphs with specific technical details."""

    sys_msg = SystemMessage(content=system_prompt)
    user_msg = HumanMessage(content=user_prompt)
    
    print("     🤖 [DEBUG] Invoking LLM for content generation...")
    response = llm.invoke([sys_msg, user_msg])
    content = response.content
    
    print("     ✅ [DEBUG] Technical Feasibility Study generated")
    
    return f"# TECHNICAL FEASIBILITY STUDY\n\n{content}"


def generate_market_analysis(project_data: Dict, llm) -> str:
    """
    Generate Market Analysis & Demand Assessment using Template + LLM
    """
    print("  📝 Generating: Market Analysis & Demand Assessment")
    print("     🔧 [DEBUG] Using Template + LLM approach")
    
    cluster_type = project_data.get("cluster_type", "N/A")
    location = project_data.get("location", "N/A")
    members = project_data.get("members", 0)
    
    system_prompt = """You are a market research analyst specializing in MSME sectors.
Generate comprehensive market analysis for the Market Analysis & Demand Assessment section.
Include market sizing, trends, competition, and demand projections.
Use data-driven language with market insights."""

    user_prompt = f"""Generate content for Market Analysis & Demand Assessment:

PROJECT DATA:
- Industry: {cluster_type}
- Location: {location}
- Cluster Size: {members} units

Generate market analysis covering:
1. MARKET SIZE & TRENDS - Current market size, growth trends, drivers
2. TARGET MARKET SEGMENTS - B2B/B2C segments, customer profiles
3. COMPETITION ANALYSIS - Key competitors, market positioning
4. DEMAND PROJECTIONS - 5-10 year demand forecast with assumptions
5. MARKET ENTRY STRATEGY - How cluster will access and grow market share

Write 5-6 paragraphs with market data and strategic insights."""

    sys_msg = SystemMessage(content=system_prompt)
    user_msg = HumanMessage(content=user_prompt)
    
    print("     🤖 [DEBUG] Invoking LLM for content generation...")
    response = llm.invoke([sys_msg, user_msg])
    content = response.content
    
    print("     ✅ [DEBUG] Market Analysis & Demand Assessment generated")
    
    return f"# MARKET ANALYSIS & DEMAND ASSESSMENT\n\n{content}"


def generate_implementation_schedule(project_data: Dict, llm) -> str:
    """
    Generate Implementation Schedule & Timeline using Template + LLM
    """
    print("  📝 Generating: Implementation Schedule & Timeline")
    print("     🔧 [DEBUG] Using Template + LLM approach")
    
    cost = project_data.get("project_cost", 0)
    facility_type = project_data.get("facility_type", "N/A")
    
    system_prompt = """You are a project management consultant specializing in infrastructure projects.
Generate detailed implementation schedule for the Implementation Schedule & Timeline section.
Include realistic timelines, milestones, and critical path activities.
Write with project management rigor and practical implementation focus."""

    user_prompt = f"""Generate content for Implementation Schedule & Timeline:

PROJECT DATA:
- Facility: {facility_type}
- Budget: ₹{cost:,}

Generate implementation plan covering:
1. PROJECT PHASES - Pre-implementation, construction, commissioning, operations
2. TIMELINE & MILESTONES - Month-by-month schedule with key milestones
3. CRITICAL PATH ACTIVITIES - Dependencies and critical activities
4. RESOURCE DEPLOYMENT PLAN - When resources (funds, equipment, people) deploy
5. MONITORING CHECKPOINTS - Review points and progress tracking

Include a realistic 12-18 month implementation timeline. Write 5-6 detailed paragraphs."""

    sys_msg = SystemMessage(content=system_prompt)
    user_msg = HumanMessage(content=user_prompt)
    
    print("     🤖 [DEBUG] Invoking LLM for content generation...")
    response = llm.invoke([sys_msg, user_msg])
    content = response.content
    
    print("     ✅ [DEBUG] Implementation Schedule & Timeline generated")
    
    return f"# IMPLEMENTATION SCHEDULE & TIMELINE\n\n{content}"


# ============================================================================
# STAGE 6: NEW CONTENT GENERATORS
# ============================================================================

def generate_management_structure(project_data: Dict, llm) -> str:
    """
    Generate Management & Organizational Structure using Template + LLM
    """
    print("  📝 Generating: Management & Organizational Structure")
    print("     🔧 [DEBUG] Using Template + LLM approach")
    
    cluster_type = project_data.get("cluster_type", "N/A")
    members = project_data.get("members", 0)
    location = project_data.get("location", "N/A")
    
    system_prompt = """You are an organizational development consultant specializing in MSME clusters.
Generate detailed content for the Management & Organizational Structure section.
Include governance models, management hierarchy, and decision-making processes.
Write professionally with focus on practical implementation."""

    user_prompt = f"""Generate content for Management & Organizational Structure:

PROJECT DATA:
- Cluster Type: {cluster_type}
- Number of Members: {members} units
- Location: {location}

Generate organizational structure covering:
1. ORGANIZATIONAL FRAMEWORK - SPV/Trust structure, legal entity
2. MANAGEMENT TEAM - Board composition, management positions, qualifications
3. ROLES & RESPONSIBILITIES - Clear role definitions for each position
4. GOVERNANCE STRUCTURE - Decision-making authority, reporting lines
5. DECISION-MAKING PROCESS - Consensus mechanisms, voting procedures

Write 5-6 detailed paragraphs with practical governance details."""

    sys_msg = SystemMessage(content=system_prompt)
    user_msg = HumanMessage(content=user_prompt)
    
    print("     🤖 [DEBUG] Invoking LLM for content generation...")
    response = llm.invoke([sys_msg, user_msg])
    content = response.content
    
    print("     ✅ [DEBUG] Management & Organizational Structure generated")
    
    return f"# MANAGEMENT & ORGANIZATIONAL STRUCTURE\n\n{content}"


def generate_economic_viability(project_data: Dict, financial_data: Dict, llm) -> str:
    """
    Generate Economic & Commercial Viability using Template + LLM
    """
    print("  📝 Generating: Economic & Commercial Viability")
    print("     🔧 [DEBUG] Using Template + LLM approach")
    
    cluster_type = project_data.get("cluster_type", "N/A")
    cost = project_data.get("project_cost", 0)
    members = project_data.get("members", 0)
    
    # Get financial metrics
    npv = financial_data.get("npv", 0)
    irr = financial_data.get("irr", 0)
    payback = financial_data.get("payback_period", 0)
    
    system_prompt = """You are a financial analyst specializing in MSME projects.
Generate comprehensive content for the Economic & Commercial Viability section.
Include economic impact, commercial feasibility, and sustainability analysis.
Use data-driven language with financial insights."""

    user_prompt = f"""Generate content for Economic & Commercial Viability:

PROJECT DATA:
- Industry: {cluster_type}
- Investment: ₹{cost:,}
- Member Units: {members}
- NPV: ₹{npv:,.2f}
- IRR: {irr}%
- Payback Period: {payback} years

Generate viability analysis covering:
1. ECONOMIC IMPACT ANALYSIS - Job creation, GDP contribution, multiplier effects
2. COMMERCIAL FEASIBILITY - Revenue potential, market demand validation
3. COST-BENEFIT ANALYSIS - Using NPV, IRR, and other metrics provided
4. REVENUE MODEL - Income streams, pricing strategy, sustainability
5. SUSTAINABILITY ASSESSMENT - Long-term viability, scalability

Write 5-6 paragraphs using the financial metrics provided."""

    sys_msg = SystemMessage(content=system_prompt)
    user_msg = HumanMessage(content=user_prompt)
    
    print("     🤖 [DEBUG] Invoking LLM for content generation...")
    response = llm.invoke([sys_msg, user_msg])
    content = response.content
    
    print("     ✅ [DEBUG] Economic & Commercial Viability generated")
    
    return f"# ECONOMIC & COMMERCIAL VIABILITY\n\n{content}"


def generate_swot_analysis(project_data: Dict, llm) -> str:
    """
    Generate SWOT Analysis using Template + LLM
    """
    print("  📝 Generating: SWOT Analysis")
    print("     🔧 [DEBUG] Using Template + LLM approach")
    
    cluster_type = project_data.get("cluster_type", "N/A")
    location = project_data.get("location", "N/A")
    members = project_data.get("members", 0)
    facility_type = project_data.get("facility_type", "N/A")
    
    system_prompt = """You are a strategic planning consultant specializing in MSME clusters.
Generate comprehensive SWOT Analysis for the project.
Be specific, realistic, and strategic in identifying factors.
Write in clear, business-focused language."""

    user_prompt = f"""Generate SWOT Analysis content:

PROJECT DATA:
- Cluster Type: {cluster_type}
- Location: {location}
- Members: {members} units
- Facility: {facility_type}

Generate detailed SWOT covering:
1. STRENGTHS - Internal advantages (skilled workforce, established cluster, location, etc.)
2. WEAKNESSES - Internal limitations (technology gaps, infrastructure, capital constraints)
3. OPPORTUNITIES - External favorable factors (market growth, government schemes, exports)
4. THREATS - External challenges (competition, policy changes, economic factors)
5. STRATEGIC IMPLICATIONS - How to leverage S, overcome W, exploit O, mitigate T

Write 5-6 detailed paragraphs with specific, actionable insights."""

    sys_msg = SystemMessage(content=system_prompt)
    user_msg = HumanMessage(content=user_prompt)
    
    print("     🤖 [DEBUG] Invoking LLM for content generation...")
    response = llm.invoke([sys_msg, user_msg])
    content = response.content
    
    print("     ✅ [DEBUG] SWOT Analysis generated")
    
    return f"# SWOT ANALYSIS\n\n{content}"


def generate_risk_analysis(project_data: Dict, llm) -> str:
    """
    Generate Risk Analysis & Mitigation using Template + LLM
    """
    print("  📝 Generating: Risk Analysis & Mitigation")
    print("     🔧 [DEBUG] Using Template + LLM approach")
    
    cluster_type = project_data.get("cluster_type", "N/A")
    cost = project_data.get("project_cost", 0)
    facility_type = project_data.get("facility_type", "N/A")
    
    system_prompt = """You are a risk management consultant specializing in manufacturing and MSME projects.
Generate comprehensive Risk Analysis & Mitigation strategies.
Identify specific risks and provide actionable mitigation plans.
Write with practical risk management focus."""

    user_prompt = f"""Generate content for Risk Analysis & Mitigation:

PROJECT DATA:
- Industry: {cluster_type}
- Facility: {facility_type}
- Investment: ₹{cost:,}

Generate risk analysis covering:
1. RISK IDENTIFICATION - Technical, financial, market, operational, regulatory risks
2. RISK ASSESSMENT - Probability and impact assessment for each risk
3. MITIGATION STRATEGIES - Specific actions to reduce/prevent each risk
4. CONTINGENCY PLANS - Backup plans if risks materialize
5. RISK MONITORING - How to track and review risks ongoing

Write 5-6 detailed paragraphs with specific risks and mitigation strategies."""

    sys_msg = SystemMessage(content=system_prompt)
    user_msg = HumanMessage(content=user_prompt)
    
    print("     🤖 [DEBUG] Invoking LLM for content generation...")
    response = llm.invoke([sys_msg, user_msg])
    content = response.content
    
    print("     ✅ [DEBUG] Risk Analysis & Mitigation generated")
    
    return f"# RISK ANALYSIS & MITIGATION\n\n{content}"


def generate_environmental_impact(project_data: Dict, llm) -> str:
    """
    Generate Environmental & Social Impact Assessment using Template + LLM
    """
    print("  📝 Generating: Environmental & Social Impact Assessment")
    print("     🔧 [DEBUG] Using Template + LLM approach")
    
    cluster_type = project_data.get("cluster_type", "N/A")
    location = project_data.get("location", "N/A")
    facility_type = project_data.get("facility_type", "N/A")
    members = project_data.get("members", 0)
    
    system_prompt = """You are a sustainability consultant specializing in environmental and social impact.
Generate comprehensive Environmental & Social Impact Assessment.
Include compliance, sustainability measures, and CSR initiatives.
Write with focus on responsible and sustainable operations."""

    user_prompt = f"""Generate content for Environmental & Social Impact Assessment:

PROJECT DATA:
- Industry: {cluster_type}
- Location: {location}
- Facility: {facility_type}
- Serving: {members} units

Generate impact assessment covering:
1. ENVIRONMENTAL IMPACT - Emissions, waste management, resource usage, carbon footprint
2. SOCIAL IMPACT - Employment generation, skill development, community benefits
3. SUSTAINABILITY MEASURES - Green technologies, renewable energy, waste recycling
4. COMPLIANCE REQUIREMENTS - Environmental clearances, pollution norms, regulations
5. CSR INITIATIVES - Community development, education, health programs

Write 5-6 detailed paragraphs with specific environmental and social considerations."""

    sys_msg = SystemMessage(content=system_prompt)
    user_msg = HumanMessage(content=user_prompt)
    
    print("     🤖 [DEBUG] Invoking LLM for content generation...")
    response = llm.invoke([sys_msg, user_msg])
    content = response.content
    
    print("     ✅ [DEBUG] Environmental & Social Impact Assessment generated")
    
    return f"# ENVIRONMENTAL & SOCIAL IMPACT ASSESSMENT\n\n{content}"


# ============================================================================
# MAIN AGENT FUNCTION
# ============================================================================

def document_generator_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Document Generation Agent - Generates 13 DPR sections in Markdown format
    
    Stage 4 (3 sections):
    1. Executive Summary
    2. Organization Details
    3. Financial Plan
    
    Stage 5 (5 sections):
    4. Project Introduction & Background
    5. Cluster Profile Analysis
    6. Technical Feasibility Study
    7. Market Analysis & Demand Assessment
    8. Implementation Schedule & Timeline
    
    Stage 6 (5 NEW sections):
    9. Management & Organizational Structure
    10. Economic & Commercial Viability
    11. SWOT Analysis
    12. Risk Analysis & Mitigation
    13. Environmental & Social Impact Assessment
    
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
    print(f"   Content: Real data")
    print(f"   Stage: 6 (13 sections total)\n")
    
    # Initialize LLM
    llm = ChatVertexAI(model_name=LLM_MODEL, temperature=0.3)
    
    print("🔄 Generating 13 sections:")
    print("="*50)
    
    # ========================================================================
    # STAGE 4 SECTIONS
    # ========================================================================
    
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
    
    print()
    
    # ========================================================================
    # STAGE 5 SECTIONS
    # ========================================================================
    
    # Generate Section 4: Project Introduction & Background
    try:
        project_intro = generate_project_introduction(project_data, llm)
        state["dpr_sections"]["project_introduction"] = project_intro
        print("  ✅ Project Introduction & Background complete")
    except Exception as e:
        print(f"  ❌ Error generating Project Introduction: {e}")
        state["dpr_sections"]["project_introduction"] = "# PROJECT INTRODUCTION & BACKGROUND\n\nError generating content."
    
    print()
    
    # Generate Section 5: Cluster Profile Analysis
    try:
        cluster_profile = generate_cluster_profile(project_data, llm)
        state["dpr_sections"]["cluster_profile"] = cluster_profile
        print("  ✅ Cluster Profile Analysis complete")
    except Exception as e:
        print(f"  ❌ Error generating Cluster Profile: {e}")
        state["dpr_sections"]["cluster_profile"] = "# CLUSTER PROFILE ANALYSIS\n\nError generating content."
    
    print()
    
    # Generate Section 6: Technical Feasibility Study
    try:
        technical_feasibility = generate_technical_feasibility(project_data, llm)
        state["dpr_sections"]["technical_feasibility"] = technical_feasibility
        print("  ✅ Technical Feasibility Study complete")
    except Exception as e:
        print(f"  ❌ Error generating Technical Feasibility: {e}")
        state["dpr_sections"]["technical_feasibility"] = "# TECHNICAL FEASIBILITY STUDY\n\nError generating content."
    
    print()
    
    # Generate Section 7: Market Analysis & Demand Assessment
    try:
        market_analysis = generate_market_analysis(project_data, llm)
        state["dpr_sections"]["market_analysis"] = market_analysis
        print("  ✅ Market Analysis & Demand Assessment complete")
    except Exception as e:
        print(f"  ❌ Error generating Market Analysis: {e}")
        state["dpr_sections"]["market_analysis"] = "# MARKET ANALYSIS & DEMAND ASSESSMENT\n\nError generating content."
    
    print()
    
    # Generate Section 8: Implementation Schedule & Timeline
    try:
        implementation_schedule = generate_implementation_schedule(project_data, llm)
        state["dpr_sections"]["implementation_schedule"] = implementation_schedule
        print("  ✅ Implementation Schedule & Timeline complete")
    except Exception as e:
        print(f"  ❌ Error generating Implementation Schedule: {e}")
        state["dpr_sections"]["implementation_schedule"] = "# IMPLEMENTATION SCHEDULE & TIMELINE\n\nError generating content."
    
    print()
    
    # ========================================================================
    # STAGE 6 SECTIONS (NEW - 5 sections)
    # ========================================================================
    
    # Generate Section 9: Management & Organizational Structure
    try:
        management_structure = generate_management_structure(project_data, llm)
        state["dpr_sections"]["management_structure"] = management_structure
        print("  ✅ Management & Organizational Structure complete")
    except Exception as e:
        print(f"  ❌ Error generating Management Structure: {e}")
        state["dpr_sections"]["management_structure"] = "# MANAGEMENT & ORGANIZATIONAL STRUCTURE\n\nError generating content."
    
    print()
    
    # Generate Section 10: Economic & Commercial Viability
    try:
        economic_viability = generate_economic_viability(project_data, financial_data, llm)
        state["dpr_sections"]["economic_viability"] = economic_viability
        print("  ✅ Economic & Commercial Viability complete")
    except Exception as e:
        print(f"  ❌ Error generating Economic Viability: {e}")
        state["dpr_sections"]["economic_viability"] = "# ECONOMIC & COMMERCIAL VIABILITY\n\nError generating content."
    
    print()
    
    # Generate Section 11: SWOT Analysis
    try:
        swot_analysis = generate_swot_analysis(project_data, llm)
        state["dpr_sections"]["swot_analysis"] = swot_analysis
        print("  ✅ SWOT Analysis complete")
    except Exception as e:
        print(f"  ❌ Error generating SWOT Analysis: {e}")
        state["dpr_sections"]["swot_analysis"] = "# SWOT ANALYSIS\n\nError generating content."
    
    print()
    
    # Generate Section 12: Risk Analysis & Mitigation
    try:
        risk_analysis = generate_risk_analysis(project_data, llm)
        state["dpr_sections"]["risk_analysis"] = risk_analysis
        print("  ✅ Risk Analysis & Mitigation complete")
    except Exception as e:
        print(f"  ❌ Error generating Risk Analysis: {e}")
        state["dpr_sections"]["risk_analysis"] = "# RISK ANALYSIS & MITIGATION\n\nError generating content."
    
    print()
    
    # Generate Section 13: Environmental & Social Impact Assessment
    try:
        environmental_impact = generate_environmental_impact(project_data, llm)
        state["dpr_sections"]["environmental_impact"] = environmental_impact
        print("  ✅ Environmental & Social Impact Assessment complete")
    except Exception as e:
        print(f"  ❌ Error generating Environmental Impact: {e}")
        state["dpr_sections"]["environmental_impact"] = "# ENVIRONMENTAL & SOCIAL IMPACT ASSESSMENT\n\nError generating content."
    
    print("="*50)
    print()
    
    # Summary
    section_keys = [
        "executive_summary", "organization_details", "financial_plan",
        "project_introduction", "cluster_profile", "technical_feasibility",
        "market_analysis", "implementation_schedule",
        "management_structure", "economic_viability", "swot_analysis",
        "risk_analysis", "environmental_impact"
    ]
    sections_generated = len([k for k in section_keys if k in state["dpr_sections"]])
    
    print(f"✅ Document generation complete")
    print(f"   Sections generated: {sections_generated}/13 (Stage 6)")
    print(f"   Progress: {sections_generated}/21 total MSE-CDP sections ({round(sections_generated/21*100, 1)}%)")
    print(f"   Storage: state['dpr_sections'][section_name]")
    print(f"   Format: Markdown")
    print()
    
    return state