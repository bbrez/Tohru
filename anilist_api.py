import requests

url = 'https://graphql.anilist.co'


def find_char(query_character):
    print(query_character)

    query = None
    with open('queries/character.ql', 'r') as query_file:
        query = query_file.read()

    variables = {
        'char': query_character
    }

    response = requests.post(url, json={'query': query, 'variables': variables})
    character = response.json()['data']['Character']

    return character


def find_anime(query_anime):
    print(query_anime)

    query = None
    with open('queries/anime.ql', 'r') as query_file:
        query = query_file.read()

    variables = {
        'anime': query_anime
    }

    response = requests.post(url, json={'query': query, 'variables': variables})
    anime = response.json()['data']['Media']

    return anime


def find_manga(query_manga):
	print(query_manga)

	query = None
	with open('queries/manga.ql', 'r') as query_file:
		query = query_file.read()

	variables = {
		'manga': query_manga
	}

	response = requests.post(url, json={'query': query, 'variables': variables})
	manga = response.json()['data']['Media']

	return manga

def get_trending():
    query = None
    with open('queries/trending.ql', 'r') as query_file:
        query = query_file.read()

    variables = {
        'pp': 5
    }

    response = requests.post(url, json={'query': query, 'variables': variables})
    anime = response.json()['data']['Page']['media']

    return anime


def get_trending_manga():
	query = None

	with open('queries/trending_manga.ql', 'r') as query_file:
		query = query_file.read()
	
	variables = {
	    'pp': 5
    }

	response = requests.post(url, json={'query': query, 'variables': variables})
	manga = response.json()['data']['Page']['media']

	return manga