import yaml
# from module import Site
import pytest

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
# site = Site(testdata["address"])

def test_step1(site, selector_login, selector_passwd, selector_button, selector_error):
    input1 = site.find_element("xpath", selector_login)
    input1.send_keys("test")
    
    input2 = site.find_element("xpath", selector_passwd)
    input2.send_keys("test")
    
    btn = site.find_element("css", selector_button)
    btn.click()
    err_text3 =site.find_element("xpath", selector_error)

    assert err_text3.text == "401"

def test_step2(site, selector_login, selector_passwd, selector_button, selector_home):
    input1 = site.find_element("xpath", selector_login)
    input1.send_keys(testdata.get("username"))
    
    input2 = site.find_element("xpath", selector_passwd)
    input2.send_keys(testdata.get("password"))
    
    btn = site.find_element("css", selector_button)
    btn.click()

    home_path = site.find_element("xpath", selector_home)

    assert home_path.text == "Home", "test FAIL"


if __name__ == "__main__":
    pytest.main(["-vv"])