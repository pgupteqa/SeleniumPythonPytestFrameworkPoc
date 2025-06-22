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


    def logintosalesforce(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        homepage = HomePage(self.driver)
        return homepage

    def validate_invalidlogin_mgs(self):
        try:
            errormsgtext = self.driver.find_element(*self.invalid_loginmsg).text
            assert "Please check your username and password" in errormsgtext
        except Exception as e:
            print(f"Validation failed: {e}")
            raise