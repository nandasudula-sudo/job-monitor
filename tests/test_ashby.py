from scrapers.ashby import fetch_jobs

jobs = fetch_jobs()

print(f"Number of jobs: {len(jobs)}")

for job in jobs[:10]:
    print(job)