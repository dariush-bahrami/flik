import requests
from fake_useragent import UserAgent
from .utils import fetch_imdb_id


def fetch_movie_info_by_imdb_id(imdb_id, omdb_api_key, plot="short"):
    url = f"http://www.omdbapi.com/?apikey={omdb_api_key}&"
    ua = UserAgent()
    headers = {"User-Agent": ua.chrome}
    request_type = "movie"
    request_parameters = {"i": imdb_id, "plot": plot}
    response = requests.get(url, headers=headers, params=request_parameters)
    return response.json()


def fetch_movie_info(title, omdb_api_key, plot="short"):
    imdb_id = fetch_imdb_id(title)
    return fetch_movie_info_by_imdb_id(imdb_id, omdb_api_key, plot=plot)
