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
slash = SlashCommand(client=bot, sync_commands=True)


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
	name='manga',
	description='Searches a manga on AniList',
	options=[
		create_option(
			name='name',
			description='Manga name',
			option_type=SlashCommandOptionType.STRING,
			required=True
		)
	]
)
async def manga(ctx, *, name):
	f_manga = anilist_api.find_manga(name)
	if f_manga is not None:
		pprint.pprint(f_manga)
		await ctx.send(embed=embed.anime_embed(f_manga))
	else:
		await ctx.send(f'Manga {name} not found')


@slash.slash(
    name='trending',
    description='Top 5 Trending anime or manga',
	options = [
		create_option(
			name='mediatype',
			description='"anime" or "manga"',
			option_type=SlashCommandOptionType.STRING,
			required=False
		)
	]
)
async def trending(ctx, mediatype=None):
	if mediatype is None:
		mediatype = 'anime'

	if mediatype.lower() == 'manga':
		f_anime = anilist_api.get_trending_manga()
	elif mediatype.lower() == 'anime':
		f_anime = anilist_api.get_trending()
	else:
		await ctx.send(f'mediatype {mediatype} not found')

	if f_anime is not None:
		pprint.pprint(f_anime)
		await ctx.send(embed=embed.trending_embed(f_anime))




bot.run(TOKEN)
