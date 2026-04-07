def compute_score(total_profit, max_possible_profit):

    epsilon = 1e-6

    # 🛑 avoid division issues
    if max_possible_profit <= 0:
        return epsilon

    score = total_profit / max_possible_profit

    # 🛑 handle NaN or weird values
    if not isinstance(score, (int, float)):
        return epsilon

    # 🛑 clamp strictly inside (0,1)
    if score <= 0:
        return epsilon
    if score >= 1:
        return 1.0 - epsilon

    return score