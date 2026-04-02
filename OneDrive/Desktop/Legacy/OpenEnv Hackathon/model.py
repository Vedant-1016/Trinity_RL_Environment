from pydantic import BaseModel
from typing import Optional


# ---------------------------
# ACTION
# ---------------------------
class PricingAction(BaseModel):
    price: float  # price set by the agent


# ---------------------------
# OBSERVATION (what agent sees)
# ---------------------------
class PricingObservation(BaseModel):
    day: int
    inventory: int
    last_sales: int
    last_price: float
    competitor_price: float
    demand_trend: str  # "increasing", "decreasing", "stable"


# ---------------------------
# STATE (internal, full info)
# ---------------------------
class PricingState(BaseModel):
    day: int
    inventory: int
    max_days: int

    last_sales: int
    last_price: float

    competitor_price: float
    demand_trend: str

    # hidden variables (not shown to agent)
    base_demand: float