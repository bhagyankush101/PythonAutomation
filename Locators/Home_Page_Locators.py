from selenium.webdriver.common.by import By

class HomePageLocators:
    HEADER = (By.CSS_SELECTOR, "h6.oxd-text")
    HELP_ICON = '//button[@class="oxd-icon-button"and @title="Help"]'
    PERFORMANCE_NAVBAR = (By.XPATH, '//a/span[text()="Performance"]')
    DASHBOARD_NAVBAR=(By.XPATH,'//a/span[text()="Dashboard"]')
    Admin_NAVBAR = (By.XPATH, '//a/span[text()="Admin"]')
    ORANGE_HRM = (By.LINK_TEXT, "OrangeHRM, Inc")
    My_info = (By.LINK_TEXT, 'My Info')
