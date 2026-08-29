"""
Module: authority_hub_generator.py
Implements Skill 3: Generate_Local_Authority_Hub
Generates local Dubai topical authority content and embeds valid FAQPage JSON-LD schema markup.
"""

import json
from typing import Dict, Any, List

class AuthorityHubGenerator:
    def __init__(self):
        pass

    def generate_rta_permit_guide(self) -> Dict[str, Any]:
        title = "Complete Guide: How to Get an RTA E-Scooter Permit in Dubai (2026)"
        slug = "rta-e-scooter-permit-dubai"
        description = "Step-by-step guide to applying for a free Dubai RTA e-scooter driver permit online, legal requirements, designated tracks, and fines."
        
        faqs = [
            {
                "question": "Is an RTA permit mandatory for riding an e-scooter in Dubai?",
                "answer": "Yes. An RTA permit is mandatory for riding an e-scooter on designated Dubai streets and shared tracks unless you hold a valid UAE driver's license or international driving permit."
            },
            {
                "question": "How much does the Dubai RTA e-scooter permit cost?",
                "answer": "The RTA e-scooter permit is 100% free of charge and can be obtained instantly online through the official RTA website after passing an awareness test."
            },
            {
                "question": "What is the minimum age to get an e-scooter permit in Dubai?",
                "answer": "Riders must be at least 16 years of age to apply for an RTA e-scooter permit and operate an electric scooter in Dubai."
            },
            {
                "question": "What is the fine for riding an e-scooter without a permit in Dubai?",
                "answer": "Riding an electric scooter without a permit or valid driver's license carries an official fine of AED 300 imposed by the Dubai Police and RTA."
            }
        ]

        content_markdown = """# Complete Guide: How to Get an RTA E-Scooter Permit in Dubai

## Overview of Dubai RTA E-Scooter Regulations
Under Dubai Executive Council Resolution No. (13) of 2022, operating an electric scooter on designated roads and tracks in Dubai requires an official **RTA Electric Scooter Driving Permit**. The regulation ensures road safety and protects riders across high-density urban areas like **Jumeirah Lakes Towers (JLT)**, **Dubai Marina**, **Business Bay**, and **Downtown Dubai**.

---

## Who Needs an RTA E-Scooter Permit?
- **Mandatory for:** Individuals aged 16 and older who do **not** possess a UAE Driving License.
- **Exempt from Permit:** Anyone holding a valid UAE Driving License or an approved International Driving Permit.

> **Important:** Riding on non-designated tracks or without a valid permit incurs an immediate **AED 300 fine** enforced by Dubai Police.

---

## Step-by-Step Guide to Applying for your Free RTA Permit

1. **Visit the Official RTA Portal:** Navigate to `learn.rta.ae` or the main RTA Dubai online services portal.
2. **Login with UAE PASS:** Authenticate your identity using your UAE PASS credentials.
3. **Complete the Online Awareness Training Course:** Complete a short 20-minute educational module covering traffic signs, speed limits (capped at 25 km/h), helmet rules, and track safety.
4. **Pass the Multiple-Choice Safety Test:** Answer questions regarding emergency braking, right of way, and night light requirements.
5. **Instant Permit Download:** Upon achieving a passing score, your digital RTA E-Scooter Permit will be generated instantly as a PDF. Save it on your mobile device.

---

## Essential Safety Rules for Dubai Scooter Riders
- **Maximum Speed Limit:** 25 km/h on dedicated tracks; 15-20 km/h in shared pedestrian zones.
- **Protective Gear:** Helmets and reflective vests are legally mandatory during night rides.
- **Equipment Requirements:** Front white light, rear red reflector/brake light, functional bell, and dual braking systems (as featured on all Mankeel scooters).
"""
        return {
            "title": title,
            "slug": slug,
            "description": description,
            "faqs": faqs,
            "content": content_markdown
        }

    def generate_battery_maintenance_guide(self) -> Dict[str, Any]:
        title = "E-Scooter Battery Maintenance in UAE Summer Heat (45°C+ Guide)"
        slug = "battery-maintenance-uae-summer"
        description = "Essential guide to preserving e-scooter lithium battery health, preventing thermal degradation, and optimizing range in extreme Dubai summer heat."

        faqs = [
            {
                "question": "Does extreme heat damage electric scooter batteries in Dubai?",
                "answer": "Yes, temperatures exceeding 40°C cause chemical degradation in lithium-ion battery cells. Storing or charging scooters in direct sunlight leads to capacity loss and thermal stress."
            },
            {
                "question": "Can I charge my e-scooter immediately after riding in Dubai summer?",
                "answer": "No. Always allow the battery to cool down indoors for 30 to 45 minutes before plugging in the charger to prevent cell overheating."
            },
            {
                "question": "What is the safest indoor temperature for storing an e-scooter in UAE?",
                "answer": "Ideal indoor storage temperatures range between 20°C and 25°C in air-conditioned environments."
            }
        ]

        content_markdown = """# E-Scooter Battery Maintenance in UAE Summer Heat (45°C+ Guide)

## Understanding Thermal Stress on Lithium Batteries
Dubai summer temperatures routinely exceed **45°C**, with surface pavement temperatures reaching up to **65°C**. For electric scooter owners riding Mankeel models, thermal management is vital to maintaining peak range (35–55 km) and preventing premature battery wear.

---

## 5 Golden Rules for Summer E-Scooter Maintenance in Dubai

### 1. Never Charge a Hot Battery
After commuting across Dubai Marina or Business Bay, your scooter's lithium cells will retain internal friction heat. 
* **Protocol:** Wait 30–45 minutes in an air-conditioned room before plugging in your charger.

### 2. Avoid Direct Sunlight Parking
Parking your scooter exposed to direct UAE sun rapidly increases internal battery housing temperatures past safe operating thresholds.
* **Protocol:** Utilize covered parking facilities or bring your lightweight scooter (e.g., Mankeel MX-14 at 14.2 kg) inside your apartment or office.

### 3. Maintain 20% to 80% State of Charge (SoC)
Extreme charge states (0% or 100%) during high heat accelerate battery cell breakdown.
* **Protocol:** Charge your scooter to 80-90% for daily rides and never leave it plugged in overnight unattended.

### 4. Inspect Moisture & IP Rating Integrity
Summer humidity in coastal Dubai can reach 90%. Ensure your scooter's **IPX5/IP54 ingress seal** is clean and free of sand debris.

### 5. Check Tire Pressure Regularly
Hot asphalt expands air in pneumatic tires. Keep tires inflated to manufacturer specifications (36-40 PSI) to minimize rolling resistance and battery drain.
"""
        return {
            "title": title,
            "slug": slug,
            "description": description,
            "faqs": faqs,
            "content": content_markdown
        }

    def generate_tracks_guide(self) -> Dict[str, Any]:
        title = "Top 7 Best E-Scooter Tracks & Designated Zones in Dubai (2026)"
        slug = "best-e-scooter-tracks-dubai"
        description = "Discover Dubai's top rated e-scooter tracks: JLT, Dubai Water Canal, Downtown, City Walk, Nad Al Sheba, and Business Bay."

        faqs = [
            {
                "question": "Where can I legally ride an e-scooter in Dubai?",
                "answer": "You can legally ride e-scooters on designated RTA tracks in 10 major districts including Jumeirah Lakes Towers (JLT), Dubai Marina, Business Bay, Downtown Dubai, City Walk, Dubai Water Canal, and Al Rigga."
            },
            {
                "question": "Are e-scooters allowed on Dubai Metro trains?",
                "answer": "RTA allows folded non-motorized and compact folded electric scooters on Dubai Metro trains inside dedicated luggage compartments outside peak rush hours."
            }
        ]

        content_markdown = """# Top 7 Best E-Scooter Tracks & Designated Zones in Dubai

## 1. Jumeirah Lakes Towers (JLT) Loop
- **Track Distance:** 55 km of continuous promenade loops surrounding Cluster A to Cluster Z.
- **Highlights:** Fully paved, pedestrian-separated pathways with abundant charging points and cafe access. Perfect for Mankeel MK083 P1 commuters.

## 2. Dubai Water Canal Promenade
- **Track Distance:** 12 km scenic waterfront path extending from Business Bay to Jumeirah Beach.
- **Highlights:** Dedicated smooth asphalt track, nighttime LED illumination, breathtaking skyline views.

## 3. Business Bay & Downtown Boulevard
- **Track Distance:** 7 km urban track connecting Sheikh Mohammed bin Rashid Blvd and Dubai Mall Metro.
- **Highlights:** Ideal for last-mile connectivity between metro hubs and financial offices.

## 4. City Walk Dedicated Mobility Corridor
- **Track Distance:** 4.5 km ultra-modern red-surfaced track.
- **Highlights:** Wide lanes, shaded walkways, excellent surface grip.

## 5. Dubai Marina Walk
- **Track Distance:** 7 km perimeter loop around the Marina basin.
- **Highlights:** High foot-traffic zone requiring adherence to the 15 km/h pedestrian speed threshold.

## 6. Al Qudra & Nad Al Sheba Park Connectors
- **Track Distance:** Dedicated fitness tracks with long straightaways.
- **Highlights:** Excellent for long-range battery testing (e.g. Mankeel MX-14 55 km range).
"""
        return {
            "title": title,
            "slug": slug,
            "description": description,
            "faqs": faqs,
            "content": content_markdown
        }

    def build_faq_schema(self, faqs: List[Dict[str, str]]) -> Dict[str, Any]:
        main_entities = []
        for faq in faqs:
            main_entities.append({
                "@type": "Question",
                "name": faq["question"],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": faq["answer"]
                }
            })
        return {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": main_entities
        }

if __name__ == "__main__":
    generator = AuthorityHubGenerator()
    guide1 = generator.generate_rta_permit_guide()
    schema1 = generator.build_faq_schema(guide1["faqs"])
    print(f"Generated Guide: {guide1['title']} with {len(guide1['faqs'])} FAQs. Schema: {schema1['@type']}")
