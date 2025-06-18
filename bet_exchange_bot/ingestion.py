import asyncio
from typing import Any, Dict, List

import aiohttp


class SportsGameOddsIngestor:
    """Fetch data from the Sports Game Odds API."""

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = "https://api.sportsgameodds.com/v2"

    async def fetch_sports(self) -> List[Dict[str, Any]]:
        """Fetch the list of available sports."""
        url = f"{self.base_url}/sports/"
        headers = {"X-Api-Key": self.api_key}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=10) as resp:
                resp.raise_for_status()
                return await resp.json()


async def main() -> None:
    ingestor = SportsGameOddsIngestor(api_key="YOUR_API_KEY")
    data = await ingestor.fetch_sports()
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
