from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def review(movie):
    query = "+".join(f"Movie {movie.title()}".split())
    url = f"https://www.google.com/search?q={query}"
    ua = UserAgent()
    headers = {"User-Agent": ua.chrome}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    star_tags = soup.find_all("div", class_="Hk2yDb KsR1A")

    rating_tags = []
    for s in star_tags:
        parents = s.parents
        done = False
        while not done:
            tag = next(parents)
            if tag.attrs == {"class": ["v9i61e"]}:
                rating_tags.append(tag)
                done = True

    reviews = {}
    for r in rating_tags:
        parents = r.parents
        done = False
        while not done:
            tag = next(parents)
            if tag.attrs == {"class": ["ZINbbc", "xpd", "O9g5cc", "uUPGi"]}:
                done = True
        url = tag.find("a")["href"].split("q=")[1]
        reviewer = urlparse(url).netloc
        rate = tag.find(class_="Eq0J8 oqSTJd").text
        reviews[reviewer] = rate
    return reviews
