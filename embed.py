import pprint
import re

import discord


def character_embed(character):
    embed = discord.Embed()
    embed.type = 'rich'

    embed.url = character['siteUrl']
    embed.title = character['name']['full']
    embed.set_image(url=character['image']['large'])

    names = list()
    try:
        if len(character['name']['alternative'][0]) > 0:
        	names.extend(character['name']['alternative'])
    except Exception:
        print('Character has no alternative name')

    try:
        if len(character['name']['alternativeSpoiler'][0]) > 0:
        	names.extend(character['name']['alternativeSpoiler'])
    except Exception:
	    print('Character has no alternativeSpoiler name')

    names.append(character['name']['native'])
    pprint.pprint(names)

    desc = f'_{", ".join(names)}_\n\n'
    character['description'] = re.sub("[<].*?[>]|_+", "", character['description']) #Removes underlines from description
    character['description'] = re.sub("~!|!~", "||", character['description']) #Changes spoiler notation to Discord's
    desc += character['description']

    if len(desc) > 2048:
        desc = desc[:2045]+'...'

    embed.description = desc
    embed.add_field(name="Favourites", value=character['favourites'])
    embed.set_footer(text='source: AniList.co', icon_url='https://anilist.co/img/icons/android-chrome-512x512.png')
    return embed


def anime_embed(anime):
    embed = discord.Embed()
    embed.type = 'rich'

    embed.url = anime['siteUrl']
    if anime['title']['userPreferred'] is not None:
        embed.title = anime['title']['userPreferred']
    else:
        embed.title = anime['title']['romaji']
    embed.set_image(url=anime['coverImage']['large'])

    if anime['coverImage']['color'] is not None:
        colours = anime['coverImage']['color'].lstrip('#')
        colours = tuple(int(colours[i:i + 2], 16) for i in (0, 2, 4))
        embed.colour = discord.Colour.from_rgb(colours[0], colours[1], colours[2])

    desc = f'_{", ".join(anime["genres"])}_\n\n'
    anime['description'] = re.sub("[<].*?[>]", "", anime['description'])
    desc += anime['description']

    if len(desc) > 2048:
        desc = desc[:2045]+'...'

    embed.add_field(name="Score", value=anime['averageScore'])
    embed.add_field(name="Episodes", value=anime['episodes'])
    embed.add_field(name="Status", value=anime['status'])

    embed.description = desc
    embed.set_footer(text='source: Anilist.co', icon_url='https://anilist.co/img/icons/android-chrome-512x512.png')
    return embed


def trending_embed(animes):
    embed = discord.Embed()
    embed.type = 'rich'

    embed.title = 'Trending Top 5:'

    desc = ''
    for idx, anime in enumerate(animes, start=1):
        desc += f'{idx} - [{anime["title"]["userPreferred"]}]({anime["siteUrl"]})\n'

    embed.description = desc

    embed.set_image(url=animes[0]['coverImage']['extraLarge'])

    if animes[0]['coverImage']['color'] is not None:
        colours = animes[0]['coverImage']['color'].lstrip('#')
        colours = tuple(int(colours[i:i + 2], 16) for i in (0, 2, 4))
        embed.colour = discord.Colour.from_rgb(colours[0], colours[1], colours[2])

    embed.set_footer(text='source: Anilist.co', icon_url='https://anilist.co/img/icons/android-chrome-512x512.png')

    return embed
