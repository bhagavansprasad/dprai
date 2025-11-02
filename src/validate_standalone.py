#!/usr/bin/env python3
# validate_standalone.py
"""
Standalone DPR Validation Tester - Phase 2, Step 2.1
Tests validation logic quickly without regenerating DPR

Usage:
    # Test with real generated files (PRIMARY)
    python validate_standalone.py --source real --path /home/bhagavan/aura/dprai/output/Printing_Industry_Tirupati/
    
    # Test with mock data (SECONDARY - edge cases)
    python validate_standalone.py --source mock
    
    # Test both (COMPREHENSIVE)
    python validate_standalone.py --source both --path /home/bhagavan/aura/dprai/output/Printing_Industry_Tirupati/
"""

import sys
import os
import argparse
from pathlib import Path

# Add validation_agent to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from validation_agent import validate_executive_summary, ValidationResult, generate_validation_report


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

def test_real_data(output_path: str, project_data: dict):
    """
    Test validation with real generated DPR files
    """
    print("\n" + "="*80)
    print("🔍 PRIMARY TEST: REAL GENERATED DPR FILES")
    print("="*80)
    
    executive_summary_path = Path(output_path) / "01_executive_summary.md"
    
    print(f"\n📁 Reading: {executive_summary_path}")
    
    content, success, error = read_dpr_file(str(executive_summary_path))
    
    if not success:
        print(f"\n❌ ERROR: {error}")
        print("\n💡 Make sure the path is correct:")
        print(f"   Expected: {executive_summary_path}")
        return None
    
    print(f"✅ File loaded successfully ({len(content)} characters)")
    
    # Run validation
    print("\n" + "🔬"*40)
    result = validate_executive_summary(content, project_data)
    
    # Display results
    print("\n" + "="*80)
    print("📊 REAL DATA VALIDATION RESULTS")
    print("="*80)
    
    display_results(result, "Real Generated DPR")
    
    return result


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


def display_results(result: ValidationResult, label: str):
    """
    Display validation results in a clear format
    """
    print(f"\n🎯 {label}")
    print(f"   Overall Score: {result.overall_score:.1f}%")
    print(f"   Grade: {result.grade}")
    print(f"   Status: {result.status}")
    print(f"   Ready for Submission: {'✅ Yes' if result.ready_for_submission else '❌ No'}")
    
    print(f"\n📊 Breakdown:")
    print(f"   Structure:  {result.structure['score']:.1f}% ({result.structure['passed']}/{result.structure['total']} passed)")
    print(f"   Content:    {result.content['score']:.1f}% ({result.content['passed']}/{result.content['total']} passed) [Not implemented]")
    print(f"   Compliance: {result.compliance['score']:.1f}% ({result.compliance['passed']}/{result.compliance['total']} passed) [Not implemented]")
    print(f"   Quality:    {result.quality['score']:.1f}% [Not implemented]")
    
    if result.issues:
        print(f"\n⚠️  Issues Found ({len(result.issues)}):")
        for i, issue in enumerate(result.issues, 1):
            print(f"   {i}. {issue}")
    
    if result.suggestions:
        print(f"\n💡 Suggestions ({len(result.suggestions)}):")
        for i, suggestion in enumerate(result.suggestions, 1):
            print(f"   {i}. {suggestion}")
    
    # Detailed structure checks
    print(f"\n🔍 Detailed Structure Checks:")
    for detail in result.structure['details']:
        status_icon = "✅" if detail['status'] == "PASS" else "⚠️" if detail['status'] == "PASS_WITH_WARNING" else "❌"
        print(f"   {status_icon} [{detail['check']}] {detail['name']}: {detail['message']}")


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
        print("   ✅ Ready to move to Phase 2, Step 2.2 (Content validation)")
    elif real_result.overall_score >= 70:
        print("   ⚠️  ACCEPTABLE: Your DPR is decent but has room for improvement")
        print("   💡 Review issues and suggestions above")
    else:
        print("   ❌ NEEDS WORK: Your DPR requires significant improvements")
        print("   💡 Review document_generator.py prompts for Executive Summary")
    
    # Check if validation logic is working
    print("\n🔧 Validation Logic Check:")
    if mock_results:
        good_pass = mock_results['good'].structure['score'] >= 80
        poor_fail = mock_results['poor'].structure['score'] < 80
        
        if good_pass and poor_fail:
            print("   ✅ Validation logic is working correctly")
            print("   ✅ Good content scores high, poor content scores low")
        else:
            print("   ⚠️  Validation logic may need adjustment")


# ============================================================================
# MAIN
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Standalone DPR Validation Tester - Phase 2, Step 2.1",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Test with real files (PRIMARY)
  python validate_standalone.py --source real --path /home/bhagavan/aura/dprai/output/Printing_Industry_Tirupati/
  
  # Test with mock data (SECONDARY)
  python validate_standalone.py --source mock
  
  # Test both (COMPREHENSIVE)
  python validate_standalone.py --source both --path /home/bhagavan/aura/dprai/output/Printing_Industry_Tirupati/
        """
    )
    
    parser.add_argument(
        '--source',
        choices=['real', 'mock', 'both'],
        default='both',
        help='Data source for testing (default: both)'
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
    print("🧪 STANDALONE DPR VALIDATION TESTER")
    print("Phase 2, Step 2.1: Tier 1 (Structure) Validation")
    print("="*80)
    
    real_result = None
    mock_results = None
    
    # Test real data
    if args.source in ['real', 'both']:
        real_result = test_real_data(args.path, project_data)
        if real_result is None:
            return 1
    
    # Test mock data
    if args.source in ['mock', 'both']:
        mock_results = test_mock_data(project_data)
    
    # Compare results if both were run
    if args.source == 'both' and real_result:
        compare_results(real_result, mock_results)
    
    # Final summary
    print("\n\n" + "="*80)
    print("✅ VALIDATION TESTING COMPLETE")
    print("="*80)
    
    if real_result:
        print(f"\nYour Real DPR Score: {real_result.overall_score:.1f}% ({real_result.status})")
    
    print("\n📋 Current Implementation Status:")
    print("   ✅ Phase 2, Step 2.1: Tier 1 (Structure) - IMPLEMENTED")
    print("   ⏸️  Phase 2, Step 2.2: Tier 2 (Content) - PENDING")
    print("   ⏸️  Phase 2, Step 2.3: Tier 3 (Compliance) - PENDING")
    print("   ⏸️  Phase 2, Step 2.4: Tier 4 (Quality) - PENDING")
    
    print("\n🚀 Next Steps:")
    if real_result and real_result.overall_score >= 80:
        print("   ✅ Structure validation passed!")
        print("   ➡️  Proceed to Phase 2, Step 2.2 (Content validation)")
    elif real_result:
        print("   ⚠️  Structure validation needs improvement")
        print("   💡 Review issues and update document_generator.py")
        print("   🔄 Re-generate DPR and re-test")
    
    print("="*80 + "\n")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())