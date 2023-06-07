from selenium.webdriver.common.by import By
from POMDemo_1.Pages.BasePage import BasePage
from POMDemo_1.Config.config import TestData

class LoginPage(BasePage):

    """By locators"""
    EMAIL = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'loginBtn')
    SINGUP_LINK = (By.LINK_TEXT, 'Registrarme')

    """"Constructor of the pages class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
    
    """Page Actions for Login Page"""

    """This is to get the page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)
    
    """this is used to check sing up link"""
    def is_signup_link_visible(self):
        return self.is_visible(self.SINGUP_LINK)
    
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        #return HomePage(self.driver)

