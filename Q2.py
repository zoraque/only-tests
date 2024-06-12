# Python 3.9.2

import requests
import re
from operator import itemgetter


def getAllSeries():
    url = 'https://jsonmock.hackerrank.com/api/tvseries'
    page = 1
    data_info = []

    while True:
        response = requests.get(url=url, params={'page': page})

        if response.status_code != 200:
            raise Exception(f"Failed to read data! API response with status code ${response.status_code}")

        data = response.json()

        for show in data.get('data'):
            data_info.append({
                'name': show.get('name'),
                'genre': show.get('genre').upper(),
                'imdb_rating': show.get('imdb_rating')
            })

        total_pages = data.get('total_pages')
        if page >= total_pages:
            break
        page += 1

    return data_info


def filterSeries(genre: str, series: list):
    
    filtered = [show for show in series if genre in show['genre']]
    sorted_series = sorted(filtered, key=itemgetter('name'))

    if not sorted_series:
        return "No series of this genre was found."

    sorted_series = sorted(filtered, key=lambda x: (-x['imdb_rating'], x['name']))

    return sorted_series[0]['name']


def bestInGenre(genre: str):
    if (checkInput(genre)):
        series = getAllSeries()
        result = filterSeries(genre.upper(), series)
        print(result)
    else:
        print("Invalid genre! Accept only letters and hyphen.")
        return False


def checkInput(genre: str):
    pattern = re.compile(r'^[A-Za-z-]{1,10}$')
    if (pattern.match(genre)):
        return True
    else:
        return False


if __name__ == "__main__":
    genre = input("What genre do you want to find the best rating for? ")
    bestInGenre(genre)
