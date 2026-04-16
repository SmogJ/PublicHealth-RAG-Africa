import requests
import hashlib
from pathlib import Path
from bs4 import BeautifulSoup

# ==========================
# Define HTML data directory
# ==========================
project_dir: Path= Path(__file__).resolve().parent.parent.parent # root directory of the project
html_dir: Path= project_dir / "data" / "raw" / "html"
html_dir.mkdir(parents=True, exist_ok=True) # create the html data directory if it doesn't exist
# print(f"Project directory: {html_dir}")


# =================================
# Main function to run the pipeline
# ================================
def main():
    r= requests.get("https://www.who.int/health-topics")

    # 1. Check if the request was successful
    if r.status_code != 200:
        print(f"Error: Failed to retrieve WHO health topics page. Status code: {r.status_code}")
    else:
        print(f"WHO Website Status:{r.status_code} !!!") # check if the request was successful

    #  2. Get HTML content of the page
    health_topics_html= r.text
    # print(health_topics_html)

    # 3. Get all health topics links and types
    health_topics= find_health_topics_links(health_topics_html)
    print(f"Number of 'a' tags found: {len(health_topics['types'])}")
    print(f"First 5 urls: {health_topics['urls'][:5]}")
    print(f"Last 5 urls: {health_topics['urls'][-5:]}")

    # 4. Get Health topic content
    # Loop through the health topics links and get the content of each topic page
    for title, url in zip(health_topics["titles"], health_topics["urls"]):
        print(f"Getting html for the {title}, with the url: {url}")
        html= get_html(url)
        print(html)


# =======================================
# find WHO health topics liinks and types
# =======================================
def find_health_topics_links(html: str) -> dict:
    
    soup: BeautifulSoup = BeautifulSoup(html, "html.parser") # parse the HTML content using BeautifulSoup
    
    # 1. find all "a" tags with class="link-container table" or/and role="link"
    urls: list= [link.get("href") for link in soup.find_all("a", class_="link-container table")]
    titles: list = [title.get_text() for title in soup.find_all("p", class_= "heading text-underline")]
    types: list = [cat_type.get_text() for cat_type in soup.find_all("span", class_= "timestamp")]
    
    return {
        "titles": titles,
        "urls": urls,
        "types": types,
    }


# ===========================================================================
# Get the HTML content of each topic page
# ==========================================================================
def get_html(url: str):

    r= requests.get(url, timeout=10) # make a GET request to the topic page URL

    status_code= r.status_code # check if the request was successful

    # 1. Check if the request was successful
    if status_code != 200:
        print(f"Error: Failed to retrieve content for URL: {url} with status code: {status_code}")
    else:
        print(f"Successfully retrieved content for URL: {url} with status code: {status_code}")

    # 2. Get HTML content of the topic page
    soup: BeautifulSoup= BeautifulSoup(r.text, "html.parser")

    return soup
    



# Extract the title, word_count, type, category, credits and tag

# Download/save the content of each topic as html files in the html data directory


if __name__ == "__main__":    main()