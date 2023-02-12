
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:
    main_signup_btn_xpath= "//button[contains(text(),'SIGN UP')]"
    email_field_name= "email"
    password_field_name= "password"
    referal_code_field_name= "referred_by"
    checkbox_name= "privacypolicy"
    signup_btn_class= "mt-3"

    def __init__(self,driver):
        self.driver= driver

    def clickMainSignup(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.main_signup_btn_xpath)))
        element.click()

    def enterEmail(self, email):
        self.driver.find_element(By.NAME,self.email_field_name).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element(By.NAME,self.password_field_name).send_keys(password)

    def enterRefercode(self, referalcode):
        self.driver.find_element(By.NAME, self.referal_code_field_name).send_keys(referalcode)

    def clickCheckbox(self):
        self.driver.find_element(By.NAME, self.checkbox_name).click()

    def clickSignup(self):
        self.driver.find_element(By.CLASS_NAME, self.signup_btn_class).click()