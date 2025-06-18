from typing import Dict, Any


def naive_prediction(team_a: str, team_b: str) -> Dict[str, Any]:
    """Return a naive probability estimate for team_a winning."""
    # placeholder: 50/50 chance
    return {"team_a": team_a, "team_b": team_b, "p_win_a": 0.5}
