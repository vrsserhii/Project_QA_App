"""Stores tests related to start page"""

import pytest
from selenium.webdriver.chrome import webdriver

from conftest import BaseTest
from constants.base import BaseConstants
from pages.start_page import StartPage


class TestStartPage(BaseTest):

    @pytest.fixture(scope="function")
    def driver(self):
        """Create and return driver and close after test"""
        driver = webdriver.WebDriver(BaseConstants.DRIVER_PATH)
        driver.implicitly_wait(1)  # Ожидание 1с
        yield driver
        driver.close()

    @pytest.fixture(scope="function")
    def start_page(self, driver):
        """Return Start Page"""
        driver.get(BaseConstants.URL)
        return StartPage(driver)

    @pytest.fixture(scope="function")
    def start_page_1(self, driver):
        """Return Start Page"""
        driver.get(BaseConstants.URL_1)
        return StartPage(driver)

    @pytest.fixture(scope="function")
    def registered_user(self, start_page):
        """Registered User and return Data"""
        username_value = "Serg"
        email_value = "2074957@gmail.com"
        password_value = "5555544444"
        """Fill email, login and password"""

        return email_value, username_value, password_value

    def test_valid_login(self, start_page, registered_user):
        """
        - Preconditions:
            - Open start page
            - Registered user
        - Steps:
            - Fill valid Username, password values
            - Click on sign in button
            - Verify message
        """
        # Init User data from fixture
        email_value, _, password_value = registered_user
        # fill valid values
        main_page = start_page.login(email_value, password_value)
        # fill valid values
        #  main_page = start_page.login("2074957@gmail.com", "5555544444")
        self.log.info("Fields are filled valid USERNAME and PASSWORD")
        # verify 'welcome' message
        main_page.verify_welcome_message()
        self.log.info("Welcome message was received")

    def test_login_username_invalid(self, start_page):
        """
        - Preconditions:
            - Open start page
        Steps:
            - Fill invalid Username, valid password value
            - Click on sign in button
            - Verify Error message
        """
        # fill invalid username
        start_page.login(" ", "555444")
        self.log.info("Fields are filled invalid USERNAME")
        # verify error message
        start_page.verify_incorrect_login()
        self.log.info("Error message Invalid USERNAME appears")

    def test_login_password_invalid(self, start_page):
        """
        - Preconditions:
            - Open start page
        Steps:
            - Fill invalid Password, valid Username value
            - Click on sign in button
            - Verify Error message
        """
        # fill invalid password
        start_page.login("Serg", " ")
        self.log.info("Fields are filled invalid PASSWORD")
        # verify error  message
        start_page.verify_incorrect_login()
        self.log.info("Error message Invalid PASSWORD appears")

    def test_login_invalid(self, start_page):
        """
        - Preconditions:
            - Open start page
        Steps:
            - Fill empty value Username and Password
            - Click on sign in button
            - Verify Error message
        """
        # fill invalid password
        start_page.login(" ", " ")
        self.log.info("Fields are filled empty Data")
        # verify error  message
        start_page.verify_incorrect_login()
        self.log.info("Error message Invalid login appears")

    def test_invalid_registration_page(self, start_page_1):
        """
        - Preconditions:
            - Open start page
        Steps:
            - Fill Username, email, password fields
            - Click on Register button
            - Verify message
        """
        username_value = f""
        email_value = f""
        password_value = f""
        # fill username, email, password fields
        main_page = start_page_1.register(username_value, email_value, password_value)
        self.log.info("User don't registered ")
        # Verify invalid registered
        main_page.verify_incorrect_register()
        self.log.info("Invalid Registration test passed")
