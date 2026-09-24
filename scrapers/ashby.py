import requests

from config.loader import load_json
from models.job import create_job


URL = "https://jobs.ashbyhq.com/api/non-user-graphql"


def fetch_company_jobs(company_name):
    payload = {
        "query": f"""
        query {{
            jobBoardWithTeams(
                organizationHostedJobsPageName: "{company_name}"
            ) {{
                jobPostings {{
                    id
                    title
                    locationName
                }}
            }}
        }}
        """
    }

    try:
        response = requests.post(
            URL,
            json=payload,
            timeout=30,
        )

        if response.status_code != 200:
            print(
                f"Unable to retrieve jobs for "
                f"{company_name}"
            )
            return []

        data = response.json()

    except Exception as error:
        print(
            f"Error while processing "
            f"{company_name}: {error}"
        )
        return []

    board = (
        data.get("data", {})
        .get("jobBoardWithTeams")
    )

    if board is None:
        print(
            f"No job board found for "
            f"{company_name}, skipping."
        )
        return []

    postings = board.get("jobPostings", [])

    jobs = []

    for posting in postings:
        job_id = posting.get("id", "")

        jobs.append(
            create_job(
                company=company_name,
                title=posting.get("title", ""),
                location=posting.get(
                    "locationName", ""
                ),
                url=f"ashby://{company_name}/{job_id}",
                source="ashby",
            )
        )

    return jobs


def fetch_jobs():
    config = load_json(
        "config/ashby_companies.json"
    )

    companies = config["companies"]

    all_jobs = []

    for company in companies:
        print(f"Checking {company} ...")

        jobs = fetch_company_jobs(company)

        print(f"Collected {len(jobs)} jobs.")

        all_jobs.extend(jobs)

    return all_jobs
