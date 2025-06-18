from typing import Any, Dict, List


def normalize_odds(raw: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Convert odds into decimal format and unify event identifiers."""
    normalized = []
    for event in raw:
        for book in event.get("bookmakers", []):
            for market in book.get("markets", []):
                for outcome in market.get("outcomes", []):
                    # convert American odds to decimal if necessary
                    price = outcome.get("price")
                    if price is None:
                        continue
                    if price >= 0:
                        decimal = 1 + price / 100
                    else:
                        decimal = 1 - 100 / price
                    normalized.append(
                        {
                            "event": event.get("id"),
                            "bookmaker": book.get("title"),
                            "outcome": outcome.get("name"),
                            "odds": decimal,
                        }
                    )
    return normalized
