import os

class CONFIG(object):

    TMDB_V3_KEY = os.environ.get("TMDB_V3_API_TOKEN")
    TMDB_V4_KEY = os.environ.get("TMDB_V4_API_TOKEN")
