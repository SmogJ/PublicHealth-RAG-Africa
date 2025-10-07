import json
import time
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from extract_html import get_page_urls, get_all_content_urls



# Index Page url
pub_url= "https://www.afro.who.int/publications"


def get_pdf(pub_url):
    """Get content from html webpage and download pdf file"""

    # --- Setup Directories ---
    # Define the data folder
    # Make sure the directory exists
    project_root = Path(__file__).parent.parent
    data = project_root / "data"
    data.mkdir(parents=True, exist_ok=True)

    data_html_pub = Path(data, "html_publication")
    data_html_pub.mkdir(exist_ok=True)

    data_file = data_html_pub / "who_africa_publications.json"
    # data_file.touch(exist_ok=True)

    # --- Get all the Pages and Content URLs ---
    pages= get_page_urls(pub_url)
    print(f"Total Pages: {len(pages)}")

    pdf_page_urls= get_all_content_urls(pages[:1])
    print(f"Total pdf page URLs: {len(pdf_page_urls)}")

    
    # --- Process Content URLs (OPTIMIZED LOOP) ---
    pdf_links = []
    pdf_names = []
    pdf_metadata = []

    for page_url in pdf_page_urls:
        try: 
            # CALL THE FUNCTION ONLY ONCE
            content_tuple = get_pdf_page_content(page_url)
            
            if content_tuple is None:
                continue # Skip if content could not be retrieved
            
            title, summary, links = content_tuple

            # 1. Build Metadata
            pdf_metadata.append(
                {
                    "title": title, 
                    "summary": summary, 
                    "urls": links,
                    "source_url": page_url # Added for better tracking
                }
            )
            
            # 2. Collect Links and Names
            for link in links:
                pdf_links.append(link)
                # Extract the file name from the URL path (assuming a consistent structure)
                # Use a cleaner split/pop method
                file_name = link.split("/")[-1]
                pdf_names.append(file_name)
            
            print(f"Successfully processed: {title}")
            time.sleep(0.5) # Be polite!

        except requests.exceptions.RequestException as e:
            print(f"Error getting content from {page_url}: {e}")
            continue
        except Exception as e:
             # Catch other errors, like index out of range if get_pdf_page_content returned partial data
            print(f"An unexpected error occurred while processing {page_url}: {e}")
            continue
    
    # --- Save Metadata to JSON ---
    print(f"\nTotal PDF links collected: {len(pdf_links)}")
    with open(data_file, "w", encoding="utf-8") as jsonfile:
        json.dump(pdf_metadata, jsonfile, ensure_ascii=False, indent=4)
    print(f"Metadata saved to {data_file.resolve()}")

    # --- Download PDFs ---
    if len(pdf_links) == len(pdf_names):
        print(f"\nStarting download of {len(pdf_links)} PDF files...")
        
        for link, name in zip(pdf_links[:10], pdf_names[:10]):
            download_extract_pdf_file_content(link, name)
            time.sleep(1) # Add a slight delay for downloads
    else:
        print("Warning: Link count mismatch. Skipping downloads.")


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
            pdf_name= [a.get_text() for a in pdf_content.select("span.file-link > a")]

            return  pdf_title, pdf_desc, pdf_items,

    except requests.exceptions.RequestException as e:
        print(f"Error getting content from {url}: {e}")
        return None


def download_extract_pdf_file_content(url, name):
    """Download pdf file"""
    # Define the data folder
    # Make sure the directory exists
    data = Path("../data")
    data.mkdir(parents=True, exist_ok=True)

    # --- Setup Directories ---
    project_root = Path(__file__).parent.parent
    data = project_root / "data"
    data_pdf = data / "pdf_publication"
    data_pdf.mkdir(exist_ok=True)
    data_file = data_pdf / name

    # --- Download Logic ---
    try:
        response = requests.get(url, stream=True, timeout=30) # Streaming on for large files stream=True for large files
        response.raise_for_status() # Check for bad status codes
        
        # Save the PDF file locally
        with open(data_file, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
                
        print(f"SUCCESS: Downloaded '{name}'")
        # Returning True can be useful for logging success
        return True 

    except requests.exceptions.RequestException as e:
        print(f"FAILED: Error downloading {name} from {url}: {e}")
        return False
    


if __name__=="__main__":
    get_pdf(pub_url)