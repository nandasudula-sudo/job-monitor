from database.database import initialize_database
from orchestrator.job_processor import process_job
from scrapers.sample_source import fetch_jobs


def main():
    initialize_database()

    jobs = fetch_jobs()

    for job in jobs:
        process_job(job)

    print("Completed.")


if __name__ == "__main__":
    main()