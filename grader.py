def compute_score(total_profit, max_possible_profit):

    score = total_profit / max_possible_profit
    epsilon = 1e-6

    return max(epsilon, min(score, 1.0-epsilon))