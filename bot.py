import os
import discord
from discord.ext import tasks
from datetime import datetime
from zoneinfo import ZoneInfo

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Replace these with your actual Discord voice channel IDs
DATE_CHANNEL_ID = 1485046858521907372
TIME_CHANNEL_ID = 1485046960036778006

# Central Time
TIMEZONE = "America/Chicago"

intents = discord.Intents.default()
client = discord.Client(intents=intents)


def ordinal(n: int) -> str:
    if 11 <= (n % 100) <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


def format_date(dt: datetime) -> str:
    return f"{dt.strftime('%A')}, {dt.strftime('%b')} {ordinal(dt.day)}"


def format_time(dt: datetime) -> str:
    tz_abbr = dt.strftime("%Z")
    time_str = dt.strftime("%I:%M%p").lstrip("0").lower()
    return f"{time_str} {tz_abbr}"


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    if not update_channels.is_running():
        update_channels.start()


@tasks.loop(minutes=1)
async def update_channels():
    now = datetime.now(ZoneInfo(TIMEZONE))

    date_channel = client.get_channel(DATE_CHANNEL_ID)
    time_channel = client.get_channel(TIME_CHANNEL_ID)

    if date_channel is None:
        print("Date channel not found.")
    else:
        new_date_name = f"🔒 Date: {format_date(now)}"
        if date_channel.name != new_date_name:
            await date_channel.edit(name=new_date_name)
            print(f"Updated date channel to: {new_date_name}")

    if time_channel is None:
        print("Time channel not found.")
    else:
        new_time_name = f"🔒 Time: {format_time(now)}"
        if time_channel.name != new_time_name:
            await time_channel.edit(name=new_time_name)
            print(f"Updated time channel to: {new_time_name}")


@update_channels.before_loop
async def before_update():
    await client.wait_until_ready()


client.run(TOKEN)
