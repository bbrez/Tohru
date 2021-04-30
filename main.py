import os
import pprint

from dotenv import load_dotenv

from discord.ext import commands

from discord_slash import SlashCommand
from discord_slash.model import SlashCommandOptionType
from discord_slash.utils.manage_commands import create_option

import anilist_api
import embed

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


bot = commands.Bot(command_prefix='&')
slash = SlashCommand(client=bot, sync_commands=False)


@bot.event
async def on_ready():
    print(f'{bot.user.name} connected!')


@slash.slash(
    name='pers',
    description='Procura um personagem no AniList',
    options=[
        create_option(
            name='nome',
            description='Nome do personagem',
            option_type=SlashCommandOptionType.STRING,
            required=True
        )
    ]
)
async def character(ctx, *, nome):
    char = anilist_api.find_char(nome)
    if char is not None:
        pprint.pprint(char)
        await ctx.send(embed=embed.waifu_embed(char))
    else:
        await ctx.send(f'Personagem {nome} não encontrado')


@slash.slash(
    name='anime',
    description='Procura um anime no AniList',
    options=[
        create_option(
            name='nome',
            description='Nome do anime',
            option_type=SlashCommandOptionType.STRING,
            required=True
        )
    ]
)
async def anime(ctx, *, nome):
    f_anime = anilist_api.find_anime(nome)
    if f_anime is not None:
        pprint.pprint(f_anime)
        await ctx.send(embed=embed.anime_embed(f_anime))
    else:
        await ctx.send(f'Anime {nome} não encontrado')

bot.run(TOKEN)
