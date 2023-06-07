from selenium.webdriver.common.by import By
from POMDemo_1.Pages.BasePage import BasePage
from POMDemo_1.Config.config import TestData

class HomePage(BasePage):
    HEADER = (By.XPATH, "//div[@class='oxd-topbar-header-title']//h6")
    ACCOUNT_ICON = (By.ID, "account-menu")
    ACCOUNT_DETAILS = (By.CLASS_NAME, "accountexpansion expansion")
    ACCOUNT_EMAIL = (By. CLASS_NAME, "user-info-email")

    def __init__(self, driver):
        super().__init__(driver)
    
    def get_home_page_title(self, title):
        return self.get_title(title)
    
    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)
    
    def is_account_details_visible(self):
        return self.is_visible(self.ACCOUNT_DETAILS)
    
    def get_account_email(self):
        return self.get_element_text(self.ACCOUNT_EMAIL)
