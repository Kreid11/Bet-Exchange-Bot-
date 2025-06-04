# Bet-Exchange-Bot-
This is a seamless bot designed to profit from arb opportunities.

## Telegram Configuration
The workflow sends latency and arbitrage information via Telegram. Set the following
environment variables before running the workflow:

- `TELEGRAM_TOKEN` – Bot token from BotFather
- `TELEGRAM_CHAT_ID` – Chat ID where notifications are sent

Latency details are included in the Telegram message sent by the workflow.
