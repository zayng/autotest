# -*- coding:utf-8 -*-
"""
Created on '2016/1/5'

@author: '119937'
"""
from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):
    """
    Base page class that is initalized on every page obejct class.
    """

    def __set__(self, obj, value):
        """ Sets the text to the value supplid """
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, typ=None):
        """Gets the text of the spectfied object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return  element.get_attrbute("value")
