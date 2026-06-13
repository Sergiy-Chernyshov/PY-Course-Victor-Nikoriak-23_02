# task 3

import json
import time
import requests
from threading import Thread


BASE_URL = "https://api.pushshift.io/reddit/comment/search/"
SUBREDDIT = "learnpython"

COMMENTS_PER_REQUEST = 100
NUMBER_OF_THREADS = 5

OUTPUT_FILE = "comments.json"


all_comments = []


def download_comments(thread_number, before_timestamp):
    params = {
        "subreddit": SUBREDDIT,
        "size": COMMENTS_PER_REQUEST,
        "sort": "desc",
        "sort_type": "created_utc",
        "before": before_timestamp
    }

    print(f"Thread {thread_number}: sending request...")

    response = requests.get(BASE_URL, params=params, timeout=15)
    response.raise_for_status()

    data = response.json()
    comments = data.get("data", [])

    print(f"Thread {thread_number}: downloaded {len(comments)} comments")

    all_comments.extend(comments)


def main():
    threads = []

    current_time = int(time.time())

    for i in range(NUMBER_OF_THREADS):
        before_timestamp = current_time - (i * 60 * 60)

        thread = Thread(
            target=download_comments,
            args=(i + 1, before_timestamp)
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    sorted_comments = sorted(
        all_comments,
        key=lambda comment: comment.get("created_utc", 0)
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(sorted_comments, file, indent=4, ensure_ascii=False)

    print(f"Saved {len(sorted_comments)} comments to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()