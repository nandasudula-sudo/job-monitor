import logging

from config.loader import load_json
from scrapers.ashby import fetch_jobs as fetch_ashby_jobs
from scrapers.greenhouse import fetch_jobs as fetch_greenhouse_jobs


SOURCE_MAPPING = {
    "greenhouse": fetch_greenhouse_jobs,
    "ashby": fetch_ashby_jobs,
}


def fetch_all_jobs():
    config = load_json("config/sources.json")

    sources = config["sources"]

    all_jobs = []

    for source in sources:
        if source not in SOURCE_MAPPING:
            logging.warning(
                f"Unknown source: {source}"
            )
            continue

        try:
            jobs = SOURCE_MAPPING[source]()

            logging.info(
                f"Collected {len(jobs)} jobs "
                f"from {source}"
            )

            all_jobs.extend(jobs)

        except Exception as error:
            logging.error(
                f"Error while processing "
                f"{source}: {error}"
            )

    logging.info(
        f"Total jobs collected: {len(all_jobs)}"
    )

    return all_jobs