import asyncio
from fastapi import FastAPI

from .ingestion import SportsGameOddsIngestor
from .normalization import normalize_odds
from .arbitrage import scan_two_way_arbitrage

app = FastAPI()


@app.get("/ping")
def ping() -> dict:
    return {"status": "ok"}


@app.on_event("startup")
async def startup() -> None:
    # Example background task to fetch odds and search for an arbitrage
    async def worker() -> None:
        odds_data = []
        ingestor = SportsGameOddsIngestor(api_key="YOUR_API_KEY")
        raw = await ingestor.fetch_sports()
        odds_data.extend(normalize_odds(raw))

        arbs = scan_two_way_arbitrage(odds_data)
        for arb in arbs:
            print("Arbitrage found", arb)

    asyncio.create_task(worker())
