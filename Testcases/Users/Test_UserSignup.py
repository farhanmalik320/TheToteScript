import time
from Configurations.Config import testdata
from pageObjects.Users.Users_SignupPage import SignupPage
from Testcases.test_base import BaseTest
import datetime
import json

class Test_Signup(BaseTest):

    baseURL = testdata.user_signup_url
    email = testdata.user_signup_email
    password = testdata.user_password
    confirm_Password = testdata.confirm_password

    def test_signupForm(self):
        self.driver.get(self.baseURL)
        self.driver.obj = SignupPage(self.driver)
        self.driver.obj.setuserEmail(self.email)
        self.driver.obj.setPassword(self.password)
        self.driver.obj.setConfirm_Password(self.confirm_Password)

        # Click the "Get Started" button
        self.driver.obj.click_started_button()

        # check the API and print the response of the API
        time.sleep(3)

        try:
            verify_email_msg= self.driver.obj.get_verify_email_msg()
            if verify_email_msg== "Check Your Email":
                print("Successfully Registered")
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

                response = request.response.body
                # store the response json in the variable
                # convert response to JSON
                response_body = json.loads(response)

                if request.response.status_code==400:

                    # extract the verification code from the response
                    message = response_body["error"]["message"]
                    print("Test case fail", message)
                    now = datetime.datetime.now()
                    file_name = "Users-" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".png"
                    self.driver.get_screenshot_as_file("C:\\Users\\cva\\PycharmProjects\\TheTote\\Screenshots\\"+  file_name)
                    print("A screenshot was saved as " + file_name)
                else:
                    # extract the verification code from the response
                    message = response_body["message"]
                    print("Test case Pass", message)
                    self.driver.obj.open_email_URL()
