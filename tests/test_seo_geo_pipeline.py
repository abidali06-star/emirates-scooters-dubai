"""
Unit and Integration Test Suite for Mankeel GEO & SEO Automation Pipeline (10/10 Readiness).
"""

import unittest
import os
import json
import subprocess
import sys
import xml.etree.ElementTree as ET

class TestGEOSEOPipeline(unittest.TestCase):
    
    def test_01_skills_exist(self):
        skills = [
            "skills/extract_and_structure_specs.json",
            "skills/rewrite_for_geo_compliance.json",
            "skills/generate_local_authority_hub.json"
        ]
        for skill_path in skills:
            self.assertTrue(os.path.exists(skill_path), f"Skill definition missing: {skill_path}")
            with open(skill_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.assertIn("name", data)
                self.assertIn("system_prompt", data)

    def test_02_product_data_valid(self):
        """Catalogue comes from the owner's spec sheet: MK083, MX-14, MK085, MX25, G1."""
        data_path = "data/mankeel_products.json"
        self.assertTrue(os.path.exists(data_path))
        with open(data_path, "r", encoding="utf-8") as f:
            products = json.load(f)
        self.assertCountEqual(
            [p["model"] for p in products],
            ["MK083", "MX-14", "MK085", "MX25", "G1"],
        )
        for p in products:
            self.assertIn("price_aed", p)
            self.assertIn("max_speed_kmh", p["specs"])
            self.assertIsInstance(p["inStock"], bool)

    def test_03_pipeline_execution(self):
        result = subprocess.run([sys.executable, "run_all.py"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, f"run_all.py failed with stdout:\n{result.stdout}\nstderr:\n{result.stderr}")
        self.assertIn("Completed Successfully", result.stdout)

    def test_04_verify_generated_outputs(self):
        product_files = [
            "output/products/mx-14.html",
            "output/products/mk083.html"
        ]
        for pf in product_files:
            self.assertTrue(os.path.exists(pf), f"Generated product file missing: {pf}")
            with open(pf, "r", encoding="utf-8") as f:
                content = f.read()
                self.assertIn('application/ld+json', content)
                self.assertIn('mankeel-specs-table', content)

        blog_files = [
            "output/blogs/rta-e-scooter-permit-dubai.html",
            "output/blogs/battery-maintenance-uae-summer.html",
            "output/blogs/best-e-scooter-tracks-dubai.html",
            "output/blogs/best-electric-scooters-dubai-comparison.html",
            "output/blogs/best-electric-scooter-dubai-metro-commute.html",
            "output/blogs/puncture-proof-vs-pneumatic-tires-dubai.html",
            "output/blogs/best-off-road-scooters-dubai-under-1500-aed.html"
        ]
        for bf in blog_files:
            self.assertTrue(os.path.exists(bf), f"Generated blog file missing: {bf}")
            with open(bf, "r", encoding="utf-8") as f:
                content = f.read()
                self.assertIn('FAQPage', content)
                self.assertIn('Frequently Asked Questions', content)

    def test_05_part2_gbp_manifest_valid(self):
        gbp_path = "output/reports/gbp_bilingual_setup_manifest.json"
        self.assertTrue(os.path.exists(gbp_path), f"GBP manifest missing: {gbp_path}")
        with open(gbp_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertIn("local_business_schema", data)
            self.assertIn("bilingual_posts", data)

            schema = data["local_business_schema"]
            # Emirates E-Scooters is a SERVICE AREA BUSINESS: delivery only, no
            # premises open to the public. The schema must therefore never carry
            # a street address or geo coordinates, and must carry areaServed.
            # Publishing an address for a business with no premises is what gets
            # a Google listing suspended.
            self.assertEqual(schema["@type"], "LocalBusiness")
            self.assertNotIn("streetAddress", schema.get("address", {}),
                             "Service area business must not publish a street address")
            self.assertNotIn("geo", schema,
                             "Service area business must not publish geo coordinates")
            self.assertIn("areaServed", schema)
            self.assertTrue(schema["areaServed"], "areaServed must not be empty")

    def test_06_part2_offsite_citations_valid(self):
        citations_path = "output/reports/offsite_citations_sentiment_manifest.json"
        self.assertTrue(os.path.exists(citations_path), f"Citations manifest missing: {citations_path}")
        with open(citations_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertIn("aggregate_rating_schema", data)
            self.assertIn("consensus_faqs", data)

            # The manifest must NEVER carry rating schema that isn't backed by
            # verified, observed review data. When no citations are verified yet,
            # aggregate_rating_schema is null and consensus_faqs is empty --
            # that is the correct, policy-compliant state, not a failure.
            rating = data["aggregate_rating_schema"]
            if rating is None:
                self.assertEqual(data["status"], "no_verified_citations_yet")
                self.assertEqual(data["consensus_faqs"], [])
            else:
                self.assertEqual(rating["@type"], "AggregateRating")
                # Any published rating must cite where each number came from.
                self.assertIn("_provenance", rating)
                self.assertTrue(rating["_provenance"], "Rating published with no provenance")
                counted = sum(int(p["observed_review_count"]) for p in rating["_provenance"])
                self.assertEqual(int(rating["ratingCount"]), counted,
                                 "ratingCount must equal the sum of observed review counts")

    def test_07_nextjs_server_components_valid(self):
        layout_path = "src/nextjs/app/layout.tsx"
        product_page_path = "src/nextjs/app/products/[slug]/page.tsx"
        data_json_path = "src/nextjs/lib/data/products.json"
        
        self.assertTrue(os.path.exists(layout_path), f"Next.js Root Layout missing: {layout_path}")
        self.assertTrue(os.path.exists(product_page_path), f"Next.js Product Page missing: {product_page_path}")
        self.assertTrue(os.path.exists(data_json_path), f"Next.js product database JSON missing: {data_json_path}")
        
        with open(data_json_path, "r", encoding="utf-8") as f:
            products = json.load(f)
        with open("data/mankeel_products.json", "r", encoding="utf-8") as f:
            source = json.load(f)
        published = [p for p in source if p.get("inStock")]
        # Only in-stock models are published (owner decision 2026-09-02). Out-of-stock
        # models stay in the source catalogue but must not reach the site.
        self.assertEqual(len(products), len(published),
                         "Next.js product data must contain exactly the in-stock models")
        self.assertTrue(all(p["inStock"] for p in products),
                        "An out-of-stock model reached the published product data")
            
        with open(layout_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("dangerouslySetInnerHTML", content)
            self.assertIn("metadataBase", content)
            
        with open(product_page_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("generateMetadata", content)
            self.assertIn("dangerouslySetInnerHTML", content)
            self.assertIn("In Stock", content)

    def test_08_llms_txt_valid(self):
        llms_path = "src/nextjs/public/llms.txt"
        self.assertTrue(os.path.exists(llms_path), f"llms.txt missing: {llms_path}")
        with open(llms_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Mankeel MX-14", content)
            # Must state the RTA position factually and must never claim a status
            # we don't hold (RTA certification / authorised dealer).
            self.assertIn("RTA", content)
            self.assertIn("20 km/h", content)
            for forbidden in ("RTA certified", "RTA approved", "RTA Authorized Dealer",
                              "RTA Authorised Dealer"):
                self.assertNotIn(forbidden, content,
                                 f"llms.txt must not claim: {forbidden}")

    def test_09_merchant_feed_xml_valid(self):
        feed_path = "src/nextjs/public/google-merchant-feed.xml"
        self.assertTrue(os.path.exists(feed_path), f"Merchant feed XML missing: {feed_path}")
        tree = ET.parse(feed_path)
        root = tree.getroot()
        items = root.findall(".//item")
        with open("data/mankeel_products.json", "r", encoding="utf-8") as f:
            source = json.load(f)
        published = [p for p in source if p.get("inStock")]
        self.assertEqual(len(items), len(published),
                         "Merchant feed must list exactly the in-stock models")

    def test_10_sitemap_and_robots_valid(self):
        robots_path = "src/nextjs/public/robots.txt"
        sitemap_path = "src/nextjs/public/sitemap.xml"
        self.assertTrue(os.path.exists(robots_path))
        self.assertTrue(os.path.exists(sitemap_path))
        
        with open(robots_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("GPTBot", content)
            self.assertIn("Google-Extended", content)
            self.assertIn("PerplexityBot", content)

    def test_11_no_unsupported_comparison_claims(self):
        """
        Comparison claims must be traceable to data/competitor_benchmark.json,
        which records observed UAE retail prices. The site previously claimed
        "30-40% better value" with no competitor data behind it; the real gap is
        about 20% on the MX-14 and roughly nil on the MK083.
        """
        banned = ["30% to 40%", "30-40%", "30–40%", "Unbeatable Value"]
        targets = [
            "src/nextjs/public/llms.txt",
            "src/nextjs/public/llms-full.txt",
            "src/nextjs/app/page.tsx",
        ]
        for path in targets:
            if not os.path.exists(path):
                continue
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            for phrase in banned:
                self.assertNotIn(phrase, content,
                                 f"Unsupported comparison claim '{phrase}' found in {path}")

        self.assertTrue(os.path.exists("data/competitor_benchmark.json"),
                        "Comparison claims require a benchmark file with observed prices")

    def test_12_published_surfaces_are_in_stock_only(self):
        """Out-of-stock models must not reach the sitemap or the merchant feed."""
        with open("data/mankeel_products.json", "r", encoding="utf-8") as f:
            source = json.load(f)
        out_of_stock = [p["id"] for p in source if not p.get("inStock")]

        with open("src/nextjs/public/sitemap.xml", "r", encoding="utf-8") as f:
            sitemap = f.read()
        for pid in out_of_stock:
            self.assertNotIn(f"/products/{pid}", sitemap,
                             f"Out-of-stock model {pid} is in the sitemap")

        with open("src/nextjs/public/llms.txt", "r", encoding="utf-8") as f:
            llms = f.read()
        self.assertNotIn("Out of Stock", llms,
                         "llms.txt should only advertise in-stock models")


if __name__ == "__main__":
    unittest.main()
