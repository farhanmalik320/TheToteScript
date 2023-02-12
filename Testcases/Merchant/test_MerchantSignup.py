
from pageObjects.Merchant.Marchant_SignupPage import Marchantsignup
import time
import datetime

from testCases.test_base import BaseTest


class Test_02_MarchantSignup(BaseTest):

    baseURL = "https://develop.dc4234a3ywtax.amplifyapp.com/signup"
    firstname = "gohar"
    lastname = "younas"
    email="gohar51@yopmail.com"
    password="Abc1234@"
    conformpassword="Abc1234@"
    # chechbox="

    def test_Marchantsignup(self):
        self.driver.get(self.baseURL)
        self.lp = Marchantsignup(self.driver)
        self.lp.setfirstName(self.firstname)
        self.lp.setlastName(self.lastname)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.setConfirmPassword(self.conformpassword)
        self.lp.setagreecheckbox()
        self.lp.setCreateAccountButton()

        time.sleep(5)
        for request in self.driver.requests:
            if request.response and '/api/' in request.url:
                print(
                    request.url,
                    request.response.status_code,
                    request.response.body
                )
                if request.response.status_code == 400:
                    print("Test case fail")
                    now = datetime.datetime.now()
                    file_name = "Merchants-" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
                    self.driver.get_screenshot_as_file(
                        "C:\\Users\\cva\\PycharmProjects\\TheTote\\Screenshots\\" + file_name)
                    print("A screenshot was saved as " + file_name)
                else:
                    print("Test case Pass")