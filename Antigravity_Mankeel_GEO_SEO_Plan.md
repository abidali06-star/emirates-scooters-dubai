# Antigravity Execution Plan: Mankeel E-Scooter GEO & SEO Automation

## 1. Project Objective
To establish dominant local search rankings (Google) and secure top generative AI recommendations (ChatGPT, Gemini) for Mankeel E-Scooters in the Dubai market. This will be achieved by utilizing Google Antigravity to autonomously audit, rewrite, structure, and deploy optimized e-commerce codebase updates.

---

## 2. System Architecture & Prerequisites
Before executing this plan, ensure the Antigravity environment is configured with the necessary integrations and access rights to your web hosting infrastructure and data layers.

*   **Codebase Access:** Antigravity must have read/write access to the e-commerce frontend repository.
*   **LLM Engine:** Gemini (Configured with system prompts for strict, verifiable output to avoid API limits).
*   **MCP (Model Context Protocol) Tools:**
    *   `SERP_API` or equivalent for live Dubai search data.
    *   `Search_Console_API` for indexing requests and performance tracking.

---

## 3. Core Antigravity Skills to Define

To run this workflow autonomously, define the following Skills within your Antigravity workspace. 

### Skill 1: `Extract_And_Structure_Specs`
**Purpose:** Scrape existing product pages and convert unstructured marketing text into machine-readable JSON and HTML tables.
**System Prompt Instructions:**
1. Parse the provided product URL or raw text for Mankeel scooters.
2. Extract quantifiable data (e.g., 350W motor, 20 km/h speed, IP54 rating, battery life).
3. Output a strict HTML `<table>` summarizing these technical specifications.
4. Output a validated JSON-LD `Product` schema, mapping the specifications to the correct schema properties.

### Skill 2: `Rewrite_For_GEO_Compliance`
**Purpose:** Reformat product descriptions to meet Generative Engine Optimization (GEO) standards (Answer-First, citation-ready, verifiable).
**System Prompt Instructions:**
1. Take the raw product data and rewrite the main description.
2. The first sentence MUST directly answer: "What is this product and who is it for in Dubai?" (e.g., "The Mankeel [Model] is a 350W electric scooter designed for daily commuting in Dubai, compliant with RTA speed regulations.")
3. Remove qualitative fluff ("best", "ultimate") and replace it with factual, engineering-focused capabilities.
4. Output the updated copy in Markdown format, structured with `##` and `###` headers.

### Skill 3: `Generate_Local_Authority_Hub`
**Purpose:** Create local Dubai topical authority content to capture long-tail Google Search intent.
**System Prompt Instructions:**
1. Using the target keyword provided (e.g., "Dubai RTA E-scooter rules"), draft a comprehensive, highly accurate guide.
2. Include specific Dubai locations (JLT, Marina, Downtown).
3. Generate valid `FAQPage` JSON-LD schema based on the generated H2 questions and answers.
4. Output the final HTML/Markdown ready for publication.

---

## 4. Execution Workflow (The Antigravity Runbook)

Execute the following commands sequentially within Antigravity to deploy the changes.

### Phase 1: Product Page Overhaul
**Command 1:** `Run Extract_And_Structure_Specs on all Mankeel product URLs in the repository.`
*Antigravity Action:* Agent reads the product files, extracts specs, and generates the tables and schema.

**Command 2:** `Run Rewrite_For_GEO_Compliance on the output of Command 1.`
*Antigravity Action:* Agent drafts the new answer-first content blocks.

**Command 3:** `Inject the new HTML tables, GEO-optimized copy, and JSON-LD schema into the corresponding product page components in the codebase. Ensure mobile responsiveness is maintained. Create a pull request/commit for review.`
*Antigravity Action:* Agent modifies the actual code (e.g., React/Next.js components or raw HTML) and stages the deployment.

### Phase 2: Topical Authority Deployment
**Command 4:** `Run Generate_Local_Authority_Hub for the following topics: 1. How to get an RTA E-Scooter Permit in Dubai. 2. Battery maintenance for E-scooters in UAE summer heat. 3. Best E-scooter tracks in Dubai.`
*Antigravity Action:* Agent writes the localized blog posts/guides.

**Command 5:** `Create new blog pages in the repository for the output of Command 4. Include the generated FAQPage schema in the <head> of each document. Commit the changes.`
*Antigravity Action:* Agent creates the new routes/files in your project structure.

### Phase 3: Automated Indexing & Briefing
**Command 6:** `Once the codebase is deployed, use the Search_Console_API to submit the updated product URLs and new blog URLs for immediate indexing.`

---

## 5. Continuous Monitoring & Automation
To maintain positioning, configure a recurring automated workflow (e.g., utilizing an n8n webhook or cron job trigger linked to Antigravity/Gemini) to perform the following daily actions:
*   Monitor local Dubai SERP rankings for target keywords.
*   Check for any new RTA regulation updates to inject into the FAQ schema.
*   Generate a daily market intelligence brief summarizing visibility shifts and competitor movements.
