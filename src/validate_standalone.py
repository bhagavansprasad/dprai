#!/usr/bin/env python3
# validate_standalone.py
"""
Standalone DPR Validation Tester - Phase 5
Tests validation logic quickly without regenerating DPR

Usage:
    # Test all sections with real generated files
    python validate_standalone.py --source real --path ../output/Printing_Industry_Tirupati/
    
    # Test specific section
    python validate_standalone.py --source real --path ../output/Printing_Industry_Tirupati/ --section market
    
    # Test with mock data (edge cases)
    python validate_standalone.py --source mock
"""

import sys
import os
import argparse
from pathlib import Path

# Add validation_agent to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from validation_agent import (
    validate_executive_summary,
    validate_financial_plan,
    validate_technical_feasibility,
    validate_market_analysis,
    ValidationResult,
    generate_validation_report
)

# File paths
EXECUTIVE_SUMMARY_FILE = "01_executive_summary.md"
FINANCIAL_PLAN_FILE = "03_financial_plan.md"
TECHNICAL_FEASIBILITY_FILE = "06_technical_feasibility.md"
MARKET_ANALYSIS_FILE = "07_market_analysis.md"

# ============================================================================
# MOCK DATA FOR EDGE CASE TESTING
# ============================================================================

MOCK_DATA_GOOD = """
# EXECUTIVE SUMMARY

## Project Overview

The proposed project aims to establish a Common Facility Centre (CFC) for the Printing Industry cluster in Tirupati, Andhra Pradesh. This cluster comprises 50 member units engaged in various printing activities including offset printing, digital printing, and packaging solutions. The project seeks to address the technological gaps and infrastructure limitations currently faced by the cluster members through the establishment of a state-of-the-art Digital Printing Equipment facility.

The total project cost is estimated at ₹8.2 crore (₹82,000,000), which will be funded through the MSE-CDP (Micro & Small Enterprises - Cluster Development Programme) scheme with 60-80% government subsidy support. This initiative will significantly enhance the competitive capabilities of cluster members and enable them to access larger markets.

## Cluster Profile

The Printing Industry cluster in Tirupati has been operational for over two decades, serving both local and regional markets. The cluster faces several challenges including outdated technology, lack of access to modern equipment, limited working capital, and difficulty in meeting quality standards required by larger clients. The proposed CFC will address these critical gaps by providing access to advanced digital printing technology, training facilities, and quality certification support.

Current cluster characteristics include an average turnover of ₹50 lakhs per unit, employment of approximately 300 workers, and primary focus on educational materials, commercial printing, and packaging. The cluster has strong linkages with local educational institutions and businesses, providing a stable demand base.

## Financial Highlights

The financial analysis demonstrates strong viability for the proposed project:

- **Total Project Cost:** ₹8.2 crore (₹82,000,000)
- **Grant Support:** 70% (₹5.74 crore) under MSE-CDP scheme
- **Member Contribution:** 30% (₹2.46 crore)
- **Net Present Value (NPV):** ₹2.87 crore (Positive - indicating good returns)
- **Internal Rate of Return (IRR):** 15.5% (Well above 10% requirement)
- **Debt Service Coverage Ratio (DSCR):** 4.2:1 (Exceeds 3:1 requirement)
- **Break-even Point:** 45.2% capacity utilization (Below 60% threshold)
- **Payback Period:** 6.8 years

All key financial metrics meet or exceed MSE-CDP compliance requirements, confirming the project's economic viability.

## Expected Impact

The implementation of this Common Facility Centre is expected to deliver significant positive impacts:

**Economic Impact:**
- Direct employment generation: 85 new jobs
- Indirect employment: 150+ jobs in allied services
- Cluster turnover increase: 40% within 3 years (from ₹25 crore to ₹35 crore)
- Individual unit capacity increase: 50-60%

**Technology Impact:**
- Access to digital printing technology for all 50 units
- Quality improvement through standardized processes
- Reduction in production time by 30%
- Enhanced capability to serve premium market segments

**Market Impact:**
- Access to national markets through improved quality
- Ability to compete for larger contracts
- Diversification into new product categories
- Strengthened bargaining power with suppliers

**Social Impact:**
- Skill development through training programs
- Women participation in technical roles
- Environmental compliance through modern equipment
- Enhanced social security for workers

## Recommendation

Based on comprehensive technical, financial, and economic analysis, this project is strongly recommended for approval under the MSE-CDP scheme. The project demonstrates clear need, financial viability, strong impact potential, and full compliance with MSE-CDP guidelines. The Special Purpose Vehicle (SPV) has been constituted with participation from all 50 member units, and state government approval is in process. The implementation timeline of 18 months is realistic and achievable. Approval of this project will catalyze the growth of the printing industry cluster in Tirupati and serve as a model for similar clusters in the region.
"""

MOCK_DATA_POOR = """
# Executive Summary

This is about a printing project in Tirupati. We want to buy some machines.

The project costs 8.2 crore rupees. Government will give some money.

We think it's a good idea and you should approve it.
"""

MOCK_DATA_MISSING_SECTIONS = """
# EXECUTIVE SUMMARY

## Project Overview

The proposed project aims to establish a Common Facility Centre for the Printing Industry cluster in Tirupati.

## Financial Highlights

Total cost is ₹8.2 crore.
"""


# ============================================================================
# FILE READER
# ============================================================================

def read_dpr_file(file_path: str) -> tuple:
    """
    Read a DPR section file
    
    Returns:
        (content, success, error_message)
    """
    try:
        path = Path(file_path)
        if not path.exists():
            return None, False, f"File not found: {file_path}"
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove metadata header (everything before first # heading)
        lines = content.split('\n')
        content_start = 0
        for i, line in enumerate(lines):
            if line.strip().startswith('#'):
                content_start = i
                break
        
        clean_content = '\n'.join(lines[content_start:])
        
        return clean_content, True, None
        
    except Exception as e:
        return None, False, f"Error reading file: {str(e)}"


# ============================================================================
# TEST RUNNER
# ============================================================================

def test_real_data(output_path: str, project_data: dict, section: str = 'all'):
    """
    Test validation with real generated DPR files
    """
    print("\n" + "="*80)
    print("🔍 VALIDATION TEST: REAL GENERATED DPR FILES")
    print("="*80)
    
    output_dir = Path(output_path)
    
    # Dummy financial data for validation
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
        }
    }
    
    results = {}
    
    # Executive Summary
    if section in ['executive', 'all']:
        exec_path = output_dir / EXECUTIVE_SUMMARY_FILE
        if exec_path.exists():
            print(f"\n📁 Reading: {exec_path}")
            content, success, error = read_dpr_file(str(exec_path))
            if success:
                print(f"✅ File loaded ({len(content)} characters)")
                result = validate_executive_summary(content, project_data)
                results['executive'] = result
                display_results(result, "Executive Summary")
            else:
                print(f"❌ ERROR: {error}")
        else:
            print(f"\n⚠️  Executive Summary not found: {exec_path}")
    
    # Financial Plan
    if section in ['financial', 'all']:
        fin_path = output_dir / FINANCIAL_PLAN_FILE
        if fin_path.exists():
            print(f"\n📁 Reading: {fin_path}")
            content, success, error = read_dpr_file(str(fin_path))
            if success:
                print(f"✅ File loaded ({len(content)} characters)")
                result = validate_financial_plan(content, project_data, financial_data)
                results['financial'] = result
                display_results(result, "Financial Plan")
            else:
                print(f"❌ ERROR: {error}")
        else:
            print(f"\n⚠️  Financial Plan not found: {fin_path}")
    
    # Technical Feasibility
    if section in ['technical', 'all']:
        tech_path = output_dir / TECHNICAL_FEASIBILITY_FILE
        if tech_path.exists():
            print(f"\n📁 Reading: {tech_path}")
            content, success, error = read_dpr_file(str(tech_path))
            if success:
                print(f"✅ File loaded ({len(content)} characters)")
                result = validate_technical_feasibility(content, project_data, financial_data)
                results['technical'] = result
                display_results(result, "Technical Feasibility")
            else:
                print(f"❌ ERROR: {error}")
        else:
            print(f"\n⚠️  Technical Feasibility not found: {tech_path}")
    
    # Market Analysis
    if section in ['market', 'all']:
        market_path = output_dir / MARKET_ANALYSIS_FILE
        if market_path.exists():
            print(f"\n📁 Reading: {market_path}")
            content, success, error = read_dpr_file(str(market_path))
            if success:
                print(f"✅ File loaded ({len(content)} characters)")
                result = validate_market_analysis(content, project_data, financial_data)
                results['market'] = result
                display_results(result, "Market Analysis")
            else:
                print(f"❌ ERROR: {error}")
        else:
            print(f"\n⚠️  Market Analysis not found: {market_path}")
    
    # Display cumulative summary if all sections tested
    if section == 'all' and len(results) > 0:
        display_cumulative_summary(results)
    
    return results


def test_mock_data(project_data: dict):
    """
    Test validation with mock data for edge cases
    """
    print("\n" + "="*80)
    print("🔍 SECONDARY TEST: MOCK DATA (Edge Cases)")
    print("="*80)
    
    results = {}
    
    # Test 1: Good mock data
    print("\n" + "🔬"*40)
    print("\n📋 TEST 1: Well-Structured Mock Data")
    print("Expected: Should pass most checks")
    print("-"*80)
    
    result_good = validate_executive_summary(MOCK_DATA_GOOD, project_data)
    results['good'] = result_good
    
    print("\n" + "="*80)
    print("📊 MOCK DATA (GOOD) RESULTS")
    print("="*80)
    display_results(result_good, "Good Mock Data")
    
    # Test 2: Poor mock data
    print("\n\n" + "🔬"*40)
    print("\n📋 TEST 2: Poorly-Structured Mock Data")
    print("Expected: Should fail most checks")
    print("-"*80)
    
    result_poor = validate_executive_summary(MOCK_DATA_POOR, project_data)
    results['poor'] = result_poor
    
    print("\n" + "="*80)
    print("📊 MOCK DATA (POOR) RESULTS")
    print("="*80)
    display_results(result_poor, "Poor Mock Data")
    
    # Test 3: Missing sections
    print("\n\n" + "🔬"*40)
    print("\n📋 TEST 3: Missing Sections Mock Data")
    print("Expected: Should fail subsection checks")
    print("-"*80)
    
    result_missing = validate_executive_summary(MOCK_DATA_MISSING_SECTIONS, project_data)
    results['missing'] = result_missing
    
    print("\n" + "="*80)
    print("📊 MOCK DATA (MISSING SECTIONS) RESULTS")
    print("="*80)
    display_results(result_missing, "Missing Sections Mock")
    
    return results


def display_results(result, label: str):
    """
    Display validation results - handles both old ValidationResult and new dict format
    """
    print(f"\n🎯 {label}")
    
    # Check if it's the new dict format (Phase 3+) or old ValidationResult format
    if isinstance(result, dict) and 'summary' in result:
        # New format (Phase 3+)
        summary = result['summary']
        print(f"   Overall Score: {summary['percentage']:.1f}%")
        print(f"   Grade: {summary['grade']}")
        print(f"   Checks: {summary['passed']}/{summary['total_checks']} passed")
        
        print(f"\n📊 Tier Breakdown:")
        for tier in result['tiers']:
            print(f"   {tier['tier']:<12}: {tier['percentage']:.1f}% ({tier['passed']}/{tier['total']} passed)")
        
        # Show failed checks
        failed_checks = []
        for tier in result['tiers']:
            for check in tier['checks']:
                if not check['passed'] and check['severity'] in ['critical', 'high']:
                    failed_checks.append(f"{check['id']}: {check['description']}")
        
        if failed_checks:
            print(f"\n⚠️  Critical/High Issues ({len(failed_checks)}):")
            for i, issue in enumerate(failed_checks[:5], 1):  # Show top 5
                print(f"   {i}. {issue}")
    
    else:
        # Old format (Phase 2 - Executive Summary)
        print(f"   Overall Score: {result.overall_score:.1f}%")
        print(f"   Grade: {result.grade}")
        print(f"   Status: {result.status}")
        print(f"   Ready for Submission: {'✅ Yes' if result.ready_for_submission else '❌ No'}")
        
        print(f"\n📊 Breakdown:")
        print(f"   Structure:  {result.structure['score']:.1f}% ({result.structure['passed']}/{result.structure['total']} passed)")
        print(f"   Content:    {result.content['score']:.1f}% ({result.content['passed']}/{result.content['total']} passed)")
        print(f"   Compliance: {result.compliance['score']:.1f}% ({result.compliance['passed']}/{result.compliance['total']} passed)")
        print(f"   Quality:    {result.quality['score']:.1f}%")
        
        if result.issues:
            print(f"\n⚠️  Issues Found ({len(result.issues)}):")
            for i, issue in enumerate(result.issues[:5], 1):
                print(f"   {i}. {issue}")


def display_cumulative_summary(results: dict):
    """
    Display cumulative summary for all tested sections
    """
    print("\n" + "="*80)
    print("📊 CUMULATIVE VALIDATION SUMMARY")
    print("="*80)
    
    total_checks = 0
    total_passed = 0
    
    for section_name, result in results.items():
        if isinstance(result, dict) and 'summary' in result:
            # New format (Phase 3+: Financial Plan, Technical Feasibility, Market Analysis)
            summary = result['summary']
            print(f"{section_name.title():<25}: {summary['percentage']:.1f}% ({summary['grade']}) - {summary['passed']}/{summary['total_checks']}")
            total_checks += summary['total_checks']
            total_passed += summary['passed']
        else:
            # Old format (Phase 2: Executive Summary)
            # Calculate totals from old ValidationResult format
            section_checks = (result.structure['total'] + 
                            result.content['total'] + 
                            result.compliance['total'] + 
                            6)  # Quality tier has 6 checks
            section_passed = (result.structure['passed'] + 
                            result.content['passed'] + 
                            result.compliance['passed'] + 
                            int(result.quality['score'] / 100 * 6))  # Estimate quality passed
            
            print(f"{section_name.title():<25}: {result.overall_score:.1f}% ({result.grade}) - {section_passed}/{section_checks}")
            total_checks += section_checks
            total_passed += section_passed
    
    if total_checks > 0:
        overall = (total_passed / total_checks) * 100
        print(f"\n{'OVERALL':<25}: {overall:.1f}% - {total_passed}/{total_checks} checks passed")
    
    print("="*80)


def compare_results(real_result, mock_results):
    """
    Compare real data results with mock data results
    """
    print("\n\n" + "="*80)
    print("📊 COMPARATIVE ANALYSIS")
    print("="*80)
    
    print("\n🎯 Score Comparison:")
    print(f"   Real Generated DPR:        {real_result.overall_score:.1f}% ({real_result.grade})")
    if mock_results:
        print(f"   Mock (Good):               {mock_results['good'].overall_score:.1f}% ({mock_results['good'].grade})")
        print(f"   Mock (Poor):               {mock_results['poor'].overall_score:.1f}% ({mock_results['poor'].grade})")
        print(f"   Mock (Missing Sections):   {mock_results['missing'].overall_score:.1f}% ({mock_results['missing'].grade})")
    
    print("\n📈 Structure Score Comparison:")
    print(f"   Real Generated DPR:        {real_result.structure['score']:.1f}%")
    if mock_results:
        print(f"   Mock (Good):               {mock_results['good'].structure['score']:.1f}%")
        print(f"   Mock (Poor):               {mock_results['poor'].structure['score']:.1f}%")
        print(f"   Mock (Missing Sections):   {mock_results['missing'].structure['score']:.1f}%")
    
    print("\n🎓 Quality Assessment:")
    if real_result.overall_score >= 80:
        print("   ✅ PASS: Your generated DPR meets quality standards!")
    elif real_result.overall_score >= 70:
        print("   ⚠️  ACCEPTABLE: Your DPR is decent but has room for improvement")
    else:
        print("   ❌ NEEDS WORK: Your DPR requires significant improvements")


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Standalone DPR Validation Tester - Phase 5",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Test all sections
  python validate_standalone.py --source real --path ../output/Printing_Industry_Tirupati/
  
  # Test specific section
  python validate_standalone.py --source real --path ../output/Printing_Industry_Tirupati/ --section market
  
  # Test with mock data
  python validate_standalone.py --source mock
        """
    )
    
    parser.add_argument(
        '--source',
        choices=['real', 'mock', 'both'],
        default='real',
        help='Data source for testing (default: real)'
    )
    
    parser.add_argument(
        '--section',
        choices=['executive', 'financial', 'technical', 'market', 'all'],
        default='all',
        help='Which section to validate (default: all)'
    )
    
    parser.add_argument(
        '--path',
        type=str,
        help='Path to generated DPR output directory (required for real/both)'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.source in ['real', 'both'] and not args.path:
        parser.error("--path is required when --source is 'real' or 'both'")
    
    # Project data for testing
    project_data = {
        "cluster_type": "Printing Industry",
        "location": "Tirupati, Andhra Pradesh",
        "members": 50,
        "project_cost": 82000000,
        "facility_type": "Digital Printing Equipment",
        "grant_scheme": "MSE-CDP",
        "subsidy_range": "60-80%"
    }
    
    print("\n" + "="*80)
    print("🧪 STANDALONE DPR VALIDATION TESTER - PHASE 5")
    print("Validates: Executive Summary, Financial Plan, Technical Feasibility, Market Analysis")
    print("="*80)
    
    real_results = None
    mock_results = None
    
    # Test real data
    if args.source in ['real', 'both']:
        real_results = test_real_data(args.path, project_data, args.section)
        if not real_results:
            return 1
    
    # Test mock data
    if args.source in ['mock', 'both']:
        mock_results = test_mock_data(project_data)
    
    # Compare results if both were run (only for executive summary)
    if args.source == 'both' and real_results and 'executive' in real_results:
        compare_results(real_results['executive'], mock_results)
    
    # Final summary
    print("\n\n" + "="*80)
    print("✅ VALIDATION TESTING COMPLETE")
    print("="*80)
    
    print("\n📋 Implementation Status:")
    print("   ✅ Phase 2: Executive Summary Validation - COMPLETE (29 checks)")
    print("   ✅ Phase 3: Financial Plan Validation - COMPLETE (31 checks)")
    print("   ✅ Phase 4: Technical Feasibility Validation - COMPLETE (30 checks)")
    print("   ✅ Phase 5: Market Analysis Validation - COMPLETE (30 checks)")
    print("   ⏸️  Phase 6+: Remaining Sections - PENDING")
    
    total_checks = 120  # 29 + 31 + 30 + 30
    print(f"\n   Total Validation Checks Implemented: {total_checks}")
    
    print("="*80 + "\n")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
    