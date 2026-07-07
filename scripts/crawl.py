import asyncio

from app.config.settings import settings
from app.crawler.crawler import crawl_website
from app.crawler.storage import save_pages


async def main():

    print(f"Crawling {settings.WEBSITE_URL}...")

    pages = await crawl_website(settings.WEBSITE_URL)

    print(f"Pages Crawled : {len(pages)}")

    save_pages(pages)

    print("Done")


if __name__ == "__main__":
    asyncio.run(main())