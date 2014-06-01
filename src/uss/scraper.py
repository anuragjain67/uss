import requests
import json

SCRAPPER_URL = "http://api.embed.ly/1/oembed"


def scraper(link_to_scrap):
    scraper_link = SCRAPPER_URL + '?url=' + link_to_scrap
    response = requests.get(scraper_link)
    return json.loads(response.content)
