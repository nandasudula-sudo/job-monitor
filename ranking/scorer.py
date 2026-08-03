def calculate_score(job):
    score = 0

    title = job["title"].lower()
    location = job["location"].lower()

    title_scores = {
        "software engineer": 10,
        "backend engineer": 10,
        "java developer": 8,
        "machine learning engineer": 8,
        "data scientist": 8,
        "security engineer": 8,
    }

    location_scores = {
        "hyderabad": 10,
        "bengaluru": 10,
        "pune": 8,
        "chennai": 8,
        "gurgaon": 8,
        "noida": 8,
        "mumbai": 8,
        "remote": 5,
    }

    for keyword, points in title_scores.items():
        if keyword in title:
            score += points

    for keyword, points in location_scores.items():
        if keyword in location:
            score += points

    return score