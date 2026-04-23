import requests
import hashlib
import json
from pathlib import Path
from bs4 import BeautifulSoup


# ==========================
# Define HTML data directory
# ==========================
project_dir: Path= Path(__file__).resolve().parent.parent.parent # root directory of the project
html_dir: Path= project_dir / "data" / "raw" / "html"
html_dir.mkdir(parents=True, exist_ok=True) # create the html data directory if it doesn't exist
index_file: Path= project_dir / "data" / "raw" / "index_file.jsonl"
# print(f"Project directory: {html_dir}")


# =================================
# Main function to run the pipeline
# ================================
def main():
    # r= requests.get("https://www.who.int/health-topics")

    # # 1. Check if the request was successful
    # if r.status_code != 200:
    #     print(f"Error: Failed to retrieve WHO health topics page. Status code: {r.status_code}")
    # else:
    #     print(f"WHO Website Status:{r.status_code} !!!") # check if the request was successful

    # #  2. Get HTML content of the page
    # health_topics_html= r.text
    # # print(health_topics_html)

    # # 3. Get all health topics links and types
    # health_topics= find_health_topics_links(health_topics_html)
    # print(f"Number of 'a' tags found: {len(health_topics['types'])}")
    # print(f"First 5 urls: {health_topics['urls'][:5]}")
    # print(f"Last 5 urls: {health_topics['urls'][-5:]}")

    # # 4. Get Health topic content
    # # Loop through the health topics links and get the content of each topic page
    # for title, url, cat_type in zip(health_topics["titles"], health_topics["urls"], health_topics["types"]):
    #     print(f"Getting html for the {title}, with the url: {url}")
    #     doc_id, file_path = save_html(url, title, cat_type)
    #     print(f"html for {title} saved successfully")

    # # 5. Extract Content HTML
    print(extract_content())
    # print(f"Content extracted from '{file}' successfully")


# =======================================
# find WHO health topics liinks and types
# =======================================
# def find_health_topics_links(html: str) -> dict:
    
#     soup: BeautifulSoup = BeautifulSoup(html, "html.parser") # parse the HTML content using BeautifulSoup
    
#     # 1. find all "a" tags with class="link-container table" or/and role="link"
#     urls: list= [link.get("href") for link in soup.find_all("a", class_="link-container table")]
#     titles: list = [title.get_text() for title in soup.find_all("p", class_= "heading text-underline")]
#     types: list = [cat_type.get_text() for cat_type in soup.find_all("span", class_= "timestamp")]
    
#     return {
#         "titles": titles,
#         "urls": urls,
#         "types": types,
#     }


# ===============================================================
# Save the html content of each topic and Index the topic content
# ===============================================================
# def save_html(url: str, title: str, cat_type:str | None) -> tuple[str, Path] -> tuple[str, Path]:
#     # 1. Get page
#     r= requests.get(url, timeout=15)
#     status_code= r.status_code # check if the request was successful

#     # 2. Check if the request was successful
#     if status_code != 200:
#         print(f"Error: Failed to retrieve content for URL: {url} with status code: {status_code}")
#     else:
#         print(f"Successfully retrieved content for URL: {url} with status code: {status_code}")

#     # 3. Get HTML content of the topic page
#     html= r.text

#     # 4. Create a hash for the url of the html
#     doc_id= hashlib.sha256(url.encode()).hexdigest()
#     file_path= html_dir / f"{doc_id}.html"

#     # 5. Save the html using the hash as the filename in html_dir
#     with open(file_path, "w", encoding="utf-8") as f:
#         f.write(html)

#     # 6. Save Doc index
#     with open(index_file, "a", encoding="utf-8") as f:
#             f.write(json.dumps({
#                 "id": doc_id,
#                 "title": title,
#                 "category": cat_type,
#                 "type": "html",
#                 "url": url,
#                 "file_path": str(file_path)
#             }) + "\n")

#     return doc_id, file_path


# ======================================
# Extract the content of each html page
# ======================================
def extract_content() -> dict:
    # 1. Get html form html_dir and index data from index_file
    # a. Get index data from index_file
    with open(index_file, "r", encoding="utf-8") as f:
        # file_info= [(json.loads(line.split("\n")[0])["file_path"]).split("\\")[-1] for line in f]
        file_info= [(json.loads(line.split("\n")[0])["id"]) for line in f]        

    # b. Get html files from html_dir
    for file in list(html_dir.glob("*.html")): # loop through all html files in the html_dir
        file_id= file.stem
        # html= str(file).split("\\")[-1]
        # print(html)

        # 2. Check if the file is in the index file
        if file_id not in file_info:
            print(f"File: '{file_id}' not in file index")
        else:
            print(f"Extracting content from '{file}'...")

        # 3. Extract html content
        soup= BeautifulSoup(file.read_text(encoding="utf-8"), "html.parser") 

        if not soup:
            raise ValueError(f"Error: Failed to parse HTML content for file: {file}")
        else:    
            article: BeautifulSoup | None = soup.find(name="article", class_="sf-detail-body-container sf-detail-body-wrapper health-topic--detail dynamic-content dynamic-content__article")
        
        # 3 a. Extracting Article content
        if not article:
            raise ValueError(f"Error: Failed to find article content for file: {file}")
        else:
            article_content: str = article.find(name="div", class_="sf_colsOut flex-clear").get_text(separator="\n") if soup.find_all("p") else None 
        # article_content= soup.find(name="div", class_="sf_colsIn single-tabContent").get_text(separator="\n") if soup.find(name="div", class_="sf_colsOut flex-clear") else None

        # 3 b. Extracting article title
        if not article:
            raise ValueError(f"Error: Failed to find article content for file: {file}")
        else:
            article_title: str = article.find(name="h1", class_="dynamic-content__title-text").get_text(strip= True)

        # 3 c. Extracting article credits
        if not article:
            raise ValueError(f"Error: Failed to find article content for file: {file}")
        else:
            article_credits: str = article.find(name="div", class_= "sf-image-credit__inner").get_text(strip= True)
        
        return {
            "id": file_id,
            "title": article_title,
            "credits": article_credits,
            "content": article_content
        }
            

if __name__ == "__main__":    main()