# Listing Submission Pack — Emirates E-Scooters

> ## ⚠️ OUT OF SCOPE — retained for reference only
>
> **Updated 2026-08-29.** The owner has decided not to pursue a UAE trade licence.
> Google Business Profile verification, Google Merchant Center, Bing Places, Apple
> Business Connect and Trustpilot/Dubizzle business profiles all require business
> documentation, so **none of them are achievable and none should be planned for.**
>
> Do not raise licensing again. See `PROJECT_STATUS.md` §2.
>
> This pack is kept only so the prepared values aren't lost if circumstances ever
> change. The field values below are correct and current; the *plan* is not active.
>
> **The in-scope channels are the website, `llms.txt`, content and the Facebook page.**

---

## 1. Business type: SERVICE AREA BUSINESS

Emirates E-Scooters is a delivery-only business with **no premises open to the public**. This governs every listing below.

- **Do not publish a street address anywhere.** Not on Google, Bing, Apple, any directory, or the website.
- The Motor City Waitrose location is a customer meeting point, not premises the business occupies. It must never appear as an address.
- Each platform still needs a **real base address for verification only** (normally the owner's home). It is stored privately and never displayed. Saam enters this himself — it is not in this pack. It must not be a PO box, a virtual office, or the Waitrose meeting point.

**The citation set — paste identically everywhere:**

| Field | Value |
|---|---|
| Business name | `Emirates E-Scooters` |
| Business name (Arabic) | `إميرتس إي سكوترز` |
| Street address | **none — hidden** |
| City / Emirate | `Dubai` / `Dubai` |
| Country | `United Arab Emirates` |
| Phone | `+971 56 667 2354` |
| Website | `https://emirates-scooters-dubai.vercel.app` |
| Contact & delivery hours | `08:00 – 22:00`, all seven days |

Service areas (11, owner-revised): Motor City · Sports City · JVC · Arabian Ranches · Damac Hills · Mudon · Studio City · Al Barsha South · Production City · Green Community · JVT

Do **not** append "Dubai" or "UAE" to the business name — Google treats location stuffing in the title as a violation.

---

## 2. Google Business Profile

**Form:** https://business.google.com/create

| Field | Value |
|---|---|
| Business name | `Emirates E-Scooters` |
| Business name (Arabic) | `إميرتس إي سكوترز` |
| Primary category | `Scooter Repair Shop` or `Motor Scooter Dealer` — pick whichever matches the dominant activity; a retail-first shop is usually the dealer category |
| Secondary categories | `Electric Vehicle Charging Station` only if you actually offer it; otherwise leave empty |
| Address | **hidden — service area business** |
| Service area | Motor City, Dubai Sports City, Dubai Studio City, JVC, Arabian Ranches, Damac Hills, Mudon, Al Barsha South |
| Phone | `+971 56 667 2354` |
| Website | `https://emirates-scooters-dubai.vercel.app` |
| Hours | `08:00 – 22:00`, Monday–Sunday (all seven days) |
| Description (750 char max) | see below |
| Opening date | Saam to supply |

**Description — as currently live on the GBP draft (713 chars):**

```
Emirates E-Scooters supplies Mankeel electric scooters across Dubai. We are a delivery-based business: we bring the scooter to you rather than running a shop, so you can inspect it in person before you accept it.

Models: the Mankeel MK083 city commuter (350W, 699 AED) and the Mankeel MX-14 off-road (800W, 1,499 AED). Both include a one-year warranty and VAT-inclusive AED pricing.

We also handle servicing, genuine Mankeel spare parts, and battery health checks, including the summer thermal checks that matter in UAE heat.

Delivery across Motor City, Sports City, Studio City, JVC, Arabian Ranches, Damac Hills, Mudon and Al Barsha South. Ask us about RTA permit requirements and where you can legally ride.
```

**Status:** the profile already exists and was reconfigured on 2026-08-29 to *"No location; deliveries and home services only"*, with the description rewritten to delivery framing. It is **not yet verified** and not publicly visible.

**Verification to expect:** with the address hidden, Google usually stops asking for a storefront video. Expect postcard to your real base address, a phone call, or a video showing you genuinely operate — stock, branded materials, tools, delivery setup. All of those you can do honestly.

If it still demands a storefront walkthrough, stop and re-check the listing type rather than improvising a video. Filming premises you don't occupy is what gets accounts banned.

---

## 3. Bing Places

**Form:** https://www.bingplaces.com

Bing offers "import from Google Business Profile" — **do GBP first**, then import. Faster and guarantees the NAP matches.

| Field | Value |
|---|---|
| Business name | `Emirates E-Scooters` |
| Category | `Motorcycle & Scooter Dealers` |
| Address | **hidden — service area business** |
| Phone / website | as §1 |
| Hours | `08:00 – 22:00`, Monday–Sunday (all seven days) |
| Description | reuse the §2 description |

**Verification:** phone call or postcard. Bing generally verifies faster than Google.

---

## 4. Apple Business Connect

**Form:** https://businessconnect.apple.com

| Field | Value |
|---|---|
| Business name | `Emirates E-Scooters` |
| Category | `Shopping > Automotive` (Apple's tree differs from Google's; pick the nearest retail-automotive node) |
| Address | **hidden — service area business** |
| Phone / website | as §1 |
| Hours | `08:00 – 22:00`, Monday–Sunday (all seven days) |

**Verification:** Apple requires an Apple ID plus proof of authority — normally a trade licence. Note that Apple Business Connect is oriented to places on the map; a delivery-only business may have limited options there. Do GBP and Bing first.

**Trade licence:** not held, and not being pursued. This is why this pack is inactive.

---

## 5. Field status

**Trading hours — RESOLVED.** Saam confirmed 08:00–22:00, all seven days. Now published in schema, the GBP manifest, llms.txt and the tables above.

**Arabic trading name — CONFIRMED.** Saam chose the transliteration: **`إميرتس إي سكوترز`** — a phonetic rendering of "Emirates E-Scooters" that carries no descriptive meaning in Arabic. Use it verbatim wherever a listing offers an Arabic name field.

One caveat, not a blocker: if a UAE trade licence has already been issued, the Arabic name printed on it is the legal identifier and listings should match it exactly. Check the licence — if it differs, the licence wins and every listing needs updating. A side effect of the transliteration choice is that the Arabic name contains no words meaning "electric scooter", so Arabic-language search relevance now has to come from the Arabic description rather than the name.

**Speed modes — RESOLVED.** Three selectable modes; mode 1 is limited to 20 km/h, matching the RTA maximum. Published as a factual capability. Never claim 'RTA certified/approved' or 'RTA Authorized Dealer'.

---

## 6. Speed and the RTA limit — RESOLVED

RTA requires that an e-scooter's maximum speed be set to **20 km/h** ([rta.ae](https://www.rta.ae/wps/portal/rta/ae/home/promotion/rta-esccoter)). The site previously stated 25 km/h — wrong as a claim about the law, and corrected everywhere.

**Owner confirmed 2026-08-29:** every model ships with **three selectable speed modes, mode 1 limited to 20 km/h**. That is publishable as a factual capability and is now stated on the site and in `llms.txt`.

- ✅ Say: "Three speed modes; mode 1 is limited to 20 km/h, matching Dubai's RTA limit."
- ❌ Never say: "RTA certified", "RTA approved", "RTA Authorized Dealer" — statuses the business does not hold. Enforced by `test_08`.

Full catalogue and specs: `data/mankeel_products.json` (5 models). See `PROJECT_STATUS.md` §5.
