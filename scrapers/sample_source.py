from datetime import datetime


def fetch_jobs():
    return [
        {
            "company": "Google",
            "title": "Software Engineer",
            "location": "Bengaluru",
            "source": "sample",
            "url": "https://example.com/job1_v2",
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
        {
            "company": "ABC",
            "title": "Marketing Manager",
            "location": "Delhi",
            "source": "sample",
            "url": "https://example.com/job3",
            "discovered_at": datetime.now().isoformat(),
        }
    ]