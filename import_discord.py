import discord
from discord.ext import commands


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='#',intents=intents)

@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')

@bot.command()
async def hello(message):
    await message.channel.send('Hi!')

bot.run('MTE1MDY0MjA0MzMzNzU3NjQ5OA.GDCHn7.maqY4pJWWbaNRlso6XH5AxAxptubgK5zzGXymQ')