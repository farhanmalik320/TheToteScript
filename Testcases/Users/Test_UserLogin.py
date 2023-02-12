import time  # Importing the time module
import pytest
from Configurations.Config import testdata
from pageObjects.Users.Users_LoginPage import LoginPage
from Testcases.test_base import BaseTest
import datetime
import json

class Test_Login(BaseTest):
    # Declaring class level variables for URL, email and password
    baseURL = testdata.user_login_url
    email = testdata.user_email
    password = testdata.user_password

    # Test method to test the login functionality
    @pytest.fixture
    def test_Login(self):
        # Navigating to the login page
        self.driver.get(self.baseURL)
        # Creating the object of the LoginPage class
        self.driver.obj = LoginPage(self.driver)
        time.sleep(2)  # Pausing execution for 2 seconds
        # Setting the email
        self.driver.obj.setuserEmail(self.email)
        # Setting the password
        self.driver.obj.setPassword(self.password)
        # Clicking on the login button
        self.driver.obj.click_login_btn()

        # check the API and print the response of the API
        time.sleep(3)  # Pausing execution for 3 seconds

        # Checking if the Enter Login PIN message is displayed

        try:
            verify_email_msg= self.driver.obj.get_enterPin_msg()
            if verify_email_msg== "Enter login PIN":
                print("Redirected to the PIN screen...")
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
                if request.response.status_code==200:
                    print("Test case Pass")

                    response = request.response.body

                    # store the response json in the variable
                    # convert response to JSON
                    response_body = json.loads(response)

                    # extract the verification code from the response
                    verification_code = response_body["data"]["verificationCode"]

                    print(verification_code)

                else:
                    print("Test case fail")
                    now = datetime.datetime.now()
                    file_name = "Users-" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
                    self.driver.get_screenshot_as_file(
                        "\\Screenshots\\" + file_name)
                    print("A screenshot was saved as " + file_name)

        return verification_code


    def test_EnterPin(self, test_Login):

        if not test_Login:
            pytest.skip("test_Login failed, skipping test_EnterPin")

        self.driver.obj = LoginPage(self.driver)
        time.sleep(2)
        self.driver.obj.input_otpcode(test_Login)
        time.sleep(2)
        self.driver.obj.click_verify_btn()
        time.sleep(2)

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
                if request.response.status_code == 200:
                    print("Test case Pass")

                else:
                    print("Test case fail")
                    now = datetime.datetime.now()
                    file_name = "Users-InputPin" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
                    self.driver.get_screenshot_as_file(
                        "\\Screenshots\\" + file_name)
                    print("A screenshot was saved as " + file_name)