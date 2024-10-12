from selenium import webdriver

def test_login():
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000/login")
    driver.find_element_by_name("username").send_keys("user")
    driver.find_element_by_name("password").send_keys("pass")
    driver.find_element_by_name("submit").click()
    assert "Welcome" in driver.page_source
    driver.quit()
