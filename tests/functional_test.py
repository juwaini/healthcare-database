import unittest
from selenium import webdriver

class PageFunctionalCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_index_page(self):
        #User A opens the page and see correct title
        self.browser.get('localhost:5000')
        self.assertIn('Welcome To Healthcare Database System', self.browser.title)

        #User A is not logged in, so a modal pop up and ask him to login
        #KIV

        #User A can see a table in the page with the following table title []
        table = self.browser.find_element_by_tag_name('table')

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
