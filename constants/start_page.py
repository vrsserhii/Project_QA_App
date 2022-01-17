class StartPageConstants:
    # SIGN_REG
    SIGN_UP_USERNAME_XPATH = ".//*[@id='fullname']"
    SIGN_UP_EMAIL_XPATH = ".//*[@id='email']"
    SIGN_UP_PASSWORD_XPATH = ".//*[@id='passwd1']"
    SIGN_UP_BUTTON_XPATH = ".//*[@id='submit']"
    # SIGN_IN
    SIGN_IN_USERNAME_XPATH = ".//input[@id='login']"
    SIGN_IN_PASSWORD_XPATH = ".//input[@id='passwd']"
    SIGN_IN_BUTTON_XPATH = ".//input[@id='submit']"
    SIGN_IN_ERROR_MESSAGE_TEXT = "Неверный пароль. Возможно, Вы забыли пароль?"
    SIGN_IN_ERROR_MESSAGE_XPATH = ".//p[@class='error']"
