import os
import re
import requests
from pathlib import Path
from bs4 import BeautifulSoup


def main(url):
    url_content= get_url(url)
    print(parse_url(url_content[0], url_content[2]))
    


def get_url(url):
    try:
        # send a get request to url
        r= requests.get(url)
        r.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        url_status= r.status_code
        url_headers= r.headers['content-type']
        url_content= r.text # get url content as text

        return url_status, url_headers, url_content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_url(status, content):
    print(f"Website status: {status}")

    # --- Strategy for extracting main content ---
        # The Feature Store Page contents highlights of news and stories.
        # This news and story content are found in a div (div class="view-content"), that contains a common div (div class="row views-row").
        # The row views-row contains common tags, which are:
        #   - h3 tag (class="teaser-full__title"), which we use to get the the a tag.
        #   - the a tag has the link, and the title of the story, we'll use this to get to the main html content.
        #   - a time elememt containing the date and time of publication, we'll use to get the data and time of publication of the story.

    # Parse the html content
    soup = BeautifulSoup(content, 'html.parser')   


    main_content= soup.find("div", "region region-content")
    div_content= main_content.find("div", "view-content")
    h3_a_href= div_content.find_all("h3")

    
    # # Navigation of the Feature/news Afro WHO website
    
    
    # # Get news and stories from features_stories page
    base_url = "https://www.afro.who.int"
    content_links= []

    for h3 in h3_a_href:
        a_href= h3.find("a")
        content_links.append(f"{base_url}{a_href.get("href")}")

        

    return content_links


if __name__=="__main__":
    url= "https://www.afro.who.int/news/feature_stories"
    main(url)
