<p>Let get the basic on the ground and build a proper foundation for the project. By that, I mean what are the right questions to ask to get a general idea of
what I am about to begin, so it directs me through the project and helps me decides on how I should go about it, and probably how long the project will last.

Here are some of the questions I could think of at one siting, keeping my fingers crossed I hope this help me get my foundations right.
</p>

1. _Who might need a Public Health RAG Application?_ 
2. _What specific Problems do they have as relates to a RAG?_ 
3. _Why will they need a RAG?_ 
4. _what risk are there when they use it?_
5. _what the RAG can not solve as related to Public Health?_
6. _what Policies and Regulation exist around using RAG in the Public Health sector?_
7. _Are there international and local security, safety, and privacy laws as regard using RAG or AI in the Public Health sector?_
8. _Are there standards to follow when developing a RAG are there standards and specifications to follow?_


---
# 1. Who might need a Public Health RAG Application?

### Primary users

#### 1. **Healthcare professionals**

* Frontline Healthcare Workers & Clinicians, like, Doctors, nurses, community health workers.

  __*Why:*__

* They need quick access to updated guidelines, treatment protocols, outbreak info for infectious diseases and rising NCDs without manually sifting through hundreds of pages of PDFs.
* WHO notes AI can *augment health workers’ knowledge and skills* ([World Health Organization][1])

---

#### 2. **Public health officials & policymakers**

* Ministries of Health
* Africa CDC teams
* NGOs

  __*Why:*__

* Policy decision support
* Outbreak monitoring
* Program planning
* Tto synthesize historical epidemiological data to draft new outbreak containment strategies.

---

#### 3. **Researchers & students**

* Medical researchers
* Epidemiologists
* Public health students

  __*Why:*__

* Literature search
* Evidence synthesis
* Cross-reference local health reports with international WHO standards

---

#### 4. **General public (with caution)**

* Citizens seeking health information

  __*But:*__

* Must be carefully designed (high risk of misuse)

---

### Insight

In Africa, where there is **shortage of healthcare professionals**, AI tools (like RAG) can help scale knowledge access

---

# 2. What specific problems do they have (that RAG solves)?

### Core problems

#### 1. **Information fragmentation**
Critical public health data is scattered across discrete Ministry of Health websites, WHO portals, and academic journals. Finding the specific, current protocol for managing a cholera outbreak or diabetes care requires significant manual effort.

  __*Problem*__
* Guidelines spread across:

  * WHO
  * Africa CDC
  * National MoH
  * Journals

__*Solution*__

* Centralized retrieval across sources

---

#### 2. **Outdated knowledge**
The sheer volume of newly published clinical evidence and policy updates outpaces human capacity to read and internalize it.

  __*Problem*__
* Medical knowledge changes constantly

__*Solution*__
* RAG solves → retrieves **latest documents**

---

#### 3. **Time pressure**
__*Problem*__
* Clinicians don’t have time to read long documents

__*Solutin*__

* Summarizes + retrieves relevant sections

---

#### 4. **Hallucination in LLMs**
Standard Generative AI models suffer from knowledge cutoffs. In healthcare, relying on a model trained in 2023 to answer questions about a 2026 localized viral outbreak is dangerous.

  __*Problem*__
* Standard LLMs “guess”

__*Solution*__

* Grounds answers in real documents
* Reduces hallucination risk

---

# 3. Why do they need a RAG (not just normal AI)?

### Without RAG:

* __Real-Time Data Grounding:__ As highlighted by Forbes and applied AI use cases, healthcare requires real-time data updates. RAG allows the system to fetch the most recently published health bulletins right before answering.

* __Mitigation of Hallucinations:__ The NEJM and Nature frameworks emphasize that standard LLMs confidently generate plausible but fabricated medical advice. RAG forces the model to synthesize answers only from the retrieved, authoritative context, drastically reducing clinical risk.
  > LLM = trained once → becomes outdated
  > Can hallucinate

* __Source Verifiability:__ RAG natively provides citations. A public health official can immediately click the link to verify the exact paragraph in the WHO guideline the answer was drawn from, establishing the necessary trust for medical decision-making.
  > Cannot cite sources

---

### With RAG:

* Uses **external knowledge base**
* Provides **citations**
* Can be **updated without retraining**
  > Accuracy + traceability = life or death

---

# 4. What risks are there?

#### 1. **Wrong or harmful medical advice**
If the vector database surfaces an outdated malaria treatment guideline instead of the current one, the LLM will provide a perfectly formatted, highly confident, but clinically wrong answer.
  * Misdiagnosis
  * Incorrect treatment
  * Even with RAG: If retrieval fails the model may still hallucinate
  * If the RAG index is stale it may give wrong answers
  > WHO warns AI errors can lead to **serious harm**

---

#### 2. **Bias in data**
If the ingested documents lack data representative of specific local populations, the RAG system's recommendations may inadvertently widen health inequities.
  * Data may not represent African populations
  * inaccurate recommendations
  * inequity ([World Health Organization][1])

---

#### 3. **Privacy & data leakage**
If user queries (which might contain sensitive outbreak locations or patient demographics) are logged or processed insecurely, it poses a major privacy risk.
  * Health data is sensitive
  * exposure of personal health info

---

#### 4. **Over-reliance on AI**
The WHO warns that users may become overly reliant on AI outputs, accepting them without exercising independent clinical judgment.
  * Users trust system blindly
  * WHO warns: overestimating AI may lead to dangerous decisions

---

# 5. What can RAG NOT solve?

### RAG cannot:

#### 1. Replace doctors
A RAG app can summarize hypertension protocols, but it cannot assess a patient's physical state, socio-economic barriers to acquiring medication, or provide the human empathy required in care delivery.
  * It is **decision support**, not decision maker

---

#### 2. Guarantee correctness
If the original Ministry of Health report contains statistical errors or flawed methodologies, the RAG system will simply repeat those errors. It cannot independently verify the scientific validity of the source document or fix data quality.
  * It improves accuracy, but:

    * depends on retrieval quality
    * depends on data quality ("Garbage In, Garbage Out")

---

#### 3. Handle real-time patient diagnosis safely (alone)

* Needs:

  * clinical validation
  * regulatory approval

---

#### 4. Solve systemic health issues
Information access does not solve the physical lack of vaccines, diagnostic equipment, or trained medical personnel in a region.
  * e.g.:

    * lack of hospitals
    * drug shortages

---

# 6. What policies & regulations exist?

### Global Governance Guidance (2021 & 2023)
The WHO outlines six core principles for AI in health:
- protecting human autonomy, promoting human well-being and safety, 
- ensuring transparency and explainability, fostering responsibility and accountability, 
- ensuring inclusiveness and equity, 
- and promoting AI that is responsive and sustainable.

#### WHO AI Guidelines (core reference)
  * Emphasizes:
    * safety
    * transparency
    * data protection
    * human oversight-

---

#### WHO Ethical Principles (2021)
Regulations increasingly demand that any AI system used in clinical decision support must be transparent about its methodology and clearly state that the output is AI-generated, ensuring human oversight remains in the loop.
  * Includes:
    * human autonomy
    * transparency
    * accountability
    * equity
  
  > AI in health must be **regulated across its lifecycle**

---

# 7. Are there international & local laws?

### International
frameworks like the GDPR (Europe) and HIPAA (USA) set the gold standard for handling Protected Health Information (PHI). Even if the RAG app primarily uses public documents, any user interaction data must be secured and stripped of Personally Identifiable Information (PII).
#### 1. **GDPR (EU)**

* Data protection
* Consent
* Right to explanation

#### 2. **HIPAA (USA)**

* Health data privacy

  > WHO explicitly mentions both as relevant frameworks ([World Health Organization][1])

---

### Africa / Local (important for your project)
Systems operating regionally must comply with localized data protection frameworks, such as the Nigeria Data Protection Regulation (NDPR) or South Africa's POPIA, which dictate how health-related data can be processed, stored, and transmitte
  * Nigeria Data Protection Act (NDPA)
  * National Health Data policies
  * Country-specific MoH regulations

---

### Software as a Medical Device (SaMD)
Depending on how prescriptive the RAG app's answers become, local regulatory bodies (like NAFDAC or equivalent medical agencies) may classify the software as a medical device, requiring rigorous clinical safety audits before deployment.

---

# 8. Are there standards / best practices?
__Data Interoperability:__ While your initial build relies on PDFs and HTML, production healthcare systems standardize data using Fast Healthcare Interoperability Resources (FHIR) to ensure different systems can "talk" to each other securely.

__AI Risk Management:__ The National Institute of Standards and Technology provides a framework specifically for mapping, measuring, and managing the risks of AI systems, highly applicable to minimizing medical misinformation.

__ISO/IEC 42001 & 27001:__ These are the international standards for Artificial Intelligence Management Systems and Information Security Management, providing the architectural specifications for deploying secure, enterprise-grade AI applications.

---

## Core standards to follow

### 1. **Evidence-based AI**

* Only use verified sources (WHO, CDC, journals)

---

### 2. **Explainability**

* Show sources (RAG citations)

---

### 3. **Human-in-the-loop**

* AI assists, human decides

---

### 4. **Data quality standards**

* Clean, validated, up-to-date data

---

### 5. **Security standards**

* Encryption
* Access control

---

### 6. **Interoperability standards**

* HL7 / FHIR (for clinical systems) ([Forbes][3])

---

### 7. **Evaluation standards**

* Accuracy
* Faithfulness (answer grounded in context)
* Relevance

---

### 8. **Continuous updates**

* Medical AI must stay current
  ([Forbes][3])

--

### 9. **Risk Management**
* NiST AI RMF

---

## Source:
- [RAG in Healthcare: Real Adoption Use Case](https://appliedai.tools/ai-for-health/rag-in-healthcare-real-adoption-use-case-examples/)
- [RAG in Healthcare: 2026 Complete Guide](https://arkenea.com/blog/rag-in-healthcare/)
- [RAG in Health Care: A Novel Framework for Improving Communication and Decision-Making by Addressing LLM Limitations](https://ai.nejm.org/doi/full/10.1056/AIra2400380)
- [Retrieval-augmented generation for generative artificial intelligence in health care](https://www.nature.com/articles/s44401-024-00004-1)
- [Retrieval-augmented generation in healthcare](https://talbotwest.com/services/retrieval-augmented-generation/rag-in-healthcare)
- [WHO outlines considerations for regulation of artificial intelligence for health](https://www.who.int/news/item/19-10-2023-who-outlines-considerations-for-regulation-of-artificial-intelligence-for-health?utm_source=chatgpt.com)
- [AI risks in global health ‘must be accounted for’ – WHO](https://www.gavi.org/vaccineswork/ai-risks-global-health-must-be-accounted-who?utm_source=chatgpt.com)
- [ "Why AI In Healthcare Requires Real-Time Data Updates"](https://www.forbes.com/councils/forbestechcouncil/2025/07/31/why-ai-in-healthcare-requires-real-time-data-updates/?utm_source=chatgpt.com)
- [Retrieval-augmented generation (RAG) in healthcare: the benefits, the evidence, and how to do it safely | iatroX Clinical AI Insights](https://www.iatrox.com/blog/rag-in-healthcare-benefits-evidence-safe-deployment-guide?utm_source=chatgpt.com)
- [WHO Releases Governance Guidelines for Generative Artificial Intelligence | TechTarget](https://www.techtarget.com/healthtechanalytics/news/366589843/WHO-Releases-Governance-Guidelines-for-Generative-Artificial-Intelligence?utm_source=chatgpt.com)
- [Ethics and governance of artificial intelligence for health: WHO guidance - WHO | Regulations.AI - The Site on AI Laws and Regulations | Regulations.ai](https://regulations.ai/regulations/who-ai-health-guidance-2021?utm_source=chatgpt.com) 
- [Harnessing artificial intelligence for health](https://www.who.int/teams/digital-health-and-innovation/harnessing-artificial-intelligence-for-health?utm_source=chatgpt.com) 
