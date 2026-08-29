"""
Unit tests for BacklogManager and Dashboard Web Server functions.
"""

import unittest
import os
import json
from src.automation.backlog_manager import BacklogManager

class TestBacklogAndDashboard(unittest.TestCase):
    def setUp(self):
        self.test_file = "data/test_backlog.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.bm = BacklogManager(filepath=self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_backlog_creation_and_add(self):
        data = self.bm.load()
        self.assertIn("posts", data)
        self.assertIn("blogs", data)

        new_post = self.bm.add_post(
            topic="Test Commute",
            title_en="English Test Title",
            title_ar="Arabic Test Title",
            body_en="Body English",
            body_ar="Body Arabic",
            target_models=["MK083", "MX-14"]
        )

        self.assertEqual(new_post["topic"], "Test Commute")
        updated_data = self.bm.load()
        self.assertEqual(len(updated_data["posts"]), 3)

    def test_add_blog(self):
        new_blog = self.bm.add_blog(
            title="New Test Blog",
            slug="new-test-blog",
            description="Test Description"
        )
        self.assertEqual(new_blog["slug"], "new-test-blog")
        updated_data = self.bm.load()
        self.assertEqual(len(updated_data["blogs"]), 4)

if __name__ == "__main__":
    unittest.main()
