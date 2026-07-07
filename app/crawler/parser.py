from app.crawler.models import RawPage


def parse_result(result):

    return RawPage(
        title=result.metadata.get("title", ""),
        url=result.url,
        markdown=result.markdown or "",
        html=result.html or "",
        metadata=result.metadata or {},
        internal_links=result.links.get("internal", []),
        external_links=result.links.get("external", []),
        images=result.media.get("images", []),
    )