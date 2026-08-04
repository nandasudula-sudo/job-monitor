from scrapers.greenhouse import fetch_jobs

jobs = fetch_jobs()

keywords = [
    "india",
    "hyderabad",
    "bengaluru",
    "bangalore",
    "pune",
    "mumbai",
    "chennai",
    "gurgaon",
    "remote"
]

count = 0

for job in jobs:
    location = job["location"].lower()

    if any(keyword in location for keyword in keywords):
        count += 1
        print(job)

print()
print(f"Indian jobs found: {count}")