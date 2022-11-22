from selenium import webdriver
from selenium.webdriver.common.by import By


def test_log_in_pass():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://seleniumdemo.com")
    driver.find_element(By.XPATH, "//li[@id = 'menu-item-22']//a").click()
    driver.find_element(By.ID, "username").send_keys("asd@asd.pl")
    driver.find_element(By.ID, "password").send_keys("aGp615904!")
    driver.find_element(By.NAME, "login").click()
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()


def test_log_in_failed():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://seleniumdemo.com")
    driver.find_element(By.XPATH, "//li[@id = 'menu-item-22']//a").click()
    driver.find_element(By.ID, "username").send_keys("asd@asd.pl")
    driver.find_element(By.ID, "password").send_keys("aGp615905!")
    driver.find_element(By.NAME, "login").click()
    assert 'ERROR: Too many failed login' in driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/article/div/section/div/div/div[1]/ul/li").text
