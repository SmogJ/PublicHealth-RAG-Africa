# RAG App for Public Health in Africa Project Plan

---
## PHASE 0: Problem Framing 
---
0.1 Define key user questions (e.g., malaria treatment guidelines Nigeria) 
0.2 Define success criteria (what is a “good answer”?) 
0.3 Define risks (misinformation, outdated data) 
0.4 Define evaluation dataset (10–20 gold questions manually)

---
## Phase 1: Architecture & System Design
### Sprint 1 (Week of Apr 6): 
---
1.1 System Architecture Diagram 
1.1.2 Data ingestion (WHO, NCDC, PDFs)
1.1.2 Preprocessing pipeline
1.1.3 Vector store
1.1.4 Retriever
1.1.5 Generator
1.1.6 Guardrails
1.1.7 API layer
1.1.8 UI


1.2 Repository Setup 
1.2.1 .gitignore
1.2.2 README.md (VERY IMPORTANT — don’t skip)
1.2.3 Environment setup (.env, config management)


1.3 Folder Structure 


1.4 Retrieval Strategy Design/Spec (CORE of RAG) 
1.4.1 Chunking approach (PDF-aware, table-aware) 
1.4.2 Embedding model choice
1.4.3 Index type (vector vs hybrid?)
1.4.4 Metadata schema


1.5 Prompt + Generation Design/Strategy 
1.5.1 System prompt template per (global rules):
        i. Intent: F, P, C, S
        ii. Risk level (STRICT, CONTROLLED, INFO) 


1.6 Guardrails Design (This is BIG in healthcare) 
1.6.1 Pre-query validation
1.6.2 Retrieval sufficiency check
1.6.3 Post-generation validation


1.7 Failure Mode Orchestration 
1.7.1 Conditions → actions: (ASK_CLARIFICATION , ALLOW_IDK , REFUSE_SAFE , MUST_ANSWER )
    i. Query validation
    ii. Ambiguity detection


1.8 Config System 
1.8.1 models
1.8.2 thresholds
1.8.3 risk rules
1.8.4 retrieval settings

---
## Phase 2: Data Acquisition & Preparation (Ingestion) 
### Sprint 2 (Week of Apr 13):
---
2.0 Data Model Layer: Define canonical Document Schema  
2.2 Refactor the HTML scraper into a modular class structure. 
2.3 Define Specific Scope & Target Users (Done, Initial: Infectious & NCDs)
2.4 Identify & Prioritize Data Sources (URLs for WHO AFRO, Africa CDC, National MoH, Journals)
2.5 Develop Web Scrapers for HTML Content

---
### Sprint 3 (Week of Apr 20):
---
2.6 Refactor the PDF scraper to match the new modular structure. 
2.7  Implement the missing metadata extraction identified in previous work. 
2.8 Implement centralized logging for tracking scraper success/failure. 
2.9 Develop PDF Text Extractors
2.10 Implement Initial Data Cleaning (Remove boilerplate, headers, footers)
2.11 Implement Text Chunking Strategy (Semantic chunking with overlap)
2.12 Store Cleaned & Chunked Data (e.g., in a temporary directory or initial data lake)

---
## Phase 3: RAG Pipeline Development 
### Sprint 4 (Week of Apr 27):
---
3.1 Define the semantic chunking strategy (e.g., 500-token chunks with 50-token overlap). 
3.2 Set up the Vector Database (e.g., ChromaDB or Qdrant) and run the first ingestion. 
3.3 Select & Integrate Embedding Model (e.g., Sentence Transformers)
3.4 Choose & Set Up Vector Database (e.g., ChromaDB for prototyping)
3.5 Ingest Embeddings into Vector Database
3.6 Develop Retrieval Mechanism (Similarity search)
3.7 Implement Initial Prompt Engineering for LLM
3.8 Select & Integrate LLM (e.g., a suitable open-source model or API)
3.9 Retrieval Strategy Design: Define retrieval strategy 

---
## Phase 4: Application Development & Quality Assurance
### Sprint 5 (Week of May 04):
---
4.1 Develop the FastAPI backend to handle retrieval and LLM generation. 
4.2 Implement data safety checks (ensuring the LLM only answers from the provided context). 
4.3 Set up secrets management (using `.env` for all keys/endpoints).  
4.4 Choose & Set Up Web Framework (e.g., Streamlit)
4.5 Design & Implement User Interface (Input, Output, Source Display)
4.6 Integrate RAG Pipeline with UI
4.7 Implement Conversational History (Optional, for enhanced UX)
4.8 Safety Layer: Implement safety guardrails 

---
## Phase 5: Evaluation & Iteration & Safety 
### Sprint 6 (Week of May 10):
---
5.1 Write unit tests for data validation and scraper logic using `pytest`. 
5.2 Configure GitHub Actions for CI/CD (automatically run tests on every push). 
5.3 Define & Implement Evaluation Metrics (Retrieval Accuracy, Generation Quality)
5.4 Conduct Initial Testing & Gather Feedback (Internal Alpha Testing)
5.5 Iterate & Refine Data Cleaning, Chunking, Retrieval, and Prompt Engineering
5.6 Explore Advanced RAG Techniques (Hybrid Search, Re-ranking, etc.)
5.7 Observability Layer: Logs 

---
## Phase 6: Deployment & Security 
### Sprint 7 (Week of May 17):
6.1 Build the Streamlit frontend. 
6.3 Containerize Application (Docker)
6.4 Select Cloud Platform & Services (e.g., GCP, Supabase)
6.3 Implement Data Privacy & Security Measures (Access Control, Encryption)
6.4 Deploy Application
6.5 Set Up Monitoring & Logging
6.6 Plan for Continuous Data Updates & Model Maintenance
6.7 Final end-to-end testing and project retrospective. 
6.8 Schedule scraper (cron job) 
6.9 Incremental updates (only new docs) 
6.10 Re-index embeddings  


<!-- 
**Versioning**

* Version: 2.0
* Status: Active Development Roadmap
* Owner: Jeffrey Esedo (Developer) -->
