"""
Module: gbp_manifest_generator.py
Implements Section 2 of Part 2: Google Business Profile (GBP) & Local Maps Engine.
Generates LocalBusiness schema, bilingual GBP posts, and NAP consistency manifests.
"""

import json
from typing import Dict, Any

class GBPManifestGenerator:
    def __init__(self, profile_path: str = "data/dubai_gbp_profile.json"):
        with open(profile_path, "r", encoding="utf-8") as f:
            self.profile = json.load(f)

    def generate_local_business_schema(self) -> Dict[str, Any]:
        nap = self.profile["nap_data"]
        b_name = self.profile["business_name"]["en"]
        desc_en = self.profile["bilingual_descriptions"]["en"]
        
        schema = {
            "@context": "https://schema.org",
            "@type": "Store",
            "name": b_name,
            "image": "https://emirates-scooters.ae/images/storefront-jlt.jpg",
            "telephone": nap["phone"],
            "url": "https://emirates-scooters.ae",
            "description": desc_en,
            "address": {
                "@type": "PostalAddress",
                "streetAddress": f"{nap['unit']}, {nap['building_name']}, {nap['cluster_area']}",
                "addressLocality": nap["city"],
                "addressRegion": nap["emirate"],
                "postalCode": nap["postal_code"],
                "addressCountry": "AE"
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": nap["geo_coordinates"]["latitude"],
                "longitude": nap["geo_coordinates"]["longitude"]
            },
            "openingHoursSpecification": [
                {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                    "opens": "09:00",
                    "closes": "21:00"
                }
            ],
            "priceRange": "AED 1399 - AED 2299",
            "areaServed": self.profile["neighborhood_coverage"]
        }
        return schema

    def generate_bilingual_posts(self) -> Dict[str, Any]:
        posts = [
            {
                "topic": "RTA Compliance",
                "title_en": "Mankeel Scooters are 100% RTA Dubai Compliant!",
                "title_ar": "سكوترات مانكيل معتمدة 100% من هيئة الطرق والمواصلات بدبي!",
                "body_en": "Cruising in JLT, Marina, or Business Bay? All Mankeel scooters come pre-configured with 25 km/h speed governors and dual braking systems required by Dubai RTA.",
                "body_ar": "هل تتنقل في أبراج بحيرات جميرا، دبي مارينا، أو الخليج التجاري؟ جميع سكوترات مانكيل تأتي مجهزة بمحدد سرعة 25 كم/س ونظام فرامل مزدوج معتمد من هيئة الطرق والمواصلات."
            },
            {
                "topic": "Summer Maintenance Protocol",
                "title_en": "Protect Your Scooter Battery in UAE Summer Heat",
                "title_ar": "احمِ بطارية السكوتر في حرارة الصيف بدبي",
                "body_en": "Keep your battery in peak condition during 45°C+ summer heat. Visit our JLT store for free battery thermal diagnostic checks.",
                "body_ar": "حافظ على كفاءة البطارية أثناء حرارة الصيف التي تتجاوز 45 درجة. تفضل بزيارة متجرنا في أبراج بحيرات جميرا لفحص بطاريتك مجاناً."
            }
        ]
        return {"gbp_posts": posts}

if __name__ == "__main__":
    generator = GBPManifestGenerator()
    schema = generator.generate_local_business_schema()
    posts = generator.generate_bilingual_posts()
    print(f"Generated LocalBusiness Schema for: {schema['name']}")
    print(f"Bilingual Posts Count: {len(posts['gbp_posts'])}")
