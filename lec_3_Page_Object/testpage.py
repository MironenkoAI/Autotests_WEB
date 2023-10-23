from BaseApp import BasePage
from selenium.webdriver.common.by import By

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """// *[ @ id = "login"] / div[1] / label / input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """// *[ @ id = "login"] / div[2] / label / input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")

class OperationsHelper(BasePage):
    def enter_login(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()
        
    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        return error_field.text