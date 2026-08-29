# Step 3 — Off-Site Citations (The ChatGPT & Gemini Fuel)

Source: `Antigravity_Mankeel_Execution_Plan_Part_2.md`, Section 3.
Business of record: **Emirates E-Scooters**, Motor City Waitrose, Dubai, UAE · +971 56 667 2354 · Owner: Saam Khan.
NAP source of truth: `data/nap_master_record.json`.

---

## 0. Blocker — read this first

The Step 3 assets already in this repo are **placeholder fiction**, not collected data:

- `data/offsite_citations_registry.json` lists a Trustpilot profile, a Google Maps CID, a Khaleej Times article and a Dubizzle guide. None of these were verified to exist; the URLs are constructed, not observed.
- `output/reports/offsite_citations_sentiment_manifest.json` publishes an `AggregateRating` of **4.85 from 148 reviews**. `src/automation/ai_citation_sentiment_engine.py` computes that number by averaging four hand-written "trust_score" values and hardcoding `ratingCount: "148"`.
- The `consensus_faqs` block asserts, in schema meant for Google and LLMs, that specific publications made specific recommendations.

Publishing invented review counts and third-party endorsements is a Google structured-data policy violation (manual action / rich-result loss) and is straightforwardly deceptive to customers. **Nothing in the sentiment manifest should go live.** The generator needs to read from real, collected review data or be removed.

Second blocker: the entire repo is built for a different business — "Mankeel E-Scooters Dubai" at Silver Tower, JLT, phone +971 4 456 7890. Citations are worthless if the NAP is wrong, and Step 3 is *entirely* a NAP-consistency exercise. That correction has to land before any listing is submitted.

---

## 1. What Step 3 actually calls for

Two sub-goals from the plan:

1. **Review generation** — a steady stream of recent, genuine reviews, primarily on Google Business Profile, because local ranking and LLM recommendation both lean on it.
2. **Targeted AI citations** — get Emirates E-Scooters mentioned on the specific third-party platforms that ChatGPT/Gemini already cite when recommending e-scooters in Dubai.

---

## 2. Prerequisite: NAP lockdown

Before a single citation is submitted, the exact string set below must be final and identical everywhere.

```
Emirates E-Scooters
[Unit/Store no. TBC], Waitrose, Motor City, Dubai, United Arab Emirates
+971 56 667 2354
[production domain TBC]
```

Open items for Saam:

- Exact unit/store number and street at the Motor City Waitrose site.
- Whether this is a standalone unit or a concession inside Waitrose — this determines whether a GBP listing is even eligible, and getting it wrong causes suspension.
- Confirmed lat/long (drop a pin at the actual door, not the mall centroid).
- Final production domain (the repo currently assumes a `.vercel.app` staging URL).
- Approved Arabic trading name.

Then: sweep the 25 files listed in the audit for the old JLT/Mankeel values and regenerate outputs.

---

## 3. Citation target list — to be verified, not assumed

Work top-down. Each is a *candidate* until someone opens it and confirms the business qualifies. Do not record a URL in the registry until the listing actually exists.

**Tier 1 — highest weight, do first**

| Target | Why | Action |
|---|---|---|
| Google Business Profile | The single largest input to both Maps ranking and AI local recommendations | Claim & verify (Step 2 dependency) |
| Google Merchant Center | Feeds product-level results; feed already generated in `output/google-merchant-feed.xml` | Correct NAP + pricing, then submit |
| Apple Business Connect | Apple Maps / Siri surface | Claim |
| Bing Places | Feeds Copilot and Bing local | Claim |

**Tier 2 — UAE local directories and marketplaces**

Candidates worth evaluating: Dubizzle, Yellow Pages UAE, Connect.ae, UAE Contact, Hidubai, Yelo.ae, Trustpilot, Facebook Page, Instagram business profile. For each: confirm the platform still operates, confirm the category fits e-mobility retail, submit with the exact NAP string.

**Tier 3 — editorial and community mentions (the actual "AI fuel")**

This is the part that moves LLM recommendations, and it cannot be automated into existence:

- UAE tech/mobility YouTubers and Instagram creators — outreach for a review unit.
- Dubai commuter and expat communities (Reddit r/dubai, local Facebook groups) — participate honestly; do not astroturf.
- Local press pitches (Khaleej Times, Gulf News, Time Out Dubai tech/mobility desks) tied to a real news hook: RTA permit changes, summer battery safety, a new model launch.

**Research task before outreach:** run the target queries ("best e-scooter Dubai", "where to buy electric scooter Dubai", "RTA approved scooter shop") through ChatGPT and Gemini and record which sources they actually cite. That observed list — not a guessed one — becomes the real target registry.

---

## 4. Review generation SOP

- Ask every customer at handover; a printed QR code to the GBP review link at the point of sale is the highest-yield mechanism.
- Follow up by WhatsApp 3–5 days after delivery, once the customer has actually ridden it.
- Never offer discounts or gifts in exchange for reviews — prohibited by Google and Trustpilot, and grounds for removal of the whole review corpus.
- Respond to every review, positive and negative, within 48 hours. Response text is itself indexed and cited.
- Target cadence: 4–8 genuine new reviews per month, sustained, beats a burst.

Only once real reviews exist can `AggregateRating` schema be published — and it must then be generated from the actual count and average, pulled from the GBP API, not from a hand-edited JSON file.

---

## 5. Status

**Done (2026-08-29):**

- NAP corrected across the codebase to Emirates E-Scooters / Store 001, Waitrose, Motor City / +971 56 667 2354 / 25.041390, 55.229148. Source of truth: `data/nap_master_record.json`.
- Fabricated review data removed. `ai_citation_sentiment_engine.py` now refuses to emit `AggregateRating` or consensus FAQs without verified, observed review data, and any rating it does emit must carry `_provenance` per source. The registry was rebuilt as *prospects*, not endorsements.
- `llms.txt` / `llms-full.txt` now generate the catalog from `data/mankeel_products.json`. They previously advertised two models that don't exist (MX25, MK085), duplicated the MX-14 slug with conflicting specs, and marked in-stock models as out of stock.
- Service areas rewritten from JLT/Marina/Business Bay to the Motor City catchment.
- `run_all.py` runs clean; 10/10 pipeline tests pass.

**Owner actions — I can't do these (account credentials + external submission):**

1. Claim Google Business Profile at `business.google.com` using the NAP above.
2. Add and verify the domain property in Search Console, submit the sitemap.
3. Submit the corrected feed to Google Merchant Center.
4. Claim Bing Places and Apple Business Connect.

**Still blocking, needs your answer:**

- Standalone unit vs. concession inside Waitrose — decides GBP eligibility and category.
- Final production domain (code still assumes `emirates-scooters-dubai.vercel.app` / the Vercel staging URL).
- Approved Arabic trading name (currently `TO_CONFIRM`).
- Actual trading hours and price range — the 09:00–21:00 in the schema is an unverified placeholder.

**Two accuracy conflicts to resolve before publishing:**

- `llms.txt` claims speed governors capped at 25 km/h, but the catalog lists 45 km/h (MX-14) and 30 km/h (MK083). Both can't be true.
- `indexing_and_serp_monitor.py` prints "Search Console Submission Status: 200 OK" without calling anything. It's a mock; don't read it as confirmation that URLs were submitted.

**Then:** run the §3 research to find which sources ChatGPT and Gemini actually cite, and build the outreach list from that.
