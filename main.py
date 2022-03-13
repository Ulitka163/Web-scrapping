import requests
import bs4

url = 'https://habr.com/ru/all/'

response = requests.get(url)
response.raise_for_status()
text = response.text

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all(class_='tm-article-snippet')
for article in articles:
    date_time = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
    article_header = article.find(class_='tm-article-snippet__title-link').find('span').text
    article_url = article.find(class_='tm-article-snippet__title-link').attrs['href']
    print(f'<{date_time}> - <{article_header}> - <https://habr.com{article_url}>')
    print()




