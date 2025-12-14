import pytest
from pages.login_page import LoginPage
from utils.data_loader import load_test_data

class TestLogin:
    
    @pytest.mark.parametrize("username, password, expected", load_test_data("login_data.json"))
    def test_login(self, driver, username, password, expected):
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.login(username, password)
        assert login_page.get_login_result() == expected
