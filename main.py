import discord, os, keep_alive, asyncio, datetime, pytz, requests

from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix='YJ!',
  self_bot=True
)

async def on_ready():
    client.remove_command('help')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Your's Jarvis"))

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
