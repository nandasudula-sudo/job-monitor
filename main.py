from database.database import initialize_database
from logs.logger import logger
from orchestrator.job_processor import process_job
from scrapers.source_manager import fetch_all_jobs


def main():
    initialize_database()

    logger.info("Starting job monitor")

    jobs = fetch_all_jobs()

    logger.info(f"Total jobs collected: {len(jobs)}")

    for job in jobs:
        process_job(job)

    logger.info("Finished execution")


if __name__ == "__main__":
    main()