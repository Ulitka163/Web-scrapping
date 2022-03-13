import re
from main import resp, HEADERS, url, KEYWORDS

if __name__ == '__main__':
    soup = resp(url, HEADERS)
    articles = soup.find_all(class_='tm-article-snippet')

    for article in articles:
        article_url = 'https://habr.com' + article.find(class_='tm-article-snippet__title-link').attrs['href']
        content = resp(article_url, HEADERS)
        article_content = content.find(class_='tm-article-presenter__content tm-article-presenter__content_narrow').text
        article_content = set(article_content.split())
        for key in KEYWORDS:
            if key in article_content:
                date_time = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
                article_header = article.find(class_='tm-article-snippet__title-link').find('span').text
                print(f'<{date_time}> - <{article_header}> - <{article_url}>')