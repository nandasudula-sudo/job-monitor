from database.database import insert_job
from database.database import job_exists
from filters.job_filter import matches
from notifier.telegram_bot import send_message
from ranking.scorer import calculate_score


MINIMUM_SCORE = 10


def process_job(job):

    if not matches(job):
        print(f"Rejected: {job['title']}")
        return

    score = calculate_score(job)

    if score < MINIMUM_SCORE:
        print(f"Low score: {job['title']}")
        return

    if job_exists(job["url"]):
        print(f"Skipping: {job['title']}")
        return

    insert_job(job)

    message = (
        f"🚀 NEW JOB\n\n"
        f"Company: {job['company']}\n"
        f"Role: {job['title']}\n"
        f"Location: {job['location']}\n"
        f"Score: {score}\n"
        f"Source: {job['source']}\n"
        f"Link: {job['url']}"
    )

    send_message(message)

    print(f"Added: {job['title']}")