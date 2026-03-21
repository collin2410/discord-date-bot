# Discord Date/Time VC Bot

This bot renames two Discord voice channels every minute:

- 🔒 Date: Saturday, Mar 21st
- 🔒 Time: 5:58pm CDT

## Files
- `bot.py`
- `requirements.txt`

## Before you deploy
Open `bot.py` and replace:

- `DATE_CHANNEL_ID = 123456789012345678`
- `TIME_CHANNEL_ID = 234567890123456789`

with your real Discord voice channel IDs.

## Render setup
Build command:
`pip install -r requirements.txt`

Start command:
`python bot.py`

Environment variable:
- `DISCORD_BOT_TOKEN` = your Discord bot token
