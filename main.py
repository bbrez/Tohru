import os
import json
import random

from dotenv import load_dotenv
import db

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='&')

def waifu_embed(waifu):
    embed = discord.Embed()
    embed.colour = discord.Colour.from_rgb(153, 00, 230)
    embed.type = 'rich'
    embed.title = waifu['nameWaifu']
    embed.description = waifu['nickWaifu'] + '\n' + waifu['tierWaifu']*'*'
    return embed

@bot.event
async def on_ready():
    print(f'{bot.user.name} connected!')

@bot.command(name='waifu', help='Gives you a random waifu')
async def get_waifu(ctx):
    with open('waifus.json', 'r') as waifu_file:
        waifus = json.load(waifu_file)

    response = random.choice(waifus['waifus'])
    await ctx.send(response) 

@bot.command(name='addwaifu', help='Register a waifu / !register name age source')
async def register_waifu(ctx, name: str, age: str, source: str):
    await ctx.send(f'registered: {name}, {age} y/o from {source}')

@bot.command(name='addalias', help='Adds an alias to a registered Waifu / !register waifu alias')
async def register_waifu_alias(ctx, waifu: str, alias: str):
    await ctx.send(f'added {alias} as alias for {waifu}')


@bot.command(name='initdb')
async def initdb(ctx):
    db.init_db()

@bot.command(name='shutdown', help='Bot is no more')
async def shutdown_bot(ctx):
    await ctx.send(f'Shutting down bot...')
    db.close_db()
    exit()

@bot.command(name='createsource')
async def create_source(ctx, nameSource: str):
    await ctx.send(f'Source created: {db.create_source(nameSource)}')

@bot.command(name='readsource')
async def read_source(ctx, nameSource: str = None):
    await ctx.send(f'Sources found: {db.read_source(nameSource)}')

@bot.command(name='searchwaifu', aliases=['sw'])
async def read_waifu(ctx, nameWaifu: str = None):
    waifu = db.read_waifu(nameWaifu)
    await ctx.send(embed=waifu_embed(waifu))


db.open_db()
bot.run(TOKEN)