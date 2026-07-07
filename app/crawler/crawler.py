from collections import deque
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup
from crawl4ai import (
    AsyncWebCrawler,
    BrowserConfig,
    CrawlerRunConfig,
)

from app.crawler.parser import parse_result


def get_internal_links(base_url: str, html: str) -> list[str]:
    """
    Extract all internal links from a page.
    """

    soup = BeautifulSoup(html, "html.parser")

    base_domain = urlparse(base_url).netloc

    links = set()

    for tag in soup.find_all("a", href=True):

        href = tag["href"].strip()

        if not href:
            continue

        if href.startswith("#"):
            continue

        if href.startswith("mailto:"):
            continue

        if href.startswith("tel:"):
            continue

        if href.startswith("javascript:"):
            continue

        absolute = urljoin(base_url, href)

        parsed = urlparse(absolute)

        if parsed.netloc != base_domain:
            continue

        absolute = absolute.split("#")[0]

        links.add(absolute)

    return list(links)


async def crawl_website(start_url: str):

    browser_config = BrowserConfig(
        headless=True
    )

    run_config = CrawlerRunConfig()

    pages = []

    visited = set()

    queue = deque([start_url])

    async with AsyncWebCrawler(
        config=browser_config
    ) as crawler:

        while queue:

            current_url = queue.popleft()

            if current_url in visited:
                continue

            print(f"Crawling : {current_url}")

            visited.add(current_url)

            try:

                result = await crawler.arun(
                    url=current_url,
                    config=run_config,
                )

                if not result.success:
                    continue

                pages.append(parse_result(result))

                links = get_internal_links(
                    current_url,
                    result.html,
                )

                for link in links:

                    if link not in visited:
                        queue.append(link)

            except Exception as e:

                print(e)

    return pages