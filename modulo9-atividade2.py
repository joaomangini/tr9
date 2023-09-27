import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def scrape_page(url, session):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            # Suponhamos que os títulos das notícias estão em elementos <h2>
            headlines = soup.find_all('h2')
            for headline in headlines:
                print(headline.text)
    except Exception as e:
        print(f"Erro ao raspar {url}: {str(e)}")

async def main():
    base_url = 'https://example.com/page'
    urls = [f'{base_url}/{i}' for i in range(1, 11)]

    async with aiohttp.ClientSession() as session:
        tasks = [scrape_page(url, session) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
