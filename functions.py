import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

# Data structure to hold tag and class mappings for each site
url_mappings = {
    "https://www.uol.com.br/esporte/futebol/campeonatos/brasileirao/": {
        "container_tag": "div",
        "container_class": "thumbnails-item grid col-xs-4 col-sm-6 small",
        "title_tag": "h3",
        "title_class": "thumb-title title-xsmall title-lg-small",
        "link_tag": "a"
    },
    "https://www.terra.com.br/esportes/futebol/brasileiro-serie-a/tabela/": {
        "container_tag": "div",
        "container_class": "card card-news card-h card-has-image",
        "title_tag": "a",
        "title_class": "card-news__text--title main-url",
        "link_tag": "a"
    },
    "https://www.revistacolorada.com.br/?s=brasileir%C3%A3o+serie+a": {
        "container_tag": "article",
        "container_class": "listing-item listing-item-grid listing-item-grid-1",
        "title_tag": "h2",
        "title_class": "card-news__text--title main-url",
        "link_tag": "a"
    },
    "https://esportenewsmundo.com.br/?s=Brasileir%C3%A3o+serie+a": {
        "container_tag": "li",
        "container_class": "infinite-post",
        "title_tag": "h2",
        "title_class": None,  # No class needed
        "link_tag": "a"
    }
}

def extract_headlines(url, mapping, retries=3, delay=2):
    headlines = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.5'
    }
    
    # Attempt to request the page with retries
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                # Extract the headline containers
                headline_tags = soup.find_all(mapping['container_tag'], class_=mapping['container_class'])

                print(f"Encontradas {len(headline_tags)} manchetes em {url}")

                for tag in headline_tags:
                    link_tag = tag.find(mapping['link_tag'])
                    if link_tag:
                        # Find title within the tag
                        title_tag = tag.find(mapping['title_tag'], class_=mapping['title_class']) if mapping['title_class'] else tag.find(mapping['title_tag'])
                        if title_tag:
                            headlines.append({'texto': title_tag.get_text(strip=True), 'fonte': link_tag['href']})

                print(headlines)
                break  # Exit loop if successful
            else:
                print(f"Erro ao acessar {url}: {response.status_code}")
                time.sleep(delay)  # Wait before retrying
        except Exception as e:
            print(f'Ocorreu um erro com {url}: {e}')
            if attempt < retries - 1:
                print(f"Tentativa {attempt + 1} falhou, tentando novamente após {delay} segundos...")
                time.sleep(delay)  # Wait before retrying
            else:
                print(f"Falha ao tentar acessar {url} após {retries} tentativas.")
    
    return headlines
