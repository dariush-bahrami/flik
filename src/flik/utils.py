import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def fetch_imdb_id(title):
    query = "+".join(title.split()) + "%3Aimdb.com"
    url = f"https://www.google.com/search?q={query}"
    ua = UserAgent()
    headers = {"User-Agent": ua.chrome}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    imdb_links = [a for a in soup.find_all("a") if "www.imdb.com/title" in a["href"]]
    imdb_ids = [a["href"].split("title/")[1].split("/")[0] for a in imdb_links]
    most_frequent_id = max(set(imdb_ids), key=imdb_ids.count)
    return most_frequent_id
