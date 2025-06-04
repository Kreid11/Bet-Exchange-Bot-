from typing import Tuple


def kelly_stake(p: float, odds: float, bankroll: float, fraction: float = 0.5) -> float:
    """Compute fractional Kelly stake."""
    edge = p * (odds - 1) - (1 - p)
    if edge <= 0:
        return 0.0
    stake = bankroll * (edge / (odds - 1)) * fraction
    return max(stake, 0.0)


def arbitrage_stakes(o1: float, o2: float, total: float) -> Tuple[float, float]:
    """Split total stake between two outcomes to lock in profit."""
    inv_sum = 1 / o1 + 1 / o2
    s1 = total / (o1 * inv_sum)
    s2 = total / (o2 * inv_sum)
    return s1, s2
