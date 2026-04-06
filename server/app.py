from fastapi import FastAPI
from model import PricingAction
from server.pricing_env import PricingEnv
from typing import Optional, Dict

app = FastAPI()

# Create single environment instance
env = PricingEnv()


# -------------------------
# RESET
# -------------------------
@app.post("/reset")
def reset(config: Optional[Dict] = None):
    obs = env.reset(config)
    return obs.model_dump()

@app.get("/")
def home():
    return {
        "message": "Pricing Environment API 🚀",
        "docs": "https://vedant-10-pricing-environment.hf.space/docs ",
        "usage": "Use /reset and /step endpoints"
    }
# -------------------------
# STEP
# -------------------------
@app.post("/step")
def step(action: PricingAction):
    obs, reward, done, info = env.step(action)
    
    return {
        "observation": obs.model_dump(),
        "reward": reward,
        "done": done,
        "info": info
    }


# -------------------------
# STATE (optional but useful)
# -------------------------
@app.get("/state")
def state():
    return env.state.model_dump()