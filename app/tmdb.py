from calendar import monthrange
from datetime import date

import requests

from config import CONFIG

endpoint = "https://api.themoviedb.org/3/"
discover = "discover/movie/"
image_base = "https://image.tmdb.org/t/p/original/"
headers = {
    "Accept" : "application/json",
    "Authorization":  "Bearer " + CONFIG.TMDB_V4_KEY,
}

def monthly_movies(month=date.today().month, year=date.today().year, page = 1):
    first_day = 1
    last_day = monthrange(year, month)[1]
    params = {
        "api_key" : CONFIG.TMDB_V3_KEY,
        "region" : "IN",
        "with_release_type" : "2|3|4",
        "primary_release_date.gte" : str(date(year, month, first_day)),
        "primary_release_date.lte" : str(date(year, month, last_day)),
        "page": page,
    }

    url = endpoint + discover
    response = requests.get(url, params=params, headers=headers)
    response_json = response.json()
    movies = {
        'page': response_json['page'],
        'total_pages': response_json['total_pages'],
        'total_results': response_json['total_results'],
        'results': [],
    }
    for item in response_json['results']:
        if item['poster_path'] and item['overview']:
            movies['results'].append(item)
    return movies
