import time
from selenium.webdriver.common.by import By

class SignupPage:

    email_name= "email"
    password_name= "password"
    confirm_password_name= "confirmPassword"
    Click_getstarted_butoon_xpath = "//button[normalize-space()='Get Started']"
    otp_code_by_clname = "//*[@id='root']/div[2]/div/div/form/div[4]/input[1]"
    Verify_button_click_xpath="//*[@id='root']/div[2]/div/div/form/div[6]/button"
    success_message_class= "//div[contains(text(),'Email is already registered')]"
    sucess_msg_class= "body.dark-theme:nth-child(2) div.Toastify div.Toastify__toast-container.Toastify__toast-container--top-right div.Toastify__toast.Toastify__toast-theme--light.Toastify__toast--error.Toastify__toast--close-on-click div.Toastify__toast-body > div:nth-child(2)"
    verify_email_xpath= "//div[contains(text(),'Check Your Email')]"

    def __init__(self, driver):
        self.driver = driver

    def setuserEmail(self, Email):

        self.driver.find_element(By.NAME, self.email_name)
        self.driver.find_element(By.NAME, self.email_name).send_keys(Email)

    def setPassword(self, Password):
        self.driver.find_element(By.NAME, self.password_name).clear()
        self.driver.find_element(By.NAME, self.password_name).send_keys(Password)

    def setConfirm_Password(self, confirm_Password):
        password_field = self.driver.find_element(By.NAME, self.confirm_password_name)
        password_field.clear()
        self.driver.find_element(By.NAME, self.confirm_password_name).send_keys(confirm_Password)

    def click_started_button(self):
        self.driver.find_element(By.XPATH, self.Click_getstarted_butoon_xpath).click()

    def get_success_message(self):
        success_message= self.driver.find_element(By.XPATH, self.success_message_class)
        return success_message.text

    def get_verify_email_msg(self):

        verify_email= self.driver.find_element(By.XPATH, self.verify_email_xpath)
        return verify_email.text

    def Otp_code(self, tp_code):
        self.driver.find_element(By.XPATH, self.otp_code_by_clname)
        self.driver.find_element(By.XPATH, self.otp_code_by_clname).click()
        self.driver.find_element(By.XPATH, self.otp_code_by_clname).send_keys(tp_code)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.otp_code_by_clname).click()




