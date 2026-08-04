import requests

from config.loader import load_json


def fetch_company_jobs(company_name):
    url = (
        f"https://boards-api.greenhouse.io/v1/boards/"
        f"{company_name}/jobs"
    )

    response = requests.get(url, timeout=30)

    if response.status_code != 200:
        print(f"Unable to retrieve jobs for {company_name}")
        return []

    data = response.json()

    jobs = []

    for job in data.get("jobs", []):
        jobs.append(
            {
                "company": company_name,
                "title": job.get("title", ""),
                "location": job.get("location", {}).get("name", ""),
                "url": job.get("absolute_url", ""),
                "source": "greenhouse",
            }
        )

    return jobs


def fetch_jobs():
    config = load_json("config/greenhouse_companies.json")

    companies = config["companies"]

    all_jobs = []

    for company in companies:
        all_jobs.extend(fetch_company_jobs(company))

    return all_jobs