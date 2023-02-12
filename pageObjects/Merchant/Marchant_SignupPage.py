from selenium.webdriver.common.by import By
import time

class Marchantsignup:
    baseurl="https://develop.dc4234a3ywtax.amplifyapp.com/signup"
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
        time.sleep(2)
        self.driver.find_element(By.NAME,self.firstname_name).send_keys(firstname)


    def setlastName(self,lastname):
        time.sleep(2)
        self.driver.find_element(By.NAME, self.lastname_name).send_keys(lastname)

    def setEmail(self,email):
        time.sleep(2)
        self.driver.find_element(By.NAME, self.email_name).send_keys(email)

    def setPassword(self,password):
        time.sleep(2)
        self.driver.find_element(By.NAME, self. password_name).send_keys(password)


    def setConfirmPassword(self,conformpassword):
        time.sleep(2)
        self.driver.find_element(By.NAME, self.confirmpassword_name).send_keys(conformpassword)

    def setagreecheckbox(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.agreecheckbox_class).click()

    def setCreateAccountButton(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.creteaccountbutton_class).click()
