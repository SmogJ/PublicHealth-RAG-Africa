# RAG App for Public Health in Africa Project Plan

---
## PHASE 0: Problem Framing 
---
0.1 Define key user questions (e.g., malaria treatment guidelines Nigeria) 
0.2 Define success criteria (what is a “good answer”?) 
0.3 Define risks (misinformation, outdated data) 
0.4 Define evaluation dataset (10–20 gold questions manually)

---
## Phase 1: Data Engineering Layer
    Data Ingestion (WHO, NCDC, PDFs) 

##### *Sprint 1 (Week of Apr 13):*

### 1.1 Define Canonical Document Schema
    Unify:
        * HTML output
        * PDF output 

### 1.2 Refactor HTML scraper
    * Remove fragile selectors
    * Output → unified schema
    * Merge text_s + text_p → content 

### 1.3 Fix PDF extractor (CRITICAL)
    * Switch to pdfplumber
    * Extract: clean text, tables
    * Output → same schema 

### 1.4 Create Processed Data Layer 

### 1.5 Logging system (basic)
    * success / fail
    * file-level logs 

### *** Sprint 2 (Apr 13 → Apr 20) ***
    Preprocessing pipeline 

### 1.6 Data Cleaning Pipeline
    * remove boilerplate
    * normalize whitespace
    * remove headers/footers 

### 1.7 Metadata Enrichment
    * disease tagging
    * country tagging
    * date normalization 

### 1.8 Deduplication
    * same article appearing twice
    * similar PDFs 

### 1.9 Quality Validation Layer
    For each doc:
        * has content?
        * has title?
        * length threshold?
        * valid language? 


## PHASE 2: Retrieval Foundation

#### *Sprint 3 (Apr 20 → Apr 27)*

### 2.1 Chunking Strategy
    *semantic chunks
    *table-aware chunks
    *metadata attached

### 2.2 Embedding Pipeline
    * Sentence Transformers

### 2.3 Vector DB Setup
    * ChromaDB

### 2.4 First Retrieval Tests
    Test queries like:
        *  “malaria dosage child 15kg”
        *  “hypertension treatment Nigeria” 

      

## PHASE 3: Evaluation System

#### *Sprint 4 (Apr 27 → May 4)*

### 3.1 Build Evaluation Engine (based on your table)
    * exact match (numeric)
    * semantic match
    * source validation 

### 3.2 Retrieval Evaluation
    * Did we retrieve correct docs?
    * Top-k accuracy 

### 3.3 Failure Analysis
    * better chunking
    * better metadata
    * better retrieval 

 

## PHASE 4: Generation Layer

#### Sprint 5 (May 4 → May 10)

### 4.1 Prompt Engineering
    * persona-aware
    * risk-aware 

### 4.2 LLM Integration 

### 4.3 Grounded Answer Generation
    * answer ONLY from context
    * citation required 



## PHASE 5: Safety & Guardrails

#### *Sprint 6 (May 10 → May 17)*

### 5.1 Query Classification
    * factual / procedural / critical 

### 5.2 Safety Policies
    * refusal rules
    * uncertainty handling 

### 5.3 Post-generation validation
    * hallucination detection
    * missing citation check



## PHASE 6: Application Layer

### *Sprint 7 (May 17 → May 24)*

### 6.1 FastAPI backend 

### 6.2 UI (Streamlit) 

### 6.3 End-to-end pipeline 



## PHASE 7: Production Readiness
    * CI/CD
    * monitoring
    * scheduled scraping
    * incremental updates 


<!-- 
**Versioning**

* Version: 3.0
* Status: Active Development Roadmap
* Owner: Jeffrey Esedo (Developer) -->
