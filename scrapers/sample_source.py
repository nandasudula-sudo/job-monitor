from datetime import datetime


def fetch_jobs():
    return [
        {
            "company": "Google",
            "title": "Software Engineer",
            "location": "Bengaluru",
            "source": "sample",
            "url": "https://example.com/job1",
            "discovered_at": datetime.now().isoformat(),
        },
        {
            "company": "Microsoft",
            "title": "Backend Engineer",
            "location": "Hyderabad",
            "source": "sample",
            "url": "https://example.com/job2",
            "discovered_at": datetime.now().isoformat(),
        },
    ]