import requests
from bs4 import BeautifulSoup

def scrape_web(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a')

    data = []

    for link in links:

        href = link.get('href')
 
        text = link.text

        data.append({'href': href, 'text': text})

    return data