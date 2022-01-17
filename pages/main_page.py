from constants.main_page import MainPageConstants
from pages.base import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.constants = MainPageConstants()

    def verify_welcome_message(self):
        """Verify Welcome user message """
        hello_message = self.wait_until_find_element(value=self.constants.WELCOME_MESSAGE_XPATH)
        assert hello_message.text == "Здравствуйте"  # assert f"Hello" in hello_message.text

    def verify_incorrect_register(self):
        """ Verify Error message invalid Register"""
        # Find incorrect message
        message = self.wait_until_find_element(value=self.constants.SIGN_UP_ERROR_MESSAGE_XPATH)
        # Verify message
        assert message.text == self.constants.SIGN_UP_ERROR_MESSAGE_TEXT  # "Заполните Контактный телефон"
