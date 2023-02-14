import datetime
from Configurations.Config import testdata
from pageObjects.Merchant.Marchant_LoginPage import MacrhantLogin
from Testcases.test_base import MerchantTest
import time
import json
import pytest

class Test_MarchantLogin(MerchantTest):

    baseURL = testdata.merchant_login_url
    merchant_email = testdata.merchant_login_email
    merchant_password = testdata.merchant_password

    # Test method to test the login functionality
    @pytest.fixture
    def test_MarchantLogin(self):
        self.driver.get(self.baseURL)
        self.lp = MacrhantLogin(self.driver)
        self.lp.setUserName(self.merchant_email)
        self.lp.setPassword(self.merchant_password)
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
                    if request.response.status_code == 200:
                        print("API Test case Pass")

                        response = request.response.body

                        # store the response json in the variable
                        # convert response to JSON
                        response_body = json.loads(response)

                        # extract the verification code from the response
                        verification_code = response_body["data"]["verificationCode"]

                        print(verification_code)

        return verification_code

    def test_EnterPin(self, test_MarchantLogin):

        if not test_MarchantLogin:
            pytest.skip("test_Login failed, skipping test_EnterPin")

        self.driver.obj = MacrhantLogin(self.driver)
        self.driver.obj.input_otpcode(test_MarchantLogin)
        self.driver.obj.click_verify_btn()
        time.sleep(3)

        # check the API and print the response of the API

        try:
            verify_myprofile_msg = self.driver.obj.get_profile_text()
            if verify_myprofile_msg == "My Profile":
                print("Successfully Login and My profile word is visible")
            else:
                print("Error")
        except Exception as e:
            print(e)

        for request in self.driver.requests:
            if request.response and '/api/' in request.url:
                print(
                    request.url,
                    request.response.status_code,
                    request.response.body
                )
                if request.response.status_code == 400:
                    print("API Test case Fail")
                    now = datetime.datetime.now()
                    file_name = "Merchant-InputPin" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
                    self.driver.get_screenshot_as_file(
                        "\\Screenshots\\" + file_name)
                    print("A screenshot was saved as " + file_name)

                else:
                    print("API Test case Pass")