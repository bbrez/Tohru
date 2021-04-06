import os
import json
import random

from dotenv import load_dotenv
import db

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} connected!')

@bot.command(name='waifu', help='Gives you a random waifu')
async def get_waifu(ctx):
    with open('waifus.json', 'r') as waifu_file:
        waifus = json.load(waifu_file)

    response = random.choice(waifus['waifus'])
    await ctx.send(response)

@bot.command(name='register', help='Register a waifu / !register name source')
async def register_waifu(ctx, name: str, source: str):
    await ctx.send(f'registered: {name} from {source}')

@bot.command(name='addalias', help='Adds an alias to a registered Waifu / !register waifu alias')
async def register_waifu_alias(ctx, waifu: str, alias: str):
    await ctx.send(f'added {alias} as alias for {waifu}')


@bot.command(name='shutdown', help='Bot is no more')
async def shutdown_bot(ctx):
    await ctx.send(f'Shutting down bot...')
    db.close_db()
    exit()

@bot.command(name='testdb')
async def testdb(ctx, sql):
    await ctx.send(db.exec_sql(sql))

db.open_db()
bot.run(TOKEN)