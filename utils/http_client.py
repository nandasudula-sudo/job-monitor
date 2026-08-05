import time

import requests


MAX_RETRIES = 3
REQUEST_TIMEOUT = 30


def get(url):
    last_exception = None

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(
                url,
                timeout=REQUEST_TIMEOUT,
            )

            return response

        except requests.exceptions.RequestException as error:
            last_exception = error

            print(
                f"Attempt {attempt + 1} failed."
            )

            time.sleep(2)

    raise last_exception