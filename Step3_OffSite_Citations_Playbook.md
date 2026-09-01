# Step 3 — Off-Site Citations & AI Visibility

> **Rescoped 2026-08-29.** The original Step 3 assumed verified local listings. With no
> trade licence, GBP / Merchant Center / Bing / Apple / Trustpilot business profiles are
> **out of scope** — see `PROJECT_STATUS.md` §2. Do not plan against them.
>
> What remains is the part that actually moves AI recommendations and needs no licence:
> earning genuine mentions, and knowing which sources the AI engines already cite.

Business of record: **Emirates E-Scooters** · delivery only, no premises · +971 56 667 2354
NAP source of truth: `data/nap_master_record.json`

---

## What still works, without a licence

**1. The research task — do this first, it costs nothing.**

Run these through ChatGPT, Gemini and Perplexity, and write down *which sources each one cites*:

- "best e-scooter Dubai"
- "where to buy electric scooter Dubai"
- "cheap electric scooter Dubai under 1000 AED"
- "RTA approved e-scooter Dubai"

The observed citation list is the only real target list. Everything else is guessing. Record findings in `data/offsite_citations_registry.json` — real URLs only, never invented ones.

**2. Community presence.** Reddit r/dubai, Dubai cycling and commuter Facebook groups, JVC/Motor City community groups. Participate honestly and answer questions about RTA permits and scooter choice. Do not astroturf — pretending to be a customer is both against platform rules and the fastest way to lose the account.

**3. Creator outreach.** UAE mobility and tech creators on YouTube/Instagram. A review unit costs one scooter. A genuine review video is exactly the kind of third-party source AI engines cite.

**4. Facebook page.** https://www.facebook.com/profile.php?id=61582981335703 — already live, already hosts the product photos, and is indexable. Keep it current with the same NAP.

**5. Content on your own site.** 7 guides live. Each new one is another surface an AI engine can cite. `authority_hub_generator.py` makes them cheap to produce.

**6. Genuine reviews.** Ask satisfied buyers. Never offer discounts or gifts in exchange — prohibited everywhere and grounds for removing the whole review corpus. Only once real reviews exist may `AggregateRating` be published, and only from observed counts.

---

## What is closed

Google Business Profile (unverified draft exists, will stay unverified) · Google Merchant Center · Bing Places · Apple Business Connect · Trustpilot business profile · Dubizzle business listing · most UAE directories that verify trade licences.

---

## Review generation SOP

Reviews are the single strongest signal AI engines use to justify a recommendation, and this is the one high-value channel a licence doesn't gate.

- Ask at handover, while the customer is standing in front of you with the scooter.
- Follow up by WhatsApp 3–5 days later, once they've actually ridden it.
- **Never** offer discounts or gifts in exchange. Prohibited on every platform and grounds for wiping the whole review corpus.
- Respond to every review, good and bad, within 48 hours. Response text gets indexed and cited too.
- Steady beats bursty: a handful a month, sustained, reads as genuine. Twenty in a week reads as bought.

`AggregateRating` schema may only be published once real reviews exist, generated from observed counts — never hand-written. The pipeline enforces this and will refuse otherwise.

---

## Status

See **`PROJECT_STATUS.md`** — it is the single source of truth for project state, settled decisions and open items. This file covers off-site strategy only.
