from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InvitePage:

    menu_btn_class= "dropdown"
    invite_friend_menu= "dropdown-item"
    copy_btn_xpath= "//*[name()='rect' and contains(@opacity,'0.2')]"
    history_tab_class= "button-one"

    def __init__(self,driver):
        self.driver= driver

    def clickmenubutton(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.menu_btn_class)))
        element.click()

    def clickselectinvite(self):
        invite_friends = self.driver.find_elements(By.CLASS_NAME, self.invite_friend_menu)
        time.sleep(1)
        invite_friends[1].click()

    def clickcopybutton(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.copy_btn_xpath)))
        element.click()

    def clickhistorytab(self):
        self.driver.find_element(By.CLASS_NAME, self.history_tab_class).click()