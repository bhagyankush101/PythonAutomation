import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:

     def __int__(self,driver):
        self.driver=driver

     def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(by_locator)).click()

     def do_send_keys(self,by_locator,text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

     def get_element_text(self,by_locator):
         element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
         return element.text

     def get_element_text1(self, by_locator):
         element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH, by_locator)))
         return element.text

     def is_visible(self,by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

     def get_title(self,title):
         WebDriverWait(self.driver,10).until(ec.title_is(title))
         return self.driver.title

     def select_dropdown_value_using_Select_Tag(self,by_locator,text):
         select = Select(by_locator)
         # select.select_by_value(text)
         option_list = select.options
         for ele in option_list:
             print(ele.text)
             if (ele.text == text):
                 ele.click()
                 break
     def select_dropdown_without_Select_tag(self,by_locator,text):
         element=self.driver.find_elements(by_locator)
         print(len(element))
         for ele in element:
            print(ele.text)
            if (ele.text == text):
                ele.click()
                break

     def clear_text(self,by_locator):
         WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).clear()

     def Mouse_Over_Element(self,by_locator):
             act = ActionChains(self.driver)
             act.move_to_element(self.driver.find_element(By.XPATH, by_locator)).perform()
     def scroll_down_towards_element(self,by_locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", by_locator)

     def do_click1(self,by_locator):
       # self.driver.find_elements(by_locator).click()
             act = ActionChains(self.driver)
             act.move_to_element(self.driver.find_element(By.XPATH,by_locator)).click().perform()

     def do_send_Keys1(self, by_locator,text):

             act = ActionChains(self.driver)
             act.move_to_element(self.driver.find_element(By.XPATH, by_locator)).send_keys(text).perform()



     def is_disabled(self,by_locator):
             element= self.driver.find_element(By.XPATH,by_locator).is_enabled()
             return bool(element)

     def get_Attribute_title(self,by_locator):
         element=self.driver.find_element(By.XPATH,by_locator)
         return element.get_attribute('title')