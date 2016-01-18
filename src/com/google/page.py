# -*- coding:utf-8 -*-
"""
Created on '2016/1/5'

@author: '119937'
"""

from com.google.element import BasePageElement
from com.google.locators import MainPageLocators

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator."""

    #The locator for search box where search sring is entered
    locator = 'q'

class BasePage(object):
    """Base class to initalize the base pages that will be called  from all pages"""

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    """Home pages action menthods come here. I.e. Python.org"""
    #Declares a variabe that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in pages title"""
        return "Python" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultsPage(BasePage):
    """Search results pages action methods come here"""

    def is_results_found(self):
        #Probably shoud search for this text in the specific pages
        #element, but as for now is works fine
        return "No results found." not in self.driver.page_source

