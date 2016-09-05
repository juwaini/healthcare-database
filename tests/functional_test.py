import unittest
from selenium import webdriver

class PageFunctionalCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_index_sanity_test(self):
        self.browser.get('localhost:5000')
        #assertIn('Healthcare Database System', self.browser.title)
        self.assertIn('Hello world!', self.browser.page_source)

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
