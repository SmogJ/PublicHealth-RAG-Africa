import os
import re
import csv
import json
import requests
from pathlib import Path
from bs4 import BeautifulSoup


def extract_text_from_html():
    base_url= "https://www.afro.who.int/news/feature_stories"
    story_urls= get_all_story_urls(base_url)
    

    # Check if any URLs were found
    if not story_urls:
        print("No story URLs were found. Exiting.")
    else:
        # Print the number of found URLs for verification
        print(f"Found {len(story_urls)} news and story URLs.")


    # Define the data folder
    # Make sure the directory exists
    data = Path("../data")
    data.mkdir(parents=True, exist_ok=True)

    # Define the file path
    data_file = data / "who_africa_features_stories.json"
    data_file.touch(exist_ok=True)
    
    # collect stories
    stories= []

    # Extract content from each story URL
    for url in story_urls[:10]:
        try:
            # print(get_story_content(url))
            story = get_story_content(url)           
            stories.append(story)
        
        except TypeError:
            continue

    # write to json file    
    with open(data_file, "w", encoding="utf-8") as json_file:
        json.dump(
            stories, json_file, ensure_ascii=False, indent=4
        )

    print(f"Saved {len(stories)} stories to {data_file.resolve()}")
    

def get_all_story_urls(base_url):
    """Scrape all feature story URLs across paginated results."""
    all_story_urls= []

    try:
        # send a get request to url
        r= requests.get(base_url, timeout=10)
        r.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        url_status= r.status_code
        print("Website status: ", url_status)
        r= r.text # get url content as text
      

        # Parse html content using beautiful soup
        # find main content of the feature stories page
        soup = BeautifulSoup(r, 'html.parser')   
        main_content= soup.find("div", "region region-content")


        # Find the last page number and use it to loop through the pages of the URL
        # loop the throught the total number of pages 
        last_page_num= main_content.find("li", "pager__item pager__item--last")
        last_num_str= int(last_page_num.find("a").get("href").strip("?page="))
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching base URL {base_url}: {e}")
        return []

    for num in range(0, last_num_str + 1):
        page_url = f"{base_url}?page={num}"
        print(f"Fetching story links from {page_url}")

        try:
            # get news/stories from  URLS from Highligth page
            content_page= requests.get(page_url, timeout= 10)
            content_page.raise_for_status()
            content_soup = BeautifulSoup(content_page.text, 'html.parser')

            # Find all the news/story links on the current page   
            div_content= content_soup.find("div", "region region-content")
            h3_tags= div_content.find_all("h3")
                
            
            for h3 in h3_tags:
                a_tag= h3.find("a")
                relative_url= a_tag.get("href")
                full_url= "https://www.afro.who.int" + relative_url.strip()
                all_story_urls.append(full_url)
                
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page_url}: {e}")
            continue # Continue to the next page even if one fails
    
    return all_story_urls


def get_story_content(url):
    """Extract title, date, location, and text from a single story."""

    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        
        soup = BeautifulSoup(r.text, 'html.parser')
        
        # Find the main content of the story itself.
        article = soup.find("article", "news full clearfix")

        # If the original structure is not found, try the alternative
        if not article:
            article = soup.find("article", class_="news is-promoted full clearfix")

        if article:
            # We get all the article title, date and time, article body
            article_title= article.find("span").get_text().strip()
            article_date_time= article.find("time").get("datetime")
            article_date= article.find("time").get_text()
            # Get text
            article_body= article.find("div", "field field--name-body field--type-text-with-summary field--label-hidden field--item")
            hyphen_pattern= re.compile(r"[-–—‒–]\W?") # search text for first occurrance of "-" hypen or dash and split
            article_location= re.split(hyphen_pattern, article_body.get_text("strong", strip=True), maxsplit=1)[0].replace("strong", "")
            article_text_s= re.split(hyphen_pattern, article_body.get_text("strong", strip=True), maxsplit=1)[1].replace("strong", "") 
            article_text_p= re.split(hyphen_pattern, article_body.get_text("p", strip=True), maxsplit=1)[1].replace("p", "")
            print(f"\nFetching story from URL: {url}")
            return {
                "url": url,
                "title":article_title,
                "date_time": article_date_time,
                "date":article_date,
                "location":article_location,
                "text_s": article_text_s,
                "text_p":article_text_p,
            } 
        else:
            print(f"Warning: Could not find article content for {url}")
            return None
        
    except requests.exceptions.RequestException as e:
        print(f"Error getting content from {url}: {e}")
        return None


if __name__=="__main__":
    extract_text_from_html()