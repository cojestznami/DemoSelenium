from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random
import pytest
from selenium.webdriver.support.select import Select

from pages.billing_address_page import BillingAddressPage
from pages.my_account_page import MyAccountPage


@pytest.mark.usefixtures("setup")
class TestUpdateBillingAddress:

    def test_update_billing_address(self):
        email = str(random.randint(0, 10000)) + "asd@asd.pl"
        my_account_page = MyAccountPage(self.driver)
        my_account_page.open_page()
        my_account_page.create_account(email, "aGp615904!")
        billing_adres_page = BillingAddressPage(self.driver)
        billing_adres_page.open_edit_billing_adres()
        billing_adres_page.set_personal_data("Dżon", "Doł")
        billing_adres_page.select_country("Poland")
        billing_adres_page.set_address("Womanowa 2", "23-233", "Warszawa")
        billing_adres_page.set_phone_number("345 456 456")
        billing_adres_page.save_address()
        assert "Address changed successfully." in billing_adres_page.get_message_text()
