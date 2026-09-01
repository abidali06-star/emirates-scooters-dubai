# Emirates E-Scooters — Project Status & Handover

**Last updated:** 2026-08-29
**Owner:** Saam Khan · +971 56 667 2354
**Repo:** `github.com/abidali06-star/emirates-scooters-dubai` (branch `master`)
**Live site:** https://emirates-scooters-dubai.vercel.app (auto-deploys on push)

This is the single source of truth for where the project stands. Read this first.

---

## 1. What this business actually is

**Emirates E-Scooters** resells Mankeel electric scooters in Dubai.

- **Delivery only.** No shop, no showroom, no premises open to the public.
- The Motor City Waitrose location is a **customer meeting point**, not premises the business occupies. It must never be published as an address.
- It is a **side business with no UAE trade licence**.

Everything below follows from those three facts. The original plan documents (`Antigravity_Mankeel_*.md`) were written assuming a licensed retailer with a physical store. **They are historical context, not the current plan.** Where they conflict with this file, this file wins.

---

## 2. Settled decisions — do not reopen

| Decision | Made | Consequence |
|---|---|---|
| **No trade licence.** Not being pursued. | Owner, 2026-08-29 | Verified local listings are permanently out of scope. Don't plan around them, don't suggest licensing. |
| **No public street address.** Service-area business. | Owner, 2026-08-29 | No `streetAddress` or `geo` in any schema, listing or page. Enforced by a test. |
| **No personal address for platform verification.** | Owner, 2026-08-29 | Reinforces the above. No workaround attempted — PO boxes and virtual offices cause suspension. |
| **No custom domain.** Staying on `.vercel.app`. | Owner, 2026-08-29 | All canonical URLs use `emirates-scooters-dubai.vercel.app`. |
| **Arabic trade name:** `إميرتس إي سكوترز` (transliteration). | Owner, 2026-08-29 | Live. Carries no descriptive meaning in Arabic, so Arabic search relevance comes from the description. |
| **Hours:** 08:00–22:00, all seven days. | Owner, 2026-08-29 | Labelled *contact and delivery* hours, not shop hours. |

### Out of scope as a result

Google Business Profile verification · Google Merchant Center · Bing Places · Apple Business Connect · Trustpilot and Dubizzle business profiles.

All of these require business documentation. The prepared field values remain in `Submission_Pack.md` in case the situation ever changes, but **no work should be planned against them.**

An unverified GBP draft exists and is correctly configured as *"No location; deliveries and home services only"*. It is not publicly visible and will stay that way.

---

## 3. In scope — where the effort should go

The website is the entire asset. AI engines and organic search read pages, not licences.

1. **Website SEO/GEO** — schema, metadata, page quality. In good shape.
2. **`llms.txt` / `llms-full.txt`** — direct feed to ChatGPT, Gemini, Perplexity, Claude. Working and accurate.
3. **Content** — 7 guides live. This is the highest-leverage remaining channel.
4. **Facebook page** — https://www.facebook.com/profile.php?id=61582981335703 — already where product photos live.
5. **Word of mouth** — Dubai commuter and cycling communities. Free, and the only real source of the genuine reviews that AI engines weigh.

---

## 4. Current state — verified live

| Asset | State |
|---|---|
| Catalogue | 5 models: MK083, MX-14 (in stock) · MK085, MX25, G1 (out of stock) |
| Product pages | `/products/{mk083,mx-14,mk085,mx25,g1}` — all live with Product schema |
| Guides | 7, all live at `/blogs/{slug}` with FAQPage schema |
| Sitemap | 14 URLs, generated from data — new guides appear automatically |
| `llms.txt` | Live, generated from the catalogue |
| Schema | `LocalBusiness`, no street address, no geo, `areaServed` × 11 |
| Hours | 08:00–22:00 all days, in schema and llms.txt |
| `priceRange` | `AED 699 - AED 1499`, derived from in-catalogue prices |

---

## 5. Facts locked down (and what may/may not be claimed)

**Speed and the RTA limit — resolved 2026-08-29.**

Every model has **three selectable speed modes; mode 1 is limited to 20 km/h**, which matches the maximum e-scooter speed RTA requires in Dubai (source: [rta.ae](https://www.rta.ae/wps/portal/rta/ae/home/promotion/rta-esccoter)).

- ✅ **Say:** "Three speed modes. Mode 1 is limited to 20 km/h, matching Dubai's RTA limit."
- ❌ **Never say:** "RTA certified", "RTA approved", "RTA Authorized Dealer". Those are authority-granted statuses the business does not hold. A test blocks these strings in `llms.txt`.
- The site previously claimed the legal limit was 25 km/h. It is 20. Corrected everywhere.

**Review data.** There are no reviews yet. `AggregateRating` schema is *refused* by the pipeline until real, observed review data exists, and any rating it emits must carry per-source provenance. Never hand-write a rating or review count — an earlier version published a fabricated 4.85 from 148 reviews.

---

## 6. Open items

| Item | Notes |
|---|---|
| **G1 weight looks wrong** | Spec sheet says 12.5 kg for a 2400W dual motor with a 52V 21Ah battery. The battery alone is ~7 kg; MX25 is 33.5 kg at 1200W. Probably a typo — likely 25–30 kg. **Published as supplied.** Correct the spec sheet and re-run. |
| **Arabic copy review** | Descriptions were written to match the English. Have a native speaker read once before wider use. |
| **Product images** | Schema references `/images/products/{slug}.jpg` and `/images/mankeel-mk083-product.jpg`. These files do not exist yet. |
| **Service areas** | 11 areas, owner-revised. Confirm they still match real delivery coverage. |
| **`indexing_and_serp_monitor.py` is a mock** | Prints "Search Console Submission Status: 200 OK" without calling anything. Don't read its output as evidence anything was submitted. |

---

## 7. How the pipeline works

```
python run_all.py      # regenerates everything
python -m pytest tests/ -q
git add -A && git commit -m "..." && git push origin master   # Vercel auto-deploys
```

**Data flows one way.** Edit the JSON in `data/`, never the generated output.

| Source of truth | Drives |
|---|---|
| `data/nap_master_record.json` | Business identity, scope decisions, service areas |
| `data/dubai_gbp_profile.json` | NAP + descriptions consumed by the generators |
| `data/mankeel_products.json` | Catalogue → product pages, schema, llms.txt, merchant feed, sitemap |
| `src/generators/authority_hub_generator.py` | The 7 guides |

Generated — **do not hand-edit**: `src/nextjs/lib/data/*.json`, `src/nextjs/public/*`, `src/nextjs/app/layout.tsx`, `src/nextjs/app/products/[slug]/page.tsx`, everything in `output/`.

Hand-maintained: `src/nextjs/app/page.tsx`, `src/nextjs/app/blogs/[slug]/page.tsx`.

---

## 8. Guardrails the tests enforce

These exist because each one was violated at some point. Don't remove them.

- `test_02` — catalogue is exactly the 5 spec-sheet models.
- `test_05` — schema is `LocalBusiness` with **no** `streetAddress`, **no** `geo`, non-empty `areaServed`.
- `test_06` — `AggregateRating` is null unless backed by provenance where `ratingCount` equals the sum of observed counts.
- `test_07` / `test_09` — Next.js product data and merchant feed match the source catalogue size.
- `test_08` — `llms.txt` states the RTA position and contains no "RTA certified/approved/Authorized Dealer" claim.

---

## 9. History — what went wrong and was fixed

Useful context, because several of these were live for a while.

1. **Wrong business entirely.** The repo was built for "Mankeel E-Scooters Dubai" at Silver Tower, JLT, phone +971 4 456 7890. Corrected to Emirates E-Scooters across 25 files.
2. **Fabricated reviews.** `ai_citation_sentiment_engine.py` published an `AggregateRating` of 4.85 from 148 reviews for a business with no reviews, plus invented endorsements from Trustpilot, Khaleej Times and Dubizzle. Removed; the engine now refuses to fabricate.
3. **Claimed a shop that doesn't exist.** "Physical showroom at Waitrose, Motor City", "Visit us in store", a postal address in schema. All removed.
4. **Wrong law.** Stated Dubai's e-scooter limit as 25 km/h. It is 20.
5. **Catalogue cut to 2 models — my error.** I trusted `mankeel_products.json` (2 models) over the real catalogue and removed MX25, MK085 and G1, describing two of them as "models that do not exist". The spec sheet proved otherwise. The only genuine error in the original data was the G1 mislabelled as a second MX-14. All 5 restored; the Next.js product file is now generated so it can't drift again.
6. **Blog routes 404'd.** The sitemap advertised `/blogs/*` URLs with no route to serve them. Added `app/blogs/[slug]/page.tsx`.
7. **Sitemap missed 4 guides.** Blog URLs were hardcoded to 3. Now data-driven.

---

## 10. Suggested next steps

1. Fix the G1 weight, re-run, push.
2. Add real product images.
3. Keep writing guides — it's the one channel fully open, and `authority_hub_generator.py` makes each one cheap.
4. Ask satisfied buyers for Google reviews on the personal/Facebook side; do not offer incentives.
5. Run the target queries ("best e-scooter Dubai", "where to buy electric scooter Dubai") through ChatGPT and Gemini and record which sources they actually cite. That observed list is the real outreach target — see `Step3_OffSite_Citations_Playbook.md`.
