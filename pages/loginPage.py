import allure
from loguru import logger
from selenium.webdriver.common.by import By

from pages.homePage import HomePage
from utility.pageutils import PageUtils


class LoginPage(PageUtils):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        #Page Locators
        self.username = (By.XPATH, "//input[@id='username']")
        self.password = (By.XPATH, "//input[@id='password']")
        self.login_button = (By.XPATH, "//input[@id='Login']")
        self.invalid_loginmsg = (By.XPATH, "//div[@id='error']")

    @allure.step("Login to Salesforce with Username:{username} and Password:{password}")
    def logintosalesforce(self, username, password):
        logger.info("Add the Username and Password")
        logger.info(f"Enter Username: {username}")
        self.driver.find_element(*self.username).send_keys(username)
        logger.info(f"Enter Password: {password}")
        self.driver.find_element(*self.password).send_keys(password)
        logger.info(f"Click on Login button")
        self.driver.find_element(*self.login_button).click()
        homepage = HomePage(self.driver)
        return homepage

    @allure.step("Validate Invalid Login Message")
    def validate_invalidlogin_mgs(self):
        logger.info("Validating invalid login error message")
        try:
            errormsgtext = self.driver.find_element(*self.invalid_loginmsg).text
            assert "Please check your username and password3333" in errormsgtext
        except Exception as e:
            print(f"Validation failed: {e}")
            raise