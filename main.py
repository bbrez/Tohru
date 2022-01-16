import os
import pprint

from discord.ext import commands
from discord.commands.options import Option

import anilist_api
import embed

import dotenv

dotenv.load_dotenv()
TOKEN = os.environ['DISCORD_TOKEN']


bot = commands.Bot(command_prefix='&')
# slash = SlashCommand(client=bot, sync_commands=True)


@bot.event
async def on_ready():
	print(f'{bot.user.name} connected!')


@bot.slash_command()
async def character(
	ctx,
 	name: Option(str, 'Character Name')):
	char = anilist_api.find_char(name)
	if char is not None:
		pprint.pprint(char)
		await ctx.send(embed=embed.character_embed(char))
	else:
		await ctx.send(f'Character {name} not found')



@bot.slash_command()
async def anime(
	ctx, 
	name: Option(str, 'Anime name')):
	f_anime = anilist_api.find_anime(name)
	if f_anime is not None:
		pprint.pprint(f_anime)
		await ctx.send(embed=embed.anime_embed(f_anime))
	else:
		await ctx.send(f'Anime {name} not found')


@bot.slash_command()
async def manga(
	ctx,
	name: Option(str, 'Manga name')):
	f_manga = anilist_api.find_manga(name)
	if f_manga is not None:
		pprint.pprint(f_manga)
		await ctx.send(embed=embed.anime_embed(f_manga))
	else:
		await ctx.send(f'Manga {name} not found')


@bot.slash_command()
async def trending(
	ctx,
	mediatype: Option(str, 'Type of media', choices=['Anime', 'Manga'])):
	'''Shows trending manga or anime'''
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



if __name__ == '__main__':
	bot.run(TOKEN)
