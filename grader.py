def compute_score(total_profit, max_possible_profit):

    score = total_profit / max_possible_profit

    return max(0.0, min(score, 1.0))