# PROBLEM FRAMING

## 0.1 Key User Questions

These questions are meant to help understand the users and their needs for the RAG APP, how they might user it, and potentially find other edge use case for the solution for the users and other user other than the ones targeted persona. 

The questions will help me under what the RAG app is expected to answer. Furthermore, it help set a boundary on how I would develop the RAG app, setting a limit to what it can and cannot do, the tyoe of data to get and where to get this data. 

The question that comes to mind is "where and how will I get my questions?", "are there exiting guidelines or methodes to do this?". During my research with the help of Gemini AI, I found out that I could *reverse-engineer* existing information architecture of global health organizations. Using sources like the *WHO FACT SHEET* to get these questions by using the sub-headers as questions, for instance one of the sub-heading of the Anaemia fact sheet is signs and symptoms of the condions, when engineered into a question this becomes, **what is Anaemia?** or **What are the Signs and Symptoms of Anaemia?**, a question a doctor, Researcher, or genreal user might ask.

Getting questions are great, but why will a healthcare worker - Researcher - Student - Publice Health Policy Maker want to ask these questions in the first place and just as important, how those RAG model (LLM) know this intent and hold them. That bring up a need to categorize this questions by the reasons they want to ask them, that is, the **INTENT** of the question, not just why are they asking the question, but what dose asking and answering the question help them solve, also, how those the model know how to deal with question. So there is need to *categorize the questions by intent*. 

What is a good guide in creating these categories so that it captures the questions in the right intent for the _RAG model_. Following industry standards the process of categorizing the questions will be done by System Complexity—specifically, how difficult the questions makes the retrieval and reasoning process for the AI, and this is done by **evaluating LLM architectures is a Multi-Dimensional Taxonomy**. And this is done by evaluate every question across three main axes:

### **Cognitive Intent** (What is the user asking the AI to do?)
- **Fact-Seeking:** "What is the dosage of Artemether-lumefantrine for a 15kg child?" (Requires precise, verbatim extraction).

- **Procedural:** "What are the steps to isolate a suspected Lassa Fever patient?" (Requires ordered lists and logical flow).

- **Comparison:** "How does the Africa CDC's approach to Mpox differ from the WHO's global guidelines?" (Requires the AI to hold two different concepts in its context window simultaneously).

### **Retrieval Complexity*** (How hard is it to find the data?)
- **Single-Hop:** The answer lives neatly in a single paragraph of one specific PDF. (Easiest for RAG).

- **Multi-Hop:** The AI must find Document A (to define a term) and link it to Document B (to get the statistic). For example: "Based on the defined high-risk zones, what is the vaccination rate in those specific areas?"

- **Structured/Table Extraction:** The answer is buried inside a complex data table within a PDF (e.g., finding the Case Fatality Rate for a specific state in an epidemiological report). This is historically the hardest task for text-based RAG systems.

### **Temporal Sensitivity** (Does time matter?)
- **Static:** "What is the biological vector for Malaria?" (The answer hasn't changed in decades).

- **Dynamic/Real-Time:** "What is the current primary variant of COVID-19 circulating in West Africa?" (If the AI pulls a document from 2023, the answer is dangerously wrong)

### Question Caategories
Breakingdown the system into caategories and what they are meant to answer:

- [F] Fact-Seeking: Simple data extraction (Single-hop).

- [P] Procedural: Step-by-step instructions.

- [C] Comparison: Comparing two regions, dates, or guidelines.

- [T] Table/Stats: Extracting numbers from complex PDF layouts.

- [S] Temporal: Questions where only the most recent data matters.*


### Healthcare Professional

| No. | Questions | Goal/Target | Category |
| --- | --------- | ----------- | -------- |
| 1.  | What is the WHO recommendation for the RTS,S and R21 malaria vaccines? | Policy Compliance |  F   |
| 2.  | How do the RTS,S and R21 malaria vaccines compare? | Comparative Logic |  C   |
| 3.  | How is TB diagnosed? | Procedural Accuracy |  P   |
| 4.  | How is TB treated? | Drug Regimens |  P   |
| 5.  | What are cardiovascular diseases? | Definition/Broad |  F   |
| 6.  | What is the dosage of Artemether-lumefantrine for a 15kg child? | Dosage Accuracy |  F   |
| 7.  | What are common symptoms of cardiovascular diseases? | Symptom Recognition |  F   |
| 8.  | The CCHF virus in animals and ticks? | Zoonotic Knowledge |  F   |
| 9.  | How is Crimean Congo Haemorrhagic Fever (CCHF) diagnosed? | Diagnostic Flow |  P   |
| 10. | What is the causative agent for the Marburg virus? | Pathogen ID |  F   |
| 11. | Are there any treatments for the Marburg virus? | Clinical Research |  F   |
| 12. | What are the guidelines for Meningitis surveillance by the NCDC? | Surveillance Rules |  P   |
| 13. | What diseases are currently under surveillance in Nigeria? | Scope Awareness |  S   |
| 14. | Dosage of Ceftriaxone for an infant? | High-Risk Dosage |  F   |
| 15. | Clinical Overview of Fungal Meningitis | Summary Logic |  P   |
| 16. | What is the first-line treatment for uncomplicated malaria in a 10kg child in Nigeria? | Localized Guideline |  F   |
| 17. | What are the steps for clinical management of a patient with suspected Lassa Fever? | Protocol Sequence |  P   |
| 18. | List the diagnostic criteria for Stage 1 Hypertension in adults according to WHO 2024. | Threshold Logic |  F   |
| 19. | What is the criteria for referral of a severe malaria case in a primary health center? | Triage Logic |  P   |
| 20. | What are the contraindications for the R21 malaria vaccine in children? | Patient Safety |  F   |


### Public Health officials & Policymakers

| No. | Questions |	Goal/Target	| Category |
| --- | --------- | ----------- | -------- |
| 1.  | What was the MVIP and how did it help to bring malaria vaccines forward? | Literature Review |  F   |
| 2.  | What is TB?	| Core Concepts	|  F   |
| 3.  |	Who is affected by Heart Disease in sub-Saharan Africa? | Demographic Study |  F   |
| 4.  | What are cardiovascular diseases?	| Broad Definition	|  F   |
| 5.  |	Difference between Sickle Cell Disease (SCD) and Anaemia? |	Biological Nuance |	 C   |
| 6.  | Which region of Africa has the highest Meningitis between 2023 and 2025?	| Trend Analysis	|  T   |
| 7.  | Summarize the evidence supporting RAG adoption in low-resource health settings. | Meta-Analysis |  P   |
| 8.  | What is the projected trend of Diabetes prevalence in West Africa through 2030?	| Forecasting	|  T   |
| 9.  |	Find 3 studies cited in the Nature 2024 RAG review regarding hallucination rates. |	Citation Depth |  F   |
| 10. | What is the efficacy of the R21 vaccine in the 12-month follow-up clinical trials?	| Data Precision	|  F   |
| 11. | How does the P. falciparum parasite distribution vary across Nigeria’s ecological zones? | Eco-Epidemiology	|  C   | 
| 12. | Explain the role of Matrix-M adjuvant in the R21 malaria vaccine.	| Bio-Mechanism	|  F   |
| 13. | What are the primary genomic variants of Mpox identified during the 2024-2025 outbreak?	| Genomic Tracking	|  S   |
| 14. | Compare the Case Fatality Rate of Marburg vs. Ebola based on recent WHO fact sheets. | Comparative Risk |  C   |
| 15. | What does the NEJM AI 2024 framework say about "Clinical Grounding" in RAG systems?	| AI Methodology	|  F   |
| 16. |	Identify the secondary palm-bush vegetation impact on Anopheles breeding in West Africa. | Environmental |  F   |
| 17. | What is the sensitivity and specificity of RDTs for Malaria in high-transmission areas?	| Metric Analysis	|  T   |
| 18. |	Analyze the relationship between financial barriers and delayed patient presentation for TB. | Social Determinant |  C   |
| 19. |	What are the current gaps in surveillance for fungal meningitis according to NCDC?	| Gap Analysis |  S   |
| 20. |	List the key pillars of the 'Africa's Health Security and Sovereignty' (AHSS) framework. |	Systemic Theory |  F   |

### Researchers & students

| No. | Questions | Goal/Target | Category |
| --- | --------- | ----------- | -------- |
| 1.  | What was the MVIP and how did it help to bring malaria vaccines forward? | Literature Review |  F   |
| 2.  | What is TB? | Core Concepts |  F   |
| 3.  | Who is affected by Heart Disease in sub-Saharan Africa? | Demographic Study |  F   |
| 4.  | What are cardiovascular diseases? | Broad Definition |  F   |
| 5.  | Difference between Sickle Cell Disease (SCD) and Anaemia? | Biological Nuance |  C   |
| 6.  | Which region of Africa has the highest Meningitis between 2023 and 2025? | Trend Analysis |  T   |
| 7.  | Summarize the evidence supporting RAG adoption in low-resource health settings. | Meta-Analysis |  P   |
| 8.  | What is the projected trend of Diabetes prevalence in West Africa through 2030? | Forecasting |  T   |
| 9.  | Find 3 studies cited in the Nature 2024 RAG review regarding hallucination rates. | Citation Depth |  F   |
| 10. | What is the efficacy of the R21 vaccine in the 12-month follow-up clinical trials? | Data Precision |  F   |
| 11. | How does the P. falciparum parasite distribution vary across Nigeria’s ecological zones? | Eco-Epidemiology |  C   |
| 12. | Explain the role of Matrix-M adjuvant in the R21 malaria vaccine. | Bio-Mechanism |  F   |
| 13. | What are the primary genomic variants of Mpox identified during the 2024-2025 outbreak? | Genomic Tracking |  S   |
| 14. | Compare the Case Fatality Rate of Marburg vs. Ebola based on recent WHO fact sheets. | Comparative Risk |  C   |
| 15. | What does the NEJM AI 2024 framework say about ""Clinical Grounding"" in RAG systems? | AI Methodology |  F   |
| 16. | Identify the secondary palm-bush vegetation impact on Anopheles breeding in West Africa. | Environmental |  F   |
| 17. | What is the sensitivity and specificity of RDTs for Malaria in high-transmission areas? | Metric Analysis |  T   |
| 18. | Analyze the relationship between financial barriers and delayed patient presentation for TB. | Social Determinant |  C   |
| 19. | What are the current gaps in surveillance for fungal meningitis according to NCDC? | Gap Analysis |  S   |
| 20. | List the key pillars of the 'Africa's Health Security and Sovereignty' (AHSS) framework. | Systemic Theory |  F   |

### General Public

| No. | Questions | Goal/Target | Category |
| --- | --------- | ----------- | -------- |
| 1.  | What is the malaria situation and who is most at risk? | Risk Awareness |   F   |
| 2.  | How were the new malaria vaccines tested to make sure they are safe? | Trust/Safety |   F   |
| 3.  | What is TB? | Basic Info |   F   |
| 4.  | How does TB infection differ from TB disease? | Concept Clarity |   C   |
| 5.  | What are cardiovascular diseases? | General Health |   F   |
| 6.  | Are there differences between Sickle Cell Disease and Thalassaemias? | Clarification |   C   |
| 7.  | How can I prevent my family from getting Cholera during the rainy season? | Prevention |   P   |
| 8.  | Where should I go if I think I have symptoms of a viral hemorrhagic fever in Abuja? | Geolocation |   F   |
| 9.  | Is the new malaria vaccine recommended for all children in Nigeria? | Local Policy |   S   |
| 10. | Can I get TB from someone who is just a 'carrier' but not sick? | Myth-busting |   F   |
| 11. | What should I do if a child under 5 starts showing signs of a high fever and vomiting? | Emergency Action |   P   |
| 12. | How much does the malaria vaccine cost for a family in a public clinic? | Cost/Access |   F   |
| 13. | Are there simple ways to check if my blood pressure is too high at home? | Self-Care |   P   |
| 14. | Does the malaria vaccine replace the need for bed nets? | Safety Behavior |   F   |
| 15. | How do I know if the water in my area is safe from Cholera? | Environmental |   F   |
| 16. | What are the signs of Sickle Cell crisis in a toddler? | Early Warning |   F   |
| 17. | Is it safe to travel to areas where Lassa Fever has been reported? | Risk Assessment |   S   |
| 18. | What is the difference between a cold and Meningitis symptoms? | Symptom Check |   C   |
| 19. | Can adults get the new malaria vaccines too? | Eligibility |   S   |
| 20. | How long does TB treatment usually take to complete? | Treatment Path |   F   |

## 0.2 Define success criteria (what is a “good answer”?)

### Expected Answer Type
This is the Ground Truth, the expected Answer Expectation of the RAG LLM.
- DEFINITION
- PROCEDURAL
- NUMERIC
- COMPARISON
- TABLE
- SUMMARY
- CITATION

### Trusted Source Requirement
it is important to keep track of the source of the questions and their answers and the **Source Sensitivity**. As not all answers should come from the same sources 
Source:
- WHO_ONLY
- WHO_NCDC
- NCDC_ONLY
- PEER_REVIEWED
- ANY_VERIFIED

### Freshness Requirement
Recency of a source is important, knowing when a information was published and if there are is important in evalutating the way the LLM deals with how it gets it them.
- STATIC
- RECENT (last 1–3 years)
- REAL-TIME (if possible)

### Query Complexity:
This helps you design retrieval later.
- SINGLE_HOP
- MULTI_HOP


## 0.3 Define risks (misinformation, outdated data)

### Question Risk Level
Another classification is the Risk Classification per Question. AI systems must consider risk-based deployment (WHO AI regulation guidance).
- LOW
- MEDIUM
- HIGH
- CRITICAL

### Safety Mode
Some questions are high-risk for misuse, so it is best to categorize them as such for evalutation, and AI systems should not replace professional medical advice, as per the WHO guide.
Safety Mode:
- STRICT
- CONTROLLED
- INFORMATIONAL

### Failure Behavior/Mode:
What happens if RAG fails? Does not understandard the question?, or Does not know where to retrieve the information?. There is need to define failure behaviour or a fallback.
- ALLOW_IDK
- ASK_CLARIFICATION
- MUST_ANSWER

### Grounding
There is need to know where the information is being retrived from, therefore there is need for strict citation grounding.
- MUST_CITE
- OPTIONAL_CITE

### Go
## 0.4 Define evaluation dataset (10–20 gold questions manually)
The evaluation dataset or **Gold Set** is an important dataset for making sure any RAG, chatbot, copilot etc. meet risk guidlines and production quality. The dataset is meant to be the standard and source of truth for the RAG or AI is to meet throughout it lifecycle, as it is build from and maintained using guidelines for AI safety and best practice, so as the it can be used for repeated evaluation of the AI, used to track and dubug failures. 

Furthermore, the Gold set is used for decision-making, engineering of the AI (decision-making for prompt engineering, model router selection, cost-latency-quality tradeoffs), and used to align governance of AI including tracing and audit. 

For evaluting 

| Question                                         | Persona   | Cat | Risk     | Type       | Source       | Freshness | Safety        | Grounding | Gold Answer | Complexity | Failure_Mode |
| ------------------------------------------------ | --------- | --- | -------- | ---------- | ------------ | --------- | ------------- | --------- | ------- | --------| --------| 
| Dosage of Artemether-lumefantrine for 15kg child | Clinician | F   | CRITICAL | NUMERIC    | WHO_ONLY     | RECENT    | STRICT        |  MUST_CITE | Combined tablet: child 5–<15 kg: 1 tablet two times a day for 3 days; child 15–24 kg: 2 tablets two times a day for 3 days | SINGLE_HOP | MUST_ANSWER |
| What is TB?                                      | Public    | F   | LOW      | SUMMARY | ANY VERIFIED | STATIC    | INFORMATIONAL | OPTIONAL_CITE | Tuberculosis (TB) is caused by bacteria (Mycobacterium tuberculosis) that most often affect the lungs. About one-quarter of the world's population has been infected with TB bacteria. In general, people with TB infection don’t feel sick and are not contagious. | MULTI_HOP | MUST_ANSWER |
| Diseases under surveillance in Nigeria           | Policy    | S   | HIGH     | SUMMARY   | WHO_NDDC     | RECENT    | CONTROLLED    | MUST_CITE  | Lassa fever, Cholera, Meningitis, Yellow Fever, Measles, Mpox (IDSR priority list) | MULTI_HOP | MUST_ANWSER |
| Compare the Case Fatality Rate of Marburg vs. Ebola based on recent WHO fact sheets. | Researcher | C   | MEDIUM | NUMERIC    | PEER-REVIEWED | STATIC  | INFO_ONLY | MUST_CITE | Marburg Case fatality rates have varied from 24% to 88% in past outbreaks, Ebola Case fatality rates have varied from 25–90% in past outbreaks (WHO 2025). | MULTI_HOP | MUST_ANSWER |
| Steps to notify NCDC of a Meningitis case?       | Policy    | P   | HIGH     | PROCEDURAL | NCDC_ONLY         | RECENT    | CONTROLLED    | MUST_CITE | **STEP 1:** Identify suspected case **STEP 2.** Recognize meningitis symptoms such as fever, neck stiffness, headache, and altered consciousness in a patient. **STEP 3.** Fill case investigation formDocument patient details, clinical signs, and preliminary diagnosis using the official NCDC case investigation form. **STEP 4.** Collect and send samplesObtain cerebrospinal fluid (CSF) or blood samples and send them to the nearest reference laboratory for confirmation. **STEP 5.** Notify local health authorityImmediately inform the Local Government Area Disease Surveillance and Notification Officer (DSNO) about the case. **STEP 6.** Escalate to state and NCDCThe DSNO reports to the State Epidemiologist, who then alerts the NCDC through the national surveillance system. **STEP 7.** Provide follow-up updatesContinue to update NCDC on patient status, lab results, and any additional suspected cases to aid outbreak monitoring (NCDC 2017). | MULTI_HOP | ASK_CLARIFICATION |
| CFR for Cholera in Lagos (Sept 2025)?            | Researcher| T   | MEDIUM   | TABLE      | NCDC_ONLY | REAL-TIME | INFORMATIONAL     | MUST_CITE | As of 14 September 2025, a total of 10,353 suspected cases of cholera, including 244 deaths (case fatality rate (CRF): 2.4 per cent), have been reported across 37 states. Lagos reported 176 caes (UNICEf/NCDC 2017) | SINGLE_HOP | MUST_ANWSER |
| How to prevent Cholera at home?                  | Public    | P   | LOW      | SUMMARY   | Any Verified | STATIC    | INFORMATIONAL     | OPTIONAL_CITE | Boil/chlorinate water, wash hands with soap, cook food thoroughly, use latrines. |  SINGLE_HOP | MUST_ANSWER |
| Is the new malaria vaccine recommended for all children in Nigeria? | Public | S | HIGH | DEFINITION | ANY_VERIFIED | RECENT | CONTROLLED | MUST-CITE | Yes, NCDC/WHO recommend R21/RTS,S for children 5-36 months in moderate-to-high transmission areas. | SINGLE_HOP | ASK CLARIFICATION |
| What should I do if a child under 5 starts showing signs of a high fever and vomiting? | Public | P | CRITICAL | PROCEDURAL | ANY_VERIFIED | STATIC | STRICT | MUST_CITE | check for immediate danger signs: a high temperature, but cold feet and hands, a high temperature that does not come down with paracetamol or ibuprofen (do not give paracetamol to a baby under 2 months and do not give ibuprofen to a baby under 3 months or under 5kg, unless prescribed by a doctor), a very high or low temperature, your child feels hot or cold to touch, or is shivering, your child is quiet and listless, even when their temperature is not high, a high temperature in a baby less than 2 months old;  rapid breathing or panting, a throaty noise while breathing, your child is finding it hard to get their breath and is sucking their stomach in under their ribs; blue, pale, blotchy, or ashen (grey) skin – on brown or black skin, this may be easier to see on the palms of the hands or soles of the feet, your child is hard to wake up, or appears disoriented or confused, your child is crying constantly and you cannot console or distract them, or the cry does not sound like their normal cry, green vomit, your child is not feeding normally and you're worried, nappies that are drier than usual – this is a sign of dehydration; check for dehydration. Seek medical care at nearest health facility immediately;| MULTI_HOP | MUST_ANSWER |
| Which region of Africa has the highest Meningitis between 2023 and 2025? | Researcher | T | MEDIUM | NUMERIC | WHO_ONLY | RECENT | Informational | MUST_CITE | African Meningitis Belt (Sahel region), specifically Nigeria, Niger, and Ethiopia. | SINGLE_HOP | MUST_ANSWER |
| Summarize the evidence supporting RAG adoption in low-resource health settings. | Researcher | P | LOW | CITATION | PEER-REVIEWED | RECENT | INFORMATIONAL | MUST_CITE | The evidence supporting the adoption of RAG in low-resource health settings is robust, with studies demonstrating its effectiveness in enhancing the accuracy and reliability of AI-driven healthcare insights. RAG addresses the limitations of traditional LLMs by integrating document retrieval into the generation process, ensuring that responses are contextually accurate and aligned with the latest clinical evidence. This approach is particularly valuable for medical question answering, diagnostics, and treatment planning, where high precision and accountability are critical. RAG models have been shown to significantly improve the relevance and reliability of AI-driven insights by combining the generative capabilities of LLMs with retrieval-based methods. This dual process of retrieving and generating ensures that responses are both contextually accurate and aligned with the latest clinical evidence, making RAG models especially valuable in healthcare settings. The adoption of RAG in low-resource settings is supported by its ability to ground AI responses in robust, causally-relevant evidence rather than mere correlations. This approach reduces the risk of overconfidence and overestimation, which can be particularly dangerous in clinical contexts where errors can have life-altering consequences. Overall, RAG is a transformative tool for advancing AI-supported healthcare outcomes, providing a foundation for more grounded and reliable AI systems.| MULTI_HOP | MUST_ANSWER |
| How does the P. falciparum parasite distribution vary across Nigeria’s ecological zones? | Researcher | C | MEDIUM | SUMMARY | PEER-REVIEWED | STATIC |INFORMATIONAL | MUST_CITE | The distribution of the P. falciparum parasite across Nigeria's ecological zones varies significantly due to factors such as climate, healthcare access, and socioeconomic conditions. In the Northern regions, such as Kano, Kaduna, and Borno, the prevalence of malaria is higher due to lower healthcare access, higher poverty rates, and climatic conditions that favor the breeding of Anopheles mosquitoes, the primary malaria vectors. In contrast, Southern Nigeria, with states like Lagos, Rivers, and Delta, reports relatively lower malaria prevalence, attributed to better healthcare systems, higher socioeconomic status, and more effective public health interventions. Lagos, for instance, has one of the lowest prevalence rates in the country, averaging 10% from 2018 to 2023. Urbanization and better access to healthcare services have significantly contributed to this lower rate. | MULTI_HOP | ASK_CLARIFICATION |
| What is the sensitivity and specificity of RDTs for Malaria in high-transmission areas? | Researcher | T | MEDIUM | NUMERIC | WHO_ONLY | RECENT |INFORMATIONAL | MUST_CITE | The sensitivity and specificity of RDTs for malaria in high-transmission areas are crucial for accurate diagnosis and effective malaria control. The pooled sensitivity of RDTs was 69.7%, with a specificity of 81.5%. These values indicate that RDTs are reliable diagnostic tools, but they may not always detect all malaria infections, especially in areas with high parasite densities. | MULTI_HOP | ASK_CLARIFICATION|
| "How do the RTS,S and R21 malaria vaccines compare?" | Clinician | C | MEDIUM | TABLE | ANY_VERIFIED | RECENT | INFORMATIONAL | MUST_CITE | RTS,S (Mosquirix) and R21 (Matrix‑M) are both WHO‑recommended malaria vaccines for children in endemic regions, but R21 has shown higher efficacy in trials and is easier to produce at scale, while RTS,S has longer safety data from years of use. | MULTI_HOP | ASK_CLARIFICATION |
| How is Crimean Congo Haemorrhagic Fever (CCHF) diagnosed? | Clinician | P | HIGH | SUMMARY | WHO_ONLY | RECENT | CONTROLLED | MUST_CITE | CCHF virus infection can be diagnosed by several different laboratory tests: **1.**enzyme-linked immunosorbent assay (ELISA) ; **2.**antigen detection; serum neutralization; **3.**reverse transcriptase polymerase chain reaction (RT-PCR) assay; **4.** and virus isolation by cell culture. | SINLGE_HOP | MUST_ANSWER |
| What are the guidelines for Meningitis surveillance by the NCDC? | Clinician | P | HIGH | PROCEDURAL | WHO_NCDC | RECENT | STRICT | MUST_CITE | **01.** Detect suspected casesUse standard case definitions such as fever, headache, neck stiffness, or altered consciousness. **02.** Notify local DSNOReport suspected cases immediately to the Local Government Disease Surveillance and Notification Officer. **03.** Escalate to state and NCDC DSNO informs the State Epidemiologist, who escalates the case to NCDC for national monitoring. **04.** Collect CSF samplesObtain cerebrospinal fluid for laboratory confirmation of the causative organism. **05.** Submit weekly IDSR reportsInclude meningitis cases in weekly surveillance reports, even if zero cases are detected. **06.** Apply outbreak thresholdsInvestigate when alert thresholds are crossed, such as 3–5 suspected cases per 100,000 in a week. **07.** Activate rapid responseDeploy teams for case management, vaccination campaigns, and community sensitization. | MULTI_HOP | MUST_ANSWER |
| Dosage of Ceftriaxone for an infant? | Clinician | F | CRITICAL | NUMERIC | WHO_NDDC | RECENT | STRICT | MUST_CITE | During outbreak in children aged 0-2 months: Ceftriaxone 100mg/kg/day, IM or IV, once a day for 7 days; Oustide outbreak the same regimen above but for a duration of 7-10 days. | SINGLE_HOP | MUST_ANSWER |
| What is the criteria for referral of a severe malaria case in a primary health center? | Clinician | P | CRITICAL | PROCEDURAL | WHO_NCDC | RECENT | STRICT | MUST_CITE | From the NCDC/WHO malaria case management guidelines, the criteria for referral of a severe malaria case from a Primary Health Center (PHC) are centered on recognizing danger signs and ensuring timely escalation to higher-level facilities: **1. Clinical Criteria for Referral: ** Any patient with signs of severe malaria (e.g., impaired consciousness, repeated convulsions, severe anemia, respiratory distress, jaundice, shock, or bleeding). Inability to take oral medication due to persistent vomiting or altered mental status. Presence of **complications** such as hypoglycemia, renal failure, or pulmonary edema.  **2. Operational Criteria for Referral: ** When the PHC lacks capacity for **parenteral treatment** (IV/IM artesunate or quinine). Absence of facilities for **blood transfusion** or advanced supportive care.  If laboratory confirmation or monitoring cannot be performed locally.  **3. Referral Protocol: ** Administer a **pre-referral dose of rectal artesunate** (if available) or parenteral antimalarial before transfer. Stabilize the patient (airway, breathing, circulation) and manage hypoglycemia. Provide clear documentation and communicate with the referral facility. Ensure safe transport, ideally accompanied by a health worker. | MULTI_HOP | MUST_ANSWER |


## Source:
- #####  [15 Types of Questions (With Definitions and Examples](https://www.indeed.com/career-advice/career-development/types-of-questions)
- #####  [How do you categorize questions for effective communication?](https://www.linkedin.com/advice/3/how-do-you-categorize-questions-effective-communication-tnorf)
- #####  [MultiHop-RAG: Benchmarking Retrieval-Augmented Generation for Multi-Hop Queries](https://arxiv.org/abs/2401.15391)
- #####  [GRADE:Generating multi-hop QA and fine-gRAined Difficulty matrix for RAGEvaluation](https://arxiv.org/pdf/2508.16994)
- #####  [HotpotQA: A Dataset for Diverse, Explainable Multi-hop Question Answering](https://arxiv.org/abs/1809.09600)
- #####  [A guide to generative AI: from how it works to best practices in model training](https://www.lxt.ai/generative-ai-guide/)
- #####  [The RAG Triad](https://www.trulens.org/getting_started/core_concepts/rag_triad/)
- #####  [RAG Evaluation Metrics: How to evaluate your RAG pipeline with Braintrust](https://www.braintrust.dev/articles/rag-evaluation-metrics)
- #####  [LLM evaluation metrics: Full guide to LLM evals and key metrics](https://www.braintrust.dev/articles/llm-evaluation-metrics-guide)
- #####  [Retrieval-Augmented Generation: A Comprehensive Survey of Architectures, Enhancements, and Robustness Frontiers](https://arxiv.org/abs/2506.00054)
- #####  [A Comprehensive Survey of Retrieval-Augmented Generation (RAG): Evolution, Current Landscape and Future Directions ](https://arxiv.org/abs/2410.12837)
- #####  [StreamingQA: A Benchmark for Adaptation to New Knowledge over Time in Question Answering Models](https://arxiv.org/abs/2205.11388)
- #####  [Retrieval-augmented generation for generative artificial intelligence in health care](https://www.nature.com/articles/s44401-024-00004-1)
- #####  [Building a “Golden Dataset” for AI Evaluation: A Step-by-Step Guide](https://www.getmaxim.ai/articles/building-a-golden-dataset-for-ai-evaluation-a-step-by-step-guide/)
- #####  [A Survey on Evaluation of Large Language Models](https://arxiv.org/abs/2307.03109)
- #####  [A Practical Guide for Evaluating LLMs and LLM-Reliant Systems](https://arxiv.org/html/2506.13023v1)