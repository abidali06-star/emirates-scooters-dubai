"""
Module: indexing_and_serp_monitor.py

IMPORTANT - behaviour change (2026-09-02)
-----------------------------------------
The previous version of this module FABRICATED results. It reported
"status_code: 200, SUBMITTED_SUCCESSFULLY" for Search Console submissions it
never made, and invented SERP data claiming google_dubai_rank: 1 with
"ChatGPT: Top Recommended" and "Gemini: Cited as RTA Compliant Top Pick" for
keywords that had never been checked. Those figures then flowed into the daily
market intelligence brief, which read like evidence of real ranking success.

Nothing here calls Search Console or any SERP API, and no credentials are
configured. So this module no longer pretends. It now produces a WORKLIST of
things a human should check, and refuses to emit rank or citation data it has
not observed.

If real monitoring is wanted later, wire an actual API in and have it record
observed values with a timestamp and a source URL.
"""

import time
from typing import List, Dict, Any


class SearchConsoleAndSERPMonitor:
    def __init__(self):
        # Queries worth checking by hand. Grounded in what the site actually
        # sells and publishes, not aspirational keywords.
        self.target_keywords = [
            "electric scooter Dubai",
            "buy electric scooter Dubai",
            "electric scooter Dubai price",
            "best electric scooter Dubai",
            "cheap electric scooter Dubai under 1000 AED",
            "Mankeel MK083",
            "Mankeel MX-14",
            "Mankeel Dubai",
            "RTA e-scooter permit Dubai how to apply",
            "e-scooter speed limit Dubai",
            "electric scooter delivery Motor City Dubai",
            "lightweight folding electric scooter Dubai Metro",
        ]

    def submit_urls_for_indexing(self, url_list: List[str]) -> Dict[str, Any]:
        """
        Does NOT submit anything. No Search Console credentials are configured
        and no API call is made. Returns the URLs that a human should submit,
        clearly marked as not submitted.
        """
        return {
            "status": "NOT_SUBMITTED",
            "reason": (
                "No Search Console API credentials are configured and this function makes "
                "no network call. Submit the sitemap manually at "
                "https://search.google.com/search-console if and when the domain is verified."
            ),
            "urls_pending_submission": list(url_list),
            "count": len(url_list),
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }

    def monitor_dubai_serp(self) -> Dict[str, Any]:
        """
        Does NOT measure rankings. Returns a manual check worklist with empty
        observation slots. Fill these in only with positions you have actually
        seen, and record the date you saw them.
        """
        return {
            "status": "NOT_MEASURED",
            "reason": (
                "No SERP API is configured. Rankings and AI-citation status must be observed "
                "by hand: run each query in Google, ChatGPT, Gemini and Perplexity, and record "
                "what you actually see. Never fill these in from expectation."
            ),
            "how_to_check": [
                "Run the query in a logged-out / incognito browser set to Dubai.",
                "For AI engines, note whether emirates-scooters-dubai.vercel.app is cited at all, "
                "and which competing sources are cited instead - that list is the real outreach target.",
                "Record observed_position as an integer, or null if not in the top 100.",
            ],
            "checks": [
                {
                    "keyword": kw,
                    "observed_position": None,
                    "observed_in_ai_answer": None,
                    "competing_sources_cited": [],
                    "checked_on": None,
                }
                for kw in self.target_keywords
            ],
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }


if __name__ == "__main__":
    m = SearchConsoleAndSERPMonitor()
    sub = m.submit_urls_for_indexing(["https://emirates-scooters-dubai.vercel.app/sitemap.xml"])
    serp = m.monitor_dubai_serp()
    print(f"Indexing: {sub['status']} - {sub['count']} URL(s) pending manual submission.")
    print(f"SERP: {serp['status']} - {len(serp['checks'])} queries to check by hand.")
