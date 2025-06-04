# Bet Exchange Bot

This repository contains a skeleton implementation of a sports betting arbitrage and analytics system.
It ingests odds from multiple sources, searches for arbitrage and value bets, applies bankroll and
stake sizing logic, and can automate bet placement.
It uses free data sources like TheRundown.io along with The Odds API.

The code is intentionally minimal and focuses on the structure outlined in the architecture plan.
All modules include basic functions and placeholder implementations so the project can be developed
further.

## Structure
- `bet_exchange_bot/ingestion.py` - fetches odds data from The Odds API and the free TheRundown API.
- `bet_exchange_bot/normalization.py` – converts odds formats and matches events.
- `bet_exchange_bot/arbitrage.py` – scans for arbitrage opportunities.
- `bet_exchange_bot/predictive.py` – contains simple predictive model stubs.
- `bet_exchange_bot/staking.py` – bankroll and stake calculations using Kelly criterion.
- `bet_exchange_bot/execution.py` – hooks for automating bet placement.
- `bet_exchange_bot/alerts.py` – basic Telegram alert sender.
- `bet_exchange_bot/server.py` – FastAPI application orchestrating the workflow.

## Requirements
- Python 3.10+
- `aiohttp`, `pydantic`, `fastapi`, `uvicorn`

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Running
The project currently only provides a basic FastAPI application. It fetches odds from The Odds API and TheRundown to demonstrate free data ingestion. Run it with:
```bash
uvicorn bet_exchange_bot.server:app --reload
```
