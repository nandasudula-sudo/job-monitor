import json

from scrapers.greenhouse import fetch_jobs as fetch_greenhouse_jobs
from scrapers.lever import fetch_jobs as fetch_lever_jobs
from scrapers.sample_source import fetch_jobs as fetch_sample_jobs


SOURCE_MAPPING = {
    "sample": fetch_sample_jobs,
    "greenhouse": fetch_greenhouse_jobs
}


def load_sources():
    with open("config/sources.json", "r") as file:
        config = json.load(file)

    sources = []

    for source_name in config["sources"]:
        if source_name in SOURCE_MAPPING:
            sources.append(SOURCE_MAPPING[source_name])

    return sources