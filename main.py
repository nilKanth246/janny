import discord
import os
from discord.ext import commands

bot = commands.Bot(commad_prefix = ['>'], help_command = None)

cogs = ["cogs.member", "cogs.admin"]

for extensions in cogs:
    bot.load_extension(extensions)

async def on_ready():
    await bot.change_presence(status = discord.Status.online, activity = discord.Game(">help"))

print ("hi")

