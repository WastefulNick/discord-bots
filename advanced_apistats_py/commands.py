import discord
from discord.ext import commands
import requests
from api import API

class CommandsCog(commands.Cog, name="All Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stats(self, ctx, *args):
        if len(args) < 2:
            await ctx.send('Usage: !stats `platform` `username`\nPlatforms: `uplay`, `psn`, `xbl`')
            return

        platforms = ['uplay','psn', 'xbl']
        platform = args[0].lower()
        username = args[1]

        if platform not in platforms:
            await ctx.send('Not a valid platform.\nValid platforms: `uplay`, `psn`, `xbl`')
            return
        if not API(platform, username).verify():
            await ctx.send(f'Could not find the user `{username}` on the platform `{platform}`\nValid platforms: `uplay`, `psn`, `xbl`')
            return
        
        stats = API(platform, username).getInfo()
        pretty_stat_names = {'level': 'Level',
                            'rank': 'Rank',
                            'mmr': 'MMR',
                            'kd': 'Ranked K/D'}

        embed = discord.Embed(title=stats['p_name'], color=0x2ecc71)
        for key, value in stats.items():
            if key != 'pfp' and key != 'p_name':
                embed.add_field(name=pretty_stat_names[key], value=value, inline=False)
        embed.set_image(url=stats['pfp'])
        embed.set_footer(text='Made by andreas#8860.\nData from R6Tab')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(CommandsCog(bot))