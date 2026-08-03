from database.database import initialize_database
from database.database import insert_job
from database.database import job_exists
from notifier.telegram_bot import send_message
from scrapers.sample_source import fetch_jobs


def main():
    initialize_database()

    jobs = fetch_jobs()

    for job in jobs:

        if job_exists(job["url"]):
            print(f"Skipping {job['title']}")
            continue

        insert_job(job)

        message = (
            f"🚀 NEW JOB\n\n"
            f"Company: {job['company']}\n"
            f"Role: {job['title']}\n"
            f"Location: {job['location']}\n"
            f"Source: {job['source']}\n"
            f"Link: {job['url']}"
        )

        send_message(message)

        print(f"Added {job['title']}")

    print("Completed.")


if __name__ == "__main__":
    main()