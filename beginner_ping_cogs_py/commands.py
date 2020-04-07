import discord
from discord.ext import commands

class CommandsCog(commands.Cog, name="All Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping') #Chang the name to change the command
    async def ping(self, ctx):
        await ctx.send('Pong!')

def setup(bot):
    bot.add_cog(CommandsCog(bot))