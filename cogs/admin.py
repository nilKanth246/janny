import discord
from discord.ext import commands
from discord.ext.commands.core import has_permissions

class Admin_Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command
    