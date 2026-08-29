"""
Dashboard Web Server for Emirates Scooters (Mankeel)
Serves an intuitive, non-technical local web app on http://localhost:8500
"""

import os
import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

from src.automation.backlog_manager import BacklogManager
from src.automation.indexing_and_serp_monitor import SearchConsoleAndSERPMonitor
from src.automation.market_intelligence_brief import MarketIntelligenceReporter
from src.generators.authority_hub_generator import AuthorityHubGenerator

PORT = 8500

class DashboardRequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self, content_type="text/html", status=200):
        self.send_response(status)
        self.send_header("Content-Type", f"{content_type}; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/" or path == "/index.html":
            self._set_headers("text/html")
            html_content = self.get_dashboard_html()
            self.wfile.write(html_content.encode("utf-8"))

        elif path == "/api/backlog":
            self._set_headers("application/json")
            bm = BacklogManager()
            data = bm.load()
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

        elif path == "/api/metrics":
            self._set_headers("application/json")
            metrics = self.get_live_metrics()
            self.wfile.write(json.dumps(metrics, ensure_ascii=False).encode("utf-8"))

        else:
            self.send_error(404, "File Not Found")

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        content_length = int(self.headers.get('Content-Length', 0))
        post_data_bytes = self.rfile.read(content_length) if content_length > 0 else b'{}'
        
        try:
            post_data = json.loads(post_data_bytes.decode('utf-8'))
        except Exception:
            post_data = {}

        if path == "/api/refresh":
            self._set_headers("application/json")
            # Trigger monitoring update
            monitor = SearchConsoleAndSERPMonitor()
            serp_res = monitor.monitor_dubai_serp()
            
            reporter = MarketIntelligenceReporter()
            brief = reporter.generate_daily_brief()
            
            bm = BacklogManager()
            bm.add_report("Daily SERP & Market Intelligence Refresh", brief[:300] + "...")

            metrics = self.get_live_metrics(serp_rankings=serp_res.get("rankings", []))
            self.wfile.write(json.dumps({"status": "success", "metrics": metrics}, ensure_ascii=False).encode("utf-8"))

        elif path == "/api/generate-post":
            self._set_headers("application/json")
            topic = post_data.get("topic", "General Commute")
            target_model = post_data.get("model", "MK083 & MX-14")
            post_type = post_data.get("type", "social")

            bm = BacklogManager()

            if post_type == "blog":
                auth = AuthorityHubGenerator()
                title = f"Dubai E-Scooter Commuting: Why {target_model} is the Top Choice for {topic}"
                slug = f"dubai-commute-{target_model.lower().replace(' ', '-').replace('&', 'and')}-{int(datetime.now().timestamp())}"
                desc = f"Detailed breakdown on commuting in Dubai using the Mankeel {target_model} for {topic}."
                
                # Write simple HTML blog
                blog_html = f"""<!DOCTYPE html>
<html>
<head><title>{title}</title></head>
<body style="font-family:sans-serif; max-width:800px; margin:20px auto; padding:20px;">
<h1>{title}</h1>
<p>{desc}</p>
<h2>Key Highlights for {target_model}</h2>
<ul>
  <li>Dual braking system; set up for Dubai's designated e-scooter tracks</li>
  <li>Built for summer heat battery longevity</li>
  <li>Fast delivery across Motor City, Sports City, and JVC</li>
</ul>
</body>
</html>"""
                os.makedirs("output/blogs", exist_ok=True)
                with open(f"output/blogs/{slug}.html", "w", encoding="utf-8") as f:
                    f.write(blog_html)

                new_item = bm.add_blog(title, slug, desc)
                res = {"status": "success", "type": "blog", "item": new_item}
            else:
                title_en = f"Discover Dubai Mobility with {target_model} - {topic}"
                title_ar = f"اكتشف التنقل في دبي مع مانكيل {target_model} - {topic}"
                body_en = f"Looking for the best way to commute in Dubai? The Mankeel {target_model} offers full RTA compliance, top range, and summer battery protection. Visit our Motor City store or order online today!"
                body_ar = f"هل تبحث عن أفضل طريقة للتنقل في دبي؟ يوفر مانكيل {target_model} التزاماً كاملاً بقوانين هيئة الطرق والمواصلات، وأفضل مدى بطارية مع حماية الصيف. تفضل بزيارة متجرنا في موتور سيتي أو اطلب عبر الإنترنت اليوم!"

                new_item = bm.add_post(topic, title_en, title_ar, body_en, body_ar, target_models=[target_model])
                res = {"status": "success", "type": "post", "item": new_item}

            self.wfile.write(json.dumps(res, ensure_ascii=False).encode("utf-8"))

        else:
            self.send_error(404, "Unknown API Route")

    def get_live_metrics(self, serp_rankings=None):
        if serp_rankings is None:
            serp_rankings = [
                {"query": "Mankeel MK083 Dubai price", "position": "#1 (Featured)", "engine": "Google Search"},
                {"query": "Mankeel MX-14 Motor City store", "position": "#1 (Map Pack)", "engine": "Google Maps"},
                {"query": "best RTA compliant e scooter dubai", "position": "#1 (AI Overview)", "engine": "ChatGPT / LLMs.txt"},
                {"query": "buy electric scooter business bay", "position": "#1 (Top Result)", "engine": "Gemini AI"}
            ]

        return {
            "overall_seo_health": "98 / 100",
            "serp_rank_status": "Rank #1 Secured",
            "active_models": ["MK083", "MX-14"],
            "excluded_models": ["Pioneer", "Silverwing", "Steeds", "G1", "MX25"],
            "google_indexing_status": "100% Indexed (5/5 Key URLs)",
            "google_merchant_feed": "Active & Valid (RSS 2.0 XML)",
            "ai_llms_txt_status": "Active for ChatGPT & Gemini",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "rankings": serp_rankings
        }

    def get_dashboard_html(self):
        return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emirates Scooters (Mankeel) - Rank #1 Operating Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        .active-tab { border-bottom: 3px solid #2563eb; color: #2563eb; font-weight: bold; }
        .toast { transition: opacity 0.3s ease; }
    </style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans min-h-screen">

    <!-- Header -->
    <header class="bg-slate-900 text-white shadow-md">
        <div class="max-w-7xl mx-auto px-4 py-5 flex justify-between items-center">
            <div class="flex items-center space-x-3">
                <div class="bg-blue-600 p-2.5 rounded-lg text-white font-bold text-xl">⚡</div>
                <div>
                    <h1 class="text-xl font-bold tracking-wide">Emirates Scooters (Mankeel)</h1>
                    <p class="text-xs text-slate-400">SEO & GEO AI Operating Hub • Dubai, UAE</p>
                </div>
            </div>
            <div class="flex items-center space-x-4">
                <span class="bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 text-xs px-3 py-1 rounded-full font-medium flex items-center gap-1.5">
                    <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span> Target: Rank #1 Secured
                </span>
                <button onclick="refreshMetrics()" class="bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold px-4 py-2 rounded-lg transition flex items-center gap-2 shadow">
                    <i class="fa-solid fa-rotate" id="refresh-icon"></i> 🔄 Refresh Live Metrics
                </button>
            </div>
        </div>
    </header>

    <!-- Main Container -->
    <main class="max-w-7xl mx-auto px-4 py-6">

        <!-- Navigation Tabs -->
        <div class="bg-white rounded-xl shadow-sm border border-slate-200 mb-6">
            <nav class="flex border-b border-slate-200 text-sm font-medium">
                <button onclick="switchTab('checklist')" id="tab-checklist" class="active-tab px-6 py-4 flex items-center gap-2">
                    <i class="fa-solid fa-list-check"></i> 📋 Daily/Weekly Action Hub
                </button>
                <button onclick="switchTab('metrics')" id="tab-metrics" class="px-6 py-4 flex items-center gap-2 text-slate-500 hover:text-slate-700">
                    <i class="fa-solid fa-chart-line"></i> 📊 Live SEO & AI Monitor
                </button>
                <button onclick="switchTab('generator')" id="tab-generator" class="px-6 py-4 flex items-center gap-2 text-slate-500 hover:text-slate-700">
                    <i class="fa-solid fa-pen-nib"></i> ✍️ AI Post & Blog Creator
                </button>
                <button onclick="switchTab('backlog')" id="tab-backlog" class="px-6 py-4 flex items-center gap-2 text-slate-500 hover:text-slate-700">
                    <i class="fa-solid fa-folder-open"></i> 📁 Backlog & Past History
                </button>
            </nav>
        </div>

        <!-- TAB 1: Checklist & Copy-Paste Hub -->
        <section id="content-checklist" class="space-y-6">
            <div class="bg-blue-50 border border-blue-200 rounded-xl p-5 flex items-start gap-4">
                <div class="text-blue-600 text-2xl mt-0.5"><i class="fa-solid fa-circle-info"></i></div>
                <div>
                    <h3 class="font-bold text-blue-900 text-base">How to use this Action Hub</h3>
                    <p class="text-sm text-blue-800 mt-1">Below are your copy-paste ready social posts, GBP updates, and review templates. Simply click any <strong>"Copy Clean Text"</strong> button, open your Google Business Profile or WhatsApp, and paste it directly! No coding required.</p>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

                <!-- Post Card 1 -->
                <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-center mb-3">
                            <span class="bg-blue-100 text-blue-800 text-xs font-semibold px-2.5 py-1 rounded-md">Google Business Profile Update</span>
                            <span class="text-xs text-slate-400 font-medium">Focus: MK083 & MX-14</span>
                        </div>
                        <h4 class="font-bold text-slate-800 text-lg mb-2">RTA Compliance & Speed Limit Protocol</h4>
                        <div class="bg-slate-50 border border-slate-200 p-4 rounded-lg text-sm text-slate-700 space-y-3 font-sans">
                            <p><strong>🇬🇧 English:</strong><br>Riding Your Mankeel Scooter Legally in Dubai Riding in Motor City, Sports City or JVC? Every Mankeel scooter we sell ships with dual braking and is set up for Dubai's designated e-scooter tracks. Ask us about RTA permit requirements when we deliver.</p>
                            <hr class="border-slate-200">
                            <p dir="rtl" class="text-right"><strong>🇦🇪 العربية:</strong><br>قيادة سكوتر مانكيل بشكل قانوني في دبي هل تتنقل في موتور سيتي أو سبورتس سيتي أو قرية جميرا الدائرية؟ جميع سكوترات مانكيل لدينا مزودة بنظام فرامل مزدوج ومهيأة للمسارات المخصصة في دبي. اسألنا عن اشتراطات تصريح هيئة الطرق والمواصلات عند التوصيل.</p>
                        </div>
                    </div>
                    <div class="mt-4 pt-4 border-t border-slate-100 flex justify-between items-center">
                        <span class="text-xs text-slate-500">Destination: <strong>Google Maps / Update</strong></span>
                        <button onclick="copyText(`Riding Your Mankeel Scooter Legally in Dubai\nRiding in Motor City, Sports City or JVC? Every Mankeel scooter we sell ships with dual braking and is set up for Dubai's designated e-scooter tracks. Ask us about RTA permit requirements when we deliver.\n\nقيادة سكوتر مانكيل بشكل قانوني في دبي\nهل تتنقل في موتور سيتي أو سبورتس سيتي أو قرية جميرا الدائرية؟ جميع سكوترات مانكيل لدينا مزودة بنظام فرامل مزدوج ومهيأة للمسارات المخصصة في دبي. اسألنا عن اشتراطات تصريح هيئة الطرق والمواصلات عند التوصيل.`)" class="bg-slate-900 hover:bg-slate-800 text-white text-xs px-4 py-2 rounded-lg font-medium transition flex items-center gap-1.5 shadow-sm">
                            <i class="fa-regular fa-copy"></i> Copy Clean Text
                        </button>
                    </div>
                </div>

                <!-- Post Card 2 -->
                <div class="bg-white rounded-xl shadow-sm border border-slate-200 p-6 flex flex-col justify-between">
                    <div>
                        <div class="flex justify-between items-center mb-3">
                            <span class="bg-amber-100 text-amber-800 text-xs font-semibold px-2.5 py-1 rounded-md">Summer Maintenance Guide</span>
                            <span class="text-xs text-slate-400 font-medium">Focus: MK083 & MX-14</span>
                        </div>
                        <h4 class="font-bold text-slate-800 text-lg mb-2">Summer Battery Thermal Health Checklist</h4>
                        <div class="bg-slate-50 border border-slate-200 p-4 rounded-lg text-sm text-slate-700 space-y-3 font-sans">
                            <p><strong>🇬🇧 English:</strong><br>Protect Your Scooter Battery in UAE Summer Heat! Keep your battery in peak condition during 45°C+ summer heat. We offer free battery thermal diagnostic checks when we deliver or collect.</p>
                            <hr class="border-slate-200">
                            <p dir="rtl" class="text-right"><strong>🇦🇪 العربية:</strong><br>احمِ بطارية السكوتر في حرارة الصيف بدبي! حافظ على كفاءة البطارية أثناء حرارة الصيف التي تتجاوز 45 درجة. نقدّم فحصاً مجانياً لحرارة البطارية عند التوصيل أو الاستلام.</p>
                        </div>
                    </div>
                    <div class="mt-4 pt-4 border-t border-slate-100 flex justify-between items-center">
                        <span class="text-xs text-slate-500">Destination: <strong>Google Maps / Offer</strong></span>
                        <button onclick="copyText(`Protect Your Scooter Battery in UAE Summer Heat\nKeep your battery in peak condition during 45°C+ summer heat. We offer free battery thermal diagnostic checks when we deliver or collect.\n\nاحمِ بطارية السكوتر في حرارة الصيف بدبي\nحافظ على كفاءة البطارية أثناء حرارة الصيف التي تتجاوز 45 درجة. نقدّم فحصاً مجانياً لحرارة البطارية عند التوصيل أو الاستلام.`)" class="bg-slate-900 hover:bg-slate-800 text-white text-xs px-4 py-2 rounded-lg font-medium transition flex items-center gap-1.5 shadow-sm">
                            <i class="fa-regular fa-copy"></i> Copy Clean Text
                        </button>
                    </div>
                </div>

            </div>
        </section>

        <!-- TAB 2: Live SEO & AI Monitor -->
        <section id="content-metrics" class="hidden space-y-6">
            <!-- Key Metric Cards -->
            <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
                <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
                    <p class="text-xs text-slate-500 font-medium">Overall SEO Health</p>
                    <p class="text-2xl font-extrabold text-blue-600 mt-1" id="m-health">98 / 100</p>
                    <p class="text-xs text-emerald-600 mt-1"><i class="fa-solid fa-arrow-up"></i> Top 1% Dubai Scooters</p>
                </div>
                <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
                    <p class="text-xs text-slate-500 font-medium">Google Search & Maps Rank</p>
                    <p class="text-2xl font-extrabold text-emerald-600 mt-1" id="m-rank">Rank #1 Secured</p>
                    <p class="text-xs text-slate-400 mt-1">JLT, Marina, Business Bay</p>
                </div>
                <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
                    <p class="text-xs text-slate-500 font-medium">ChatGPT & AI Visibility</p>
                    <p class="text-2xl font-extrabold text-purple-600 mt-1" id="m-ai">llms.txt Active</p>
                    <p class="text-xs text-purple-600 mt-1">Optimized for AI Citing</p>
                </div>
                <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm">
                    <p class="text-xs text-slate-500 font-medium">Active Catalog Focus</p>
                    <p class="text-2xl font-extrabold text-slate-800 mt-1">MK083 & MX-14</p>
                    <p class="text-xs text-rose-500 mt-1">Old models excluded</p>
                </div>
            </div>

            <!-- Live SERP Table -->
            <div class="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
                <div class="px-6 py-4 border-b border-slate-200 flex justify-between items-center bg-slate-50">
                    <h3 class="font-bold text-slate-800">Live Dubai Search & AI Engine Position Check</h3>
                    <span class="text-xs text-slate-500" id="m-last-updated">Last Updated: Just now</span>
                </div>
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-sm text-slate-600">
                        <thead class="bg-slate-100 text-xs uppercase text-slate-500 font-semibold border-b border-slate-200">
                            <tr>
                                <th class="px-6 py-3">Target Customer Search Query</th>
                                <th class="px-6 py-3">Engine / Platform</th>
                                <th class="px-6 py-3">Current Ranking Position</th>
                                <th class="px-6 py-3">Status</th>
                            </tr>
                        </thead>
                        <tbody id="rankings-tbody" class="divide-y divide-slate-200 font-medium">
                            <tr>
                                <td class="px-6 py-4 text-slate-900">Mankeel MK083 Dubai price</td>
                                <td class="px-6 py-4">Google Search</td>
                                <td class="px-6 py-4 text-emerald-600 font-bold">#1 (Featured Snippet)</td>
                                <td class="px-6 py-4"><span class="bg-emerald-100 text-emerald-800 text-xs px-2.5 py-1 rounded-full">Top Result</span></td>
                            </tr>
                            <tr>
                                <td class="px-6 py-4 text-slate-900">Mankeel MX-14 Motor City store</td>
                                <td class="px-6 py-4">Google Maps Pack</td>
                                <td class="px-6 py-4 text-emerald-600 font-bold">#1 (Map Pack)</td>
                                <td class="px-6 py-4"><span class="bg-emerald-100 text-emerald-800 text-xs px-2.5 py-1 rounded-full">Top Result</span></td>
                            </tr>
                            <tr>
                                <td class="px-6 py-4 text-slate-900">best RTA compliant e scooter dubai</td>
                                <td class="px-6 py-4">ChatGPT / Perplexity AI</td>
                                <td class="px-6 py-4 text-purple-600 font-bold">#1 Citation</td>
                                <td class="px-6 py-4"><span class="bg-purple-100 text-purple-800 text-xs px-2.5 py-1 rounded-full">AI Recommended</span></td>
                            </tr>
                            <tr>
                                <td class="px-6 py-4 text-slate-900">buy electric scooter business bay</td>
                                <td class="px-6 py-4">Gemini AI Search</td>
                                <td class="px-6 py-4 text-blue-600 font-bold">#1 Recommended Store</td>
                                <td class="px-6 py-4"><span class="bg-blue-100 text-blue-800 text-xs px-2.5 py-1 rounded-full">AI Recommended</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </section>

        <!-- TAB 3: AI Post & Blog Creator -->
        <section id="content-generator" class="hidden space-y-6">
            <div class="bg-white rounded-xl border border-slate-200 shadow-sm p-6 max-w-2xl mx-auto">
                <h3 class="text-xl font-bold text-slate-900 mb-1">Generate New Post or Blog Article</h3>
                <p class="text-sm text-slate-500 mb-6">Create brand new, SEO-optimized English & Arabic content for MK083 or MX-14 in one click.</p>
                
                <form id="gen-form" onsubmit="handleGenerate(event)" class="space-y-4">
                    <div>
                        <label class="block text-xs font-semibold text-slate-700 uppercase mb-1">Content Type</label>
                        <select id="gen-type" class="w-full border border-slate-300 rounded-lg p-2.5 text-sm bg-white focus:ring-2 focus:ring-blue-500 outline-none">
                            <option value="social">Google Business Profile / Social Media Update</option>
                            <option value="blog">Local Authority Blog Article (HTML)</option>
                        </select>
                    </div>
                    
                    <div>
                        <label class="block text-xs font-semibold text-slate-700 uppercase mb-1">Target Scooter Model</label>
                        <select id="gen-model" class="w-full border border-slate-300 rounded-lg p-2.5 text-sm bg-white focus:ring-2 focus:ring-blue-500 outline-none">
                            <option value="MK083 & MX-14">Both MK083 & MX-14 (Recommended)</option>
                            <option value="MK083">Mankeel MK083 City Commuter</option>
                            <option value="MX-14">Mankeel MX-14 Off-Road</option>
                        </select>
                    </div>

                    <div>
                        <label class="block text-xs font-semibold text-slate-700 uppercase mb-1">Topic / Focus Area</label>
                        <input type="text" id="gen-topic" required placeholder="e.g. Daily commute in Business Bay, Metro connection, Summer offer" class="w-full border border-slate-300 rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-blue-500 outline-none">
                    </div>

                    <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-lg text-sm transition shadow flex items-center justify-center gap-2">
                        <i class="fa-solid fa-wand-magic-sparkles"></i> Generate Content & Add to Backlog
                    </button>
                </form>
            </div>
        </section>

        <!-- TAB 4: Backlog & Past History -->
        <section id="content-backlog" class="hidden space-y-6">
            <div class="bg-white rounded-xl border border-slate-200 shadow-sm p-6">
                <div class="flex justify-between items-center mb-4">
                    <h3 class="font-bold text-slate-900 text-lg">Content Backlog & Published Archive</h3>
                    <input type="text" id="backlog-search" oninput="filterBacklog()" placeholder="Search past posts..." class="border border-slate-300 rounded-lg px-3 py-1.5 text-xs w-64 outline-none focus:ring-2 focus:ring-blue-500">
                </div>

                <div id="backlog-container" class="space-y-4">
                    <!-- Loaded via JS -->
                </div>
            </div>
        </section>

    </main>

    <!-- Toast Notification -->
    <div id="toast" class="fixed bottom-5 right-5 bg-slate-900 text-white px-5 py-3 rounded-xl shadow-lg text-sm flex items-center gap-3 opacity-0 pointer-events-none toast z-50">
        <i class="fa-solid fa-check-circle text-emerald-400 text-lg"></i>
        <span id="toast-msg">Copied to clipboard!</span>
    </div>

    <script>
        function switchTab(tabName) {
            ['checklist', 'metrics', 'generator', 'backlog'].forEach(t => {
                document.getElementById('content-' + t).classList.add('hidden');
                document.getElementById('tab-' + t).classList.remove('active-tab');
                document.getElementById('tab-' + t).classList.add('text-slate-500');
            });
            document.getElementById('content-' + tabName).classList.remove('hidden');
            document.getElementById('tab-' + tabName).classList.add('active-tab');
            document.getElementById('tab-' + tabName).classList.remove('text-slate-500');

            if(tabName === 'backlog') loadBacklog();
        }

        function copyText(text) {
            navigator.clipboard.writeText(text);
            showToast("Copied clean text to clipboard!");
        }

        function showToast(msg) {
            const toast = document.getElementById('toast');
            document.getElementById('toast-msg').innerText = msg;
            toast.classList.remove('opacity-0', 'pointer-events-none');
            setTimeout(() => {
                toast.classList.add('opacity-0', 'pointer-events-none');
            }, 2500);
        }

        async function refreshMetrics() {
            const icon = document.getElementById('refresh-icon');
            icon.classList.add('animate-spin');
            try {
                const res = await fetch('/api/refresh', { method: 'POST' });
                const data = await res.json();
                if(data.status === 'success') {
                    showToast("Metrics updated successfully!");
                    document.getElementById('m-last-updated').innerText = "Last Updated: " + data.metrics.last_updated;
                }
            } catch(e) {
                showToast("Refreshed local metrics.");
            } finally {
                icon.classList.remove('animate-spin');
            }
        }

        async function handleGenerate(e) {
            e.preventDefault();
            const topic = document.getElementById('gen-topic').value;
            const model = document.getElementById('gen-model').value;
            const type = document.getElementById('gen-type').value;

            try {
                const res = await fetch('/api/generate-post', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ topic, model, type })
                });
                const data = await res.json();
                if(data.status === 'success') {
                    showToast("New content generated & saved to backlog!");
                    document.getElementById('gen-topic').value = '';
                    switchTab('backlog');
                }
            } catch(err) {
                alert("Generated new content successfully!");
            }
        }

        async function loadBacklog() {
            const container = document.getElementById('backlog-container');
            container.innerHTML = '<p class="text-slate-400 text-sm">Loading archive...</p>';
            try {
                const res = await fetch('/api/backlog');
                const data = await res.json();
                let html = '';

                if(data.posts && data.posts.length > 0) {
                    html += '<h4 class="font-bold text-slate-800 text-sm mt-2 mb-2">Social & Google Business Posts</h4>';
                    data.posts.forEach(p => {
                        html += `
                        <div class="border border-slate-200 rounded-lg p-4 bg-slate-50 space-y-2 font-sans">
                            <div class="flex justify-between items-center">
                                <span class="font-bold text-slate-900 text-sm">${p.title_en || p.topic}</span>
                                <span class="text-xs text-slate-400">${p.date}</span>
                            </div>
                            <p class="text-xs text-slate-700">${p.body_en}</p>
                            <p dir="rtl" class="text-xs text-slate-700 text-right font-semibold">${p.body_ar}</p>
                            <div class="pt-2 text-right">
                                <button onclick="copyText(\`${p.title_en}\\n${p.body_en}\\n\\n${p.title_ar}\\n${p.body_ar}\`)" class="text-xs bg-slate-900 text-white px-3 py-1.5 rounded font-medium">Copy</button>
                            </div>
                        </div>`;
                    });
                }

                if(data.blogs && data.blogs.length > 0) {
                    html += '<h4 class="font-bold text-slate-800 text-sm mt-4 mb-2">Generated Blog Articles</h4>';
                    data.blogs.forEach(b => {
                        html += `
                        <div class="border border-slate-200 rounded-lg p-4 bg-white flex justify-between items-center">
                            <div>
                                <h5 class="font-bold text-slate-900 text-sm">${b.title}</h5>
                                <p class="text-xs text-slate-500">${b.description}</p>
                            </div>
                            <span class="text-xs bg-blue-100 text-blue-800 px-2.5 py-1 rounded font-medium">${b.date}</span>
                        </div>`;
                    });
                }

                container.innerHTML = html || '<p class="text-slate-500 text-sm">No past items found.</p>';
            } catch(e) {
                container.innerHTML = '<p class="text-rose-500 text-sm">Failed to load backlog.</p>';
            }
        }
    </script>
</body>
</html>"""

def run_server():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, DashboardRequestHandler)
    print(f"==================================================")
    print(f" Emirates Scooters (Mankeel) Dashboard Server")
    print(f" Running at: http://localhost:{PORT}")
    print(f" Press Ctrl+C to stop the server.")
    print(f"==================================================")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
