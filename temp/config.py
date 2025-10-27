"""
Configuration settings for AI-DPR Genie
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file (optional, for overrides)
load_dotenv()

# ============================================
# API Configuration
# ============================================

# Gemini API Key - Load from system environment first, then .env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found in environment variables. "
        "Please set it in your .bashrc or .env file"
    )

# Gemini Model
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")

# ============================================
# Application Settings
# ============================================

# Environment
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Logging Level
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()


# ============================================
# Paths
# ============================================

# Base directory
BASE_DIR = Path(__file__).parent

# Outputs directory
OUTPUTS_DIR = BASE_DIR / "outputs"

# Create outputs directory if it doesn't exist
OUTPUTS_DIR.mkdir(exist_ok=True)

# ============================================
# Agent Configuration
# ============================================

# Gemini Generation Settings
GEMINI_TEMPERATURE = 0.7
GEMINI_MAX_TOKENS = 2048
GEMINI_TOP_P = 0.95
GEMINI_TOP_K = 40

# ============================================
# Validation
# ============================================

print(f"✓ Configuration loaded successfully")
print(f"✓ Environment: {ENVIRONMENT}")
print(f"✓ Gemini Model: {GEMINI_MODEL}")
print(f"✓ Outputs Directory: {OUTPUTS_DIR}")

