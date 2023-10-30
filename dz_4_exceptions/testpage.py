from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import time
import yaml

class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])
    

class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.ids['LOCATOR_LOGIN_FIELD']}")
        try:
            login_field = self.find_element(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'])
        except:
            logging.exception("Element not found")
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.ids['LOCATOR_PASS_FIELD']}")
        login_field = self.find_element(TestSearchLocators.ids['LOCATOR_PASS_FIELD'])
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.ids['LOCATOR_LOGIN_BTN']).click()

    def click_exit(self):
        logging.info("Click exit button")
        self.find_element(TestSearchLocators.ids['LOCATOR_TEXT_FIELD']).click()
        self.find_element(TestSearchLocators.ids['LOCATOR_LOGOUT_BTN']).click()
        
    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'], time=3)
        text = error_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.ids['LOCATOR_ERROR_FIELD']}")
        return text
    
    def get_text(self):
        text_field = self.find_element(TestSearchLocators.ids['LOCATOR_TEXT_FIELD'], time=3)
        text = text_field.text
        logging.info(f"We find text {text} in text field {TestSearchLocators.ids['LOCATOR_TEXT_FIELD']}")        
        return text
    
    def click_contact_button(self):
        logging.info("Click contact button")
        self.find_element(TestSearchLocators.ids['LOCATOR_CONTACT_BTN']).click()

    def enter_name(self, text):
        logging.info(f"Send {text} to element {TestSearchLocators.ids['LOCATOR_NAME_FIELD']}")
        name_field = self.find_element(TestSearchLocators.ids['LOCATOR_NAME_FIELD'])
        name_field.clear()
        name_field.send_keys(text)

    def enter_email(self, text):
        logging.info(f"Send {text} to element {TestSearchLocators.ids['LOCATOR_EMAIL_FIELD']}")
        email_field = self.find_element(TestSearchLocators.ids['LOCATOR_EMAIL_FIELD'])
        email_field.clear()
        email_field.send_keys(text)

    def enter_content(self, text):
        logging.info(f"Send {text} to element {TestSearchLocators.ids['LOCATOR_CONTENT_FIELD']}")
        content_field = self.find_element(TestSearchLocators.ids['LOCATOR_CONTENT_FIELD'])
        content_field.clear()
        content_field.send_keys(text)

    def click_contact_us_button(self):
        logging.info("Click Contact us button")
        self.find_element(TestSearchLocators.ids['LOCATOR_CONTACT_US_BTN']).click()

    def get_alert_message(self):
        time.sleep(1)
        logging.info("Get alert message")
        alert = self.driver.switch_to.alert
        message = alert.text
        logging.info(f"Alert message is {message}")
        alert.accept()
        return message