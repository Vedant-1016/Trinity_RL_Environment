import requests
from model import PricingAction


import os

class PricingEnvClient:

    def __init__(self, base_url=None):
        if base_url is None:
            base_url = os.getenv(
                "API_BASE_URL",
                "https://vedant-10-pricing-environment.hf.space"
            )
        self.base_url = base_url

    # -------------------------
    # RESET
    # -------------------------
    def reset(self, config=None):
        response = requests.post(
            f"{self.base_url}/reset",
            json=config
        )
        print("CONFIG USED:", config)
        return response.json()

    # -------------------------
    # STEP
    # -------------------------
    def step(self, action: PricingAction):
        response = requests.post(
            f"{self.base_url}/step",
            json=action.model_dump()
        )
        return response.json()

    # -------------------------
    # STATE (optional)
    # -------------------------
    def state(self):
        response = requests.get(f"{self.base_url}/state")
        return response.json()