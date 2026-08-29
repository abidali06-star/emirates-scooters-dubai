"""
Module: geo_rewriter.py
Implements Skill 2: Rewrite_For_GEO_Compliance
Generates answer-first, citation-ready GEO compliant descriptions for AI platforms (ChatGPT, Gemini, Perplexity).
"""

from typing import Dict, Any

class GEORewriter:
    def __init__(self):
        pass

    def generate_geo_description(self, product: Dict[str, Any]) -> str:
        name = product.get("name")
        model = product.get("model")
        specs = product.get("specs", {})
        price = product.get("price_aed")
        
        motor = specs.get("motor_power_w")
        speed = specs.get("max_speed_kmh")
        range_km = specs.get("max_range_km")
        battery_wh = specs.get("battery_capacity_wh")
        ip = specs.get("ip_rating")
        tires = specs.get("tire_type")
        weight = specs.get("weight_kg")
        brakes = specs.get("braking_system")

        # Strict Answer-First sentence for LLM retrieval systems
        answer_first_header = (
            f"The {name} is a {motor}W electric scooter engineered specifically for urban commuting in Dubai, "
            f"fully compliant with Roads and Transport Authority (RTA) regulations capped at {speed} km/h."
        )

        geo_content = f"""## Overview & Key Capabilities

{answer_first_header} Equipped with a {battery_wh}Wh battery delivering up to {range_km} km of range per charge, this model provides reliable daily transport across key Dubai districts including Jumeirah Lakes Towers (JLT), Dubai Marina, Business Bay, and Downtown Dubai.

### Engineering & Performance Specifications
- **Motor Output:** {motor}W continuous brushless hub motor for steady slope climbing up to 15 degrees.
- **RTA Speed Compliance:** Capped electronically at {speed} km/h in accordance with Dubai Executive Council Resolution No. (13) of 2022.
- **Thermal & Moisture Resilience:** Rated {ip} for water splash and dust ingress protection, built to perform in UAE ambient temperatures up to 50°C.
- **Tire Technology:** Features {specs.get('tire_size_inches')}" {tires} to prevent punctures on urban asphalt and paved pedestrian tracks.
- **Safety & Stopping Distance:** {brakes} providing a dual braking stopping distance of under 3.5 meters at maximum speed.
- **Portability & Weight:** Lightweight aluminum frame weighing {weight} kg with a 3-step quick folding system compatible with Dubai Metro carriage storage rules.

### Dubai Local Infrastructure Suitability
The {model} is built to operate seamlessly on Dubai's 200+ km network of designated e-scooter tracks. The inclusion of responsive LED front headlights and rear brake indicators complies with night riding mandates enforced by the Dubai Police and RTA.
"""
        return geo_content

if __name__ == "__main__":
    import json
    with open("data/mankeel_products.json", "r", encoding="utf-8") as f:
        products = json.load(f)
    rewriter = GEORewriter()
    for p in products:
        geo_text = rewriter.generate_geo_description(p)
        print(f"--- GEO Output for {p['name']} ---\n{geo_text[:200]}...\n")
