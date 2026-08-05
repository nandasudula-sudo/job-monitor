from config.loader import load_json


def load_preferences():
    return load_json("config/preferences.json")


def matches(job):
    preferences = load_preferences()

    include_keywords = preferences["include_keywords"]
    exclude_keywords = preferences["exclude_keywords"]
    experience_keywords = preferences["experience_keywords"]
    locations = preferences["locations"]

    title = job["title"].lower()
    location = job["location"].lower()

    title_match = any(
        keyword.lower() in title
        for keyword in include_keywords
    )

    excluded = any(
        keyword.lower() in title
        for keyword in exclude_keywords
    )

    experience_match = any(
        keyword.lower() in title
        for keyword in experience_keywords
    )

    location_match = any(
        keyword.lower() in location
        for keyword in locations
    )

    return (
        title_match
        and location_match
        and not excluded
        and not experience_match
    )