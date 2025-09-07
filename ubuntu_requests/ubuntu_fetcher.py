import requests
import os
import hashlib
from urllib.parse import urlparse
from pathlib import Path

def get_filename_from_url(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    return filename if filename else "downloaded_image.jpg"

def is_duplicate(content, directory):
    # Check if image with same hash already exists
    image_hash = hashlib.md5(content).hexdigest()
    for file in Path(directory).glob("*"):
        with open(file, 'rb') as f:
            if hashlib.md5(f.read()).hexdigest() == image_hash:
                return True
    return False

def fetch_image(url, directory):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Check content type
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (not an image): {url}")
            return

        # Check for duplicates
        if is_duplicate(response.content, directory):
            print(f"✗ Duplicate image skipped: {url}")
            return

        # Save image
        filename = get_filename_from_url(url)
        filepath = os.path.join(directory, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Please enter image URLs separated by commas:\n").split(',')

    directory = "Fetched_Images"
    os.makedirs(directory, exist_ok=True)

    for url in map(str.strip, urls):
        if url:
            fetch_image(url, directory)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()