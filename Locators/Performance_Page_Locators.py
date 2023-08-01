from selenium.webdriver.common.by import By

class PerformancePageLocators:

    HEADER = (By.CSS_SELECTOR, "h6.oxd-text")
    Configure = (By.XPATH, '//span[text()="Configure"]')
    configure_tab = (By.XPATH, "(//span[@class='oxd-topbar-body-nav-tab-item'])[1]")
    KPIs = (By.XPATH, "//ul[@class='oxd-dropdown-menu']//li//a[contains(text(),'KPIs')]")
    select_all_Key_PerformanceIndicator = '//div[@class="oxd-table-header-cell oxd-padding-cell oxd-table-th"]//input'
    Delete_Selected = (By.XPATH,'//*[text()=" Delete Selected "]')