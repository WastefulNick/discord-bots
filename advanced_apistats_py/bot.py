import discord
from discord.ext import commands
import sys, traceback
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

prefix = '!'

bot = commands.Bot(command_prefix=prefix, description='Intro bot')
bot.remove_command('help')

extensions = ['commands']

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print(f'Ready as: {bot.user.name}')
    game = discord.Game("Rainbow Six Siege")
    await bot.change_presence(status=discord.Status.online, activity=game)

bot.run(token, bot=True, reconnect=True) 