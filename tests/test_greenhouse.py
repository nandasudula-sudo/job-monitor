from scrapers.greenhouse import fetch_jobs

url = "https://boards-api.greenhouse.io/v1/boards/openai/jobs"

jobs = fetch_jobs(url)

print(jobs)