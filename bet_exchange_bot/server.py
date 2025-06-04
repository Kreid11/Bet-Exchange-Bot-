import asyncio
from fastapi import FastAPI

from .ingestion import OddsIngestor, RundownIngestor
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
        ingestor1 = OddsIngestor(api_key="YOUR_API_KEY")
        ingestor2 = RundownIngestor(api_key="YOUR_RUNDOWN_KEY")
        raw1 = await ingestor1.fetch()
        raw2 = await ingestor2.fetch()
        odds_data.extend(normalize_odds(raw1))
        odds_data.extend(normalize_odds(raw2))

        arbs = scan_two_way_arbitrage(odds_data)
        for arb in arbs:
            print("Arbitrage found", arb)

    asyncio.create_task(worker())
