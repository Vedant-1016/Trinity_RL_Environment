from client import PricingEnvClient
from model import PricingAction


def run_episode():

    env = PricingEnvClient()

    obs = env.reset()
    print("START:", obs)

    total_reward = 0

    price = 100  # initial price

    while True:

        # simple strategy
        if obs["last_sales"] > 20:
            price += 5
        elif obs["last_sales"] < 10:
            price -= 5

        # keep price in reasonable range
        price = max(10, min(price, 200))

        result = env.step(PricingAction(price=price))

        obs = result["observation"]
        reward = result["reward"]
        done = result["done"]

        total_reward += reward

        print(f"DAY {obs['day']} | PRICE {price} | SALES {obs['last_sales']} | PROFIT {reward}")

        if done:
            break

    print("\nTOTAL PROFIT:", total_reward)


if __name__ == "__main__":
    run_episode()