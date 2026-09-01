"""
Module: merchant_center_feed.py
Generates Google Merchant Center RSS 2.0 XML product feed for Google Shopping and AI Commerce assistants.
"""

import os
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
from typing import Dict, Any

class MerchantCenterFeedGenerator:
    def __init__(self, products_path: str = "data/mankeel_products.json"):
        with open(products_path, "r", encoding="utf-8") as f:
            self.products = json.load(f)

    def generate_feed_xml(self) -> str:
        rss = ET.Element("rss", {
            "version": "2.0",
            "xmlns:g": "http://base.google.com/ns/1.0"
        })
        
        channel = ET.SubElement(rss, "channel")
        
        title = ET.SubElement(channel, "title")
        title.text = "Emirates E-Scooters Official Feed"
        
        link = ET.SubElement(channel, "link")
        link.text = "https://emirates-scooters-dubai.vercel.app"
        
        description = ET.SubElement(channel, "description")
        description.text = "Official product feed for Mankeel electric scooters in Dubai, UAE."

        for p in self.products:
            item = ET.SubElement(channel, "item")
            
            g_id = ET.SubElement(item, "g:id")
            g_id.text = p["sku"]
            
            g_title = ET.SubElement(item, "g:title")
            g_title.text = f"Mankeel {p['model']} Electric Scooter ({p['specs']['motor_power']}, {p['specs']['max_speed']})"
            
            g_desc = ET.SubElement(item, "g:description")
            g_desc.text = f"Buy Mankeel {p['model']} in Dubai. Motor: {p['specs']['motor_power']}, Speed: {p['specs']['max_speed']}, Range: {p['specs']['max_range']}, Battery: {p['specs']['battery']}. Free Dubai delivery."
            
            g_link = ET.SubElement(item, "g:link")
            g_link.text = f"https://emirates-scooters-dubai.vercel.app/products/{p['id']}"
            
            # Only emit image_link when a real image file exists. A 404 image_link
            # causes Merchant Center item disapproval.
            if p.get("image"):
                g_image = ET.SubElement(item, "g:image_link")
                g_image.text = f"https://emirates-scooters-dubai.vercel.app{p['image']}"
            
            g_condition = ET.SubElement(item, "g:condition")
            g_condition.text = "new"
            
            g_availability = ET.SubElement(item, "g:availability")
            g_availability.text = "in_stock" if p["inStock"] else "out_of_stock"
            
            g_price = ET.SubElement(item, "g:price")
            g_price.text = f"{p['price_aed']}.00 AED"
            
            g_brand = ET.SubElement(item, "g:brand")
            g_brand.text = "Mankeel"
            
            g_mpn = ET.SubElement(item, "g:mpn")
            g_mpn.text = p["sku"]
            
            g_category = ET.SubElement(item, "g:google_product_category")
            g_category.text = "Sporting Goods > Outdoor Recreation > Scooters > Electric Scooters"
            
            g_shipping = ET.SubElement(item, "g:shipping")
            g_country = ET.SubElement(g_shipping, "g:country")
            g_country.text = "AE"
            g_service = ET.SubElement(g_shipping, "g:service")
            g_service.text = "Standard Delivery"
            g_shipping_price = ET.SubElement(g_shipping, "g:price")
            g_shipping_price.text = "0.00 AED"

        rough_string = ET.tostring(rss, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")

    def export_feed_files(self, nextjs_public_dir: str = "src/nextjs/public", output_dir: str = "output") -> Dict[str, str]:
        os.makedirs(nextjs_public_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)
        
        xml_content = self.generate_feed_xml()
        paths = {
            "nextjs_feed_xml": f"{nextjs_public_dir}/google-merchant-feed.xml",
            "output_feed_xml": f"{output_dir}/google-merchant-feed.xml"
        }
        
        with open(paths["nextjs_feed_xml"], "w", encoding="utf-8") as f:
            f.write(xml_content)
        with open(paths["output_feed_xml"], "w", encoding="utf-8") as f:
            f.write(xml_content)
            
        return paths

if __name__ == "__main__":
    generator = MerchantCenterFeedGenerator()
    paths = generator.export_feed_files()
    print(f"Exported Google Merchant Center Feed XML:\n- {paths['nextjs_feed_xml']}\n- {paths['output_feed_xml']}")
