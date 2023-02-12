from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class MacrhantLogin:
    textbox_email_name = "email"
    textbox_password_name = "password"
    button_login_xpath = "//button[@class='c-leIVPW c-leIVPW-lbzlto-size-lg c-leIVPW-MnczI-color-red c-leIVPW-ikJzvVT-css']"
    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,usrername):
        # time.sleep(2)
        # self.driver.find_element(By.CLASS_NAME, self.textbox_email_class).clear()
        time.sleep(4)
        self.driver.find_element(By.NAME, self.textbox_email_name).send_keys(usrername)

    def setPassword(self,password):
        # self.driver.find_element(By.ID, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()















