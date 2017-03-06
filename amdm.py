import re
import requests
from bs4 import BeautifulSoup

class AmDm:
    """Класс для поиска аккордов с сайта AmDm.ru
    """
    def __init__(self):
        pass

    def get_chords_list(self, query):
        """Получаем список песен по поиску в формате:
        [
            {
                'artist': '...',
                'title': '...',
                'url': '...'
            }
        ]
        Или False если ничего не найдено
        :param query: поисковый запрос
        """
        result = requests.post('http://amdm.ru/search/?q={}'.format(
            re.sub('\s', '+', query)))
        soup = BeautifulSoup(result.content, "lxml")
        table = soup.find_all("table", "items")[0]
        if " ".join(table['class']) == "items debug2":
            return False
        r = table.find_all("a", {"class":"artist"})

        results = []
        for index, item in enumerate(r[::2]):
            results.append({'artist': item.contents[0]})
            r.remove(item)

        for index, item in enumerate(r):
            results[index]['title'] = item.contents[0]
            results[index]['url'] = 'http:{}'.format(item['href'])
        return results

    def get_chords_song(self, url):
        """Получаем аккорды для песни по URL в формате HTML.
        :param url: URL для amdm.ru
        """
        song = requests.get(url)
        soup = BeautifulSoup(song.content, "lxml")
        content = soup.find_all("pre", {"itemprop":"chordsBlock"})[0]
        txt = ''
        for item in content.contents:
            if item.name is None: txt += re.sub(' +', ' ', item.string)
            else: txt += str(item)
        return txt
