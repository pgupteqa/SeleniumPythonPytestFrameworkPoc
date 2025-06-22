import random
import string

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageUtils:

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def wait_for_Presence_of_Element(self, locator):
        """This function is use to wait for presence of particular page element for about 20 sec, If element not present in a
        given time, then this menthod will throw a timeout exception"""
        wait = WebDriverWait(self.driver,10)
        return wait.until(EC.presence_of_element_located((By.XPATH, locator)))

    def wait_for_Visibility_of_Element(self, locator):
        """This function is use to wait upto a particular page element is visible or not for about 20 sec"""
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.visibility_of_element_located((By.XPATH, locator)))

    def wait_for_Invisibility_of_Element(self, locator):
        """This function is use to wait upto a particular page element is invisible or not for about 20 sec. We can use this
        method for loading icon to invisible on the page"""
        wait = WebDriverWait(self.driver, 10)
        return wait.until(EC.presence_of_element_located((By.XPATH, locator)))

    def getText_By_Xpath(self, locator):
        '''This method is used to get text present within a element'''
        self.logger.info("Get text of the present page")
        return self.driver.find_element((By.XPATH, locator)).text

    def selectVisibleTextFromDropdown(self, locator, textvalue):
        """This method will select value as visible text from the dropdown"""
        sel = Select(locator)
        return sel.select_by_visible_text(textvalue)

    def selectValuefromDropdown(self, locator, optionvalue):
        """This method will return the selected value from the dropdown"""
        sel = Select(locator)
        return sel.select_by_value(optionvalue)

    def randomdata_generator(self,size=8, chars=string.ascii_uppercase + string.digits):
        """This method is use to generate the random data for email"""
        return ''.join(random.choice(chars) for _ in range(size))
