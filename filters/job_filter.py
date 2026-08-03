import json


def load_keywords():
    with open("config/keywords.json", "r") as file:
        return json.load(file)


def matches(job):
    keywords = load_keywords()

    titles = keywords["titles"]
    locations = keywords["locations"]

    title = job["title"].lower()
    location = job["location"].lower()

    title_match = any(keyword in title for keyword in titles)

    location_match = any(keyword in location for keyword in locations)

    return title_match and location_match