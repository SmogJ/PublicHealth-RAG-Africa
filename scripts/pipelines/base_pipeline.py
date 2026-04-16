import requests
import hashlib
from bs4 import BeautifulSoup 
from pathlib import Path
from who_pipeline import find_health_topics_links


# ==========================
# Define HTML data directory
# ==========================
project_dir: Path= Path(__file__).resolve().parent.parent.parent # root directory of the project
html_dir: Path= project_dir / "data" / "raw" / "html"
html_dir.mkdir(parents=True, exist_ok=True) # create the html data directory if it doesn't exist
# print(f"Project directory: {html_dir}")


def main():
    ...
    # 1. Import pipeline
    # 2. Save pipeline raw html
    # 3. Extract pipeline content
    # 4. Save pipeline content as JSONL

# ===================================
# Save the html content of each topic
# ===================================
def save_html(url: str) -> None:
    # 1. Get page
    r= requests.get(url, timeout=15)
    status_code= r.status_code # check if the request was successful

    # 2. Check if the request was successful
    if status_code != 200:
        print(f"Error: Failed to retrieve content for URL: {url} with status code: {status_code}")
    else:
        print(f"Successfully retrieved content for URL: {url} with status code: {status_code}")

    # 3. Get HTML content of the topic page
    html= r.text

    # 4. Create a hash for the url of the html
    doc_id= hashlib.md5(url.encode()).hexdigest()
    file_path= html_dir / f"{doc_id}.html"

    # 5. Save the html using the hash as the filename in html_dir
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)


# ======================================
# Extract the content of each html page
# ======================================
def extract_content(html: str | None, url: str | None, title: str | None, cat_type: str | None) -> dict:
    # 1. Get html form html_dir
    # 2. Extract content


# ======================================
# Save the extracted content as JSONL
# ======================================


if __name__=="__main__":    main()