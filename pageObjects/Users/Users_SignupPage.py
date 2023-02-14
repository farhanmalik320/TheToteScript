import time
from Configurations.Config import testdata
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:

    input_email_by_name= "email"
    input_password_by_name= "password"
    input_confirm_password_by_name= "confirmPassword"
    click_getstartedbtn_by_xpath = "//button[normalize-space()='Get Started']"
    get_verify_email_text_by_xpath= "//div[contains(text(),'Check Your Email')]"
    user_email= testdata.user_signup_email
    click_confirm_btn_xpath= "//span[contains(text(),'Confirm My Email')]"


    def __init__(self, driver):
        self.driver = driver

    def setuserEmail(self, email):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_email_by_name))).send_keys(email)

    def setPassword(self, password):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_password_by_name))).send_keys(password)

    def setConfirm_Password(self, confirm_Password):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_confirm_password_by_name))).send_keys(confirm_Password)

    def click_started_button(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.click_getstartedbtn_by_xpath))).click()

    def get_verify_email_msg(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.get_verify_email_text_by_xpath)))
        verify_email= self.driver.find_element(By.XPATH, self.get_verify_email_text_by_xpath)
        return verify_email.text

    def open_email_URL(self):

        # execute JavaScript to open a new tab and switch to it
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        # navigate to the second URL
        self.driver.get("https://www.yopmail.com")

        enter_email= WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='login']")))
        enter_email.clear()
        enter_email.send_keys(self.user_email)
        enter_email.send_keys(Keys.RETURN)

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'ifmail')))

        iframe_by_title = self.driver.find_element(By.ID, "ifmail")

        self.driver.switch_to.frame(iframe_by_title)

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, self.click_confirm_btn_xpath))).click()

        time.sleep(5)

        #self.driver.switch_to.window(self.driver.window_handles[2])

