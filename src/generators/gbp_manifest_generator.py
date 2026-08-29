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
            "image": "TO_CONFIRM: real photo of the Motor City storefront, hosted on the production domain",
            "telephone": nap["phone"],
            "url": self.profile.get("website_url", "TO_CONFIRM"),
            "description": desc_en,
            "address": {
                "@type": "PostalAddress",
                "streetAddress": f"{nap['store_number']}, {nap['building_name']}, {nap['area']}",
                "addressLocality": nap["city"],
                "addressRegion": nap["emirate"],
                "addressCountry": nap.get("country_code", "AE")
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": nap["geo_coordinates"]["latitude"],
                "longitude": nap["geo_coordinates"]["longitude"]
            },
            # Hours confirmed by the owner 2026-08-29: 08:00-22:00, all seven days.
            "openingHoursSpecification": [
                {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday",
                                  "Friday", "Saturday", "Sunday"],
                    "opens": "08:00",
                    "closes": "22:00"
                }
            ],
            "areaServed": self.profile["neighborhood_coverage"]
        }
        return schema

    def generate_bilingual_posts(self) -> Dict[str, Any]:
        posts = [
            {
                "topic": "RTA Compliance",
                "title_en": "Riding Your Mankeel Scooter Legally in Dubai",
                "title_ar": "قيادة سكوتر مانكيل بشكل قانوني في دبي",
                "body_en": "Riding in Motor City, Sports City or JVC? Every Mankeel scooter we sell ships with dual braking and is set up for Dubai's designated e-scooter tracks. Ask us in store about RTA permit requirements.",
                "body_ar": "هل تتنقل في موتور سيتي أو سبورتس سيتي أو قرية جميرا الدائرية؟ جميع سكوترات مانكيل لدينا مزودة بنظام فرامل مزدوج ومهيأة للمسارات المخصصة في دبي. اسألنا في المتجر عن اشتراطات تصريح هيئة الطرق والمواصلات."
            },
            {
                "topic": "Summer Maintenance Protocol",
                "title_en": "Protect Your Scooter Battery in UAE Summer Heat",
                "title_ar": "احمِ بطارية السكوتر في حرارة الصيف بدبي",
                "body_en": "Keep your battery in peak condition during 45°C+ summer heat. Visit our Motor City store for free battery thermal diagnostic checks.",
                "body_ar": "حافظ على كفاءة البطارية أثناء حرارة الصيف التي تتجاوز 45 درجة. تفضل بزيارة متجرنا في موتور سيتي لفحص بطاريتك مجاناً."
            }
        ]
        return {"gbp_posts": posts}

if __name__ == "__main__":
    generator = GBPManifestGenerator()
    schema = generator.generate_local_business_schema()
    posts = generator.generate_bilingual_posts()
    print(f"Generated LocalBusiness Schema for: {schema['name']}")
    print(f"Bilingual Posts Count: {len(posts['gbp_posts'])}")
