import requests
import bs4

url = 'https://habr.com/ru/all/'

HEADERS = {
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': '_ym_uid=1639148487334283574; _ym_d=1639149414; _ga=GA1.2.528119004.1639149415; _gid=GA1.2.512914915.1639149415; fl=ru; hl=ru; _ym_isad=2; __gads=ID=87f529752d2e0de1 221b467103cd00b7:T=1639149409:S=ALNI_MYKvHcaV4SWfZmCb3_vXDx2olu6kw; habr_web_home=ARTICLES_LIST_ALL',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cashe Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Команда', 'iOS']

def resp(url, HEADERS):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    text = response.text
    return bs4.BeautifulSoup(text, features='html.parser')

if __name__ == '__main__':
    soup = resp(url, HEADERS)
    articles = soup.find_all(class_='tm-article-snippet')

    for article in articles:
        article_text = article.text.split()
        for key in KEYWORDS:
            if key in article_text:
                date_time = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
                article_header = article.find(class_='tm-article-snippet__title-link').find('span').text
                article_url = article.find(class_='tm-article-snippet__title-link').attrs['href']
                print(f'<{date_time}> - <{article_header}> - <https://habr.com{article_url}>')

