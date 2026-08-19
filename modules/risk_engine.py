def calculate_risk(
    balance,
    tx_count,
    registry_hit,
    linked_cases
):

    score = 0

    if balance > 1:
        score += 10

    if balance > 10:
        score += 20

    if balance > 100:
        score += 30

    if tx_count > 100:
        score += 10

    if tx_count > 1000:
        score += 20

    if registry_hit:
        score += 30

    score += (
        len(linked_cases) * 5
    )

    if score < 25:

        return score, "LOW"

    elif score < 50:

        return score, "MEDIUM"

    elif score < 75:

        return score, "HIGH"

    else:

        return score, "CRITICAL"
