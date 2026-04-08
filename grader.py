def compute_score(total_profit, max_possible_profit):
    """
    Computes normalized score.
    """

    if max_possible_profit <= 0:
        return 0.0

    try:
        score = float(total_profit) / float(max_possible_profit)
    except Exception:
        return 0.0

    return score