import asyncio
from typing import Any, Dict, List

import aiohttp


class OddsIngestor:
    """Fetches live odds from various sources."""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = "https://api.the-odds-api.com/v4/sports"

    async def fetch(self, sport: str = "soccer_epl") -> List[Dict[str, Any]]:
        """Fetch odds for a given sport from The Odds API."""
        url = f"{self.base_url}/{sport}/odds"
        params = {"apiKey": self.api_key, "regions": "us", "markets": "h2h"}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, timeout=10) as resp:
                resp.raise_for_status()
                return await resp.json()


class RundownIngestor:
    """Fetch odds from TheRundown's free API."""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = "https://therundown.io/api/v1"

    async def fetch(self, sport_id: str = "3") -> List[Dict[str, Any]]:
        """Fetch odds for a given sport from TheRundown API."""
        url = f"{self.base_url}/sports/{sport_id}/events"
        params = {"apikey": self.api_key, "include": "all_odds"}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, timeout=10) as resp:
                resp.raise_for_status()
                data = await resp.json()
                return data.get("events", [])


async def main():
    ingestor = OddsIngestor(api_key="YOUR_API_KEY")
    data = await ingestor.fetch()
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
