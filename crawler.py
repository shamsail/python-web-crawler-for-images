import sys
import time
import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin

results = []
visited_urls = set()

def crawl(url, specified_depth, depth=0):
    if depth < 0 or url in visited_urls or depth > specified_depth:
        return

    visited_urls.add(url)  # Mark URL as visited

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        print(f"Crawling: {url} (Depth: {depth})")  # Print with depth value

        # Download images on the page and store results
        for img_tag in soup.find_all('img'):
            img_src = img_tag.get('src')
            if img_src:
                img_url = urljoin(url, img_src)
                store_result(img_url, url, depth)

        # Find links on the page and recursively crawl them
        links = soup.find_all('a', href=True)
        for link in links:
            absolute_link = urljoin(url, link['href'])
            crawl(absolute_link, specified_depth, depth + 1)  # Increment depth here

    except requests.exceptions.RequestException as e:
        print(f"Error crawling {url}: {e}")

    time.sleep(1)  # Add a delay of 1 second before making the next request

def store_result(img_url, source_url, depth):
    results.append({
        "imageUrl": img_url,
        "sourceUrl": source_url,
        "depth": depth
    })

def save_results_to_json(results):
    with open("results.json", "w") as f:
        json.dump({"results": results}, f, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python crawler.py <start_url> <depth>")
        sys.exit(1)

    start_url = sys.argv[1]
    specified_depth = int(sys.argv[2])

    crawl(start_url, specified_depth)  # Start with depth 0
    save_results_to_json(results)