import json

from logs.logger import logger
from scrapers.greenhouse import fetch_jobs as fetch_greenhouse_jobs



SOURCE_MAPPING = {
    "greenhouse": fetch_greenhouse_jobs,
}


def load_sources():
    with open("config/sources.json", "r") as file:
        config = json.load(file)

    sources = []

    for source_name in config["sources"]:
        if source_name in SOURCE_MAPPING:
            sources.append(SOURCE_MAPPING[source_name])
        else:
            logger.warning(f"Unknown source: {source_name}")

    return sources


def fetch_all_jobs():
    all_jobs = []

    for source in load_sources():
        try:
            jobs = source()
            all_jobs.extend(jobs)

            logger.info(
                f"Collected {len(jobs)} jobs from {source.__name__}"
            )

        except Exception as error:
            logger.error(
                f"Error while processing {source.__name__}: {error}"
            )

    return all_jobs