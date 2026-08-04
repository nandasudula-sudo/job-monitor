import requests

from config.loader import load_json


def fetch_company_jobs(company_name):
    url = f"https://api.lever.co/v0/postings/{company_name}?mode=json"

    try:
        response = requests.get(url, timeout=30)

        print(f"{company_name}: {response.status_code}")

        if response.status_code != 200:
            return []

        data = response.json()

    except Exception as e:
        print(f"{company_name}: {e}")
        return []

    jobs = []

    for job in data:
        jobs.append(
            {
                "company": company_name,
                "title": job.get("text", ""),
                "location": job.get("categories", {}).get(
                    "location", ""
                ),
                "url": job.get("hostedUrl", ""),
                "source": "lever",
            }
        )

    return jobs


def fetch_jobs():
    config = load_json("config/sources.json")

    companies = config["lever_companies"]

    all_jobs = []

    for company in companies:
        all_jobs.extend(fetch_company_jobs(company))

    return all_jobs