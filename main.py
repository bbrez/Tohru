import os
import pprint

from discord.ext import commands

from discord_slash import SlashCommand #upm package(discord-py-slash-command)
from discord_slash.model import SlashCommandOptionType
from discord_slash.utils.manage_commands import create_option

import anilist_api
import embed


TOKEN = os.environ['DISCORD_TOKEN']


bot = commands.Bot(command_prefix='&')
slash = SlashCommand(client=bot, sync_commands=False)


@bot.event
async def on_ready():
    print(f'{bot.user.name} connected!')


@slash.slash(
    name='char',
    description='Searcher a character on AniList',
    options=[
        create_option(
            name='name',
            description='Character Name',
            option_type=SlashCommandOptionType.STRING,
            required=True
        )
    ]
)
async def character(ctx, *, name):
    char = anilist_api.find_char(name)
    if char is not None:
        pprint.pprint(char)
        await ctx.send(embed=embed.character_embed(char))
    else:
        await ctx.send(f'Character {name} not found')


@slash.slash(
    name='anime',
    description='Searches an anime on AniList',
    options=[
        create_option(
            name='name',
            description='Anime name',
            option_type=SlashCommandOptionType.STRING,
            required=True
        )
    ]
)
async def anime(ctx, *, name):
    f_anime = anilist_api.find_anime(name)
    if f_anime is not None:
        pprint.pprint(f_anime)
        await ctx.send(embed=embed.anime_embed(f_anime))
    else:
        await ctx.send(f'Anime {name} not found')


@slash.slash(
    name='trending',
    description='Top 5 Trending anime'
)
async def trending(ctx):
    f_anime = anilist_api.get_trending()
    if f_anime is not None:
        pprint.pprint(f_anime)
        await ctx.send(embed=embed.trending_embed(f_anime))
    else:
        await ctx.send('Error getting trending anime')

bot.run(TOKEN)
