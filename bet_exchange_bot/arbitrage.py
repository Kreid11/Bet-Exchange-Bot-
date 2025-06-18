from collections import defaultdict
from typing import List, Dict, Any, Optional


def find_two_way_arbitrage(odds: List[Dict[str, Any]], threshold: float = 1.0) -> Optional[Dict[str, Any]]:
    """Return an arbitrage opportunity if found.

    Args:
        odds: list of normalized odds records.
        threshold: sum of inverse odds must be below this number to be an arb.
    """
    if len(odds) < 2:
        return None

    # group by outcome
    by_outcome: Dict[str, Dict[str, Any]] = {}
    for item in odds:
        out = item["outcome"]
        if out not in by_outcome or item["odds"] > by_outcome[out]["odds"]:
            by_outcome[out] = item

    if len(by_outcome) != 2:
        return None

    outcomes = list(by_outcome.values())
    inv_sum = sum(1 / o["odds"] for o in outcomes)
    if inv_sum < threshold:
        margin = 1 - inv_sum
        return {"margin": margin, "legs": outcomes}
    return None


def scan_two_way_arbitrage(odds: List[Dict[str, Any]], threshold: float = 1.0) -> List[Dict[str, Any]]:
    """Scan a list of normalized odds for arbitrage opportunities by event."""

    events: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for record in odds:
        events[record.get("event")].append(record)

    results: List[Dict[str, Any]] = []
    for event_id, records in events.items():
        arb = find_two_way_arbitrage(records, threshold)
        if arb:
            arb["event"] = event_id
            results.append(arb)

    return results
