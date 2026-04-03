from client import PricingEnvClient
from model import PricingAction

env = PricingEnvClient()

obs = env.reset()
print("RESET:", obs)

result = env.step(PricingAction(price=100))
print("STEP:", result)