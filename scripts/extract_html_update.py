import sys
import os
import json
from pathlib import Path
from extract_html import get_all_content_urls, get_story_content, get_all_content_urls


# check if the most recent article is an update
def chcek_for_update():
    """Check for and Scrape the most recent story on the index page"""
    
    # --- Setup Directories ---
    # Define the data folder
    # Make sure the directory exists
    project_root = Path(__file__).parent.parent
    data = project_root / "data"
    data.mkdir(parents=True, exist_ok=True)

    # Define the file path
    data_html_pub = Path(data, "html_publication")
    data_html_pub.mkdir(exist_ok=True)

    # Define the file path
    data_file = data_html_pub / "who_africa_features_stories.json"
    data_file.touch(exist_ok=True)


    last_article_in_database= get_last_article()
    recent_story= get_update()

    #  Comparing the recent data to existing data in the database
    if last_article_in_database != recent_story:
        print(f"New Article Detected. URL: {recent_story["url"]}")
    else:
        sys.exit("DATABASE IS UP TO DATE!!!!!")

    #  Get recent data from most recent article
    recent_article= get_story_content(recent_story["url"])

    # Load Existing Data "Help from Gemini"
    existing_articles = []
    if data_file.exists() and data_file.stat().st_size > 0:
        try:
            with open(data_file, "r", encoding="utf-8") as json_file:
                existing_articles = json.load(json_file)
            print(f"Loaded {len(existing_articles)} existing articles from the database.")
        except json.JSONDecodeError:
            print("Warning: Existing JSON file is corrupted or empty. Starting with only the new article.")
            
    # Prepend the new article
    # Insert the new article at the beginning of the list
    existing_articles.insert(0, recent_article)

    # write to json file    
    with open(data_file, "w", encoding="utf-8") as json_file:
        json.dump(
            existing_articles, json_file, ensure_ascii=False, indent=4
        )
        
    

# get the date of the last scraped article
def get_last_article():
    """Get the last article metadata from the database"""
    # get article directory
    articles_dir= Path("data")
    if articles_dir.is_dir():
        articles_file = Path(articles_dir, "who_africa_features_stories.json")
        if articles_file.exists():
            with open(articles_file, "r", encoding="utf-8") as f:
                articles_json= json.load(f)
                article_url= articles_json[0]["url"]
                article_title= articles_json[0]["title"]
                article_date_time= articles_json[0]["date_time"]
                return {
                    "url":article_url, 
                    "title":article_title, 
                    "date_time": article_date_time
                    }
        else:
            print(f"File not found: {articles_file}")
            return None
    else:
        print(f"File not found: {articles_dir}")
        return None


# get the data from the url of the lastest html article
def get_update():
    """Get the most recent article metadata on the index page"""
    index_page= ["https://www.afro.who.int/news/feature_stories?page=0"]
    contents_of_index= get_all_content_urls(index_page)
    get_lastest_article= get_story_content(contents_of_index[0])
    return {
        "url":get_lastest_article["url"],
        "title": get_lastest_article["title"],
        "date_time": get_lastest_article["date_time"]
        }


if __name__=="__main__":
    chcek_for_update()