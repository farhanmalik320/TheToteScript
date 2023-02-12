from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ChangePasswordPage:

    menu_btn_class= "dropdown"
    drop_down_menu_class= "dropdown-item"
    old_password_name= "oldPassword"
    new_password_name= "newPassword"
    confirm_password_name= "confirmPassword"
    save_btn_XPATH= "//button[normalize-space()='Save Changes']"

    def __init__(self,driver):
        self.driver= driver

    def clickmenubutton(self):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, self.menu_btn_class)))
        element.click()

    def clickChangepassword(self):
        change_password = self.driver.find_elements(By.CLASS_NAME, self.drop_down_menu_class)
        time.sleep(1)
        change_password[0].click()

    def enteroldpassword(self, oldpassword):
        old_password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, self.old_password_name)))
        old_password.send_keys(oldpassword)

    def enternewpassword(self, newpassword):
        new_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.new_password_name)))
        new_password.send_keys(newpassword)

    def enterconfirmpassword(self, confirmpassword):
        confirm_passord = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, self.confirm_password_name)))
        confirm_passord.send_keys(confirmpassword)

    def clicksavebtn(self):
        save_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.save_btn_XPATH)))
        save_btn.click()
