import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.product_page import ProductPage

class TestCheckout:
    
    def test_checkout_process(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")

        home_page = HomePage(driver)
        assert home_page.get_title() == "Swag Labs"

        home_page.add_product_to_cart("Sauce Labs Backpack")
        home_page.go_to_cart()

        # Aquí agregarías la lógica para completar el proceso de checkout
        # (por ejemplo, ingresar datos de envío, confirmar la compra, etc.)
