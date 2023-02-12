from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    main_login_btn_xpath= "//button[contains(text(),'LOGIN')]"
    email_field_name= "email"
    password_field_name= "password"
    login_btn_xpath= "//button[contains(text(),'Login')]"

    def __init__(self,driver):
        self.driver= driver

    def clickMainlogin(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.main_login_btn_xpath)))
        element.click()

    def enterEmail(self, email):
        self.driver.find_element(By.NAME,self.email_field_name).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element(By.NAME,self.password_field_name).send_keys(password)

    def clickLoginbtn(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()