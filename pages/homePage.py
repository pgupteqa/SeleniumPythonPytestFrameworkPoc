from asyncio import sleep

import allure
from loguru import logger
from utility import salesforce_data_utils
from utility.pageutils import PageUtils
from utility.salesforce_data_utils import SalesforceUtils


class HomePage(PageUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.sf_utils = SalesforceUtils()
        # Page locators

    @allure.step("Verify Home Page Title")
    def verify_page_title(self):
        logger.info("Verifying page title contains 'Home | Salesforce'")
        pagetitle = self.getTitle()
        assert "Home | Salesforce" in pagetitle

    @allure.step("Verify contact by last name: {contact_lastname}")
    def verify_contact_details_by_lastname(self,contact_lastname):
        logger.info(f"Verifying contact with last name: {contact_lastname}")
        contact_details = self.sf_utils.get_contact_detail_by_lastname(contact_lastname)
        contact_name = contact_details['Name']
        assert "Andy Young" in contact_name
