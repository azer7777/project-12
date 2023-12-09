import unittest
from unittest.mock import patch, MagicMock
from views.menu import Menu


class TestMenu(unittest.TestCase):
    def test_auth_menu_successful_login_management(self):
        with patch("builtins.input", side_effect=["1", "test_user", "test_password", "0"]), patch(
            "views.menu.authenticate", return_value=("Test User", "management")
        ), patch("views.menu.Menu.management_menu", MagicMock()):
            menu = Menu()
            menu.auth_menu()

    def test_auth_menu_successful_login_sales(self):
        with patch("builtins.input", side_effect=["1", "test_user", "test_password", "0"]), patch(
            "views.menu.authenticate", return_value=("Test User", "sales")
        ), patch("views.menu.Menu.sales_menu", MagicMock()):
            menu = Menu()
            menu.auth_menu()

    def test_auth_menu_successful_login_support(self):
        with patch("builtins.input", side_effect=["1", "test_user", "test_password", "0"]), patch(
            "views.menu.authenticate", return_value=("Test User", "support")
        ), patch("views.menu.Menu.support_menu", MagicMock()):
            menu = Menu()
            menu.auth_menu()

    def test_auth_menu_failed_login(self):
        with patch("builtins.input", side_effect=["1", "test_user", "wrong_password", "0"]), patch(
            "views.menu.authenticate", return_value=(None, None)
        ):
            menu = Menu()
            menu.auth_menu()
