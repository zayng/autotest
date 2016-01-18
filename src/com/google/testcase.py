# -*- coding:utf-8 -*-
"""
Created on '2016/1/5'

@author: '119937'
"""
import unittest
from selenium import webdriver
from com.google import page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how pages object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        """
        Tests python.org search feature. Searches for the word "pycon" then verified that some results show u
        Note that is does not look for any particular test search results pages.This test verifies that the
        results were not empty
        """

        #Load the main pages. In this case the home pages of pages.org.
        main_page = page.MainPage(self.driver)
        #check if the word "Python" in title
        assert main_page.is_title_matches(), "python.org title doesn't match"
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results pages is not empty
        assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
