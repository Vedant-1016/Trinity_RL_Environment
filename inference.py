from client import PricingEnvClient
from model import PricingAction
from tasks import get_task_config
from grader import compute_score
import os

# REQUIRED ENV VARIABLES (for compliance)
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
HF_TOKEN = os.getenv("HF_TOKEN")


def run_task(task_name):

    print(f"[START] task={task_name}")

    config = get_task_config(task_name)

    env = PricingEnvClient()

    obs = env.reset(config)

    total_reward = 0
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
        reward = result["reward"]
        done = result["done"]

        total_reward += reward
        step_count += 1

        # ✅ REQUIRED STRUCTURED LOG
        print(
            f"[STEP] task={task_name} step={step_count} price={price} reward={reward} inventory={obs['inventory']}"
        )

        if done:
            break

    max_profit = {
    "easy": 10000,
    "medium": 12000,
    "hard": 15000
}[task_name]
    score = compute_score(total_reward, max_profit)

    # ✅ REQUIRED FINAL LOG
    print(
        f"[END] task={task_name} total_profit={total_reward} score={score}"
    )


if __name__ == "__main__":

    for task in ["easy", "medium", "hard"]:
        run_task(task)