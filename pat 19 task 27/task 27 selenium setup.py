from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.username_locator = (By.ID, "txtUsername")
        self.password_locator = (By.ID, "txtPassword")
        self.login_button_locator = (By.ID, "btnLogin")

    def login(self, username, password):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_locator)).send_keys(username)
        self.driver.find_element(*self.password_locator).send_keys(password)
        self.driver.find_element(*self.login_button_locator).click()