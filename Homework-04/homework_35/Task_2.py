#Task2

import json
import time
import requests
import multiprocessing
from concurrent.futures import ThreadPoolExecutor


BASE_URL = "https://api.pushshift.io/reddit/comment/search/"
SUBREDDIT = "learnpython"

COMMENTS_PER_REQUEST = 100
THREADS_COUNT = 5

OUTPUT_FILE = "comments.json"


def download_comments(before_timestamp):
    params = {
        "subreddit": SUBREDDIT,
        "size": COMMENTS_PER_REQUEST,
        "sort": "desc",
        "sort_type": "created_utc",
        "before": before_timestamp
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=15)

        if response.status_code == 403:
            print("403 Forbidden: Pushshift blocked the request")
            return []

        response.raise_for_status()

        data = response.json()
        comments = data.get("data", [])

        print(f"Downloaded {len(comments)} comments")
        return comments

    except requests.exceptions.RequestException as error:
        print("Request error:")
        print(error)
        return []


def download_with_threads():
    print("\nDownloading with ThreadPoolExecutor...")

    current_time = int(time.time())
    timestamps = []

    for i in range(THREADS_COUNT):
        before_timestamp = current_time - (i * 60 * 60)
        timestamps.append(before_timestamp)

    all_comments = []

    with ThreadPoolExecutor(max_workers=THREADS_COUNT) as executor:
        results = executor.map(download_comments, timestamps)

        for comments in results:
            all_comments.extend(comments)

    return all_comments


def download_with_multiprocessing():
    print("\nDownloading with multiprocessing...")

    current_time = int(time.time())
    timestamps = []

    for i in range(THREADS_COUNT):
        before_timestamp = current_time - (i * 60 * 60)
        timestamps.append(before_timestamp)

    all_comments = []

    with multiprocessing.Pool(processes=THREADS_COUNT) as pool:
        results = pool.map(download_comments, timestamps)

        for comments in results:
            all_comments.extend(comments)

    return all_comments


def save_comments_to_json(comments, filename):
    sorted_comments = sorted(
        comments,
        key=lambda comment: comment.get("created_utc", 0)
    )

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(sorted_comments, file, indent=4, ensure_ascii=False)

    print(f"\nSaved {len(sorted_comments)} comments to {filename}")


def main():
    start_time = time.perf_counter()

    thread_comments = download_with_threads()

    thread_end_time = time.perf_counter()
    thread_time = thread_end_time - start_time

    process_start_time = time.perf_counter()

    process_comments = download_with_multiprocessing()

    process_end_time = time.perf_counter()
    process_time = process_end_time - process_start_time

    all_comments = thread_comments + process_comments

    save_comments_to_json(all_comments, OUTPUT_FILE)

    print("\nPerformance:")
    print(f"ThreadPoolExecutor time: {thread_time:.2f} seconds")
    print(f"Multiprocessing time: {process_time:.2f} seconds")

    print("\nTotal comments:", len(all_comments))


if __name__ == "__main__":
    main()