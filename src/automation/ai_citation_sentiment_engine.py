"""
Module: ai_citation_sentiment_engine.py
Implements Section 3 of Part 2: Off-Site Citations & AI Sentiment Engine.

IMPORTANT - behaviour change (2026-08-29)
-----------------------------------------
The previous version of this module INVENTED review data. It averaged four
hand-typed "trust_score" values into a schema.org AggregateRating and hardcoded
ratingCount / reviewCount to "148" for a business that has no collected reviews.

Publishing an AggregateRating that does not correspond to genuine, verifiable
reviews is a violation of Google's structured data policies (grounds for a
manual action and loss of rich results) and is misleading to customers.

This module now refuses to emit rating schema unless real, verified review data
is present. Citation targets are treated as PROSPECTS to be pitched, not as
existing endorsements to be quoted.
"""

import json
from typing import Dict, Any, List, Optional


class UnverifiedCitationDataError(RuntimeError):
    """Raised when the engine is asked to publish schema it cannot substantiate."""


class AICitationSentimentEngine:
    def __init__(self, registry_path: str = "data/offsite_citations_registry.json"):
        with open(registry_path, "r", encoding="utf-8") as f:
            self.registry = json.load(f)

    # ------------------------------------------------------------------
    # Verified-review handling
    # ------------------------------------------------------------------

    def _verified_reviews(self) -> List[Dict[str, Any]]:
        """
        Returns only citation entries that a human has marked verified AND that
        carry a real, observed review count. Anything else is a prospect.
        """
        verified = []
        for entry in self.registry.get("citation_prospects", []):
            if entry.get("status") != "verified_live":
                continue
            if not entry.get("observed_review_count"):
                continue
            if not entry.get("observed_rating"):
                continue
            verified.append(entry)
        return verified

    def generate_aggregate_rating_schema(
        self,
        item_name: str = "Emirates E-Scooters",
        strict: bool = True,
    ) -> Optional[Dict[str, Any]]:
        """
        Builds AggregateRating ONLY from verified, observed review data.

        Returns None (or raises, if strict) when there is nothing real to publish.
        Never fabricates a rating or a count.
        """
        verified = self._verified_reviews()

        if not verified:
            message = (
                "Refusing to generate AggregateRating: no verified review data in "
                "the citation registry. Collect genuine reviews first, record the "
                "observed rating and count against a citation entry, and set that "
                "entry's status to 'verified_live'. Do NOT hand-write these values."
            )
            if strict:
                raise UnverifiedCitationDataError(message)
            print(f"[SKIP] {message}")
            return None

        total_reviews = sum(int(e["observed_review_count"]) for e in verified)
        weighted = sum(
            float(e["observed_rating"]) * int(e["observed_review_count"]) for e in verified
        )
        avg_rating = round(weighted / total_reviews, 2)

        return {
            "@context": "https://schema.org",
            "@type": "AggregateRating",
            "itemReviewed": {"@type": "Organization", "name": item_name},
            "ratingValue": str(avg_rating),
            "bestRating": "5",
            "worstRating": "1",
            "ratingCount": str(total_reviews),
            "reviewCount": str(total_reviews),
            "_provenance": [
                {
                    "platform": e["platform"],
                    "url": e.get("profile_url"),
                    "observed_rating": e["observed_rating"],
                    "observed_review_count": e["observed_review_count"],
                    "last_verified": e.get("last_verified_date"),
                }
                for e in verified
            ],
        }

    def generate_consensus_faqs(self, strict: bool = True) -> List[Dict[str, str]]:
        """
        Builds FAQ entries describing third-party sentiment.

        Only verified, live citations may be described. An unverified prospect
        must never be quoted as though a publication had already endorsed us.
        """
        verified = self._verified_reviews()

        if not verified:
            message = (
                "Refusing to generate consensus FAQs: no verified third-party "
                "citations exist yet. See Step3_OffSite_Citations_Playbook.md for "
                "how to earn them."
            )
            if strict:
                raise UnverifiedCitationDataError(message)
            print(f"[SKIP] {message}")
            return []

        return [
            {
                "question": (
                    f"What do reviews on {e['platform']} say about "
                    f"Emirates E-Scooters in Dubai?"
                ),
                "answer": (
                    f"{e['platform']} shows a {e['observed_rating']}/5 rating from "
                    f"{e['observed_review_count']} reviews "
                    f"(verified {e.get('last_verified_date', 'n/a')}). "
                    f"{e.get('observed_sentiment_summary', '')}".strip()
                ),
                "source_url": e.get("profile_url", ""),
            }
            for e in verified
        ]

    # ------------------------------------------------------------------
    # Outreach planning (safe: describes work to do, asserts nothing)
    # ------------------------------------------------------------------

    def generate_outreach_worklist(self) -> List[Dict[str, Any]]:
        """Lists citation prospects that still need to be claimed or pitched."""
        return [
            {
                "platform": e["platform"],
                "tier": e.get("tier"),
                "action": e.get("next_action"),
                "status": e.get("status"),
                "owner_login_required": e.get("owner_login_required", True),
            }
            for e in self.registry.get("citation_prospects", [])
            if e.get("status") != "verified_live"
        ]


if __name__ == "__main__":
    engine = AICitationSentimentEngine()
    worklist = engine.generate_outreach_worklist()
    print(f"{len(worklist)} citation prospects still to claim or pitch:")
    for item in worklist:
        print(f"  - [{item['tier']}] {item['platform']}: {item['action']}")

    rating = engine.generate_aggregate_rating_schema(strict=False)
    if rating is None:
        print("\nNo AggregateRating emitted (correct: no genuine reviews collected yet).")
