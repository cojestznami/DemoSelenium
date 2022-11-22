import random

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_create_account_failed():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys("asd@asd.pl")
    driver.find_element(By.ID, "reg_password").send_keys("aGp615904!", Keys.ENTER)
    error_msg = "Error: An account is already registered with your email address. Please log in."
    assert error_msg in driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/article/div/section/div/div/div[1]/ul/li").text


def test_create_account_passed():
    str(random.randint(0, 10000)) + "asd@asd.pl"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys(str(random.randint(0, 10000)) + "asd@asd.pl")
    driver.find_element(By.ID, "reg_password").send_keys("aGp615904!", Keys.ENTER)
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()
