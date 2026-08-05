import os
import sys
import time

import schedule


ROOT_DIRECTORY = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        ".."
    )
)

sys.path.insert(0, ROOT_DIRECTORY)

from main import main


def run_job():
    print("Starting scheduled execution")

    main()

    print("Execution completed")


schedule.every(4).hours.do(run_job)

run_job()

while True:
    schedule.run_pending()
    time.sleep(5)