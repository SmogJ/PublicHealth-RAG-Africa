# Project Journal: Public Health RAG for Africa

This journal documents the progress, challenges, decisions, and learning points throughout the development of the Public Health RAG for Africa application.

---

## **Week 1 (July 14, 2025)**

### **Goals for the Week:**
* Set up local development environment (Python virtual environment).
* Initialize Git repository and set up basic project structure.
* Create initial `README.md` and `JOURNAL.md` files.
* Identify initial data sources (specific URLs for testing).

### **Progress Made:**
* Successfully created and activated a Python virtual environment (`P_H_RAG`).
* Initialized Git repository.
* Created `README.md` outlining the project vision, problem, solution, and goals.
* Created this `JOURNAL.md` for ongoing documentation.
* Provide initial data source URLs for testing.

### **Challenges Encountered & Solutions:**
* _No significant challenges encountered yet in environment setup._

### **Libraries/Tools Used & Rationale:**
* **Python (3.x):** Core language for AI/ML and web development.
* **`venv` (Python built-in):** For creating isolated virtual environments to manage project dependencies. Essential for preventing dependency conflicts.
* **Git & GitHub:** For version control, tracking changes, and enabling future collaboration. GitHub provides a remote backup and project visibility.

### **Next Steps:**
* Research and sort data sources (WHO AFRO, Africa CDC, National MoH documents on Infectious Diseases and NCDs).
* Begin drafting Python scripts for web scraping (HTML) and PDF text extraction.

### **Lessons Learned:**
* Early environment setup and version control are critical for a smooth development process.
* Clear documentation, even at the initial stage, helps define scope and track progress.

---

## **Week 8 (Aug 2, 2025 - ...)**

### **Goals for the Week:**
* Develop robust web scraping script for HTML content.

### **Progress Made:**
* Research data sources element to understand data extraction strategy
* Write web scraping script to scrape WHO Africa features and stories from HTML
* Write web scraping script to scrape WHO Africa PDF documents

### **Challenges Encountered & Solutions:**
* coding for only one day in a week make the whole process slow
* got stuck in extracting data from html because of other important events and tasks.

### **Libraries/Tools Used & Rationale:**
* **Request**
* **Beautifulsoup**
* **JSON**
* **CSV**
* **Pathlib**

### **Next Steps:**
* complete the html article extraction scrapt as by the comming week

### **Lessons Learned:**
* Scheduling a day for coding is not a good way to go, need to make out more time for the project.

---

## **Week 9 (Aug 9, 2025 - ...)**

### **Goals for the Week:**
* Develop robust web scraping script for HTML content.

### **Progress Made:**
* Was able to complete the html scraping script and save as json file.
* was able to start the extract_pdf script.


### **Challenges Encountered & Solutions:**
* Writing script was still slow, need to improve my code speed and style
* still struggle with reading and understanding documentations

### **Libraries/Tools Used & Rationale:**
* **Request**
* **Beautifulsoup**
* **JSON**
* **CSV**
* **Pathlib**

### **Next Steps:**
* finish PDF extraction script

### **Lessons Learned:**
* Scheduling a day for coding is not a good way to go, still a challenge, will improve.
---

## **Week 10 (Sep 30, 2025 )**

### **Goals for the Week:**
* Develop robust web scraping script for PDF content.

### **Progress Made:**
* Was able to scrape the pdf files for the WHO publication website to a database.
* using the html scraping script made it faster and easier to write. 


### **Challenges Encountered & Solutions:**
* Writing scripts is still pretty much slow as I'm only able to work once in a week for about 4 to 6 hours.
* studing documentation is becoming easier, but I'm challenged a bit in coverting knowledge to code.

### **Libraries/Tools Used & Rationale:**
* **Request**
* **Beautifulsoup**
* **JSON**
* **from extract_html [html scraping script]**
* **Pathlib**

### **Next Steps:**
* scrape data from pdf file.
* finish PDF scraping script.

### **Lessons Learned:**
* Modularizing code make them reusable in other code.
---

## **Week 11 (Oct 07, 2025 )**

### **Goals for the Week:**
* Develop robust web scraping script for PDF content.

### **Progress Made:**
* change the renamed the extract_pdf to get_pdf.
* merged all branches to the main branch and deleted them.
* started a new brach extact_pdf 


### **Challenges Encountered & Solutions:**
* I'm not new to git and Github but using it this extensively fir CI/CD and version control has been a bit of a learning, I have been using command other than commit and status, just saying. 

### **Libraries/Tools Used & Rationale:**
* **git**
* **Github**

### **Next Steps:**
* extract data from pdf files.
* finish PDF scraping script.

### **Lessons Learned:**
* using git / Github and learning CI/CD best practices.
---

## **Week 12 (Oct 14, 2025 )**

### **Goals for the Week:**
* Develop robust web scraping script for PDF content.

### **Progress Made:**
* Work on the extraction of text and other data form pdf files
* Also found out that the metedata gotten from the etract_html script is not complete, need to go back to it
* The extract_html_update only find the update but those not extract the metadata and text.
* Its also the same with the get_pdf script, some relevant data is not being extracted, I need to go back to it.


### **Challenges Encountered & Solutions:**
* Decide which pdf extrator library is best, had to work with a combination of libraries.

### **Libraries/Tools Used & Rationale:**
* **PYMUPDF**
* **PYPDF2**
* **Pathlib**

### **Next Steps:**
* extract data from pdf files.
* finish PDF scraping script.
* go back to get_pdf, extract_html, and extract_html_update to add scrape for missing metadata

### **Lessons Learned:**
* You might sometime missing certian information when scrape date.
* Reviews and second options are important, always clear doubts.
* Ask for help even if it is from AI, a little goes along way.
---
*(Continue adding new weekly entries above this line)*