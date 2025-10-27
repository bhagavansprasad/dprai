# DPR Automation Platform - Stage 1

## Files Overview

```
├── config.py              # Configuration (LLM model, settings)
├── lg_utility.py          # Utility functions (graph visualization, state dump)
├── dpr_orchestrator.py    # Main orchestrator graph with dummy nodes
└── dpr_main.py           # Entry point to test the orchestrator
```

## Setup Instructions

### 1. Prerequisites

```bash
pip install langgraph langchain-google-vertexai langchain-core termcolor
```

### 2. Google Cloud Setup (for Gemini)

Make sure you have:
- Google Cloud project with Vertex AI API enabled
- Authentication set up (gcloud auth application-default login)

### 3. Copy Files

Copy all 4 files to your project directory:
```bash
/home/bhagavan/aura/dprai/src/
├── config.py
├── lg_utility.py
├── dpr_orchestrator.py
└── dpr_main.py
```

## Running the Test

```bash
cd /home/bhagavan/aura/dprai/src/
python dpr_main.py
```

## Expected Output

You should see:
1. Graph building message
2. Each node executing in sequence:
   - ORCHESTRATOR_INIT (cyan)
   - COORDINATOR_AGENT (green)
   - WORKFLOW_PLANNER (yellow)
   - OUTPUT_FORMATTER (magenta)
3. Final JSON output with Stage 1 completion status
4. Graph PNG file generated: `dpr_orchestrator_graph.png`

## Graph Structure (Stage 1)

```
START 
  ↓
ORCHESTRATOR_INIT
  ↓
COORDINATOR_AGENT
  ↓
WORKFLOW_PLANNER
  ↓
OUTPUT_FORMATTER
  ↓
END
```

## Stage 1 Features

✅ **4 Dummy Nodes** - Skeleton functions ready  
✅ **Linear Flow** - Simple edge connections  
✅ **State Management** - DPRState with messages, project_data, dpr_sections  
✅ **Graph Visualization** - PNG generation  
✅ **Colored Output** - Easy flow tracking  

## Next Steps (Stage 2)

After Stage 1 is tested successfully, we'll add:
- Data Collection Agent
- Input validation
- User interaction flow

## Troubleshooting

**Import Error:**
- Make sure all 4 files are in the same directory
- Check that dependencies are installed

**Google Cloud Auth Error:**
- Run: `gcloud auth application-default login`
- Verify Vertex AI API is enabled in your project

**Graph PNG not generated:**
- This is optional - the orchestrator will still work
- Requires graphviz: `pip install graphviz`