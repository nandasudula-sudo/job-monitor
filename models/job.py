from datetime import datetime


def create_job(
    company,
    title,
    location,
    url,
    source
):
    return {
        "company": company,
        "title": title,
        "location": location,
        "url": url,
        "source": source,
        "discovered_at": datetime.utcnow().isoformat(),
    }