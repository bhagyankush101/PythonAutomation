from selenium.webdriver.common.by import By

class MyInfoLocators:
    My_info = (By.LINK_TEXT, 'My Info')
    Profile_Picture = (By.XPATH, "(//img[@alt='profile picture'])[2]")
    Picture_upload_details = "//p[@class='oxd-text oxd-text--p orangehrm-input-hint']"
    Tax_Exemptions=(By.LINK_TEXT,"Tax Exemptions")
    state='//div[@class="oxd-form-row"]//div[@class="oxd-select-text-input"]'
    Add_button_Upload_File=(By.XPATH,'//div[@class="orangehrm-attachment"]//button[text()=" Add "]')
    upload_file='//input[@type="file"]'
    save_button=(By.XPATH,'(//button[text()=" Save "])[3]')
    ErrorMessage="span.oxd-text.oxd-text--span.oxd-input-field-error-message.oxd-input-group__message"
