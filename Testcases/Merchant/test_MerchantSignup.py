from pageObjects.Merchant.Marchant_SignupPage import Marchantsignup
import time
import datetime
from Testcases.test_base import MerchantTest
from Configurations.Config import testdata
import json

class Test_MerchantSignup(MerchantTest):

    #app url
    baseURL = testdata.merchant_signup_url

    #form data
    firstname = testdata.merchant_firstname
    lastname = testdata.merchant_lastname
    email= testdata.merchant_signup_email
    password=testdata.merchant_password
    confirm_password= testdata.merchant_password

    def test_Marchantsignup(self):
        self.driver.get(self.baseURL)
        self.lp = Marchantsignup(self.driver)
        self.lp.setfirstName(self.firstname)
        self.lp.setlastName(self.lastname)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.setConfirmPassword(self.confirm_password)
        self.lp.setagreecheckbox()
        self.lp.setCreateAccountButton()

        time.sleep(3)
        for request in self.driver.requests:
            if request.response and '/api/' in request.url:
                print(
                    request.url,
                    request.response.status_code,
                    request.response.body
                )
                if request.response.status_code == 400:

                    response = request.response.body
                    # store the response json in the variable
                    # convert response to JSON
                    response_body = json.loads(response)

                    # extract the verification code from the response
                    message = response_body["error"]["message"]

                    print("Test case fail because ," + message)
                    now = datetime.datetime.now()
                    file_name = "Merchants-" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
                    self.driver.get_screenshot_as_file(
                        "Screenshots\\" + file_name)
                    print("A screenshot was saved as " + file_name)
                else:
                    response = request.response.body
                    # store the response json in the variable
                    # convert response to JSON
                    response_body = json.loads(response)

                    # extract the verification code from the response
                    message = response_body["message"]
                    print("Test case Pass", message )