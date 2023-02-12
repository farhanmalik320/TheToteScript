import datetime

from pageObjects.Merchant.Marchant_LoginPage import MacrhantLogin
from testCases.test_base import BaseTest
import time

class Test_01_MarchantLogin(BaseTest):

    baseURL = "https://develop.dc4234a3ywtax.amplifyapp.com/login/"
    usrername = "sohail.merchant@yopmail.com"
    password = "Abc1234#"

    def test_MarchantLogin(self):
        self.driver.get(self.baseURL)
        self.lp = MacrhantLogin(self.driver)
        self.lp.setUserName(self.usrername)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

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









