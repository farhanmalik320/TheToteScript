from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactusPage:

    contact_us_xpath= "//a[contains(text(),'Contact us')]"
    name_field_name= "name"
    email_field_name= "email"
    message_field_name= "message"
    submit_btn_xpath= "//button[contains(text(),'Submit')]"

    def __init__(self,driver):
        self.driver= driver

    def clickcontactus(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.contact_us_xpath)))
        element.click()

    def entername(self, name):
        name_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, self.name_field_name)))
        name_field.send_keys(name)

    def enteremail(self, email):
        email_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, self.email_field_name)))
        email_field.send_keys(email)

    def entermessage(self, message):
        message_field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, self.message_field_name)))
        message_field.send_keys(message)

    def clicksubmit(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.submit_btn_xpath)))
        self.driver.execute_script('arguments[0].click()', element)