# Antigravity Prompt: Strict Catalog Initialization & Schema Injection

**Role & Objective:**
You are an expert Next.js and SEO developer. Your task is to initialize the Mankeel E-Scooters Dubai catalog in our Next.js App Router repository. You must restrict the entire website, routing, and schema injection strictly to the 5 models provided below. There are NO other products launched or available in the Dubai market.

**Task 1: Create the Product Database (JSON)**
Create a local data file (`lib/data/products.json`) containing exactly the following 5 products. Map the "Stock" value to boolean `inStock` (Yes = true, No = false). Map the specs to a nested `specifications` object.

```json
[
  {
    "Model": "G1",
    "Top Speed": "65 KMH",
    "Range": "80 KM",
    "Motor": "2400W",
    "Battery": "52V 21Ah",
    "Tire": "9.5\" Tubeless",
    "Charge time": "7-8 Hours",
    "Weight": "12.5 Kg",
    "Max Load": "200 KG",
    "Key Feature 1": "Dual Suspensions",
    "Key Feature 2": "Dual Hydraulic Disk Brakes",
    "Key Feature 3": "HD LED Display",
    "Key Feature 4": "App Control",
    "Product Link": "https://www.facebook.com/media/set/?set=a.122123167389099377&type=3",
    "Price AED": 2299,
    "Stock": "No"
  },
  {
    "Model": "MX-14",
    "Top Speed": "45 KMH",
    "Range": "56 KM",
    "Motor": "800W",
    "Battery": "48V 13Ah",
    "Tire": "10\" Off-road Tires",
    "Charge time": "6-7 Hours",
    "Weight": "18 Kg",
    "Max Load": "200 KG",
    "Key Feature 1": "Dual Spring Suspensions",
    "Key Feature 2": "Dual Disk Brakes",
    "Key Feature 3": "Upgraded BMS System",
    "Key Feature 4": "App Control",
    "Product Link": "https://www.facebook.com/media/set/?set=a.122123165103099377&type=3",
    "Price AED": 1499,
    "Stock": "Yes"
  },
  {
    "Model": "MX25",
    "Top Speed": "55 KMH",
    "Range": "55 KM",
    "Motor": "1200W",
    "Battery": "60V 15.6Ah",
    "Tire": "11\" Tubeless",
    "Charge time": "7-8 Hours",
    "Weight": "33.5 Kg",
    "Max Load": "200 KG",
    "Key Feature 1": "Dual Suspensions",
    "Key Feature 2": "Dual Hydraulic Disk Brakes",
    "Key Feature 3": "HD LED Display",
    "Key Feature 4": "App Control",
    "Product Link": "https://www.facebook.com/media/set/?set=a.122123171067099377&type=3",
    "Price AED": 1999,
    "Stock": "No"
  },
  {
    "Model": "MK083",
    "Top Speed": "30 KMH",
    "Range": "35 KM",
    "Motor": "350W",
    "Battery": "36V 7.8Ah",
    "Tire": "8.5\" Honeycomb Tire",
    "Charge time": "4-5 Hours",
    "Weight": "12 Kg",
    "Max Load": "120 KG",
    "Key Feature 1": "Rear Disc Brake",
    "Key Feature 2": "Cruise control",
    "Key Feature 3": "Foldable Design",
    "Key Feature 4": "App Control",
    "Product Link": "https://www.facebook.com/media/set/?set=a.122123166645099377&type=3",
    "Price AED": 699,
    "Stock": "Yes"
  },
  {
    "Model": "MK085",
    "Top Speed": "35 KMH",
    "Range": "35 KM",
    "Motor": "350W",
    "Battery": "36V 10.4Ah",
    "Tire": "10\" Honeycomb Tire",
    "Charge time": "5-6 Hours",
    "Weight": "15 Kg",
    "Max Load": "130 KG",
    "Key Feature 1": "Dual Suspensions",
    "Key Feature 2": "Rear Disc Brake",
    "Key Feature 3": "Foldable Design",
    "Key Feature 4": "App Control",
    "Product Link": "https://www.facebook.com/media/set/?set=a.122123169441099377&type=3",
    "Price AED": 999,
    "Stock": "No"
  }
]
```

**Task 2: Dynamic Page Generation (`app/products/[slug]/page.tsx`)**
Generate the Next.js Server Component for the product page. 
1. Build an HTML `<table>` rendering the technical specifications (Top Speed, Range, Motor, Battery, Tire, Charge Time, Weight, Max Load).
2. Render an unordered list `<ul>` for the 4 Key Features.
3. If `Stock` is "No" (G1, MX25, MK085), display a prominent "Out of Stock" UI badge and disable the "Buy" button. If `Stock` is "Yes" (MX-14, MK083), display an "In Stock" badge.

**Task 3: Strict Schema Injection**
Inside the same component, inject `Product` JSON-LD schema via a `<script>` tag using `dangerouslySetInnerHTML`. Ensure:
1. `name`: "Mankeel [Model]"
2. `offers.price`: The exact "Price AED" value.
3. `offers.priceCurrency`: "AED"
4. `offers.availability`: Map to "https://schema.org/InStock" for MX-14 and MK083, and "https://schema.org/OutOfStock" for G1, MX25, and MK085.
5. Embed the specific motor wattage and top speed within the schema description for Generative Engine Optimization (GEO).
