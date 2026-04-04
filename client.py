import requests
from model import PricingAction


class PricingEnvClient:

    def __init__(self, base_url="http://127.0.0.1:8000"):
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