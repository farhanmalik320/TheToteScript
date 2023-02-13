import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    input_email_by_name = "email"
    input_password_by_name = "password"
    click_signin_btn_xpath= "(//button[@type='submit'])[1]"
    get_pin_text_xpath= "//div[contains(text(),'Enter login PIN')]"
    input_otp_fields_xpath= "//input[@aria-label='Character 1.']"
    click_verify_btn_xpath= "//button[normalize-space()='Verify']"
    get_profile_text_xpath= "//div[contains(text(),'My Profile')]"

    def __init__(self, driver):
        self.driver = driver

    def setuserEmail(self, email):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_email_by_name))).send_keys(email)

    def setPassword(self, password):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_password_by_name)))

        self.driver.find_element(By.NAME, self.input_password_by_name).send_keys(password)

    def click_login_btn(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.click_signin_btn_xpath))).click()

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

    def get_profile_text(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.get_profile_text_xpath)))
        get_verify_text = self.driver.find_element(By.XPATH, self.get_profile_text_xpath)
        return get_verify_text.text

