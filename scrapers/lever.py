import requests

from config.loader import load_json
from models.job import create_job


def fetch_company_jobs(company_name):
    url = (
        f"https://api.lever.co/v0/postings/"
        f"{company_name}?mode=json"
    )

    try:
        response = requests.get(url, timeout=30)

        print(
            f"Checking {company_name}: "
            f"{response.status_code}"
        )

        if response.status_code != 200:
            return []

        data = response.json()

    except Exception as error:
        print(
            f"Error while processing "
            f"{company_name}: {error}"
        )
        return []

    jobs = []

    for job in data:
        jobs.append(
            create_job(
                company=company_name,
                title=job.get("text", ""),
                location=job.get(
                    "categories", {}
                ).get("location", ""),
                url=job.get("hostedUrl", ""),
                source="lever",
            )
        )

    return jobs


def fetch_jobs():
    config = load_json(
        "config/lever_companies.json"
    )

    companies = config["companies"]

    all_jobs = []

    for company in companies:
        jobs = fetch_company_jobs(company)

        print(
            f"Collected {len(jobs)} jobs."
        )

        all_jobs.extend(jobs)

    return all_jobs
