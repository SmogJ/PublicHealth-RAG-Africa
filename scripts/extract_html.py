import os
import re
import requests
from pathlib import Path
from bs4 import BeautifulSoup


def main():
    url= "https://www.afro.who.int/news/feature_stories"
    nav_url= get_nav_urls(url)
    print(get_contetn_url(nav_url))
    


def get_nav_urls(url):
    try:
        # send a get request to url
        r= requests.get(url)
        r.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        url_status= r.status_code
        print(url_status)
        url_content= r.text # get url content as text
      

        # Parse html content using beautiful soup
        # find main content of the feature stories page
        soup = BeautifulSoup(url_content, 'html.parser')   
        main_content= soup.find("div", "region region-content")


        # Find the last page number and use it to loop through the pages of the URL
        last_page= main_content.find("li", "pager__item pager__item--last")
        last_a_num= int(last_page.find("a").get("href").strip("?page="))
        
        # loop the throught the total number of pages in the 
        nav_urls= []
        for num in range(0, last_a_num + 1):
            nav_urls.append(f"https://www.afro.who.int/news/feature_stories?page={num}")
        for url in nav_urls:
            return url

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_contetn_url(url):
    # --- Strategy for extracting main content ---
        # The Feature Stories Page contents highlights of news/stories.
        # They are all under the a div (div class="view-content"), but will be accessed through a div with class name="region region-content" 
        # to get the content for each news/stories, the div (div class="row views-row") contains the followung tags and attributes.
        #   - h3 tag (class="teaser-full__title"), which we use to get the the a tag.
        #   - the a tag has the link/path to the main content, and the title of the story, we'll use this to get to the main html content.

    # send a get request to url
    r= requests.get(url)
    r.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

    url_status= r.status_code
    print(url_status)
    url_content= r.text # get url content as text

    # find main content of the feature stories page
    soup= BeautifulSoup(url_content, 'html.parser')
    main_content= soup.find("div", "region region-content")


    # get news/stories from  URLS from Highligth page
    div_content= main_content.find("div", "view-content")
    h3_a_href= div_content.find_all("h3")
    
    base_url = "https://www.afro.who.int"
    content_urls= []

    for h3 in h3_a_href:
        a_href= h3.find("a")
        content_urls.append(f"https://www.afro.who.int{a_href.get("href")}")

        

    return content_urls


if __name__=="__main__":
    main()