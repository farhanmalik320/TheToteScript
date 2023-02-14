from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MacrhantLogin:

    textbox_email_name = "email"
    textbox_password_name = "password"
    button_login_xpath = "//button[@class='c-leIVPW c-leIVPW-lbzlto-size-lg c-leIVPW-MnczI-color-red c-leIVPW-ikJzvVT-css']"
    get_pin_text_xpath = "//div[contains(text(),'Enter login PIN')]"
    input_otp_fields_xpath = "//input[@aria-label='Character 1.']"
    click_verify_btn_xpath = "//button[normalize-space()='Verify']"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,email):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.textbox_email_name))).send_keys(email)

    def setPassword(self,password):
        # self.driver.find_element(By.ID, self.textbox_password_name).clear()
        self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def get_enterPin_msg(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.get_pin_text_xpath)))
        enter_pin= self.driver.find_element(By.XPATH, self.get_pin_text_xpath)
        return enter_pin.text

    def input_otpcode(self, tp_code):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.input_otp_fields_xpath)))
        self.driver.find_element(By.XPATH, self.input_otp_fields_xpath).send_keys(tp_code)

    def click_verify_btn(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.click_verify_btn_xpath)))
        self.driver.find_element(By.XPATH, self.click_verify_btn_xpath).click()















