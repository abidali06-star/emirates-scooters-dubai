"""
Module: backlog_manager.py
Manages storing, archiving, and retrieving past published content, social posts, blogs, and SERP reports.
"""

import os
import json
from datetime import datetime
from typing import Dict, Any, List

BACKLOG_FILE = "data/content_backlog.json"

class BacklogManager:
    def __init__(self, filepath: str = BACKLOG_FILE):
        self.filepath = filepath
        self.ensure_file()

    def ensure_file(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        if not os.path.exists(self.filepath):
            initial_data = {
                "posts": [
                    {
                        "id": "post_1",
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "topic": "RTA Compliance",
                        "title_en": "Riding Your Mankeel Scooter Legally in Dubai",
                        "title_ar": "قيادة سكوتر مانكيل بشكل قانوني في دبي",
                        "body_en": "Riding in Motor City, Sports City or JVC? Every Mankeel scooter we sell ships with dual braking and is set up for Dubai's designated e-scooter tracks. Ask us about RTA permit requirements when we deliver.",
                        "body_ar": "هل تتنقل في موتور سيتي أو سبورتس سيتي أو قرية جميرا الدائرية؟ جميع سكوترات مانكيل لدينا مزودة بنظام فرامل مزدوج ومهيأة للمسارات المخصصة في دبي. اسألنا عن اشتراطات تصريح هيئة الطرق والمواصلات عند التوصيل.",
                        "target_models": ["MK083", "MX-14"],
                        "status": "Ready to Post"
                    },
                    {
                        "id": "post_2",
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "topic": "Summer Maintenance",
                        "title_en": "Protect Your Scooter Battery in UAE Summer Heat",
                        "title_ar": "احمِ بطارية السكوتر في حرارة الصيف بدبي",
                        "body_en": "Keep your battery in peak condition during 45°C+ summer heat. We offer free battery thermal diagnostic checks when we deliver or collect.",
                        "body_ar": "حافظ على كفاءة البطارية أثناء حرارة الصيف التي تتجاوز 45 درجة. نقدّم فحصاً مجانياً لحرارة البطارية عند التوصيل أو الاستلام.",
                        "target_models": ["MK083", "MX-14"],
                        "status": "Ready to Post"
                    }
                ],
                "blogs": [
                    {
                        "id": "blog_1",
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "title": "Complete Guide: How to Get an RTA E-Scooter Permit in Dubai (2026)",
                        "slug": "rta-e-scooter-permit-dubai",
                        "description": "Step-by-step guide to applying for a free Dubai RTA e-scooter driver permit online, legal requirements, designated tracks, and fines."
                    },
                    {
                        "id": "blog_2",
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "title": "E-Scooter Battery Maintenance in UAE Summer Heat (45°C+ Guide)",
                        "slug": "battery-maintenance-uae-summer",
                        "description": "Essential guide to preserving e-scooter lithium battery health, preventing thermal degradation, and optimizing range in extreme Dubai summer heat."
                    },
                    {
                        "id": "blog_3",
                        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        "title": "Top 7 Best E-Scooter Tracks & Designated Zones in Dubai (2026)",
                        "slug": "best-e-scooter-tracks-dubai",
                        "description": "Discover Dubai's top rated e-scooter tracks: JLT, Dubai Water Canal, Downtown, City Walk, Nad Al Sheba, and Business Bay."
                    }
                ],
                "reports": []
            }
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(initial_data, f, indent=2, ensure_ascii=False)

    def load(self) -> Dict[str, Any]:
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, data: Dict[str, Any]):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def add_post(self, topic: str, title_en: str, title_ar: str, body_en: str, body_ar: str, target_models: List[str] = None) -> Dict[str, Any]:
        data = self.load()
        if target_models is None:
            target_models = ["MK083", "MX-14"]
        new_item = {
            "id": f"post_{len(data['posts']) + 1}",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "topic": topic,
            "title_en": title_en,
            "title_ar": title_ar,
            "body_en": body_en,
            "body_ar": body_ar,
            "target_models": target_models,
            "status": "Ready to Post"
        }
        data["posts"].insert(0, new_item)
        self.save(data)
        return new_item

    def add_blog(self, title: str, slug: str, description: str) -> Dict[str, Any]:
        data = self.load()
        new_item = {
            "id": f"blog_{len(data['blogs']) + 1}",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "title": title,
            "slug": slug,
            "description": description
        }
        data["blogs"].insert(0, new_item)
        self.save(data)
        return new_item

    def add_report(self, title: str, summary: str) -> Dict[str, Any]:
        data = self.load()
        new_item = {
            "id": f"report_{len(data['reports']) + 1}",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "title": title,
            "summary": summary
        }
        data["reports"].insert(0, new_item)
        self.save(data)
        return new_item
