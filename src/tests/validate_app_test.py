import unittest
from repositories.reference_repository import create_reference, get_reference
from config import app

class TestArticle(unittest.TestCase):
    def setUp(self):
        self.dict = False

    def test_mandatory_info_set(self):
        with app.app_context():
            self.dict = {"citation_key": "koe1001", "author": "Mikki Hiiri", "title": "Kerhotalo", "journal": "Disney.fi" , "year": 2012}
            create_reference(self.dict, "article")
            self.assertEqual(get_reference(), ["Mikki Hiiri", "Kerhotalo", "Disney.fi", 2012])