"""
Module: sitemap_robots_generator.py
Generates robots.txt (with explicit AI crawler permissions) and sitemap.xml for Google Search, ChatGPT, Gemini, and Perplexity.
"""

import os
import json
import time
from typing import Dict, Any

class SitemapRobotsGenerator:
    def _blog_slugs(self):
        """Reads the generated blog index; returns [] if the pipeline hasn't written it yet."""
        try:
            with open("src/nextjs/lib/data/blogs.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, ValueError):
            return []

    def __init__(self, products_path: str = "data/mankeel_products.json"):
        with open(products_path, "r", encoding="utf-8") as f:
            self.products = json.load(f)

    def generate_robots_txt(self) -> str:
        robots = """# Robots.txt for Emirates E-Scooters (https://emirates-scooters-dubai.vercel.app)

User-agent: *
Allow: /
Disallow: /api/

# OpenAI / ChatGPT
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

# Google Gemini / Extended AI
User-agent: Google-Extended
Allow: /

User-agent: Googlebot
Allow: /

# Perplexity AI
User-agent: PerplexityBot
Allow: /

# Anthropic Claude
User-agent: ClaudeBot
Allow: /

# Meta AI
User-agent: Meta-ExternalAgent
Allow: /

# Sitemaps & LLM Direct Feeds
Sitemap: https://emirates-scooters-dubai.vercel.app/sitemap.xml
"""
        return robots

    def generate_sitemap_xml(self) -> str:
        current_date = time.strftime("%Y-%m-%d")
        
        urls = [
            {"loc": "https://emirates-scooters-dubai.vercel.app", "priority": "1.0", "changefreq": "daily"},
            {"loc": "https://emirates-scooters-dubai.vercel.app/llms.txt", "priority": "0.9", "changefreq": "weekly"},
            # Blog URLs are read from lib/data/blogs.json so new guides appear in
            # the sitemap automatically. This list used to be hardcoded to three,
            # which silently left later guides out of the sitemap entirely.
            *[
                {"loc": f"https://emirates-scooters-dubai.vercel.app/blogs/{b['slug']}",
                 "priority": "0.8", "changefreq": "monthly"}
                for b in self._blog_slugs()
            ],
        ]
        
        for p in self.products:
            urls.append({
                "loc": f"https://emirates-scooters-dubai.vercel.app/products/{p['id']}",
                "priority": "0.9",
                "changefreq": "daily"
            })

        xml_lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        ]
        
        for u in urls:
            xml_lines.append("  <url>")
            xml_lines.append(f"    <loc>{u['loc']}</loc>")
            xml_lines.append(f"    <lastmod>{current_date}</lastmod>")
            xml_lines.append(f"    <changefreq>{u['changefreq']}</changefreq>")
            xml_lines.append(f"    <priority>{u['priority']}</priority>")
            xml_lines.append("  </url>")
            
        xml_lines.append("</urlset>")
        return "\n".join(xml_lines)

    def export_sitemap_and_robots(self, nextjs_public_dir: str = "src/nextjs/public", output_dir: str = "output") -> Dict[str, str]:
        os.makedirs(nextjs_public_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)
        
        robots = self.generate_robots_txt()
        sitemap = self.generate_sitemap_xml()
        
        paths = {
            "nextjs_robots": f"{nextjs_public_dir}/robots.txt",
            "nextjs_sitemap": f"{nextjs_public_dir}/sitemap.xml",
            "output_robots": f"{output_dir}/robots.txt",
            "output_sitemap": f"{output_dir}/sitemap.xml"
        }
        
        with open(paths["nextjs_robots"], "w", encoding="utf-8") as f:
            f.write(robots)
        with open(paths["nextjs_sitemap"], "w", encoding="utf-8") as f:
            f.write(sitemap)
        with open(paths["output_robots"], "w", encoding="utf-8") as f:
            f.write(robots)
        with open(paths["output_sitemap"], "w", encoding="utf-8") as f:
            f.write(sitemap)
            
        return paths

if __name__ == "__main__":
    generator = SitemapRobotsGenerator()
    paths = generator.export_sitemap_and_robots()
    print(f"Exported sitemap and robots.txt to:\n- {paths['nextjs_robots']}\n- {paths['nextjs_sitemap']}")
