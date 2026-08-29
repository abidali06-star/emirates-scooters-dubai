# Listing Submission Pack — Emirates E-Scooters

Prepared 2026-08-29. Everything below is staged and ready to paste.

**I cannot submit these for you.** Each requires signing into an account as the business owner and passing identity verification tied to Saam. Those steps need his credentials and, in most cases, a physical postcard or a live video call. Creating accounts or entering credentials on his behalf is out of bounds — so this pack takes it to the last click and stops there.

**One field is deliberately blank: the Arabic trading name.** Trading hours are now confirmed (08:00–22:00, all seven days) and filled in below. See §5.

---

## 1. The canonical NAP — paste this identically everywhere

Character-for-character consistency across listings is the entire point of the exercise. One variant address weakens every citation.

| Field | Value |
|---|---|
| Business name | `Emirates E-Scooters` |
| Address line | `Store 001, Waitrose, Motor City` |
| City | `Dubai` |
| Region / Emirate | `Dubai` |
| Country | `United Arab Emirates` |
| Phone | `+971 56 667 2354` |
| Website | `https://emirates-scooters-dubai.vercel.app` |
| Latitude | `25.041390226596707` |
| Longitude | `55.22914791534377` |

Do **not** append "Dubai" or "UAE" to the business name — Google treats keyword/location stuffing in the title as a violation, and it's a common cause of suspension.

**Premises type: standalone unit.** File as a normal storefront with its own entrance. Do **not** use the "located within" / store-within-a-store relationship, and do **not** select service-area-only.

---

## 2. Google Business Profile

**Form:** https://business.google.com/create

| Field | Value |
|---|---|
| Business name | `Emirates E-Scooters` |
| Primary category | `Scooter Repair Shop` or `Motor Scooter Dealer` — pick whichever matches the dominant activity; a retail-first shop is usually the dealer category |
| Secondary categories | `Electric Vehicle Charging Station` only if you actually offer it; otherwise leave empty |
| Address | as §1 |
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

**Verification to expect:** for a new UAE retail address, Google will most likely require **video verification** — a single unbroken recording showing the street/signage, the store interior, and you demonstrating proof of management (keys, POS, branded stock). Postcard is sometimes offered instead. Have signage physically up before starting; a unit with no visible branding is the most common failure.

**Before you submit:** open Google Maps satellite view at the coordinates in §1 and confirm the pin sits on your door, not on the Waitrose entrance or the car park.

---

## 3. Bing Places

**Form:** https://www.bingplaces.com

Bing offers "import from Google Business Profile" — **do GBP first**, then import. Faster and guarantees the NAP matches.

| Field | Value |
|---|---|
| Business name | `Emirates E-Scooters` |
| Category | `Motorcycle & Scooter Dealers` |
| Address / phone / website / geo | as §1 |
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
| Address / phone / website / geo | as §1 |
| Hours | `08:00 – 22:00`, Monday–Sunday (all seven days) |

**Verification:** Apple requires an Apple ID plus proof of authority — usually a document showing the business name at the address (trade licence, tenancy contract, or utility bill). Have the trade licence PDF ready.

---

## 5. Field status

**Trading hours — RESOLVED.** Saam confirmed 08:00–22:00, all seven days. Now published in schema, the GBP manifest, llms.txt and the tables above.

**Arabic trading name.** Three options are staged in `data/nap_master_record.json` under `business_name.ar_proposals`, with `الإمارات للسكوترات الكهربائية` recommended. It is marked PROPOSED and must not go on a listing until confirmed — on a UAE trade licence the Arabic name is a legal identifier, and if a licence already exists, its Arabic name overrides all three options. Two things to check first: UAE trade-name rules restrict the use of country/emirate names, so `الإمارات` may need approval; and "Emirates" is a heavily used mark in the UAE.

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
