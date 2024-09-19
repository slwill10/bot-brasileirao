import requests
from bs4 import BeautifulSoup

def uol(url):
    headlines = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            headline_tags = soup.find_all('div', class_='thumbnails-item grid col-xs-4 col-sm-6 small')

            print(f"Encontradas {len(headline_tags)}")

            for tag in headline_tags:
                link_tag = tag.find('a')
                if link_tag:
                    span_tag = tag.find('h3', class_='thumb-title title-xsmall title-lg-small')
                    headlines.append({'texto': span_tag.get_text(strip=True), 'fonte': link_tag['href']})

            print(headlines)
        else:
            print(f"Erro ao acessar {url}: {response.status_code}")

    except Exception as e: 
        print(f'Ocorreu um erro com {url}: {e}')

    return headlines

def terra(url):
    headlines = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            headline_tags = soup.find_all('div', class_='card card-news card-h card-has-image')

            print(f"Encontradas {len(headline_tags)}")

            for tag in headline_tags:
                link_tag = tag.find('a', class_="card-news__text--title main-url")
                if link_tag:
                    headlines.append({'texto': link_tag.get_text(strip=True), 'fonte': link_tag['href']})

            print(headlines)
        else:
            print(f"Erro ao acessar {url}: {response.status_code}")

    except Exception as e: 
        print(f'Ocorreu um erro com {url}: {e}')

    return headlines

def revistaColorada(url):
    headlines = []
    hearders = ""
    try:
        response = requests.get(url,headers=hearders)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            headline_tags = soup.find_all('article', class_='listing-item listing-item-grid listing-item-grid-1')


            print(f"Encontradas {len(headline_tags)}")

            for tag in headline_tags:
                link_tag = tag.find('a', class_="card-news__text--title main-url")
                if link_tag:
                    headlines.append({'texto': link_tag.get_text(strip=True), 'fonte': link_tag['href']})

            print(headlines)
        else:
            print(f"Erro ao acessar {url}: {response.status_code}")

    except Exception as e: 
        print(f'Ocorreu um erro com {url}: {e}')

    return headlines

def esportesnewmundo(url):
    headlines = []
    hearders = {
        'cookie': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        'Accept-Language': 'en-US,en;q=0.5'
    }
    try:
        response = requests.get(url, headers=hearders)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            headline_tags = soup.find_all('li', class_='infinite-post')


            print(f"Encontradas {len(headline_tags)}")

            for tag in headline_tags:
                link_tag = tag.find('a')
                if link_tag:
                    h2_tag = tag.find('h2')
                    headlines.append({'texto': h2_tag.get_text(strip=True), 'fonte': link_tag['href']})

            print(headlines)
        else:
            print(f"Erro ao acessar {url}: {response.status_code}")

    except Exception as e: 
        print(f'Ocorreu um erro com {url}: {e}')

    return headlines
