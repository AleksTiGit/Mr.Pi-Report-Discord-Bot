import os
from discord.ext import commands
from dislash import InteractionClient
import discord

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='/', intents=intents)
slash = InteractionClient(bot)

@slash.command(name='report', description='Подать жалобу.')
async def report(ctx):
    await ctx.send('<@&1186353669122297867> примите меры')

@bot.event
async def on_ready():
    print(f'Bot is online: {bot.user}')

bot.run(os.getenv("token"))