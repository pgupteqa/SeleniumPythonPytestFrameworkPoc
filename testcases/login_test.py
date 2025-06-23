import os
import sys

import allure
import pytest
from Configuration.config_reader import Login_test_data_path

from pages.loginPage import LoginPage
from testcases.basetestclass import BaseTest
from loguru import logger

@allure.epic("Salesforce Login")
class TestLogin(BaseTest):
    '''If the tests fails then it will re-run the test again 2 times'''

    @allure.feature("Valid Login")
    @pytest.mark.flaky(reruns=2)
    @pytest.mark.smoke
    @pytest.mark.login
    @pytest.mark.parametrize("test_list_item", BaseTest.get_data_from_json(Login_test_data_path,"valid_login"))
    def test_loginsalesforce_validcredentials(self, test_list_item):
        logger.info("Starting valid login test")
        loginpage = LoginPage(self.driver)
        homepage = loginpage.logintosalesforce(test_list_item["username"],test_list_item["password"])
        homepage.verify_page_title()
        homepage.verify_contact_details_by_lastname('Young')

    @pytest.mark.flaky(reruns=2)
    @pytest.mark.smoke
    @pytest.mark.parametrize("test_list_item", BaseTest.get_data_from_json(Login_test_data_path,"invalid_login"))
    def test_loginsalesforce_invalid_credentials(self,test_list_item):
        loginpage = LoginPage(self.driver)
        loginpage.logintosalesforce(test_list_item["username"],test_list_item["password"])
        loginpage.validate_invalidlogin_mgs()

