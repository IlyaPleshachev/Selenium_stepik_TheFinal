from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "#login_form > button")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "#register_form > button")