from selenium.webdriver.common.by import By


class LoginLocators:
    Email = (By.NAME, "username")
    Password = (By.NAME, "password")
    Login_Button = (By.TAG_NAME, "button")
    Invalid_Credential='//p[text()="Invalid credentials"]'
    SignUP_Link = (By.LINK_TEXT, "OrangeHRM, Inc")