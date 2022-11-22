import random

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:
    def test_create_account_failed(self):
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account("asd@asd.pl", "aGp615904!")

        error_msg = "Error: An account is already registered with your email address. Please log in."
        assert error_msg in my_account_page.get_error_message()

    def test_create_account_passed(self):
        str(random.randint(0, 10000)) + "asd@asd.pl"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(str(random.randint(0, 10000)) + "asd@asd.pl", "aGp615904!")
        assert my_account_page.is_logout_link_displayed()

