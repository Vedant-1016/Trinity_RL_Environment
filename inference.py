from client import PricingEnvClient
from model import PricingAction
from tasks import get_task_config
from grader import compute_score


def run_task(task_name):

    config = get_task_config(task_name)

    env = PricingEnvClient()

    obs = env.reset(config)

    total_reward = 0
    price = 100

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

        if done:
            break

    # assume rough max profit
    max_profit = 10000

    score = compute_score(total_reward, max_profit)

    print(f"TASK: {task_name} | PROFIT: {total_reward} | SCORE: {score}")

if __name__ == "__main__":

    for task in ["easy", "medium", "hard"]:
        run_task(task)