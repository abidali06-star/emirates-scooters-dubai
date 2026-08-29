# Listing Submission Pack — Emirates E-Scooters

Prepared 2026-08-29. Everything below is staged and ready to paste.

**I cannot submit these for you.** Each requires signing into an account as the business owner and passing identity verification tied to Saam. Those steps need his credentials and, in most cases, a physical postcard or a live video call. Creating accounts or entering credentials on his behalf is out of bounds — so this pack takes it to the last click and stops there.

**All fields below are confirmed and ready to paste.** Trading hours 08:00–22:00 all seven days; Arabic trade name `إميرتس إي سكوترز`. One caveat on the Arabic name in §5.

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

Service areas (11, as entered in GBP): Motor City · Dubai Sports City · Dubai Studio City · JVC · JVT · Arabian Ranches · Damac Hills · Mudon · Al Barsha South · Dubai Production City · Green Community Motor City

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

**Description — paste as-is (692 chars):**

```
Emirates E-Scooters is the official Mankeel electric scooter store in Dubai, located at Waitrose, Motor City. We stock the Mankeel MK083 city commuter and the Mankeel MX-14 off-road model, supplied with a one-year warranty and VAT-inclusive AED pricing.

Our workshop handles servicing, genuine Mankeel spare parts, and battery health checks — including summer thermal diagnostics, which matter in UAE heat. We deliver locally across Motor City, Sports City, Studio City, JVC, Arabian Ranches, Damac Hills, Mudon and Al Barsha South.

Visit us in store for advice on choosing a scooter, on RTA permit requirements, and on where you can legally ride in Dubai.
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

**Trade licence:** Google and Apple both ask for business documentation, and the UAE requires a licence to trade. If there isn't one yet, Dubai's e-Trader licence covers home-based online selling (~AED 1,070–1,370 government fees), though most sources restrict it to UAE/GCC nationals — if you're on a residence visa you'd need a different e-commerce licence. Worth settling before verification.

---

## 5. Field status

**Trading hours — RESOLVED.** Saam confirmed 08:00–22:00, all seven days. Now published in schema, the GBP manifest, llms.txt and the tables above.

**Arabic trading name — CONFIRMED.** Saam chose the transliteration: **`إميرتس إي سكوترز`** — a phonetic rendering of "Emirates E-Scooters" that carries no descriptive meaning in Arabic. Use it verbatim wherever a listing offers an Arabic name field.

One caveat, not a blocker: if a UAE trade licence has already been issued, the Arabic name printed on it is the legal identifier and listings should match it exactly. Check the licence — if it differs, the licence wins and every listing needs updating. A side effect of the transliteration choice is that the Arabic name contains no words meaning "electric scooter", so Arabic-language search relevance now has to come from the Arabic description rather than the name.

**Speed-governor claim.** Omitted from all product copy — see §6.

---

## 6. The speed-limit finding — this one is important

Saam suggested extracting specs from the live site. That's circular: the site is generated from `data/mankeel_products.json` by this pipeline, so reading it back just re-imports the figure in question. It confirms what we publish, not what is true.

I read it anyway. **What the live site currently states:**

| | MK083 | MX-14 |
|---|---|---|
| Price | 699 AED (VAT incl.) | 1,499 AED (VAT incl.) |
| Top speed | 30 km/h | 45 km/h |
| Range | 35 km | 56 km |
| Motor | 350W | 800W |
| Battery | 36V 7.8Ah | 48V 13Ah |
| Tyre | 8.5" honeycomb | 10" off-road |
| Charge time | 4–5 h | 6–7 h |
| Weight | 12 kg | 18 kg |
| Max payload | 120 kg | 200 kg |
| Stock | In Stock | In Stock |

**The problem is worse than the internal conflict I flagged earlier.** I checked the RTA primary source. Under General Notes on the official e-scooter page, RTA states:

> "The maximum e-scooter speed limit must be set at 20 km/h."

So the old copy claiming "speed governors set to legal 25 km/h" was wrong **twice** — wrong as a product claim, and wrong about the law. The real limit is 20 km/h, not 25. **Corrected and deployed 2026-08-29:** the RTA permit guide now states 20 km/h in both places, cited to rta.ae.

Both models' advertised top speeds (30 and 45 km/h) exceed the 20 km/h regulatory limit. That is not necessarily a problem — the hardware can be capable of more than the legal riding limit — but it does mean **"RTA compliant" cannot be asserted on top-speed grounds**, and any compliance claim needs to rest on the scooter being limited to 20 km/h in its Dubai configuration.

**Which source to trust, in order:**

1. **Mankeel's manufacturer spec sheet / declaration of conformity** for the units actually imported — authoritative for what the hardware does and whether a governor is fitted.
2. **RTA's published rules** (rta.ae) — authoritative for the legal limit. Currently 20 km/h.
3. **Saam's own records** — import documentation, supplier invoices, any UAE type-approval or conformity certificate. Authoritative for what was actually sold.
4. **Our own website** — not a source. It's downstream of the data we're trying to verify.

**Recommendation:** get the Mankeel spec sheet, confirm whether the units ship with a 20 km/h Dubai limiter, and only then write a compliance claim. Until that's settled, state the hardware top speed as a plain spec and say nothing about governors or compliance. Publishing "RTA compliant" on a scooter that isn't limited is a consumer-protection problem, not just an SEO one.

---

## 7. Order of operations

1. ~~Hours~~ — done, 08:00–22:00 all days, deployed.
2. ~~RTA legal figure corrected 25 → 20 km/h~~ — done, deployed.
3. Saam confirms the Arabic trading name against his trade licence (§5).
4. Saam obtains the Mankeel spec sheet (§6) so a compliance claim can be written, or permanently dropped.
5. Submit GBP → verify → import to Bing → Apple.
6. Only after GBP is live and collecting genuine reviews does the Step 3 citation work in `Step3_OffSite_Citations_Playbook.md` become useful.

GBP, Bing and Apple can all be submitted now — the blanks that remain (Arabic name) are optional fields, and nothing currently on the site is known to be wrong.

---

**Sources**

- RTA official e-scooter page (20 km/h limit, safety stipulations, permit): https://www.rta.ae/wps/portal/rta/ae/home/promotion/rta-esccoter
- Executive Council Resolution No. 13 of 2022: https://www.rta.ae/wps/wcm/connect/rta/14f85ce1-1c95-4803-bfb4-85e3c2feef22/Executive-Council-Resolution-13-2022-en.pdf?MOD=AJPERES
- Live product specs read 2026-08-29 from https://emirates-scooters-dubai.vercel.app/products/mk083 and /products/mx-14
