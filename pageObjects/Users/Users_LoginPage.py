import time
from selenium.webdriver.common.by import By

class LoginPage:

    input_email_name= "email"
    input_password_name= "password"
    click_signin_btn_xpath= "(//button[@type='submit'])[1]"
    get_pin_text_xpath= "//div[contains(text(),'Enter login PIN')]"
    input_otp_fields_xpath= "//input[@aria-label='Character 1.']"
    click_verify_btn_xpath= "//button[normalize-space()='Verify']"
    get_profile_text_xpath= "//div[contains(text(),'My Profile')]"

    def __init__(self, driver):
        self.driver = driver

    def setuserEmail(self, Email):

        self.driver.find_element(By.NAME, self.input_email_name).send_keys(Email)

    def setPassword(self, Password):
        self.driver.find_element(By.NAME, self.input_password_name).send_keys(Password)

    def click_login_btn(self):

        self.driver.find_element(By.XPATH, self.click_signin_btn_xpath).click()

    def get_enterPin_msg(self):

        enter_pin= self.driver.find_element(By.XPATH, self.get_pin_text_xpath)
        return enter_pin.text

    def input_otpcode(self, tp_code):

        self.driver.find_element(By.XPATH, self.input_otp_fields_xpath).send_keys(tp_code)

    def click_verify_btn(self):
        self.driver.find_element(By.XPATH, self.click_verify_btn_xpath).click()

    def get_profile_text(self):
        get_verify_text = self.driver.find_element(By.XPATH, self.get_profile_text_xpath)
        return get_verify_text.text

