"""
Module: specs_processor.py
Implements Skill 1: Extract_And_Structure_Specs
Converts product specification data into semantic HTML tables and validated JSON-LD Product schema.
"""

import json
from typing import Dict, Any

class SpecsProcessor:
    def __init__(self):
        pass

    def build_html_table(self, product: Dict[str, Any]) -> str:
        specs = product.get("specs", {})
        
        table_rows = [
            f"<tr><th>Parameter</th><th>Specification Details</th></tr>",
            f"<tr><td>Motor Power</td><td>{specs.get('motor_power', str(specs.get('motor_power_w', '')) + 'W')}</td></tr>",
            f"<tr><td>Top Speed</td><td>{specs.get('max_speed', str(specs.get('max_speed_kmh', '')) + ' KMH')}</td></tr>",
            f"<tr><td>Battery Capacity & Voltage</td><td>{specs.get('battery')}</td></tr>",
            f"<tr><td>Maximum Range</td><td>{specs.get('max_range')}</td></tr>",
            f"<tr><td>Tire Type & Dimensions</td><td>{specs.get('tire')}</td></tr>",
            f"<tr><td>Charge Duration</td><td>{specs.get('charge_time')}</td></tr>",
            f"<tr><td>Scooter Weight</td><td>{specs.get('weight')}</td></tr>",
            f"<tr><td>Max Carrying Capacity</td><td>{specs.get('max_load')}</td></tr>",
            f"<tr><td>Braking Mechanism</td><td>{specs.get('braking_system')}</td></tr>",
            f"<tr><td>Stock Status</td><td>{'In Stock' if product.get('inStock') else 'Out of Stock'}</td></tr>"
        ]
        
        html_table = (
            f'<div class="specs-table-container">\n'
            f'  <table class="mankeel-specs-table" aria-label="Technical Specifications for {product.get("name")}">\n'
            f'    <thead>\n'
            f'      <tr>\n'
            f'        <th scope="col">Feature Category</th>\n'
            f'        <th scope="col">Engineered Specification</th>\n'
            f'      </tr>\n'
            f'    </thead>\n'
            f'    <tbody>\n'
            + "\n".join(f"      {row}" for row in table_rows[1:]) + "\n"
            f'    </tbody>\n'
            f'  </table>\n'
            f'</div>'
        )
        return html_table

    def build_jsonld_schema(self, product: Dict[str, Any]) -> Dict[str, Any]:
        specs = product.get("specs", {})
        availability = "https://schema.org/InStock" if product.get("inStock") else "https://schema.org/OutOfStock"
        
        schema = {
            "@context": "https://schema.org/",
            "@type": "Product",
            "name": f"Mankeel {product.get('model', product.get('name'))}",
            "image": f"https://emirates-scooters-dubai.vercel.app/images/products/{product.get('id')}.jpg",
            "description": f"Official Mankeel {product.get('model')} electric scooter in Dubai featuring a {specs.get('motor_power')} motor and top speed of {specs.get('max_speed')}. Range: {specs.get('max_range')}.",
            "sku": product.get("sku"),
            "mpn": product.get("sku"),
            "brand": {
                "@type": "Brand",
                "name": product.get("brand", "Mankeel")
            },
            "offers": {
                "@type": "Offer",
                "url": f"https://emirates-scooters-dubai.vercel.app/products/{product.get('id')}",
                "priceCurrency": product.get("currency", "AED"),
                "price": product.get("price_aed"),
                "priceValidUntil": "2027-12-31",
                "itemCondition": "https://schema.org/NewCondition",
                "availability": availability,
                "seller": {
                    "@type": "Organization",
                    "name": "Emirates E-Scooters"
                }
            },
            "additionalProperty": [
                {
                    "@type": "PropertyValue",
                    "name": "Motor Power",
                    "value": str(specs.get("motor_power"))
                },
                {
                    "@type": "PropertyValue",
                    "name": "Top Speed",
                    "value": str(specs.get("max_speed"))
                },
                {
                    "@type": "PropertyValue",
                    "name": "Battery Range",
                    "value": str(specs.get("max_range"))
                }
            ]
        }
        return schema

if __name__ == "__main__":
    with open("data/mankeel_products.json", "r", encoding="utf-8") as f:
        products = json.load(f)
    processor = SpecsProcessor()
    for p in products:
        table = processor.build_html_table(p)
        schema = processor.build_jsonld_schema(p)
        print(f"Processed {p['name']} -> Table length: {len(table)}, Availability: {schema['offers']['availability']}")
