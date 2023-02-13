import time  # Importing the time module
import pytest
from Configurations.Config import testdata
from pageObjects.Users.Users_LoginPage import LoginPage
from Testcases.test_base import BaseTest
import datetime
import json

from pageObjects.Users.Users_ProfilePage import ProfilePage


class Test_Profile(BaseTest):
    # Declaring class level variables for URL, email and password
    baseURL = testdata.user_login_url
    email = testdata.user_login_email
    password = testdata.user_password
    first_name = "hello"
    last_name= "world"
    phone_no= "9123456754"
    country= "Pakistan"

    #add address data
    name_address= "testing"
    phone_no_address= "9123456754"
    email_address= "test@yopmail.com"
    pin_code_address= "12345"
    address_type= "Str"
    address_one= "House 720"
    address_two= "Isb"
    landmark= "Mosque"
    city= "rwp"
    state= "rwp"
    save_address_btn_xpath= "//button[normalize-space()='Save Address']"

    #change password data
    current_password= "Farhan@1234"
    new_password= "Farhan@1234"
    confirm_password= "Farhan@1234"

    def check_api_response(self, request, scenario):
        if request.response and '/api/' in request.url:
            print(
                request.url,
                request.response.status_code,
                request.response.body
            )
            if request.response.status_code == 400:
                print("API Test case Fail")
                now = datetime.datetime.now()
                file_name = scenario + now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
                self.driver.get_screenshot_as_file(
                    "Screenshots\\" + file_name)
                print("A screenshot was saved as " + file_name)

            else:
                print("API Test case Pass")

    # Test method to test the login functionality
    @pytest.fixture
    def test_Login(self):
        # Navigating to the login page
        self.driver.get(self.baseURL)
        # Creating the object of the LoginPage class
        self.driver.obj = LoginPage(self.driver)

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
                    print("API Test case Pass")

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
                    file_name = "Users-Login" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
                    self.driver.get_screenshot_as_file(
                        "\\Screenshots\\" + file_name)
                    print("A screenshot was saved as " + file_name)

        return verification_code

    def test_EnterPin(self, test_Login):

        if not test_Login:
            pytest.skip("test_Login failed, skipping test_EnterPin")

        self.driver.obj = LoginPage(self.driver)
        self.driver.obj.input_otpcode(test_Login)
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
            self.check_api_response(request, "Users-EnterPin")

    @pytest.mark.skip
    def test_userDetails(self):
        self.driver.obj = ProfilePage(self.driver)
        self.driver.obj.enter_firstname(self.first_name)
        self.driver.obj.enter_lastname(self.last_name)
        self.driver.obj.enter_phone(self.phone_no)
        self.driver.obj.click_country_dropdown()
        self.driver.obj.select_country_dropdown(self.country)
        self.driver.obj.select_gender()
        self.driver.obj.click_save_btn()
        time.sleep(3)

        # check the API and print the response of the API
        for request in self.driver.requests:
            self.check_api_response(request, "Users-Details")

    @pytest.mark.skip
    def test_userAddress(self):

        self.driver.obj = ProfilePage(self.driver)
        self.driver.obj.select_address_tab()
        self.driver.obj.click_add_Address()
        self.driver.obj.enter_address(self.name_address, self.phone_no_address, self.email_address, self.pin_code_address, self.address_one, self.address_two, self.landmark, self.city, self.state)
        self.driver.obj.click_country_dropdown()
        self.driver.obj.select_addresstype(self.address_type)
        self.driver.obj.click_save_btn()
        time.sleep(5)

        # check the API and print the response of the API
        for request in self.driver.requests:
            self.check_api_response(request, "Users-Address")

    def test_ChangePassword(self):

        self.driver.obj = ProfilePage(self.driver)
        self.driver.obj.select_security_tab()
        self.driver.obj.enterPassword(self.current_password, self.new_password, self.confirm_password)
        self.driver.obj.click_save_btn()
        time.sleep(3)
        # check the API and print the response of the API
        # check the API and print the response of the API
        for request in self.driver.requests:
            self.check_api_response(request, "Users-ChangePass")