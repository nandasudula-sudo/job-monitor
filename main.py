from database.database import initialize_database
from orchestrator.job_processor import process_job
from scrapers.source_manager import load_sources


def main():
    initialize_database()

    sources = load_sources()

    for source in sources:
        jobs = source()

        for job in jobs:
            process_job(job)

    print("Completed.")


if __name__ == "__main__":
    main()