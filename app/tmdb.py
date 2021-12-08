from calendar import monthrange
from datetime import date

import requests

from config import CONFIG

endpoint = "https://api.themoviedb.org/3/"
discover = "discover/movie/"
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
        "with_release_type" : "3|4",
        "release_date.gte" : str(date(year, month, first_day)),
        "release_date.lte" : str(date(year, month, last_day)),
        "page": page,
    }

    url = endpoint + discover
    response = requests.get(url, params=params, headers=headers)
    return response.json()

