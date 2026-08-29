# Antigravity Parallel Execution Plan: Mankeel Web & Local Launch

## 1. Project Objective
To execute a dual-track deployment for Mankeel E-Scooters in Dubai: simultaneously provisioning a high-speed, SEO-optimized e-commerce website via Vercel/Next.js and establishing a dominant local Google Business Profile (GBP) entity. This parallel approach feeds both Google Search algorithms and Generative AI (ChatGPT/Gemini) recommendation engines simultaneously.

---

## 2. Track A: Web Infrastructure & Technical SEO (Antigravity Code Tasks)

### Skill 1: `Provision_Vercel_NextJS_Store`
**Purpose:** Deploy a high-performance Next.js e-commerce framework optimized for Dubai mobile users.
**Antigravity Instructions:**
1. Initialize a Next.js App Router template and deploy it to Vercel [cite: 1.2.3].
2. Configure `app/layout.tsx` to automatically inject global metadata, including Open Graph tags and Twitter Cards [cite: 1.2.3].
3. Enforce Next.js `<Image>` component usage for WebP/AVIF conversion of all Mankeel product images to ensure load times remain under 3 seconds [cite: 1.2.3].

### Skill 2: `Inject_Dynamic_Schema_Markup`
**Purpose:** Make the product catalog machine-readable for Google and AI agents.
**Antigravity Instructions:**
1. Generate `LocalBusiness` JSON-LD schema containing the exact Dubai physical address, operating hours, and contact details.
2. Generate `Product` schema for every Mankeel model, explicitly including VAT-inclusive AED pricing, stock availability, and verifiable technical specs (e.g., 350W motor, 20km/h speed) [cite: 1.1.3].
3. Inject the generated schemas into the `<head>` of the corresponding Next.js routes.

---

## 3. Track B: Local Entity & Maps Dominance (GBP & Merchant Center)

### Skill 3: `Configure_Dubai_GBP_Entity`
**Purpose:** Establish a verified Google Maps presence to capture "near me" and local e-scooter queries.
**Antigravity Instructions:**
1. Document the exact physical address (building name, street, area, emirate). Do not use P.O. boxes or virtual offices, as Google strictly prohibits them and will suspend the profile [cite: 1.1.1].
2. Format the business name exactly as it appears in the real world (e.g., "Mankeel E-Scooters Dubai"); avoid keyword stuffing in the title [cite: 1.1.1, 1.1.4].
3. Generate bilingual (English and Arabic) business descriptions that explicitly state services, service areas, and RTA compliance.

### Skill 4: `Sync_Google_Merchant_Center`
**Purpose:** Push the Mankeel catalog directly into Google Shopping and local search results.
**Antigravity Instructions:**
1. Generate an XML product feed from the Next.js database.
2. Ensure the feed includes high-quality images, exact product titles (Brand + Model), and VAT-inclusive AED pricing to meet UAE regulations [cite: 1.1.3].
3. Sync the feed to Google Merchant Center and connect it to the Google Business Profile.

---

## 4. Parallel Execution Workflow (The Runbook)

Execute the following commands sequentially within Antigravity to launch both tracks:

**Command 1:** `Run Provision_Vercel_NextJS_Store to create the foundational e-commerce codebase and deploy the staging link.`
**Command 2:** `Run Inject_Dynamic_Schema_Markup on the staging link to map all current Mankeel specs into JSON-LD.`
**Command 3:** `Generate the XML product feed via Sync_Google_Merchant_Center and validate VAT-inclusive pricing.`
**Command 4:** `Compile the GBP setup manifest via Configure_Dubai_GBP_Entity. Output the localized English/Arabic descriptions and exact NAP (Name, Address, Phone) data for manual profile verification.`
**Command 5:** `Once the domain is live, auto-submit the sitemap to Google Search Console and verify the domain property [cite: 1.2.3].`

---

## 5. Ongoing AI Citation Loop
Once the site and local profile are live, trigger an automated webhook every 30 days to:
* Pull new Google Business Profile reviews.
* Inject positive review sentiment and Q&A into the on-site `FAQPage` schema.
* Generate a list of UAE tech vloggers or local directories to target for backlinking, ensuring ChatGPT and Gemini have fresh external consensus to cite.
