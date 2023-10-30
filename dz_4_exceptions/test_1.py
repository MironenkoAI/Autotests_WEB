from testpage import OperationsHelper
import logging
import yaml


with open("testdata.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

# ввод невалидных данных в поля login и password выводит ошибку 401
def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()


# ввод валидных данных в поля login и password открывает страницу 
# профиля (проверяем по Приветствию пользователя)
def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata.get("login"))
    testpage.enter_pass(testdata.get("passwd"))
    testpage.click_login_button()
    print("*********" + )
    assert testdata.get("login") in testpage.get_text(), "test FAILED"
    

# проверка механики работы формы Contact Us на главной странице личного кабинета: 
# открытие формы, ввод данных в поля, клик по кнопке и появление всплывающего alert.
def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata.get("login"))
    testpage.enter_pass(testdata.get("passwd"))
    testpage.click_login_button()
    testpage.click_contact_button()
    testpage.enter_name(testdata.get("name"))
    testpage.enter_email(testdata.get("email"))
    testpage.enter_content(testdata.get("content"))
    testpage.click_contact_us_button()
    assert testpage.get_alert_message() == "Form successfully submitted", "test FAILED"
