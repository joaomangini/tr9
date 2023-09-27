import requests
from bs4 import BeautifulSoup
import concurrent.futures

def scrape_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Suponhamos que os títulos das notícias estão em elementos <h2>
        headlines = soup.find_all('h2')
        for headline in headlines:
            print(headline.text)
    except Exception as e:
        print(f"Erro ao raspar {url}: {str(e)}")

def main():
    base_url = 'https://example.com/page'
    urls = [f'{base_url}/{i}' for i in range(1, 11)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(scrape_page, urls)

if __name__ == "__main__":
    main()
