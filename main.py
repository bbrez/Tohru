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
    print('Building Embed Waifu')
    for key in waifu.keys():
        print(f'{key} = {waifu[key]}')
    embed = discord.Embed()
    embed.type = 'rich'
    embed.title = '『' + waifu['nameWaifu'] + '』'

    desc = ''
    if waifu['nickWaifu'] is not None:
        desc = desc + 'Alias: ' + waifu['nickWaifu'] + '\n'
    
    embed.description = desc + waifu['tierWaifu']*'★'+ (6-waifu['tierWaifu'])*'☆'
    tier_colors = ((232, 232, 232), (102, 204, 0), (0, 85, 255), (204, 204, 0), (230, 38, 0), (102, 0, 153))
    embed.colour = discord.Colour.from_rgb(tier_colors[waifu['tierWaifu']-1][0], tier_colors[waifu['tierWaifu']-1][1], tier_colors[waifu['tierWaifu']-1][2])

    if waifu['imageURLWaifu'] is not None:
        embed.set_image(url=waifu['imageURLWaifu'])
    
    embed.set_footer(text='Source: ' + waifu['nameSource'])
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

@bot.command(name='initdb')
async def initdb(ctx):
    db.init_db()

@bot.command(name='shutdown', help='Bot is no more')
async def shutdown_bot(ctx):
    await ctx.send(f'Shutting down bot...')
    db.close_db()
    exit()

@bot.command(name='createsource')
async def create_source(ctx, nameSource:str):
    await ctx.send(f'Source created: {db.create_source(nameSource)}')

@bot.command(name='readsource')
async def read_source(ctx, nameSource:str = None):
    await ctx.send(f'Sources found: {db.read_source(nameSource)}')

@bot.command(name='addwaifu', aliases=['aw'])
#async def create_waifu(ctx, name:str, tier:str, source:str):
async def create_waifu(ctx, *, args):

    args_keys = ['name', 'tier', 'source']
    args = args.split(',', 3)
    args = [x.strip() for x in args]

    waifu = db.create_waifu(args[0], args[1], args[2])
    await ctx.send('Created waifu:', embed=waifu_embed(waifu))

@bot.command(name='searchwaifu', aliases=['sw'])
async def read_waifu(ctx, nameWaifu:str = None):
    waifu = db.read_waifu(nameWaifu)
    await ctx.send(embed=waifu_embed(waifu))

@bot.command(name='addwaifualias', aliases=['awa'])
async def add_waifu_alias(ctx, name:str, alias:str):
    db.add_waifu_alias(name, alias)
    await ctx.send(f"Alias {alias} added for {name}")

@bot.command(name='addwaifuurl', aliases=['awu'])
async def add_waifu_image(ctx, name:str, url:str):
    db.add_waifu_image(name, url)
    await ctx.send(f"Image added for {name}")
    

db.open_db()
bot.run(TOKEN)