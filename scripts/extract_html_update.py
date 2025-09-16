import os
import json
from pathlib import Path


# check if the most recent article is an update
def main():
    print(get_last_article())

# get the date of the last scraped article
def get_last_article():
    # get article directory
    articles_dir= Path("data")
    if articles_dir.is_dir():
        articles_file = Path(articles_dir, "who_africa_features_stories.json")
        if articles_file.exists():
            with open(articles_file, "r", encoding="utf-8") as f:
                articles_json= json.load(f)
                article_url= articles_json[0]["url"]
                article_url= articles_json[0]["title"]
                article_date_time= articles_json[0]["date_time"]
                return article_url, article_url, article_date_time 
        else:
            print(f"File not found: {articles_file}")
            return None
    else:
        print(f"File not found: {articles_dir}")
        return None


# get the data from the url of the lastest html article
def get_update():
    ...


if __name__=="__main__":
    main()