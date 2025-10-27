# financial_agent.py
"""
Financial Modeling Agent - Stage 3
Calculates financial metrics and generates projections for DPR

NOTE: Currently uses SIMULATED/DUMMY calculations for development.
      Actual financial formulas to be implemented in future iteration.
"""
import json
from typing import Dict, Any
from termcolor import cprint

from config import LLM_MODEL


# ============================================================================
# ⚠️  DUMMY CALCULATION SECTION - TO BE REPLACED WITH ACTUAL FORMULAS
# ============================================================================

def calculate_npv_dummy(project_cost: float, loan_amount: float, years: int = 10) -> float:
    """
    ⚠️  DUMMY NPV CALCULATION - SIMULATED VALUES ONLY
    
    TODO: Replace with actual NPV formula:
          NPV = Σ(Cash Flow / (1 + discount_rate)^t) - Initial Investment
    
    Args:
        project_cost: Total project cost
        loan_amount: Loan amount
        years: Project duration
        
    Returns:
        Simulated NPV value
    """
    print("    🔧 [DEBUG] Using DUMMY NPV calculation")
    
    # SIMULATED: Just return a positive value for now
    # Real calculation would use discounted cash flows
    dummy_npv = project_cost * 0.35  # Simulated 35% return
    
    print(f"    🔧 [DEBUG] DUMMY NPV = {dummy_npv:,.2f} (simulated)")
    return dummy_npv


def calculate_irr_dummy(project_cost: float, annual_profit: float, years: int = 10) -> float:
    """
    ⚠️  DUMMY IRR CALCULATION - SIMULATED VALUES ONLY
    
    TODO: Replace with actual IRR formula:
          IRR is the discount rate where NPV = 0
          Requires iterative calculation (Newton-Raphson method)
    
    Args:
        project_cost: Total project cost
        annual_profit: Estimated annual profit
        years: Project duration
        
    Returns:
        Simulated IRR percentage
    """
    print("    🔧 [DEBUG] Using DUMMY IRR calculation")
    
    # SIMULATED: Just return a value > 10% for now
    # Real calculation would solve for rate where NPV = 0
    dummy_irr = 15.5  # Simulated 15.5% return
    
    print(f"    🔧 [DEBUG] DUMMY IRR = {dummy_irr}% (simulated)")
    return dummy_irr


def calculate_dscr_dummy(annual_profit: float, loan_emi: float) -> float:
    """
    ⚠️  DUMMY DSCR CALCULATION - USES PYTHON FORMULA BUT SIMULATED INPUTS
    
    DSCR Formula (ACTUAL PYTHON CALCULATION):
    DSCR = Net Operating Income / Total Debt Service
    
    MSE-CDP Requirement: DSCR must be > 3:1 (i.e., > 3.0)
    
    Args:
        annual_profit: Annual profit (simulated for now)
        loan_emi: Annual loan payment (simulated for now)
        
    Returns:
        DSCR value calculated using Python formula
    """
    print("    🔧 [DEBUG] Using PYTHON formula for DSCR (but with simulated inputs)")
    
    # ✅ THIS USES ACTUAL PYTHON FORMULA
    # Input values are simulated, but calculation is real
    if loan_emi == 0:
        dscr = 999.0  # No loan = infinite DSCR
    else:
        dscr = annual_profit / loan_emi  # Real formula
    
    print(f"    🔧 [DEBUG] DSCR = {dscr:.2f} (Python calculation with simulated inputs)")
    return dscr


def calculate_breakeven_dummy(fixed_costs: float, revenue: float, variable_costs: float) -> float:
    """
    ⚠️  DUMMY BREAK-EVEN CALCULATION - USES PYTHON FORMULA BUT SIMULATED INPUTS
    
    Break-even Formula (ACTUAL PYTHON CALCULATION):
    Break-even % = (Fixed Costs / (Revenue - Variable Costs)) * 100
    
    MSE-CDP Requirement: Break-even must be < 60%
    
    Args:
        fixed_costs: Annual fixed costs (simulated)
        revenue: Annual revenue (simulated)
        variable_costs: Annual variable costs (simulated)
        
    Returns:
        Break-even percentage calculated using Python formula
    """
    print("    🔧 [DEBUG] Using PYTHON formula for Break-even (but with simulated inputs)")
    
    # ✅ THIS USES ACTUAL PYTHON FORMULA
    contribution = revenue - variable_costs
    if contribution == 0:
        breakeven = 100.0
    else:
        breakeven = (fixed_costs / contribution) * 100  # Real formula
    
    print(f"    🔧 [DEBUG] Break-even = {breakeven:.1f}% (Python calculation with simulated inputs)")
    return breakeven


def calculate_payback_period_dummy(project_cost: float, annual_cashflow: float) -> float:
    """
    ⚠️  DUMMY PAYBACK PERIOD - USES PYTHON FORMULA BUT SIMULATED INPUTS
    
    Payback Period Formula (ACTUAL PYTHON CALCULATION):
    Payback = Initial Investment / Annual Cash Flow
    
    Args:
        project_cost: Total investment (real from user data)
        annual_cashflow: Annual cash flow (simulated for now)
        
    Returns:
        Payback period in years (Python calculation)
    """
    print("    🔧 [DEBUG] Using PYTHON formula for Payback Period (but with simulated cashflow)")
    
    # ✅ THIS USES ACTUAL PYTHON FORMULA
    if annual_cashflow == 0:
        payback = 999.0
    else:
        payback = project_cost / annual_cashflow  # Real formula
    
    print(f"    🔧 [DEBUG] Payback Period = {payback:.1f} years (Python calculation)")
    return payback


# ============================================================================
# ⚠️  SIMPLIFIED PROJECTIONS - TO BE ENHANCED WITH DETAILED CALCULATIONS
# ============================================================================

def generate_simplified_projections(project_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    ⚠️  SIMPLIFIED 10-YEAR PROJECTIONS - BASIC SIMULATION ONLY
    
    TODO: Replace with detailed projections including:
          - Capacity utilization ramp-up
          - Industry-specific revenue per unit
          - Detailed operating cost breakdown
          - Working capital requirements
          - Depreciation schedules
    
    Args:
        project_data: Collected project information
        
    Returns:
        Simplified financial projections
    """
    print("    🔧 [DEBUG] Generating SIMPLIFIED projections (to be enhanced)")
    
    project_cost = project_data.get("project_cost", 82000000)
    members = project_data.get("members", 50)
    
    # SIMULATED: Simple linear growth model
    # Real version would use industry benchmarks and capacity curves
    projections = {
        "currency": "INR",
        "duration_years": 10,
        "yearly_summary": []
    }
    
    base_revenue = project_cost * 0.20  # Simulated: 20% of investment
    
    for year in range(1, 11):
        # Simple growth: 10% per year (SIMULATED)
        revenue = base_revenue * (1 + 0.10 * year)
        operating_cost = revenue * 0.65  # Simulated: 65% operating costs
        profit = revenue - operating_cost
        
        projections["yearly_summary"].append({
            "year": year,
            "revenue": round(revenue, 2),
            "operating_cost": round(operating_cost, 2),
            "profit": round(profit, 2)
        })
    
    print(f"    🔧 [DEBUG] Generated {len(projections['yearly_summary'])} years of SIMPLIFIED projections")
    return projections


# ============================================================================
# MAIN AGENT FUNCTION
# ============================================================================

def financial_modeling_agent(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Financial Modeling Agent - Calculates financial metrics and projections
    
    Currently uses SIMULATED/DUMMY calculations marked with clear comments.
    Python formulas are used where applicable, but with simulated input data.
    """
    print()
    cprint(f"{'NODE: financial_modeling_agent':-^80}", 'blue', attrs=['bold'])
    
    project_data = state.get("project_data", {})
    
    if not project_data:
        print("⚠️  No project data available for financial modeling")
        return state
    
    print(f"\n💰 Calculating financial metrics for {project_data.get('cluster_type', 'project')}...")
    print("⚠️  [IMPORTANT] Currently using DUMMY/SIMULATED calculations")
    print("⚠️  [IMPORTANT] Actual financial formulas to be implemented in next iteration\n")
    
    # Get project cost from collected data
    project_cost = project_data.get("project_cost", 82000000)
    members = project_data.get("members", 50)
    
    # SIMULATED loan calculations
    # TODO: Get actual grant percentage from project_data
    grant_percentage = 0.70  # Simulated 70% grant
    loan_amount = project_cost * (1 - grant_percentage)
    
    print(f"📊 Project Cost: ₹{project_cost:,.0f}")
    print(f"📊 Grant (70%): ₹{project_cost * grant_percentage:,.0f}")
    print(f"📊 Loan Amount: ₹{loan_amount:,.0f}")
    print()
    
    # Calculate financial metrics
    print("🔢 Calculating Financial Metrics:")
    print("=" * 50)
    
    # 1. NPV (DUMMY)
    npv = calculate_npv_dummy(project_cost, loan_amount, years=10)
    npv_status = "✅ PASS" if npv > 0 else "❌ FAIL"
    print(f"  NPV: ₹{npv:,.2f} {npv_status} (requirement: > 0)")
    
    # 2. IRR (DUMMY)
    annual_profit = project_cost * 0.12  # Simulated
    irr = calculate_irr_dummy(project_cost, annual_profit, years=10)
    irr_status = "✅ PASS" if irr > 10 else "❌ FAIL"
    print(f"  IRR: {irr:.2f}% {irr_status} (requirement: > 10%)")
    
    # 3. DSCR (PYTHON FORMULA with simulated inputs)
    loan_emi = loan_amount * 0.15  # Simulated annual EMI
    dscr = calculate_dscr_dummy(annual_profit, loan_emi)
    dscr_status = "✅ PASS" if dscr > 3.0 else "❌ FAIL"
    print(f"  DSCR: {dscr:.2f} {dscr_status} (requirement: > 3:1)")
    
    # 4. Break-even (PYTHON FORMULA with simulated inputs)
    revenue = project_cost * 0.25  # Simulated
    fixed_costs = project_cost * 0.10  # Simulated
    variable_costs = revenue * 0.50  # Simulated
    breakeven = calculate_breakeven_dummy(fixed_costs, revenue, variable_costs)
    breakeven_status = "✅ PASS" if breakeven < 60 else "❌ FAIL"
    print(f"  Break-even: {breakeven:.1f}% {breakeven_status} (requirement: < 60%)")
    
    # 5. Payback Period (PYTHON FORMULA with simulated inputs)
    annual_cashflow = annual_profit  # Simplified
    payback = calculate_payback_period_dummy(project_cost, annual_cashflow)
    print(f"  Payback Period: {payback:.1f} years")
    
    print("=" * 50)
    print()
    
    # Generate projections
    print("📈 Generating Financial Projections:")
    projections = generate_simplified_projections(project_data)
    print(f"  Generated {projections['duration_years']}-year projections")
    print()
    
    # Validate MSE-CDP requirements
    print("🔍 MSE-CDP Compliance Check:")
    all_passed = npv > 0 and irr > 10 and dscr > 3.0 and breakeven < 60
    
    if all_passed:
        print("  ✅ Project meets all MSE-CDP financial requirements")
        compliance_status = "COMPLIANT"
    else:
        print("  ⚠️  Project has some non-compliant metrics")
        compliance_status = "NON_COMPLIANT"
    
    print()
    
    # Store results in state
    financial_data = {
        "metrics": {
            "npv": npv,
            "irr": irr,
            "dscr": dscr,
            "breakeven_percentage": breakeven,
            "payback_period_years": payback
        },
        "loan_details": {
            "project_cost": project_cost,
            "grant_amount": project_cost * grant_percentage,
            "loan_amount": loan_amount,
            "grant_percentage": grant_percentage * 100
        },
        "projections": projections,
        "mse_cdp_compliance": {
            "status": compliance_status,
            "npv_check": npv > 0,
            "irr_check": irr > 10,
            "dscr_check": dscr > 3.0,
            "breakeven_check": breakeven < 60
        },
        "calculation_note": "⚠️ Using simulated/dummy calculations for development. Actual formulas to be implemented."
    }
    
    # Initialize dpr_sections if not present
    if "dpr_sections" not in state:
        state["dpr_sections"] = {}
    
    state["dpr_sections"]["financial"] = financial_data
    
    print("✅ Financial modeling complete")
    print("💾 Stored in state['dpr_sections']['financial']")
    
    return state