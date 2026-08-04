import requests

from config.loader import load_json
from models.job import create_job


def fetch_company_jobs(company_name):
    url = (
        f"https://boards-api.greenhouse.io/v1/boards/"
        f"{company_name}/jobs"
    )

    try:
        response = requests.get(url, timeout=30)

        if response.status_code != 200:
            print(
                f"Unable to retrieve jobs for "
                f"{company_name} ({response.status_code})"
            )
            return []

        data = response.json()

    except requests.exceptions.RequestException as error:
        print(f"Error while processing {company_name}: {error}")
        return []

    jobs = []

    for job in data.get("jobs", []):

        jobs.append(
            create_job(
                company=company_name,
                title=job.get("title", ""),
                location=job.get("location", {}).get("name", ""),
                url=job.get("absolute_url", ""),
                source="greenhouse",
            )
        )

    return jobs


def fetch_jobs():
    config = load_json(
        "config/greenhouse_companies.json"
    )

    companies = config["companies"]

    all_jobs = []

    for company in companies:
        print(f"Checking {company} ...")

        jobs = fetch_company_jobs(company)

        print(f"Collected {len(jobs)} jobs.")

        all_jobs.extend(jobs)

    return all_jobs