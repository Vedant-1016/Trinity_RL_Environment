def get_task_config(task_name: str):

    if task_name == "easy":
        return {
            "inventory": 120,
            "base_demand": 100,
            "max_days": 20,
            "competitor_price": 100,
            "demand_volatility": 2
        }

    elif task_name == "medium":
        return {
            "inventory": 100,
            "base_demand": 80,
            "max_days": 30,
            "competitor_price": 100,
            "demand_volatility": 5
        }

    elif task_name == "hard":
        return {
            "inventory": 80,
            "base_demand": 60,
            "max_days": 40,
            "competitor_price": 110,
            "demand_volatility": 10
        }

    else:
        raise ValueError("Invalid task name")