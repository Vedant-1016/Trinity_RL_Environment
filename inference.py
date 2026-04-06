from client import PricingEnvClient
from model import PricingAction
from tasks import get_task_config
from grader import compute_score
import os

API_BASE_URL = os.getenv("API_BASE_URL", "https://vedant-10-pricing-environment.hf.space")
MODEL_NAME = os.getenv("MODEL_NAME", "pricing-agent")
HF_TOKEN = os.getenv("HF_TOKEN")

BENCHMARK = "pricing-env"


def run_task(task_name):

    print(f"[START] task={task_name} env={BENCHMARK} model={MODEL_NAME}", flush=True)

    config = get_task_config(task_name)
    env = PricingEnvClient()

    obs = env.reset(config)

    total_reward = 0
    rewards = []
    price = 100
    step_count = 0

    while True:

        if obs["last_sales"] > 20:
            price += 5
        elif obs["last_sales"] < 10:
            price -= 5

        price = max(10, min(price, 200))

        result = env.step(PricingAction(price=price))

        obs = result["observation"]
        reward = float(result["reward"])
        done = result["done"]

        total_reward += reward
        rewards.append(reward)
        step_count += 1

        print(
            f"[STEP] step={step_count} action=price({price}) reward={reward:.2f} done={str(done).lower()} error=null",
            flush=True
        )

        if done:
            break

    max_profit = {
        "easy": 15000,
        "medium": 12000,
        "hard": 8000
    }.get(task_name, 10000)

    score = compute_score(total_reward, max_profit)

    success = score > 0.0

    rewards_str = ",".join(f"{r:.2f}" for r in rewards)

    print(
        f"[END] success={str(success).lower()} steps={step_count} score={score:.3f} rewards={rewards_str}",
        flush=True
    )


if __name__ == "__main__":

    for task in ["easy", "medium", "hard"]:
        run_task(task)