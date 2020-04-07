import discord
from discord.ext import commands
import sys, traceback #Error handling
from dotenv import load_dotenv #Using .env file as env variables
import os #To get the environment variables

load_dotenv()
token = os.getenv('DISCORD_TOKEN') #Token is loaded from env variables (.env file)

prefix = '!' #Modify this to your prefix of choice

bot = commands.Bot(command_prefix=prefix, description='Intro bot')

extensions = ['commands'] #Array with all extensions, we only have a commands one here

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

bot.run(token, bot=True, reconnect=True) 