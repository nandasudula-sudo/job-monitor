import requests


def fetch_jobs(url):
    try:
        response = requests.get(url, timeout=30)

        print("Status code:", response.status_code)
        print("Headers:", response.headers.get("content-type"))

        if response.status_code != 200:
            print(response.text)
            return []

        return response.json()

    except Exception as error:
        print("ERROR:", error)
        return []