from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Marchantsignup:

    firstname_name="firstName"
    lastname_name="lastName"
    email_name="email"
    password_name="password"
    confirmpassword_name="confirmPassword"
    agreecheckbox_class="//button[@value='on']"
    creteaccountbutton_class="//button[@class='c-leIVPW c-leIVPW-lbzlto-size-lg c-leIVPW-MnczI-color-red']"

    def __init__(self,driver):
        self.driver=driver

    def setfirstName(self,firstname):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.firstname_name))).send_keys(firstname)


    def setlastName(self,lastname):
        self.driver.find_element(By.NAME, self.lastname_name).send_keys(lastname)

    def setEmail(self,email):
        self.driver.find_element(By.NAME, self.email_name).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.NAME, self. password_name).send_keys(password)

    def setConfirmPassword(self,confirmpassword):
        self.driver.find_element(By.NAME, self.confirmpassword_name).send_keys(confirmpassword)

    def setagreecheckbox(self):
        self.driver.find_element(By.XPATH, self.agreecheckbox_class).click()

    def setCreateAccountButton(self):
        self.driver.find_element(By.XPATH, self.creteaccountbutton_class).click()
