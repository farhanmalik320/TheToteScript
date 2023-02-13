import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:

    input_firstname_by_name = "firstName"
    input_lastname_by_name = "lastName"
    input_phone_no_by_name= "phoneNumber"
    click_dropdown_list_by_css= ".css-hlgwow"
    input_country_by_css= ".css-19bb58m"
    input_text_by_ID= "react-select-2-input"
    input_addresstype_by_XPATH= "(//input[@id='react-select-4-input'])[1]"
    click_save_btn_by_CSS= "button[type='submit']"
    click_female_by_css= "button[value='FEMALE']"
    click_male_by_css = "button[value='MALE']"
    click_address_tab_by_XPATH= "(//button[normalize-space()='Address List'])[1]"
    click_security_by_XPATH= "(//button[normalize-space()='Security'])[1]"
    click_Add_address_xpath= "//button[normalize-space()='Add Address']"
    input_name_address_by_name= "fullName"
    input_email_address_by_name="email"
    input_pincode_address_by_name= "pinCode"
    input_address_one_by_name= "addressOne"
    input_address_two_by_name= "addressTwo"
    input_landmark_by_name= "landMark"
    input_city_by_name= "city"
    input_state_by_name= "state"
    input_user_current_password_name= "currentPassword"
    input_user_new_password_name= "password"
    input_user_confim_password_name= "confirmPassword"



    def __init__(self, driver):
        self.driver = driver

    def enter_firstname(self, firstname):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_firstname_by_name)))
        element.clear()
        element.send_keys(firstname)

    def enter_lastname(self, lastname):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_lastname_by_name)))
        element.clear()
        element.send_keys(lastname)

    def enter_phone(self, phone):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_phone_no_by_name)))
        element.clear()
        element.send_keys(phone)

    def click_country_dropdown(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.input_country_by_css)))
        element.click()

    def select_country_dropdown(self, country):

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, self.input_text_by_ID)))
        element.send_keys(country)
        element.send_keys(Keys.ENTER)

    def select_gender(self):

        if self.driver.find_element(By.CSS_SELECTOR, self.click_male_by_css).is_selected():
            self.driver.find_element(By.CSS_SELECTOR, self.click_female_by_css).click()
        else:
            self.driver.find_element(By.CSS_SELECTOR, self.click_male_by_css).click()

    def select_address_tab(self):

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.click_address_tab_by_XPATH)))

        self.driver.find_element(By.XPATH, self.click_address_tab_by_XPATH).click()

    def click_add_Address(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.click_Add_address_xpath))).click()

    def enter_address(self, name, mobileno, email, pincode, address1, address2, landmark, city, state):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_name_address_by_name))).send_keys(name)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_phone_no_by_name))).send_keys(mobileno)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_email_address_by_name))).send_keys(email)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_pincode_address_by_name))).send_keys(pincode)

        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.NAME, self.input_address_one_by_name))).send_keys(address1)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_address_two_by_name))).send_keys(address2)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_landmark_by_name))).send_keys(landmark)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_city_by_name))).send_keys(city)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_state_by_name))).send_keys(state)

    def select_addresstype(self, addresstype):

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.input_addresstype_by_XPATH)))
        element.send_keys(addresstype)
        element.send_keys(Keys.ENTER)

    def select_security_tab(self):

        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.click_security_by_XPATH)))

        self.driver.find_element(By.XPATH, self.click_security_by_XPATH).click()

    def enterPassword(self, currentpassword, newpassword, confirmpassword):

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_user_current_password_name))).send_keys(currentpassword)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_user_new_password_name))).send_keys(newpassword)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.input_user_confim_password_name))).send_keys(confirmpassword)

    def click_save_btn(self):

        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.click_save_btn_by_CSS)))
        self.driver.execute_script('arguments[0].click()', element)