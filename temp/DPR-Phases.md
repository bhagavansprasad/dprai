# 📄 AI-DPR Genie: Complete Project Specification Document

**Project:** AI-powered Detailed Project Report (DPR) Generator for MSMEs  
**Technology Stack:** Python, LangGraph, Gemini AI, FastAPI  
**Date:** January 2025  
**Version:** 1.0

---

## 📋 Table of Contents

1. [Project Overview](#project-overview)
2. [Phase 1: Basic Text Generation](#phase-1)
3. [Phase 2: Complete Text Sections](#phase-2)
4. [Phase 3: Financial Calculations](#phase-3)
5. [Phase 4: Document Generation](#phase-4)
6. [Phase 5: REST API Wrapper](#phase-5)
7. [Phase 6: Frontend (Placeholder)](#phase-6)
8. [Phase 7: Database Integration (Placeholder)](#phase-7)
9. [Technology Stack](#technology-stack)
10. [Project Timeline](#project-timeline)

---

## 🎯 Project Overview {#project-overview}

### Purpose
Build an AI-powered tool to generate comprehensive Detailed Project Reports (DPRs) for MSME clusters under the MSE-CDP scheme, automating what traditionally takes 3-4 weeks down to a few hours.

### Key Features
- AI-powered content generation using Gemini
- Automated financial modeling (10-year projections)
- IRR, NPV, ROCE, Break-even calculations
- Sensitivity analysis (5%, 10% scenarios)
- Multi-format output (PDF, Word, Excel)
- REST API for integration
- Web interface for user interaction

### Target Users
- MSME cluster units
- Special Purpose Vehicles (SPVs)
- State government officials
- Consultants and CDAs

---

## 📌 PHASE 1: Basic Text Generation {#phase-1}

### Objective
Build the foundational LangGraph agent that generates 2 core DPR sections

### Duration
1 week

### Complexity
Low

---

### Agent Structure

**Total Nodes: 3**

#### Node 1: `validate_input`
**Purpose:** Validate user input data

**Validations:**
- `cluster_name`: Not empty
- `num_units`: > 0
- `current_turnover`: > 0
- `direct_employment`: >= 0
- `indirect_employment`: >= 0
- All required fields present

**Input:** User data dict  
**Output:** Validation result (pass/fail + error messages)

**Logic:**
```python
- Check all required fields exist
- Check data types are correct
- Check numeric values are positive
- If validation fails: Return errors and stop workflow
- If validation passes: Continue to next node
```

---

#### Node 2: `generate_executive_summary`
**Purpose:** Generate Executive Summary section

**AI Prompt Structure:**
```
Context:
- Cluster name, location, industry
- Current state (units, turnover, employment)
- Products/services

Generate:
1. Introduction to cluster (1 para)
2. Current significance (1 para)
3. Challenges faced (1 para)
4. Proposed CFC intervention (1 para)
5. Expected outcomes (1 para)

Length: 400-500 words
Tone: Professional, persuasive
Audience: Government officials, financial institutions
```

**Input:** Validated user data  
**Output:** Executive summary text (string)

**Gemini Settings:**
- Temperature: 0.7
- Max tokens: 1000
- Model: gemini-1.5-pro

---

#### Node 3: `generate_cluster_profile`
**Purpose:** Generate Cluster Profile section

**AI Prompt Structure:**
```
Context:
- Cluster details (name, location, age)
- Units breakdown (micro/small/medium)
- Products/services list
- Current technology used

Generate sections:
1. History and development
2. Geographic spread
3. Nature and type of units
4. Products and services
5. Current technology
6. Employment generation
7. Market reach
8. Unique characteristics

Length: 600-800 words
Tone: Descriptive, factual, professional
```

**Input:** Validated user data  
**Output:** Cluster profile text (string)

**Gemini Settings:**
- Temperature: 0.7
- Max tokens: 1500
- Model: gemini-1.5-pro

---

### Workflow

```
START
  ↓
[Node 1: validate_input]
  ↓
  ├─ Validation Failed? → END (with error message)
  └─ Validation Passed? → Continue
  ↓
[Node 2: generate_executive_summary]
  ↓
[Node 3: generate_cluster_profile]
  ↓
END (save outputs to file)
```

---

### Input Schema (user_input.json)

```json
{
  "cluster_name": "Printing Cluster Tirupati",
  "industry": "printing",
  "city": "Tirupati",
  "district": "Tirupati",
  "state": "Andhra Pradesh",
  "num_units": 92,
  "num_micro": 92,
  "num_small": 0,
  "num_medium": 0,
  "current_turnover": 64.40,
  "direct_employment": 500,
  "indirect_employment": 3000,
  "products": [
    "Business Cards",
    "Wedding Cards",
    "Text Books",
    "Magazines"
  ],
  "cluster_age": 60
}
```

---

### Output Schema (dpr_output.txt)

```
============================================
AI-DPR GENIE - GENERATED REPORT
============================================
Cluster: Printing Cluster Tirupati
Generated: 2025-01-15 14:30:00
============================================

EXECUTIVE SUMMARY
============================================
[AI-generated 400-500 words]

CLUSTER PROFILE
============================================
[AI-generated 600-800 words]

============================================
END OF REPORT
============================================
```

---

### Project Structure

```
dpr-genie/
├── .env                          # GEMINI_API_KEY
├── .gitignore
├── requirements.txt
├── README.md
│
├── config.py                     # Configuration settings
├── models.py                     # Pydantic input models
├── prompts.py                    # AI prompt templates
│
├── gemini_service.py             # Gemini API wrapper
├── agent_workflow.py             # LangGraph agent (3 nodes)
│
├── run.py                        # Entry point: python run.py
├── user_input.json               # Sample input
│
└── outputs/                      # Generated files
    └── dpr_output.txt
```

---

### Dependencies (requirements.txt)

```txt
# Core
python-dotenv==1.0.0

# AI/ML
langgraph==0.0.20
langchain-google-genai==0.0.6
google-generativeai==0.3.2

# Data
pydantic==2.5.3
```

---

### Success Criteria

- ✅ Agent runs without errors
- ✅ Validation catches invalid inputs
- ✅ Executive summary is coherent and professional
- ✅ Cluster profile is detailed and accurate
- ✅ Output saved to text file
- ✅ Execution time: 2-3 minutes

---

### How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Set environment variable
# Create .env file with:
# GEMINI_API_KEY=your_key_here

# Run agent
python run.py --input user_input.json

# Output will be saved to:
# outputs/dpr_output.txt
```

---

### Limitations (Phase 1)

- ❌ Only 2 text sections generated
- ❌ No financial calculations
- ❌ No SWOT analysis
- ❌ No industry analysis
- ❌ No document formatting (PDF/Word)
- ❌ No API
- ❌ No frontend
- ❌ No database

---

## 📌 PHASE 2: Complete Text Sections {#phase-2}

### Objective
Expand agent to generate ALL text sections of a complete DPR

### Duration
1 week

### Complexity
Low-Medium

---

### Agent Structure

**Total Nodes: 5** (3 from Phase 1 + 2 new)

#### Nodes 1-3: Same as Phase 1
- validate_input
- generate_executive_summary  
- generate_cluster_profile

#### Node 4: `generate_cluster_and_industry_analysis` ✨ NEW
**Purpose:** Generate combined section covering cluster details + industry overview

**AI Prompt Structure:**
```
PART 1: CLUSTER ANALYSIS
Context:
- Cluster background, history
- Geographic advantages
- Current operations

Generate:
1. Detailed cluster overview
2. Location advantages
3. Products/services portfolio
4. Technology currently used
5. Employment patterns

PART 2: INDUSTRY ANALYSIS
Context:
- Industry type (printing/food processing/textiles etc.)
- Location (state/region)

Generate:
1. Industry overview (market size, growth)
2. Technology trends
3. Regional context
4. Government support & policies
5. Future outlook

Combined Length: 1200-1500 words
```

**Input:** User data  
**Output:** Combined cluster + industry analysis text

**Gemini Settings:**
- Temperature: 0.7
- Max tokens: 3000

---

#### Node 5: `generate_problems_interventions_swot` ✨ NEW
**Purpose:** Generate problems, solutions, and SWOT analysis

**AI Prompt Structure:**
```
SECTION 1: PROBLEMS IDENTIFIED
Input: List of cluster problems
Generate: Detailed elaboration of each problem (300-400 words)

SECTION 2: PROPOSED INTERVENTIONS
Input: List of machinery/facilities
Generate: How each intervention solves problems (400-500 words)

SECTION 3: SWOT ANALYSIS
Generate in JSON format:
{
  "strengths": ["...", "...", "...", "..."],
  "weaknesses": ["...", "...", "..."],
  "opportunities": ["...", "...", "...", "..."],
  "threats": ["...", "...", "..."]
}
```

**Input:** User data (problems, machinery list)  
**Output:** 
- `problems_text`: String
- `interventions_text`: String  
- `swot_json`: Dict

**Gemini Settings:**
- Temperature: 0.6 (more structured)
- Max tokens: 2000

---

#### Node 6: `generate_conclusion` ✨ NEW (Moved from Node 7)
**Purpose:** Generate conclusion section

**AI Prompt Structure:**
```
Context:
- Cluster name and overview
- Proposed CFC interventions
- Expected outcomes

Generate:
1. Reaffirm the need (2-3 sentences)
2. Summarize solution (2-3 sentences)
3. Emphasize impact (2-3 sentences)
4. Strong closing statement

Length: 300-400 words
Tone: Confident, forward-looking
```

**Input:** All previous generated content  
**Output:** Conclusion text

**Gemini Settings:**
- Temperature: 0.7
- Max tokens: 800

---

### Workflow

```
START
  ↓
[Node 1: validate_input]
  ↓ (if pass)
[Node 2: generate_executive_summary]
  ↓
[Node 3: generate_cluster_profile]
  ↓
[Node 4: generate_cluster_and_industry_analysis] ✨ NEW
  ↓
[Node 5: generate_problems_interventions_swot] ✨ NEW
  ↓
[Node 6: generate_conclusion] ✨ NEW
  ↓
END (save to JSON)
```

---

### Input Schema (EXPANDED)

```json
{
  "cluster_name": "Printing Cluster Tirupati",
  "industry": "printing",
  "city": "Tirupati",
  "district": "Tirupati",
  "state": "Andhra Pradesh",
  "num_units": 92,
  "num_micro": 92,
  "num_small": 0,
  "num_medium": 0,
  "current_turnover": 64.40,
  "direct_employment": 500,
  "indirect_employment": 3000,
  "products": [
    "Business Cards",
    "Wedding Cards",
    "Text Books"
  ],
  "cluster_age": 60,
  
  "cluster_problems": [
    "Lack of high-resolution multi-color printing machines",
    "No modern finishing and post-press equipment",
    "Outsourcing to other cities increases costs",
    "Low profit margins due to old technology",
    "No training facilities for skill upgradation"
  ],
  
  "machinery_list": [
    {
      "name": "Five Colour Offset Printing Machine",
      "quantity": 1,
      "purpose": "High-resolution color printing"
    },
    {
      "name": "Computer to Plate (CTP) Machine",
      "quantity": 1,
      "purpose": "Modern plate making technology"
    },
    {
      "name": "Automatic Cutting Machine",
      "quantity": 1,
      "purpose": "Precision cutting and finishing"
    }
  ]
}
```

---

### Output Schema (dpr_output.json)

```json
{
  "metadata": {
    "cluster_name": "Printing Cluster Tirupati",
    "generated_at": "2025-01-15T14:30:00",
    "phase": "2"
  },
  
  "sections": {
    "executive_summary": "...",
    
    "cluster_profile": "...",
    
    "cluster_and_industry_analysis": "...",
    
    "problems_and_interventions": {
      "problems": "...",
      "proposed_interventions": "...",
      "swot_analysis": {
        "strengths": [
          "Established cluster with 60 years of experience",
          "Strategic location in educational hub",
          "Strong local market presence",
          "Experienced workforce"
        ],
        "weaknesses": [
          "Outdated technology and machinery",
          "High dependency on outsourcing",
          "Low profit margins"
        ],
        "opportunities": [
          "Growing demand for high-quality printing",
          "Export market potential",
          "Digital printing integration",
          "Government support through MSE-CDP"
        ],
        "threats": [
          "Competition from metro cities",
          "Digital media affecting print demand",
          "Rising raw material costs"
        ]
      }
    },
    
    "conclusion": "..."
  }
}
```

---

### Project Structure Updates

```
dpr-genie/
├── config.py
├── models.py                     # Updated with new fields
├── prompts.py                    # 3 new prompt templates added
├── gemini_service.py
├── agent_workflow.py             # 3 new nodes (total 6)
├── run.py
├── user_input.json               # Expanded sample
└── outputs/
    └── dpr_output.json           # JSON output
```

---

### Success Criteria

- ✅ All 6 nodes execute successfully
- ✅ Generate all text sections
- ✅ SWOT in proper JSON format
- ✅ Combined sections are coherent
- ✅ Output saved to JSON file
- ✅ Execution time: 5-7 minutes

---

### Limitations (Phase 2)

- ❌ No financial calculations
- ❌ No implementation schedule
- ❌ No PDF/Word generation
- ❌ No API
- ❌ No frontend
- ❌ No database

---

## 📌 PHASE 3: Financial Calculations {#phase-3}

### Objective
Add comprehensive financial modeling and calculations

### Duration
2 weeks

### Complexity
Medium-High

---

### Agent Structure

**Total Nodes: 9** (6 from Phase 2 + 3 new)

#### Nodes 1-6: Same as Phase 1 & 2

#### Node 7: `calculate_project_cost` ✨ NEW
**Purpose:** Calculate detailed project cost breakdown

**Calculations:**

1. **Land Cost**
   - If status = "lease": Use `lease_cost_lakhs`
   - If status = "own": 0
   - Max: 25% of total project cost

2. **Building Cost**
   - Formula: `(building_area_sqft × ₹1,700) / 100,000`
   - Rate: ₹1,700 per sq.ft (average construction cost)

3. **Machinery Cost**
   - Formula: `Sum of all machinery estimated_cost`

4. **Misc Fixed Assets**
   - Formula: `machinery_cost × 2%`

5. **Preliminary Expenses**
   - Formula: `machinery_cost × 2%`

6. **Contingency**
   - Formula: `machinery_cost × 5%`

7. **Margin Money for Working Capital**
   - Working Capital = `machinery_cost × 10%`
   - Margin Money = `Working Capital × 25%`

8. **Total Project Cost**
   - Sum of all above

**Input:** User data (land, building, machinery)  
**Output:** Project cost dict

```python
{
  "land_cost": 45.00,
  "building_cost": 183.83,
  "machinery_cost": 2062.94,
  "misc_fixed_assets": 41.26,
  "preliminary_expenses": 41.26,
  "contingency": 103.15,
  "margin_money": 51.57,
  "total": 2528.01
}
```

---

#### Node 8: `calculate_means_of_finance` ✨ NEW
**Purpose:** Calculate funding breakdown (70:15:15 ratio)

**Calculations:**

1. **GoI Grant**
   - Formula: `total_project_cost × 70%`
   - Max: ₹30 Crore (as per MSE-CDP guidelines)

2. **State Government Grant**
   - Formula: `total_project_cost × 15%`

3. **SPV Contribution**
   - Formula: `total_project_cost × 15%`

4. **Bank Loan** (Optional)
   - Default: 0
   - Can be added if needed

**Input:** Total project cost  
**Output:** Means of finance dict

```python
{
  "goi_grant": 1769.61,      # 70%
  "state_grant": 379.20,     # 15%
  "spv_contribution": 379.20, # 15%
  "bank_loan": 0.00,
  "total": 2528.01
}
```

---

#### Node 9: `calculate_financial_projections` ✨ NEW
**Purpose:** Generate 10-year financial projections and calculate all ratios

**Sub-Calculations:**

##### 9.1 Revenue Projections
```
Base Revenue = machinery_cost × 30%
Year Revenue = Base Revenue × Capacity Utilization × Growth Factor

Capacity Utilization Schedule (10 years):
Year 1-2: 70%
Year 3-4: 75%
Year 5-6: 80%
Year 7-8: 85%
Year 9-10: 90%

Growth Factor = 1.02^(year-1)  [2% annual growth]
```

##### 9.2 Expense Calculations
```
Material Cost = Revenue × 22%
Fuel Cost = Revenue × 2%
Direct Wages = Salary base × 1.02^(year-1)  [2% increment]
Power Cost = ₹8/unit × Total KVA × Operating hours
Repair & Maintenance = 5% of revenue
Admin Expenses = 4% of revenue
```

##### 9.3 Depreciation (WDV Method)
```
Land: 0%
Building: 10% WDV
Machinery: 14% WDV
Misc Fixed Assets: 18% WDV
Preliminary Expenses: 20% WDV
Contingency: 10% WDV
```

##### 9.4 Profit Calculations
```
Revenue
- Material Cost
- Operating Expenses
- Depreciation
= Profit Before Tax (PBT)

Tax = PBT × 15%
Profit After Tax (PAT) = PBT - Tax
Cash Flow = PAT + Depreciation
```

##### 9.5 Financial Ratios

**IRR (Internal Rate of Return)**
```
Cash Flows = [-Total Project Cost, Year1 CF, Year2 CF, ..., Year10 CF]
IRR = numpy.irr(cash_flows) × 100
Target: > 10%
```

**NPV (Net Present Value)**
```
Discount Rate = 10%
NPV = numpy.npv(0.10, cash_flows)
Target: > 0
```

**ROCE (Return on Capital Employed)**
```
Average PAT = Sum of 10-year PAT / 10
Capital Employed = Total Project Cost
ROCE = (Average PAT / Capital Employed) × 100
Target: > 25%
```

**Break-Even Point**
```
Fixed Costs = Salaries + Power (fixed) + Admin + Depreciation
Variable Costs = Materials + Fuel + Variable wages
Contribution = Revenue - Variable Costs
Break-Even = (Fixed Costs / Contribution) × 100
Target: < 60%
```

##### 9.6 Sensitivity Analysis

**Scenario 1: 5% Reduction in Revenue**
- Reduce all revenue by 5%
- Recalculate: IRR, NPV, ROCE, Break-even

**Scenario 2: 10% Reduction in Revenue**
- Reduce all revenue by 10%
- Recalculate: IRR, NPV, ROCE, Break-even

**Input:** Project cost, user targets  
**Output:** 

```python
{
  "yearly_projections": [
    {
      "year": 1,
      "capacity_utilization": 0.70,
      "revenue": 1295.46,
      "material_cost": 285.00,
      "operating_expenses": 286.81,
      "depreciation": 333.17,
      "profit_before_tax": 390.48,
      "tax": 58.57,
      "profit_after_tax": 331.91,
      "cash_flow": 665.08
    },
    ... 9 more years
  ],
  
  "financial_ratios": {
    "irr": 26.0,
    "npv": 2468.84,
    "roce": 36.0,
    "breakeven": 40.0
  },
  
  "sensitivity_5_percent": {
    "irr": 24.0,
    "npv": 2328.13,
    "roce": 33.0,
    "breakeven": 41.0
  },
  
  "sensitivity_10_percent": {
    "irr": 22.0,
    "npv": 2187.41,
    "roce": 31.0,
    "breakeven": 43.0
  }
}
```

---

### Workflow

```
START
  ↓
[Nodes 1-6: Text generation from Phase 1 & 2]
  ↓
[Node 7: calculate_project_cost] ✨
  ↓
[Node 8: calculate_means_of_finance] ✨
  ↓
[Node 9: calculate_financial_projections] ✨
  ↓
[Node 6: generate_conclusion] (updated with financial data)
  ↓
END
```

---

### Input Schema (EXPANDED with Financial Data)

```json
{
  // ... all previous fields from Phase 2 ...
  
  "land_building": {
    "land_status": "lease",          // "own" | "lease" | "to_acquire"
    "land_area_acres": 0.5,
    "building_area_sqft": 10800,
    "lease_period_years": 30,
    "lease_cost_lakhs": 45.0
  },
  
  "machinery_list": [
    {
      "name": "Five Colour Offset Printing Machine",
      "quantity": 1,
      "estimated_cost": 689.15,       // in lakhs
      "power_requirement_kva": 170,
      "purpose": "High-resolution printing"
    },
    {
      "name": "CTP Machine",
      "quantity": 1,
      "estimated_cost": 76.88,
      "power_requirement_kva": 4,
      "purpose": "Plate making"
    }
    // ... more machinery
  ],
  
  "project_targets": {
    "expected_turnover_3yrs": 100.0,    // in crores
    "expected_direct_employment": 800,
    "expected_indirect_employment": 5000,
    "expected_new_units": 150,
    "export_targets": 5.0               // in crores (optional)
  },
  
  "manpower": {
    "operators": 15,
    "skilled_workers": 10,
    "support_staff": 5,
    "avg_salary_per_month": 25000
  }
}
```

---

### Output Schema (COMPLETE)

```json
{
  "metadata": { "..." },
  
  "sections": {
    "executive_summary": "...",
    "cluster_profile": "...",
    "cluster_and_industry_analysis": "...",
    "problems_and_interventions": { "..." },
    "conclusion": "..."
  },
  
  "financials": {
    "project_cost": {
      "land_cost": 45.00,
      "building_cost": 183.83,
      "machinery_cost": 2062.94,
      "misc_fixed_assets": 41.26,
      "preliminary_expenses": 41.26,
      "contingency": 103.15,
      "margin_money": 51.57,
      "total": 2528.01
    },
    
    "means_of_finance": {
      "goi_grant": 1769.61,
      "state_grant": 379.20,
      "spv_contribution": 379.20,
      "bank_loan": 0.00,
      "total": 2528.01
    },
    
    "yearly_projections": [
      {
        "year": 1,
        "capacity_utilization": 0.70,
        "revenue": 1295.46,
        "expenses": 571.81,
        "depreciation": 333.17,
        "profit_before_tax": 390.48,
        "profit_after_tax": 331.91,
        "cash_flow": 665.08
      }
      // ... years 2-10
    ],
    
    "financial_ratios": {
      "irr": 26.0,
      "npv": 2468.84,
      "roce": 36.0,
      "breakeven": 40.0
    },
    
    "sensitivity_analysis": {
      "scenario_5_percent_reduction": {
        "irr": 24.0,
        "npv": 2328.13,
        "roce": 33.0,
        "breakeven": 41.0
      },
      "scenario_10_percent_reduction": {
        "irr": 22.0,
        "npv": 2187.41,
        "roce": 31.0,
        "breakeven": 43.0
      }
    },
    
    "compliance_check": {
      "irr_target": "> 10%",
      "irr_achieved": "26%",
      "irr_status": "✓ PASS",
      
      "npv_target": "> 0",
      "npv_achieved": "2468.84 Lakhs",
      "npv_status": "✓ PASS",
      
      "breakeven_target": "< 60%",
      "breakeven_achieved": "40%",
      "breakeven_status": "✓ PASS",
      
      "roce_target": "> 25%",
      "roce_achieved": "36%",
      "roce_status": "✓ PASS",
      
      "overall_viability": "FINANCIALLY VIABLE"
    }
  }
}
```

---

### Project Structure Updates

```
dpr-genie/
├── config.py
├── models.py
├── prompts.py
├── gemini_service.py
│
├── financial_calculations.py     ✨ NEW
│   # All financial formulas:
│   - calculate_project_cost()
│   - calculate_means_of_finance()
│   - calculate_depreciation()
│   - calculate_irr()
│   - calculate_npv()
│   - calculate_roce()
│   - calculate_breakeven()
│   - generate_yearly_projections()
│   - sensitivity_analysis()
│
├── agent_workflow.py             # 3 new financial nodes (total 9)
├── run.py
└── outputs/
    └── dpr_output.json
```

---

### Dependencies Update

```txt
# Add to requirements.txt:
numpy==1.26.3          # For IRR, NPV calculations
pandas==2.1.4          # For financial projections table
```

---

### Success Criteria

- ✅ Accurate project cost calculations
- ✅ Correct 70:15:15 funding split
- ✅ 10-year projections generated
- ✅ All financial ratios calculated correctly
- ✅ IRR > 10% ✓
- ✅ NPV > 0 ✓
- ✅ Break-even < 60% ✓
- ✅ ROCE > 25% ✓
- ✅ Sensitivity analysis completed (5%, 10%)
- ✅ Financial data saved to JSON
- ✅ Execution time: 7-10 minutes

---

### Limitations (Phase 3)

- ❌ No formatted financial tables (only JSON)
- ❌ No charts/graphs
- ❌ No PDF/Word/Excel documents
- ❌ No API
- ❌ No frontend
- ❌ No database

---

## 📌 PHASE 4: Document Generation {#phase-4}

### Objective
Generate professional formatted documents (PDF, Word, Excel) from DPR data

### Duration
1 week

### Complexity
Medium

---

### Agent Structure

**Total Nodes: 12** (9 from Phase 3 + 3 new)

#### Nodes 1-9: Same as Phase 1, 2 & 3

#### Node 10: `generate_pdf` ✨ NEW
**Purpose:** Create professionally formatted PDF document

**PDF Structure:**

**Page 1: Cover Page**
- Project title
- Cluster name
- Submitted by SPV
- Date

**Page 2: Table of Contents**
- Auto-generated with page numbers

**Page 3+: Content Sections**
1. Executive Summary
2. Cluster Profile
3. Cluster and Industry Analysis
4. Problems and Proposed Interventions
5. SWOT Analysis (formatted table)
6. Project Cost (table)
7. Means of Finance (pie chart)
8. Financial Projections (tables)
9. Financial Ratios (highlighted box)
10. Implementation Schedule (Gantt chart)
11. Conclusion

**Formatting:**
- Font: Times New Roman, 11pt
- Headings: Bold, 14pt
- Line spacing: 1.5
- Margins: 1 inch all sides
- Page numbers: Bottom center
- Headers: Cluster name on each page

**Tables:**
- Professional borders
- Alternate row colors
- Bold headers

**Charts:**
- Pie chart for means of finance
- Bar chart for 10-year revenue projections
- Line chart for cash flow

**Library:** ReportLab

**Input:** Complete DPR JSON data  
**Output:** `dpr_report.pdf`

---

#### Node 11: `generate_word` ✨ NEW
**Purpose:** Create editable Word document

**Document Structure:**
- Same content as PDF
- Editable format for customization
- Styles applied (Heading 1, 2, Body Text)
- Tables with proper formatting
- Page breaks between major sections

**Library:** python-docx

**Input:** Complete DPR JSON data  
**Output:** `dpr_report.docx`

---

#### Node 12: `generate_excel` ✨ NEW
**Purpose:** Create Excel workbook with financial data

**Workbook Structure:**

**Sheet 1: Project Summary**
- Cluster details
- Key financial ratios
- Summary table

**Sheet 2: Project Cost**
- Detailed breakdown table
- Total calculations
- Percentage distribution

**Sheet 3: Means of Finance**
- Funding sources
- Amount and percentage
- Pie chart

**Sheet 4: 10-Year Projections**
- Year-wise data
- Revenue, Expenses, Profit, Cash Flow
- Conditional formatting (green/red for profit/loss)

**Sheet 5: P&L Statements**
- Detailed Profit & Loss for 10 years
- Subtotals and totals

**Sheet 6: Cash Flow Statements**
- Sources and uses of cash
- Opening and closing balances

**Sheet 7: Balance Sheet**
- Assets, Liabilities, Equity
- Year-wise progression

**Sheet 8: Sensitivity Analysis**
- Base case vs 5% vs 10% reduction
- Comparison table
- Impact charts

**Sheet 9: Calculations Reference**
- Formulas used
- Assumptions
- Notes

**Features:**
- Auto-width columns
- Freeze panes on headers
- Cell formatting (currency, percentage)
- Charts embedded
- Print-ready layout

**Library:** openpyxl

**Input:** Complete DPR JSON data  
**Output:** `dpr_financials.xlsx`

---

### Workflow

```
START
  ↓
[Nodes 1-9: All previous nodes from Phase 1-3]
  ↓
[Node 10: generate_pdf] ✨
  ↓
[Node 11: generate_word] ✨
  ↓
[Node 12: generate_excel] ✨
  ↓
END
```

---

### Output Files

```
outputs/
├── dpr_output.json              # From Phase 3
├── dpr_report.pdf               ✨ NEW (Complete DPR)
├── dpr_report.docx              ✨ NEW (Editable version)
└── dpr_financials.xlsx          ✨ NEW (Financial tables)
```

---

### Project Structure Updates

```
dpr-genie/
├── config.py
├── models.py
├── prompts.py
├── gemini_service.py
├── financial_calculations.py
│
├── document_generators.py       ✨ NEW
│   # Contains:
│   - PDFGenerator class
│   - WordGenerator class
│   - ExcelGenerator class
│
├── agent_workflow.py             # 3 new document nodes (total 12)
├── run.py
└── outputs/
    ├── dpr_output.json
    ├── dpr_report.pdf            ✨
    ├── dpr_report.docx           ✨
    └── dpr_financials.xlsx       ✨
```

---

### Dependencies Update

```txt
# Add to requirements.txt:
reportlab==4.0.9           # PDF generation
python-docx==1.1.0         # Word generation
openpyxl==3.1.2           # Excel generation
matplotlib==3.8.2         # Charts (optional)
pillow==10.1.0            # Image processing for charts
```

---

### Success Criteria

- ✅ PDF generated with all sections
- ✅ PDF professionally formatted (cover, TOC, sections)
- ✅ Word document editable and styled
- ✅ Excel workbook with 9 sheets
- ✅ All tables formatted properly
- ✅ Charts embedded correctly
- ✅ File sizes reasonable (<10MB each)
- ✅ Documents print-ready
- ✅ Execution time: 10-12 minutes total

---

### Limitations (Phase 4)

- ❌ No API (still CLI only)
- ❌ No web interface
- ❌ No database storage
- ❌ No user authentication
- ❌ No collaborative editing

---

## 📌 PHASE 5: REST API Wrapper {#phase-5}

### Objective
Wrap the working native agent in FastAPI to expose as HTTP REST API

### Duration
1 week

### Complexity
Low

---

### API Architecture

```
┌─────────────────────────────────────┐
│        Client (Postman/Frontend)    │
└──────────────┬──────────────────────┘
               │ HTTP Request (JSON)
               ▼
┌─────────────────────────────────────┐
│          FastAPI Server             │
│  ┌───────────────────────────────┐  │
│  │     API Routes/Endpoints      │  │
│  └──────────────┬────────────────┘  │
│                 │                    │
│                 ▼                    │
│  ┌───────────────────────────────┐  │
│  │   Native Agent (Phase 1-4)    │  │
│  │   - LangGraph Workflow        │  │
│  │   - Gemini AI                 │  │
│  │   - Financial Calculations    │  │
│  │   - Document Generation       │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
               │
               ▼
         File System
    (Generated DPR files)
```

---

### API Endpoints

#### 1. `POST /api/v1/generate-dpr`
**Purpose:** Generate complete DPR from user input

**Request:**
```json
{
  "cluster_name": "Printing Cluster Tirupati",
  "industry": "printing",
  "city": "Tirupati",
  // ... all user input fields
}
```

**Response:**
```json
{
  "status": "success",
  "message": "DPR generated successfully",
  "job_id": "dpr_20250115_143025_abc123",
  "data": {
    "sections": { "..." },
    "financials": { "..." }
  },
  "files": {
    "pdf": "/api/v1/download/dpr_20250115_143025_abc123/pdf",
    "word": "/api/v1/download/dpr_20250115_143025_abc123/word",
    "excel": "/api/v1/download/dpr_20250115_143025_abc123/excel",
    "json": "/api/v1/download/dpr_20250115_143025_abc123/json"
  },
  "generated_at": "2025-01-15T14:30:25",
  "execution_time_seconds": 645
}
```

**Status Codes:**
- 200: Success
- 400: Invalid input
- 500: Generation error

---

#### 2. `POST /api/v1/validate-input`
**Purpose:** Validate user input before generation

**Request:**
```json
{
  "cluster_name": "Test Cluster",
  "num_units": -5,
  // ... fields
}
```

**Response:**
```json
{
  "valid": false,
  "errors": [
    "num_units must be greater than 0",
    "current_turnover is required",
    "machinery_list cannot be empty"
  ],
  "warnings": [
    "cluster_age seems unusually high (150 years)"
  ]
}
```

---

#### 3. `GET /api/v1/download/{job_id}/{file_type}`
**Purpose:** Download generated files

**Parameters:**
- `job_id`: Unique identifier from generation
- `file_type`: pdf | word | excel | json

**Response:**
- File download with appropriate headers
- Content-Type: application/pdf | application/vnd.openxmlformats-officedocument.wordprocessingml.document | etc.

**Example:**
```
GET /api/v1/download/dpr_20250115_143025_abc123/pdf
```

---

#### 4. `GET /api/v1/status/{job_id}`
**Purpose:** Check generation status (for async implementation)

**Response:**
```json
{
  "job_id": "dpr_20250115_143025_abc123",
  "status": "processing",
  "progress": 65,
  "current_step": "Generating financial projections",
  "steps_completed": [
    "Input validation",
    "Executive summary",
    "Cluster profile",
    "Industry analysis"
  ],
  "steps_remaining": [
    "Financial projections",
    "Document generation"
  ],
  "estimated_time_remaining_seconds": 180
}
```

---

#### 5. `GET /api/v1/health`
**Purpose:** Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0",
  "gemini_api": "connected",
  "timestamp": "2025-01-15T14:30:25"
}
```

---

#### 6. `GET /api/v1/templates`
**Purpose:** List available industry templates

**Response:**
```json
{
  "templates": [
    {
      "id": "printing",
      "name": "Printing Cluster",
      "description": "For printing and publishing clusters"
    },
    {
      "id": "food_processing",
      "name": "Food Processing Cluster",
      "description": "For food and agro-processing clusters"
    }
  ]
}
```

---

### Project Structure

```
dpr-genie/
├── agent/                        # Native agent (Phase 1-4)
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── prompts.py
│   ├── gemini_service.py
│   ├── financial_calculations.py
│   ├── document_generators.py
│   └── agent_workflow.py
│
├── api/                          ✨ NEW
│   ├── __init__.py
│   ├── main.py                   # FastAPI app
│   ├── routes.py                 # API endpoints
│   ├── schemas.py                # Request/Response models
│   └── dependencies.py           # Shared dependencies
│
├── run_agent.py                  # CLI mode (Phase 1-4)
├── run_api.py                    ✨ NEW (API mode)
│
└── outputs/                      # Generated files
```

---

### Key Files

#### `api/main.py`
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router

app = FastAPI(
    title="AI-DPR Genie API",
    description="AI-powered DPR Generation for MSMEs",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router, prefix="/api/v1")

@app.get("/")
def root():
    return {
        "message": "AI-DPR Genie API",
        "version": "1.0.0",
        "docs": "/docs"
    }
```

#### `api/routes.py`
```python
from fastapi import APIRouter, HTTPException
from agent.agent_workflow import run_agent
from api.schemas import UserInputSchema, DPRResponseSchema

router = APIRouter()

@router.post("/generate-dpr", response_model=DPRResponseSchema)
async def generate_dpr(input_data: UserInputSchema):
    try:
        result = await run_agent(input_data.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ... other endpoints
```

---

### How to Run

**CLI Mode (Phase 1-4 still works):**
```bash
python run_agent.py --input user_input.json
```

**API Mode:**
```bash
python run_api.py

# Server starts at:
# http://localhost:8000

# API Docs at:
# http://localhost:8000/docs
```

**API Usage Examples:**

```bash
# Generate DPR
curl -X POST http://localhost:8000/api/v1/generate-dpr \
  -H "Content-Type: application/json" \
  -d @user_input.json

# Validate input
curl -X POST http://localhost:8000/api/v1/validate-input \
  -H "Content-Type: application/json" \
  -d @user_input.json

# Download PDF
curl -X GET http://localhost:8000/api/v1/download/job123/pdf \
  --output dpr_report.pdf

# Health check
curl -X GET http://localhost:8000/api/v1/health
```

---

### Dependencies Update

```txt
# Add to requirements.txt:
fastapi==0.109.0
uvicorn[standard]==0.27.0
python-multipart==0.0.6
aiofiles==23.2.1
```

---

### Success Criteria

- ✅ API server starts successfully
- ✅ All 6 endpoints functional
- ✅ Can generate DPR via API
- ✅ Can download all file types
- ✅ Input validation works
- ✅ Error handling proper
- ✅ API documentation (Swagger) available
- ✅ CORS configured
- ✅ CLI mode still works independently
- ✅ Response times reasonable (<15 minutes for full DPR)

---

### Limitations (Phase 5)

- ❌ No web frontend (API only)
- ❌ No user authentication
- ❌ No database (files stored in file system)
- ❌ No job queue for async processing
- ❌ No rate limiting
- ❌ No monitoring/analytics

---

## 📌 PHASE 6: Frontend {#phase-6}

### Objective
Build web interface for user-friendly DPR generation

### Duration
2-3 weeks

### Complexity
Medium-High

---

### Approach

#### Option 1: PoC with Streamlit (Quick)
- Rapid prototype
- Python-based
- Interactive forms
- Basic file upload/download
- **Time:** 1 week

#### Option 2: Production with React.js (Complete)
- Professional UI/UX
- Multi-step wizard form
- Real-time validation
- Progress tracking
- Download management
- Responsive design
- **Time:** 2-3 weeks

---

### Key Features

**1. User Registration/Login** (Optional)
- Email/password
- OAuth (Google, Microsoft)
- Guest mode

**2. DPR Creation Wizard**
- Step 1: Basic Information
- Step 2: Cluster Profile
- Step 3: Land & Building
- Step 4: Machinery List
- Step 5: Problems & Targets
- Step 6: Review & Generate

**3. Progress Tracking**
- Real-time status updates
- Current node being executed
- Estimated time remaining
- Visual progress bar

**4. Results Dashboard**
- View generated DPR sections
- Download files (PDF, Word, Excel)
- Share via email
- Print preview

**5. History & Management**
- View past DPRs
- Edit and regenerate
- Delete old DPRs
- Search and filter

**6. Templates**
- Pre-filled examples by industry
- Sample data for testing
- Quick start templates

---

### Technology Stack

**Frontend:**
- React.js 18
- TypeScript
- Tailwind CSS
- React Hook Form (validation)
- React Query (API calls)
- Zustand (state management)

**Build:**
- Vite
- ESLint
- Prettier

---

### Project Structure

```
dpr-genie-frontend/
├── public/
├── src/
│   ├── components/
│   │   ├── forms/
│   │   ├── layout/
│   │   └── ui/
│   ├── pages/
│   │   ├── HomePage.tsx
│   │   ├── CreateDPRPage.tsx
│   │   ├── ResultsPage.tsx
│   │   └── HistoryPage.tsx
│   ├── services/
│   │   └── api.ts
│   ├── hooks/
│   ├── utils/
│   └── App.tsx
├── package.json
└── vite.config.ts
```

---

### Success Criteria

- ✅ User-friendly multi-step form
- ✅ Real-time input validation
- ✅ Progress tracking during generation
- ✅ Download all file formats
- ✅ Responsive design (mobile-friendly)
- ✅ Fast load times (<2s)
- ✅ Intuitive UX
- ✅ Error handling and user feedback

---

### Limitations

- ❌ No database yet (uses API only)
- ❌ No user authentication persistence
- ❌ No collaborative editing
- ❌ No version control for DPRs

---

**Note:** Detailed specifications to be defined when starting Phase 6

---

## 📌 PHASE 7: Database Integration {#phase-7}

### Objective
Add persistent storage for users, DPRs, and analytics

### Duration
1-2 weeks

### Complexity
Medium

---

### Database Schema

#### Tables/Collections

**1. Users**
```
- id (UUID)
- email
- password_hash
- name
- organization
- role (admin/user)
- created_at
- last_login
```

**2. DPRs**
```
- id (UUID)
- user_id (FK)
- cluster_name
- industry
- status (draft/completed/failed)
- input_data (JSON)
- output_data (JSON)
- file_paths (JSON: pdf, word, excel)
- created_at
- updated_at
- version
```

**3. Templates**
```
- id (UUID)
- name
- industry
- default_data (JSON)
- created_by
- is_public
```

**4. Analytics**
```
- id (UUID)
- dpr_id (FK)
- generation_time_seconds
- file_sizes (JSON)
- api_calls_count
- timestamp
```

---

### Technology Options

**Option 1: PostgreSQL**
- Relational database
- Strong consistency
- Complex queries
- Mature ecosystem

**Option 2: MongoDB**
- Document database
- Flexible schema
- JSON-native
- Easy scaling

**Recommendation:** PostgreSQL for structured financial data

---

### ORM/ODM

- **SQLAlchemy** (for PostgreSQL)
- **Alembic** (migrations)
- **Motor** (async MongoDB, if chosen)

---

### Key Features

**1. User Management**
- Registration, login, logout
- Password reset
- Profile management
- Role-based access control

**2. DPR Persistence**
- Save drafts
- Auto-save functionality
- Load previous DPRs
- Version history

**3. Search & Filter**
- Search by cluster name
- Filter by industry, date
- Sort by creation date

**4. Sharing**
- Generate shareable links
- Permission management
- Export to cloud (Google Drive, etc.)

**5. Analytics**
- Usage statistics
- Most common industries
- Average generation time
- Success/failure rates
- User activity logs

---

### API Updates

New endpoints:
- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `GET /api/v1/dprs` (list user's DPRs)
- `GET /api/v1/dprs/{id}` (get specific DPR)
- `PUT /api/v1/dprs/{id}` (update DPR)
- `DELETE /api/v1/dprs/{id}` (delete DPR)
- `GET /api/v1/analytics/dashboard`

---

### Success Criteria

- ✅ User authentication working
- ✅ DPRs saved to database
- ✅ Load previous DPRs
- ✅ Search and filter functional
- ✅ Analytics dashboard
- ✅ Database backups configured
- ✅ Migration system in place

---

**Note:** Detailed specifications to be defined when starting Phase 7

---

## 🛠️ Technology Stack {#technology-stack}

### Core Technologies

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Language** | Python | 3.11+ | Core development |
| **AI Framework** | LangGraph | 0.0.20+ | Agent orchestration |
| **LLM** | Google Gemini | 1.5 Pro | Content generation |
| **API Framework** | FastAPI | 0.109+ | REST API server |
| **Financial Calc** | NumPy, Pandas | Latest | Financial modeling |
| **PDF Generation** | ReportLab | 4.0+ | PDF documents |
| **Word Generation** | python-docx | 1.1+ | Word documents |
| **Excel Generation** | openpyxl | 3.1+ | Excel workbooks |
| **Database** | PostgreSQL | 15+ | Data persistence |
| **ORM** | SQLAlchemy | 2.0+ | Database ORM |
| **Frontend** | React.js | 18+ | Web interface |
| **Styling** | Tailwind CSS | 3.0+ | UI styling |

---

### Development Tools

| Tool | Purpose |
|------|---------|
| **Git** | Version control |
| **GitHub** | Code repository |
| **VS Code** | IDE |
| **Postman** | API testing |
| **pytest** | Unit testing |
| **Docker** | Containerization (optional) |

---

### Dependencies Summary

```txt
# Phase 1-2
python-dotenv==1.0.0
langgraph==0.0.20
langchain-google-genai==0.0.6
google-generativeai==0.3.2
pydantic==2.5.3

# Phase 3
numpy==1.26.3
pandas==2.1.4

# Phase 4
reportlab==4.0.9
python-docx==1.1.0
openpyxl==3.1.2
matplotlib==3.8.2
pillow==10.1.0

# Phase 5
fastapi==0.109.0
uvicorn[standard]==0.27.0
python-multipart==0.0.6
aiofiles==23.2.1

# Phase 7
sqlalchemy==2.0.25
alembic==1.13.1
psycopg2-binary==2.9.9
```

---

## 📅 Project Timeline {#project-timeline}

### Overall Timeline: 9-11 Weeks

| Phase | Duration | Start | End | Status |
|-------|----------|-------|-----|--------|
| **Phase 1** | 1 week | Week 1 | Week 1 | 🟡 Pending |
| **Phase 2** | 1 week | Week 2 | Week 2 | 🟡 Pending |
| **Phase 3** | 2 weeks | Week 3 | Week 4 | 🟡 Pending |
| **Phase 4** | 1 week | Week 5 | Week 5 | 🟡 Pending |
| **Phase 5** | 1 week | Week 6 | Week 6 | 🟡 Pending |
| **Phase 6** | 2-3 weeks | Week 7 | Week 9 | 🟡 Pending |
| **Phase 7** | 1-2 weeks | Week 10 | Week 11 | 🟡 Pending |

---

### Milestone Checklist

**Phase 1 Complete:**
- [ ] 3 nodes working (validate, exec summary, cluster profile)
- [ ] Gemini integration functional
- [ ] Output saved to text file
- [ ] Execution time < 5 minutes

**Phase 2 Complete:**
- [ ] All 6 nodes working
- [ ] All text sections generated
- [ ] SWOT in JSON format
- [ ] Output saved to JSON

**Phase 3 Complete:**
- [ ] Financial calculations accurate
- [ ] 10-year projections generated
- [ ] All ratios meet MSE-CDP guidelines
- [ ] Sensitivity analysis complete

**Phase 4 Complete:**
- [ ] PDF, Word, Excel generated
- [ ] All documents professionally formatted
- [ ] File sizes reasonable
- [ ] Print-ready quality

**Phase 5 Complete:**
- [ ] API server running
- [ ] All endpoints functional
- [ ] Documentation available
- [ ] CLI mode still works

**Phase 6 Complete:**
- [ ] Web interface deployed
- [ ] Multi-step form working
- [ ] File downloads functional
- [ ] Mobile responsive

**Phase 7 Complete:**
- [ ] Database connected
- [ ] User authentication working
- [ ] DPRs persisted
- [ ] Analytics dashboard live

---

## 📄 Document Control

**Version:** 1.0  
**Date:** January 2025  
**Status:** Approved ✅  
**Next Review:** After Phase 1 completion

