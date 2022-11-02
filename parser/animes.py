from bs4 import BeautifulSoup as BS

import requests

URL = 'https://jut.su/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,'
              'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/106.0.0.0 Safari/537.36'
}


def get_html(url, params=''):
    req = requests.get(url=url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_="grid ya-grid-template")
    animes = []
    for item in items:
        info = item.find('div', class_='grid ya-grid-template').find('div').getText().split(', ')
        anime = {
            'title': item.find('div', class_='ya-unit-title ya-grid-template').find('a').getText(),
            'link': item.find('div', class_='ya-unit-category category ya-grid-template').getText(),
        }
        try:
            anime['year'] = info[0]
            anime['genre'] = info[2]
        except:
            anime['year'] = info[0]
            anime['genre'] = info[1]
        animes.append(anime)

    return animes


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        animes = []
        for i in range(1, 5):
            html = get_html(f"{URL}page/{i}/")
            current_page = get_data(html.text)
            animes.extend(current_page)
        return animes
    else:
        raise Exception("Ошибка!")