"""
Pydantic models for input validation and data structures
"""

from pydantic import BaseModel, Field, validator
from typing import List, Optional
from enum import Enum


# ============================================
# Enums
# ============================================

class IndustryType(str, Enum):
    """Supported industry types"""
    PRINTING = "printing"
    FOOD_PROCESSING = "food_processing"
    TEXTILES = "textiles"
    LEATHER = "leather"
    ENGINEERING = "engineering"
    HANDICRAFTS = "handicrafts"
    POTTERY = "pottery"
    CARPENTRY = "carpentry"


# ============================================
# Input Models (Phase 1)
# ============================================

class UserInput(BaseModel):
    """
    User input for Phase 1: Basic text generation
    Contains minimum required fields for executive summary and cluster profile
    """
    
    # Basic Information
    cluster_name: str = Field(..., min_length=3, description="Name of the cluster")
    industry: IndustryType = Field(..., description="Industry type")
    city: str = Field(..., min_length=2, description="City name")
    district: str = Field(..., min_length=2, description="District name")
    state: str = Field(..., min_length=2, description="State name")
    
    # Cluster Details
    num_units: int = Field(..., gt=0, description="Total number of units in cluster")
    num_micro: int = Field(default=0, ge=0, description="Number of micro units")
    num_small: int = Field(default=0, ge=0, description="Number of small units")
    num_medium: int = Field(default=0, ge=0, description="Number of medium units")
    
    # Financial
    current_turnover: float = Field(..., gt=0, description="Current annual turnover in Crores")
    
    # Employment
    direct_employment: int = Field(..., ge=0, description="Direct employment count")
    indirect_employment: int = Field(..., ge=0, description="Indirect employment count")
    
    # Products/Services
    products: List[str] = Field(..., min_items=1, description="List of products/services")
    
    # Other
    cluster_age: int = Field(..., gt=0, le=200, description="Age of cluster in years")
    
    @validator('num_micro', 'num_small', 'num_medium')
    def validate_unit_breakdown(cls, v, values):
        """Validate that unit breakdown doesn't exceed total units"""
        if 'num_units' in values:
            total_breakdown = values.get('num_micro', 0) + values.get('num_small', 0) + v
            if total_breakdown > values['num_units']:
                raise ValueError(
                    f"Sum of micro/small/medium units ({total_breakdown}) "
                    f"cannot exceed total units ({values['num_units']})"
                )
        return v
    
    class Config:
        """Pydantic config"""
        use_enum_values = True
        json_schema_extra = {
            "example": {
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
        }


# ============================================
# Output Models (Phase 1)
# ============================================

class ValidationResult(BaseModel):
    """Result of input validation"""
    valid: bool
    errors: List[str] = []
    warnings: List[str] = []


class DPROutputPhase1(BaseModel):
    """Output structure for Phase 1"""
    cluster_name: str
    executive_summary: str
    cluster_profile: str
    generated_at: str
    execution_time_seconds: float
