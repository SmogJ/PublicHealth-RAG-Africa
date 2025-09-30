import sys
import re
import json
import requests
from pathlib import Path
from bs4 import BeautifulSoup, SoupStrainer
from extract_html import get_page_urls, get_all_content_urls



# Index Page url
pub_url= "https://www.afro.who.int/publications"


def get_pdf(pub_url):
    """Get content from html webpage and download pdf file"""
    # Define the data folder
    # Make sure the directory exists
    data = Path("../data")
    data.mkdir(parents=True, exist_ok=True)

    # Define the file path
    data_file = data / "who_africa_publications.json"
    data_file.touch(exist_ok=True)

    pages= get_page_urls(pub_url)
    print(f"Total Pages: {len(pages)}")

    pdf_page_urls= get_all_content_urls(pages[:1])
    print(f"Total pdf page URLs: {len(pdf_page_urls)}")

    # print(get_pdf_page_content(pdf_page_urls[1]))

    # download links
    pdf_links= [link for url in pdf_page_urls  for link in get_pdf_page_content(url)[2]]


    # Page metadata
    pdf_metadata= []


    # get content of pdf page contents
    for page in pdf_page_urls:
        try: 
            pdf_metadata.append(
                {
                    "title": get_pdf_page_content(page)[0], 
                    "summary": get_pdf_page_content(page)[1], 
                    "urls": get_pdf_page_content(page)[2]
                    }
                    )
            print(f"Getting content from {page}")
        except requests.exceptions.RequestException as e:
            print(f"Error getting content from {pdf_page_urls}: {e}")
            return None
        
    print(f"Total download links {len(pdf_links)}")
    print(pdf_metadata)     

    # save in json file
    with open(data_file, "w", encoding="utf-8") as jsonfile:
        json.dump(pdf_metadata, jsonfile, ensure_ascii=False, indent=4 )


def get_pdf_page_content(url):
    """Get html metadata"""    
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()

        soup = BeautifulSoup(r.text, 'html.parser')

        # Find the main content of the story itself.
        pdf_content = soup.find("article", "publication is-promoted full clearfix")

        # If the original structure is not found, try the alternative
        if not pdf_content:
            pdf_content = soup.find("article", class_="publication full clearfix")

        if pdf_content:
            # We get all the pdf title, date and time, article body
            pdf_title= pdf_content.find("h3", "publication-title").get_text()
            if not pdf_content.find("p"):
                pdf_desc= None
            else:
                pdf_desc = pdf_content.find("p").get_text()
            pdf_items= [a.get("href") for a in pdf_content.select("span.file-link > a")] # get the pdf file download links

            return pdf_title, pdf_desc, pdf_items

    except requests.exceptions.RequestException as e:
        print(f"Error getting content from {url}: {e}")
        return None



if __name__=="__main__":
    get_pdf(pub_url)