import unittest
from selenium import webdriver


class E2ETests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(
            executable_path=r'/Applications/geckodriver')
        self.driver.get('http://localhost:5000')

    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entity', self.driver.title)

    # Data Attribute - See L26 of index.html for Example
    def test_page_heading_is_named_entity_finder(self):
        heading = self._find("heading").text
        self.assertEqual('Named Entity Finder', heading)

    def _find(self, val):
        return self.driver.find_element_by_css_selector(f'[data-test-id="{val}"]')
