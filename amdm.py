import re
import json
import requests
from bs4 import BeautifulSoup as bs

class AmDm:
    """Класс для поиска аккордов с сайта AmDm.ru
    """

    def get_chords_list(query):
        """Получаем список песен по поиску в формате:
        [
            {
                'artist': '...',
                'title': '...',
                'url': '...'
            }
        ]
        :param query: поисковый запрос
        """
        result = requests.post('http://amdm.ru/search/?q={}'.format(
            re.sub('\s', '+', query)))
        soup = bs(result.content)
        table = soup.find_all("table", {"class":"items"})[0]
        r = table.find_all("a", {"class":"artist"})

        results = []
        for index, item in enumerate(r[::2]):
            results.append({'artist': item.contents[0]})
            r.remove(item)

        for index, item in enumerate(r):
            results[index]['title'] = item.contents[0]
            results[index]['url'] = 'http:{}'.format(item['href'])
        return results

    def get_chords_song(url):
        """Получаем аккорды для песни по URL в формате HTML.
        :param url: URL для amdm.ru
        """
        song = requests.get(url)
        soup = bs(song.content)
        content = soup.find_all("pre", {"itemprop":"chordsBlock"})[0]
        txt = ''
        for item in content.contents:
            if item.name is None: txt += re.sub(' +', ' ', item.string)
            else: txt += str(item)
        return txt
