from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import time

class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """// *[ @ id = "login"] / div[1] / label / input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """// *[ @ id = "login"] / div[2] / label / input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_TEXT_FIELD = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")
    

class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True
    
    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True
    
    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text


# ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_LOGIN_FIELD, word, description="login form")
        
    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_PASS_FIELD, word, description="password form")

    def enter_name(self, text):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_NAME_FIELD, text, description="name form")
        
    def enter_email(self, text):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_EMAIL_FIELD, text, description="email form")

    def enter_content(self, text):
        self.enter_text_into_field(TestSearchLocators.LOCATOR_CONTENT_FIELD, text, description="content form")
        
# CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.LOCATOR_LOGIN_BTN, description="login button")
    
    def click_contact_button(self):
        self.click_button(TestSearchLocators.LOCATOR_CONTACT_BTN, description="contact button")

    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.LOCATOR_CONTACT_US_BTN, description="contact_us button")

# GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_ERROR_FIELD, description="error")
    
    def get_text(self):
        return self.get_text_from_element(TestSearchLocators.LOCATOR_TEXT_FIELD, description="text")
            
    def get_alert_message(self):
        time.sleep(1)
        logging.info("Get alert message")
        alert = self.driver.switch_to.alert
        message = alert.text
        logging.info(f"Alert message is {message}")
        alert.accept()
        return message