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
* Also found out that the metedata gotten from the extract_html script is not complete, need to go back to it
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

## **Week 15 (Nov 18, 2025 )**

### **Goals for the Week:**
* Develop robust web scraping script for PDF content.

### **Progress Made:**
* Include code for the creation of a new directory and json file for metadata and text
* Written a function that gets the PDF file.
* Written function that scrapes text and metadata from pdf.


### **Challenges Encountered & Solutions:**
* Decide which pdf extrator library is best, had to work with a combination of libraries.

### **Libraries/Tools Used & Rationale:**
* **PYPDF2**
* **Pathlib**

### **Next Steps:**
### **Lessons Learned:**

---




## I'm Back
I have been away from this project for a couple of week now, because I got involve in another project, a Hackathon called Design Thinking Challenge. And Honestly I learnt alot and I want to bring what I learn during the hackathon into this project. So, I will be going back to the start. What will I be doing from the start, well here is what it looks like:
<p>
<h1>RAG App for Public Health in Africa Project Plan</h1>
<h2>PHASE 0: Problem Framing</h2> 
<ol>0.1 Define key user questions (e.g., malaria treatment guidelines Nigeria) </ol>
<ol>0.2 Define success criteria (what is a “good answer”?) </ol>
<ol>0.3 Define risks (misinformation, outdated data) </ol>
<ol>0.4 Define evaluation dataset (10–20 gold questions manually) </ol>


<h2>Phase 1: Architecture & System Design</h2>
<h5><i>Sprint 1 (Week of Mar 30):</i></h5> 
<ol>1.1 Design the system architecture diagram (Data flow from WHO/Africa CDC to UI).</ol> 
<ol>1.2 Set up a professional `.gitignore` and initialize the environment.</ol> 
<ol>1.3 Refactor the project folder structure (`/src`, `/tests`, `/data`, `/config`).</ol>


<h2>Phase 2: Data Acquisition & Preparation (Ingestion)</2>
<h5><i>Sprint 2 (Week of Apr 06):</i><h5>
<ol>2.0 Data Model Layer: Define canonical Document Schema</ol>  
<ol>2.2 Refactor the HTML scraper into a modular class structure.</ol> 
<ol>2.3 Define Specific Scope & Target Users (Done, Initial: Infectious & NCDs)</ol>
<ol>2.4 Identify & Prioritize Data Sources (URLs for WHO AFRO, Africa CDC, National MoH, Journals)</ol>
<ol>2.5 Develop Web Scrapers for HTML Content</ol>
<h5><i>Sprint 3 (Week of Apr 13):</i></h5>
<ol>2.6 Refactor the PDF scraper to match the new modular structure.</ol> 
<ol>2.7  Implement the missing metadata extraction identified in previous work.</ol> 
<ol>2.8 Implement centralized logging for tracking scraper success/failure.</ol> 
<ol>2.9 Develop PDF Text Extractors</ol>
<ol>2.10 Implement Initial Data Cleaning (Remove boilerplate, headers, footers)</ol>
<ol>2.11 Implement Text Chunking Strategy (Semantic chunking with overlap)</ol>
<ol>2.12 Store Cleaned & Chunked Data (e.g., in a temporary directory or initial data lake)</ol>


<h2>Phase 3: RAG Pipeline Development</h2>
<h5><i>Sprint 4 (Week of Apr 20):</i></h5>
<ol>3.1 Define the semantic chunking strategy (e.g., 500-token chunks with 50-token overlap).</ol> 
<ol>3.2 Set up the Vector Database (e.g., ChromaDB or Qdrant) and run the first ingestion.</ol> 
<ol>3.3 Select & Integrate Embedding Model (e.g., Sentence Transformers)</ol>
<ol>3.4 Choose & Set Up Vector Database (e.g., ChromaDB for prototyping)</ol>
<ol>3.5 Ingest Embeddings into Vector Database</ol>
<ol>3.6 Develop Retrieval Mechanism (Similarity search)</ol>
<ol>3.7 Implement Initial Prompt Engineering for LLM</ol>
<ol>3.8 Select & Integrate LLM (e.g., a suitable open-source model or API)</ol>
<ol>3.9 Retrieval Strategy Design: Define retrieval strategy</ol> 


<h2>Phase 4: Application Development & Quality Assurance</h2>
<h5><i>Sprint 5 (Week of Apr 27):</i></h5>
<ol>4.1 Develop the FastAPI backend to handle retrieval and LLM generation.</ol> 
<ol>4.2 Implement data safety checks (ensuring the LLM only answers from the provided context).</ol> 
<ol>4.3 Set up secrets management (using `.env` for all keys/endpoints).</ol>  
<ol>4.4 Choose & Set Up Web Framework (e.g., Streamlit)</ol>
<ol>4.5 Design & Implement User Interface (Input, Output, Source Display)</ol>
<ol>4.6 Integrate RAG Pipeline with UI</ol>
<ol>4.7 Implement Conversational History (Optional, for enhanced UX)</ol>
<ol>4.8 Safety Layer: Implement safety guardrails</ol> 


<h2>Phase 5: Evaluation & Iteration & Safety</hs>
<h5><i>Sprint 6 (Week of May 04):</i></h5>
<ol>5.1 Write unit tests for data validation and scraper logic using `pytest`.</ol> 
<ol>5.2 Configure GitHub Actions for CI/CD (automatically run tests on every push).</ol> 
<ol>5.3 Define & Implement Evaluation Metrics (Retrieval Accuracy, Generation Quality)</ol>
<ol>5.4 Conduct Initial Testing & Gather Feedback (Internal Alpha Testing)</ol>
<ol>5.5 Iterate & Refine Data Cleaning, Chunking, Retrieval, and Prompt Engineering</ol>
<ol>5.6 Explore Advanced RAG Techniques (Hybrid Search, Re-ranking, etc.)</ol>
<ol>5.7 Observability Layer: Logs</ol> 


<h2>Phase 6: Deployment & Security</h2>
<h5><i>Sprint 7 (Week of May 11):</i></h5>
<ol>6.1 Build the Streamlit frontend.</ol> 
<ol>6.3 Containerize Application (Docker)</ol>
<ol>6.4 Select Cloud Platform & Services (e.g., GCP, Supabase)</ol>
<ol>6.3 Implement Data Privacy & Security Measures (Access Control, Encryption)</ol>
<ol>6.4 Deploy Application</ol>
<ol>6.5 Set Up Monitoring & Logging</ol>
<ol>6.6 Plan for Continuous Data Updates & Model Maintenance</ol>
<ol>6.7 Final end-to-end testing and project retrospective.</ol> 
<ol>6.8 Schedule scraper (cron job)</ol> 
<ol>6.9 Incremental updates (only new docs)</ol> 
<ol>6.10 Re-index embeddings</ol> 
</p>


