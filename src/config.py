# config.py
"""
Configuration file for DPR Automation Platform
"""

# LLM Model Configuration
LLM_MODEL = "gemini-2.0-flash-exp"

# Application Settings
APP_NAME = "DPR Automation Platform"
VERSION = "0.1.0"

# DPR Sections (MSE-CDP Compliant - 21 Sections)
DPR_SECTIONS = [
    "executive_summary",
    "organization_details",
    "cluster_profile",
    "market_analysis",
    "technical_feasibility",
    "financial_projections",
    "implementation_timeline",
    "compliance_checklist",
    "risk_analysis",
    "sustainability_plan",
    # Add remaining sections as we build agents
]

# Agent Configuration
AGENT_TIMEOUT = 300  # seconds
MAX_RETRIES = 3
