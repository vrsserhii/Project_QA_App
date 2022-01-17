"""Stores tests related to start page"""
import random
from time import sleep

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By


class TestStartPage:

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.choice(range(111111, 999999)))

    def test_login(self):
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver-2")
        # Open start page
        driver.get("https://www.aks.ua/index/login")
        # Find and clean Username field
        username = driver.find_element(by=By.XPATH, value=".//input[@id='login']")
        username.clear()
        sleep(0.5)
        username.send_keys(f"2074957@gmail.com")
        # Find and clean Password field
        password = driver.find_element(by=By.XPATH, value=".//input[@id='passwd']")
        password.clear()
        sleep(0.5)
        password.send_keys(f"5555544444")
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//input[@id='submit']")
        sleep(0.5)
        # Click button
        button.click()
        message = driver.find_element(by=By.XPATH, value=".//div[@class='header-user-text']")
        # Verify message
        assert message.text == "Здравствуйте"
        sleep(0.5)

    def test_valid_login(self):
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver-2")
        # Open start page
        driver.get("https://www.aks.ua/index/login")
        # Find and clean Username field
        username = driver.find_element(by=By.XPATH, value=".//input[@id='login']")
        username.clear()
        sleep(0.5)
        username.send_keys(f"Serg")
        # Find and clean Password field
        password = driver.find_element(by=By.XPATH, value=".//input[@id='passwd']")
        password.clear()
        sleep(0.5)
        password.send_keys(f"555444")
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//input[@id='submit']")
        sleep(0.5)
        # Click button
        button.click()
        message = driver.find_element(by=By.XPATH, value=".//p[@class='error']")
        # Verify message
        assert message.text == "Неверный пароль. Возможно, Вы забыли пароль?"
        sleep(0.5)

    def test_login_username_invalid(self):
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver-2")
        # Open start page
        driver.get("https://www.aks.ua/profile/save")
        # Find and clean Email
        email = driver.find_element(by=By.XPATH, value=".//*[@id='email']")
        email.clear()
        sleep(0.5)
        email.send_keys(f"ser@gmail.com")
        # Find and clean Username field
        username = driver.find_element(by=By.XPATH, value=".//*[@id='fullname']")
        username.clear()
        sleep(0.5)
        # Find and clean Password field
        password = driver.find_element(by=By.XPATH, value=".//*[@id='passwd1']")
        password.clear()
        sleep(0.5)
        password.send_keys(f"444555")
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//*[@id='submit']")
        sleep(0.5)
        # Click button
        button.click()
        # Error message
        message = driver.find_element(by=By.XPATH, value=".//p[2][@class='error']")
        # Verify message
        assert message.text == "Заполните Имя"

    def test_login_password_invalid(self):
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver-2")
        # Open start page
        driver.get("https://www.aks.ua/profile/save")
        # Find and clean Email
        email = driver.find_element(by=By.XPATH, value=".//*[@id='email']")
        email.clear()
        sleep(0.5)
        email.send_keys(f"ser@gmail.com")
        # Find and clean Password field
        password = driver.find_element(by=By.XPATH, value=".//*[@id='passwd1']")
        password.clear()
        sleep(0.5)
        # Find and clean Username field
        username = driver.find_element(by=By.XPATH, value=".//*[@id='fullname']")
        username.clear()
        sleep(0.5)
        username.send_keys(f"Serg")
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//*[@id='submit']")
        sleep(0.5)
        # Click button
        button.click()
        # Error message
        message = driver.find_element(by=By.XPATH, value=".//p[1][@class='error']")
        # Verify message
        assert message.text == "Заполните пароль"

    def test_invalid_registration_page(self):
        """Sample test"""
        # Create driver
        driver = webdriver.WebDriver(executable_path="./drivers/chromedriver-2.exe")
        # Open start page
        driver.get("https://www.aks.ua/profile/save")
        sleep(0.5)
        # Find and clean Email
        email = driver.find_element(by=By.XPATH, value=".//*[@id='email']")
        email.clear()
        sleep(0.5)
        email.send_keys()
        # Find and clean Password field
        password = driver.find_element(by=By.XPATH, value=".//*[@id='passwd1']")
        password.clear()
        sleep(0.5)
        password.send_keys()
        # Find and clean Username field
        username = driver.find_element(by=By.XPATH, value=".//*[@id='fullname']")
        username.clear()
        sleep(0.5)
        username.send_keys()
        # Find Sign In button
        button = driver.find_element(by=By.XPATH, value=".//*[@id='submit']")  # ".//input[text()='Регистрация']"
        # Click button
        button.click()
        sleep(0.5)
        message = driver.find_element(by=By.XPATH, value=".//p[4][@class='error']")
        # Verify message
        assert message.text == "Заполните Контактный телефон"
