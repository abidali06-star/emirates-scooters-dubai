"""
Master Pipeline Orchestrator for Emirates E-Scooters GEO & SEO Automation.
Executes Part 1, Part 2, Next.js Server Components, llms.txt AI crawler feeds, Google Merchant XML feeds, and Sitemap/Robots pipelines.
"""

import os
import json
from src.generators.specs_processor import SpecsProcessor
from src.generators.geo_rewriter import GEORewriter
from src.generators.authority_hub_generator import AuthorityHubGenerator
from src.generators.gbp_manifest_generator import GBPManifestGenerator
from src.automation.indexing_and_serp_monitor import SearchConsoleAndSERPMonitor
from src.automation.market_intelligence_brief import MarketIntelligenceReporter
from src.automation.n8n_webhook_automation import N8NWebhookAutomation
from src.automation.ai_citation_sentiment_engine import AICitationSentimentEngine
from src.generators.nextjs_schema_injector import NextJSSchemaInjector
from src.generators.llms_txt_generator import LLMsTxtGenerator
from src.generators.merchant_center_feed import MerchantCenterFeedGenerator
from src.generators.sitemap_robots_generator import SitemapRobotsGenerator

def ensure_directories():
    os.makedirs("output/products", exist_ok=True)
    os.makedirs("output/blogs", exist_ok=True)
    os.makedirs("output/reports", exist_ok=True)
    os.makedirs("src/nextjs/public", exist_ok=True)

def generate_product_html(product, html_table, geo_markdown, jsonld_schema):
    schema_str = json.dumps(jsonld_schema, indent=2)
    geo_html = geo_markdown.replace("## ", "<h2>").replace("### ", "<h3>")
    
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{product['name']} - Official Dubai Store | Emirates Scooters</title>
    <meta name="description" content="Buy {product['name']} in Dubai. Motor: {product['specs']['motor_power']}, Speed: {product['specs']['max_speed']}, Range: {product['specs']['max_range']}. Price: {product['price_aed']} AED.">
    <script type="application/ld+json">
{schema_str}
    </script>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #222; margin: 0; padding: 20px; max-width: 1000px; margin: 0 auto; }}
        header {{ background: #0f172a; color: white; padding: 30px; border-radius: 8px; margin-bottom: 20px; }}
        header h1 {{ margin: 0 0 10px 0; font-size: 2.2rem; }}
        .badge {{ background: #10b981; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold; display: inline-block; font-size: 0.9rem; }}
        .badge-out {{ background: #ef4444; color: white; padding: 5px 12px; border-radius: 20px; font-weight: bold; display: inline-block; font-size: 0.9rem; }}
        .price-tag {{ font-size: 1.8rem; font-weight: bold; color: #2563eb; margin: 15px 0; }}
        .specs-table-container {{ margin: 30px 0; overflow-x: auto; }}
        table.mankeel-specs-table {{ width: 100%; border-collapse: collapse; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; }}
        table.mankeel-specs-table th {{ background: #1e293b; color: white; padding: 14px 18px; text-align: left; }}
        table.mankeel-specs-table td {{ padding: 12px 18px; border-bottom: 1px solid #e2e8f0; }}
        table.mankeel-specs-table tr:nth-child(even) {{ background: #f1f5f9; }}
        .geo-content {{ background: #fff; padding: 20px; border: 1px solid #e2e8f0; border-radius: 8px; margin-top: 20px; }}
        .geo-content h2 {{ color: #0f172a; border-bottom: 2px solid #2563eb; padding-bottom: 8px; }}
        .geo-content h3 {{ color: #1e293b; margin-top: 20px; }}
        ul {{ padding-left: 20px; }}
        li {{ margin-bottom: 8px; }}
    </style>
</head>
<body>
    <header>
        <span class="{ 'badge' if product['inStock'] else 'badge-out' }">{ 'In Stock' if product['inStock'] else 'Out of Stock' }</span>
        <h1>{product['name']}</h1>
        <div class="price-tag">{product['price_aed']} {product['currency']}</div>
    </header>

    <main>
        <section class="geo-content">
            {geo_html}
        </section>

        <section>
            <h2>Technical Specifications Matrix</h2>
            {html_table}
        </section>
    </main>
</body>
</html>
"""
    return full_html

def generate_blog_html(guide, faq_schema):
    schema_str = json.dumps(faq_schema, indent=2)
    content_html = guide["content"].replace("# ", "<h1>").replace("## ", "<h2>").replace("### ", "<h3>").replace("---", "<hr>")
    
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{guide['title']}</title>
    <meta name="description" content="{guide['description']}">
    <script type="application/ld+json">
{schema_str}
    </script>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.7; color: #1e293b; max-width: 850px; margin: 0 auto; padding: 30px 20px; }}
        h1 {{ color: #0f172a; font-size: 2.3rem; margin-bottom: 10px; }}
        h2 {{ color: #1e293b; border-bottom: 2px solid #10b981; padding-bottom: 6px; margin-top: 30px; }}
        h3 {{ color: #334155; margin-top: 20px; }}
        blockquote {{ background: #ecfdf5; border-left: 5px solid #10b981; margin: 20px 0; padding: 15px 20px; font-weight: 500; }}
        .faq-section {{ background: #f8fafc; padding: 25px; border-radius: 8px; border: 1px solid #cbd5e1; margin-top: 40px; }}
        .faq-item {{ margin-bottom: 20px; }}
        .faq-question {{ font-weight: bold; color: #0f172a; font-size: 1.1rem; }}
        .faq-answer {{ margin-top: 5px; color: #334155; }}
    </style>
</head>
<body>
    <article>
        {content_html}
    </article>

    <section class="faq-section">
        <h2>Frequently Asked Questions (FAQ)</h2>
"""
    for faq in guide["faqs"]:
        full_html += f"""        <div class="faq-item">
            <div class="faq-question">Q: {faq['question']}</div>
            <div class="faq-answer">A: {faq['answer']}</div>
        </div>\n"""

    full_html += """    </section>
</body>
</html>
"""
    return full_html

def run_pipeline():
    print("=== Starting Mankeel E-Scooter GEO & SEO Master Automation Pipeline (Full 9.8/10 Stack) ===")
    ensure_directories()
    
    # 1. Load Product Data
    with open("data/mankeel_products.json", "r", encoding="utf-8") as f:
        products = json.load(f)

    specs_proc = SpecsProcessor()
    geo_rewriter = GEORewriter()
    generated_urls = []

    # 2. Phase 1: Product Overhaul
    print(f"\n--- Phase 1: Processing {len(products)} Official Product Pages ---")
    for prod in products:
        table_html = specs_proc.build_html_table(prod)
        jsonld_schema = specs_proc.build_jsonld_schema(prod)
        geo_copy = geo_rewriter.generate_geo_description(prod)
        
        page_html = generate_product_html(prod, table_html, geo_copy, jsonld_schema)
        out_path = f"output/products/{prod['id']}.html"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page_html)
        print(f"[OK] Generated Product Page: {out_path}")
        generated_urls.append(f"https://emirates-scooters-dubai.vercel.app/products/{prod['id']}")

    # 3. Phase 2: Topical Authority Hub
    print("\n--- Phase 2: Generating Local Authority Hubs ---")
    auth_gen = AuthorityHubGenerator()
    guides = [
        auth_gen.generate_rta_permit_guide(),
        auth_gen.generate_battery_maintenance_guide(),
        auth_gen.generate_tracks_guide()
    ]

    for g in guides:
        faq_schema = auth_gen.build_faq_schema(g["faqs"])
        blog_html = generate_blog_html(g, faq_schema)
        out_path = f"output/blogs/{g['slug']}.html"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(blog_html)
        print(f"[OK] Generated Blog/Guide Page: {out_path}")
        generated_urls.append(f"https://emirates-scooters-dubai.vercel.app/blogs/{g['slug']}")

    # 4. Part 2 - Section 1: Fast-Mode Website n8n Webhook Test Trigger
    print("\n--- Part 2 Section 1: Testing Fast-Mode n8n Webhook Automation ---")
    n8n = N8NWebhookAutomation()
    n8n_res = n8n.handle_product_update_payload({
        "id": "mx-14",
        "name": "Mankeel MX-14 Off-Road Electric Scooter"
    })
    print(f"[OK] n8n Webhook Trigger Result: Status {n8n_res['status']} ({len(n8n_res['actions_triggered'])} actions automated)")

    # 5. Part 2 - Section 2: Google Business Profile (GBP Maps Engine)
    print("\n--- Part 2 Section 2: Generating Google Business Profile (GBP) Local Maps Manifest ---")
    gbp_gen = GBPManifestGenerator()
    local_biz_schema = gbp_gen.generate_local_business_schema()
    gbp_posts = gbp_gen.generate_bilingual_posts()
    
    gbp_manifest_path = "output/reports/gbp_bilingual_setup_manifest.json"
    with open(gbp_manifest_path, "w", encoding="utf-8") as f:
        json.dump({"local_business_schema": local_biz_schema, "bilingual_posts": gbp_posts}, f, indent=2, ensure_ascii=False)
    print(f"[OK] GBP Bilingual Setup Manifest Saved to: {gbp_manifest_path}")

    # 6. Part 2 - Section 3: Off-Site Citations & AI Sentiment Engine
    print("\n--- Part 2 Section 3: Processing Off-Site Citations & AI Sentiment Consensus ---")
    sentiment_engine = AICitationSentimentEngine()

    # strict=False: emit nothing rather than fabricate. AggregateRating and
    # consensus FAQs are only produced once genuine, verified review data exists
    # in data/offsite_citations_registry.json. See Step3_OffSite_Citations_Playbook.md.
    agg_rating = sentiment_engine.generate_aggregate_rating_schema(strict=False)
    citation_faqs = sentiment_engine.generate_consensus_faqs(strict=False)
    outreach_worklist = sentiment_engine.generate_outreach_worklist()

    citation_manifest = {
        "status": "no_verified_citations_yet" if not agg_rating else "verified",
        "aggregate_rating_schema": agg_rating,
        "consensus_faqs": citation_faqs,
        "outreach_worklist": outreach_worklist,
        "publish_warning": (
            "Do not publish aggregate_rating_schema or consensus_faqs while they are "
            "null/empty. Inventing review counts violates Google structured data policy."
        ),
    }

    citation_manifest_path = "output/reports/offsite_citations_sentiment_manifest.json"
    with open(citation_manifest_path, "w", encoding="utf-8") as f:
        json.dump(citation_manifest, f, indent=2, ensure_ascii=False)
    print(f"[OK] Off-Site Citations Manifest Saved to: {citation_manifest_path}")
    if not agg_rating:
        print(f"[INFO] No rating schema emitted. {len(outreach_worklist)} citation prospects pending.")

    # 7. Next.js App Router Server Component Schema Injection Templates
    print("\n--- Generating Next.js App Router Server Component Templates (Server-Side Injection) ---")
    nextjs_injector = NextJSSchemaInjector()
    exported_nextjs = nextjs_injector.export_nextjs_files()
    print(f"[OK] Next.js Root Layout Component Saved: {exported_nextjs['layout_tsx']}")
    print(f"[OK] Next.js Product Page Component Saved: {exported_nextjs['product_page_tsx']}")

    # 8. Generative AI Search Engine Feed: llms.txt & llms-full.txt
    print("\n--- Generating Generative AI Knowledge Base Standard (llms.txt & llms-full.txt) ---")
    llms_gen = LLMsTxtGenerator()
    exported_llms = llms_gen.export_llms_files()
    print(f"[OK] llms.txt generated for ChatGPT / Gemini / Perplexity: {exported_llms['nextjs_llms_txt']}")

    # 9. Google Merchant Center XML Product Feed
    print("\n--- Generating Google Merchant Center RSS 2.0 XML Feed ---")
    merchant_gen = MerchantCenterFeedGenerator()
    exported_feed = merchant_gen.export_feed_files()
    print(f"[OK] Google Merchant Feed XML Saved: {exported_feed['nextjs_feed_xml']}")

    # 10. Sitemap.xml & Robots.txt with AI Crawlers Permission
    print("\n--- Generating Sitemap.xml & AI-Friendly Robots.txt ---")
    sitemap_gen = SitemapRobotsGenerator()
    exported_sitemap = sitemap_gen.export_sitemap_and_robots()
    print(f"[OK] robots.txt Saved: {exported_sitemap['nextjs_robots']}")
    print(f"[OK] sitemap.xml Saved: {exported_sitemap['nextjs_sitemap']}")

    # 11. Search Console Submission & Daily Market Intelligence Brief
    print("\n--- Submitting Indexing & Monitoring Dubai SERP ---")
    monitor = SearchConsoleAndSERPMonitor()
    indexing_res = monitor.submit_urls_for_indexing(generated_urls)
    print(f"[OK] Search Console Submission Status: {indexing_res['status_code']} OK ({indexing_res['total_submitted']} URLs)")
    
    serp_res = monitor.monitor_dubai_serp()
    print(f"[OK] Dubai SERP Monitoring Check: Verified {len(serp_res['rankings'])} target queries.")

    reporter = MarketIntelligenceReporter()
    brief = reporter.generate_daily_brief()
    brief_path = "output/reports/daily_market_intelligence_brief.md"
    with open(brief_path, "w", encoding="utf-8") as f:
        f.write(brief)
    print(f"[OK] Daily Brief Saved to: {brief_path}")

    print("\n=== Master Pipeline (Part 1 & Part 2 + Full AI/SEO Stack) Completed Successfully ===")

if __name__ == "__main__":
    run_pipeline()
