# AI-DPR Genie

AI-powered Detailed Project Report (DPR) Generator for MSME Clusters under MSE-CDP Scheme.

## 📋 Project Overview

**Phase 1**: Basic Text Generation  
Generates Executive Summary and Cluster Profile sections using LangGraph and Google Gemini AI.

---

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.11+
- Google Gemini API Key (set in environment)

### 2. Installation

```bash
# Clone/download the project
cd dpr-genie

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Setup Environment

Make sure `GEMINI_API_KEY` is set in your environment (already in .bashrc):

```bash
# Verify API key is set
echo $GEMINI_API_KEY
```

### 4. Run the Agent

```bash
# Generate DPR using sample input
python main.py --input user_input.json

# Specify output directory
python main.py --input user_input.json --output-dir outputs

# Generate only JSON output
python main.py --input user_input.json --format json

# Generate only text output
python main.py --input user_input.json --format text
```

---

## 📁 Project Structure

```
dpr-genie/
├── .env                    # Environment variables (optional)
├── .gitignore             # Git ignore patterns
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── config.py             # Configuration settings
├── models.py             # Pydantic data models
├── prompts.py            # AI prompt templates
├── gemini_service.py     # Gemini API wrapper
├── agent_workflow.py     # LangGraph agent (3 nodes)
├── main.py               # Entry point
├── user_input.json       # Sample input
└── outputs/              # Generated DPR files
```

---

## 📝 Input Format

Create a JSON file with the following structure:

```json
{
  "cluster_name": "Your Cluster Name",
  "industry": "printing",
  "city": "City Name",
  "district": "District Name",
  "state": "State Name",
  "num_units": 100,
  "num_micro": 90,
  "num_small": 10,
  "num_medium": 0,
  "current_turnover": 50.00,
  "direct_employment": 500,
  "indirect_employment": 2000,
  "products": [
    "Product 1",
    "Product 2",
    "Product 3"
  ],
  "cluster_age": 50
}
```

**Supported Industries:**
- `printing`
- `food_processing`
- `textiles`
- `leather`
- `engineering`
- `handicrafts`
- `pottery`
- `carpentry`

---

## 📤 Output

The agent generates two types of output files in the `outputs/` directory:

### 1. Text Format (`dpr_output_TIMESTAMP.txt`)
Formatted text document with:
- Executive Summary
- Cluster Profile

### 2. JSON Format (`dpr_output_TIMESTAMP.json`)
Structured JSON with:
- Metadata (cluster name, timestamp, execution time)
- User input (original data)
- Generated sections

---

## 🔧 Configuration

Edit `config.py` to customize:

- `GEMINI_MODEL`: Gemini model version (default: gemini-1.5-pro)
- `GEMINI_TEMPERATURE`: Creativity level (default: 0.7)
- `GEMINI_MAX_TOKENS`: Maximum output length (default: 2048)
- `LOG_LEVEL`: Logging verbosity (default: INFO)

---

## 🧪 Testing Gemini Connection

```bash
# Test if Gemini API is working
python gemini_service.py
```

---

## 🎯 Phase 1 Features

**3 LangGraph Nodes:**
1. **validate_input** - Validates user input data
2. **generate_executive_summary** - Generates executive summary (400-500 words)
3. **generate_cluster_profile** - Generates cluster profile (600-800 words)

**Current Capabilities:**
- ✅ Input validation with Pydantic
- ✅ AI-powered content generation using Gemini
- ✅ Executive summary generation
- ✅ Cluster profile generation
- ✅ Text and JSON output formats
- ✅ Error handling and logging

**Limitations (Phase 1):**
- ❌ No financial calculations
- ❌ No SWOT analysis
- ❌ No industry analysis
- ❌ No PDF/Word/Excel generation
- ❌ No REST API
- ❌ No web interface

---

## 🛣️ Roadmap

- **Phase 2**: Complete Text Sections (Industry Analysis, SWOT, Problems/Interventions)
- **Phase 3**: Financial Calculations (10-year projections, IRR, NPV, ROCE)
- **Phase 4**: Document Generation (PDF, Word, Excel)
- **Phase 5**: REST API Wrapper
- **Phase 6**: Web Frontend
- **Phase 7**: Database Integration

---

## 📊 Example Execution

```bash
$ python main.py --input user_input.json

================================================================================
AI-DPR GENIE - PHASE 1: BASIC TEXT GENERATION
================================================================================
Input File: user_input.json
Output Directory: outputs
Output Format: both
================================================================================

2025-01-15 14:30:00 - INFO - Loading user input from: user_input.json
2025-01-15 14:30:00 - INFO - ✓ User input loaded successfully
2025-01-15 14:30:00 - INFO - Validating input schema...
2025-01-15 14:30:00 - INFO - ✓ Input schema valid
2025-01-15 14:30:00 - INFO - Creating DPR Agent...
2025-01-15 14:30:01 - INFO - ✓ DPR Agent initialized successfully
2025-01-15 14:30:01 - INFO - Starting DPR generation...

============================================================
STARTING DPR GENERATION WORKFLOW
============================================================

============================================================
NODE 1: VALIDATING INPUT
============================================================
2025-01-15 14:30:01 - INFO - ✓ Input validation PASSED

============================================================
NODE 2: GENERATING EXECUTIVE SUMMARY
============================================================
2025-01-15 14:30:05 - INFO - ✓ Executive Summary generated (2847 characters)

============================================================
NODE 3: GENERATING CLUSTER PROFILE
============================================================
2025-01-15 14:30:12 - INFO - ✓ Cluster Profile generated (4512 characters)

============================================================
✓ DPR GENERATION COMPLETED in 11.23 seconds
============================================================

2025-01-15 14:30:12 - INFO - ✓ Text output saved to: outputs/dpr_output_20250115_143012.txt
2025-01-15 14:30:12 - INFO - ✓ JSON output saved to: outputs/dpr_output_20250115_143012.json

================================================================================
✓ DPR GENERATION SUCCESSFUL!
================================================================================

Cluster: Printing Cluster Tirupati
Execution Time: 11.23 seconds

Generated Files:
  • outputs/dpr_output_20250115_143012.txt
  • outputs/dpr_output_20250115_143012.json

================================================================================
```

---

## 🐛 Troubleshooting

**Issue: "GEMINI_API_KEY not found"**
```bash
# Check if API key is set
echo $GEMINI_API_KEY

# If not set, add to .bashrc or .env file
export GEMINI_API_KEY="your_api_key_here"
```

**Issue: "Module not found"**
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

**Issue: "Gemini API error"**
- Check your API key is valid
- Ensure you have internet connection
- Verify API quota/limits

---

## 📄 License

[Your License Here]

---

## 🤝 Contributing

This is Phase 1 of the project. More features coming in subsequent phases.

---

## 📧 Contact

[Your Contact Information]

---

**Version**: 1.0.0 (Phase 1)  
**Last Updated**: January 2025
