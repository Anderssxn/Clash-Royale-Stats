import discord
import os
from discord.ext import commands
import config


bot = commands.Bot(command_prefix='!CR ')


@bot.event
async def on_ready():
    print(f'{bot.user} is now online!')


@bot.command()
async def load(ctx,extension):
        bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx,extension):
        bot.unload_extension(f'cogs.{extension}')
        print(extension + " has been UNLOADED!")

@bot.command()
async def reload(ctx,extension):
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')
        print('All Extensions were reloaded!')

@bot.command()
async def reloadall(ctx):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.unload_extension(f'cogs.{filename[:-3]}')
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}') 
        
        print('All Extensions were reloaded!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')



bot.run(config.DiscordToken)
