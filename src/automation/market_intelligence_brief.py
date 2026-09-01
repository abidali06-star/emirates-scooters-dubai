"""
Module: market_intelligence_brief.py

IMPORTANT - behaviour change (2026-09-02)
-----------------------------------------
The previous version of this module invented its entire contents. It reported
"Top 3 Keyword Dominance: 92% (up +8% week-over-week)", "Generative AI Citation
Share: 87%", "#1 on Google Dubai", and "Captured Featured Snippet position 0" -
for a site that has never been measured, has no Search Console property, and had
just been published. None of it was real.

The brief now reports only what can be derived from the repo itself: what is
published, what is in stock, and what still needs to be checked by hand. It
contains no rankings, no citation share and no trend figures, because none are
measured. If real measurement is added later, put observed values here with the
date they were observed.
"""

import json
import time
from typing import Dict, Any, List


class MarketIntelligenceReporter:
    def __init__(self,
                 products_path: str = "data/mankeel_products.json",
                 blogs_path: str = "src/nextjs/lib/data/blogs.json"):
        with open(products_path, "r", encoding="utf-8") as f:
            self.products = json.load(f)
        try:
            with open(blogs_path, "r", encoding="utf-8") as f:
                self.blogs = json.load(f)
        except (FileNotFoundError, ValueError):
            self.blogs = []

    def generate_daily_brief(self) -> str:
        today = time.strftime("%Y-%m-%d")
        in_stock = [p for p in self.products if p.get("inStock")]
        out_stock = [p for p in self.products if not p.get("inStock")]

        lines = [
            "# Site Status Brief - Emirates E-Scooters",
            f"**Generated:** {today}",
            "",
            "> This brief reports what is **published**, not how it is **performing**.",
            "> No rankings, citation share or traffic figures appear here because none are",
            "> measured - there is no Search Console property and no SERP API configured.",
            "> Anything claiming otherwise would be invented. See",
            "> `output/reports/manual_checks_worklist.json` for the queries to check by hand.",
            "",
            "---",
            "",
            "## Published catalogue",
            "",
            f"- **In stock and published: {len(in_stock)}**",
        ]
        for p in in_stock:
            s = p["specs"]
            img = "image" if p.get("image") else "NO IMAGE"
            lines.append(
                f"  - Mankeel {p['model']} - {p['price_aed']:,} AED - "
                f"{s.get('motor_power')}, {s.get('max_speed')}, {s.get('max_range')} range ({img})"
            )
        lines += [
            "",
            f"- **Out of stock, held back from publication: {len(out_stock)}** "
            f"({', '.join(p['model'] for p in out_stock) if out_stock else 'none'})",
            "  - These are excluded from the sitemap, merchant feed, llms.txt and product",
            "    routes by design. They return to publication automatically when `inStock`",
            "    is set true in `data/mankeel_products.json`.",
            "",
            "## Published content",
            "",
            f"- Guides live: **{len(self.blogs)}**",
        ]
        for b in self.blogs:
            lines.append(f"  - `/blogs/{b['slug']}` ({len(b.get('faqs', []))} FAQs)")

        lines += [
            "",
            "## What is NOT known",
            "",
            "- Whether any page ranks for anything.",
            "- Whether any AI engine cites the site.",
            "- How much traffic the site receives.",
            "- Whether Google has indexed the sitemap at all.",
            "",
            "These are unmeasured, not zero and not good. Checking them is a manual task;",
            "the worklist is in `output/reports/manual_checks_worklist.json`.",
            "",
            "## Next actions that do not require any account",
            "",
            "1. Run the worklist queries in Google, ChatGPT, Gemini and Perplexity. Record",
            "   which sources they cite - that observed list is the real outreach target.",
            "2. Publish another guide. Content is the one channel fully open.",
            "3. Ask genuine buyers for reviews. No incentives.",
            "",
        ]
        return "\n".join(lines)


if __name__ == "__main__":
    print(MarketIntelligenceReporter().generate_daily_brief()[:800])
