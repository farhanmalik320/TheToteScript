from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WithdrawPage:

    menu_withdraw_xpath= "//button[normalize-space()='Withdraw']"
    sub_menu_withdraw_tab_class= "button-active"
    game_dropdown_xpath= "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/div[2]/div[1]"
    game_checbox_xpath = "//input[@id='5']"
    game_dropdown_save_btn_xpath = "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/form[1]/button[1]"
    max_btn_xpath= "//button[normalize-space()='MAX']"
    payput_image_xpath= "//img[@class='maxbuttonCurrencySymbol']"
    select_currency_id= "6"
    payout_save_changes_btn_xpath= "//button[normalize-space()='Save Changes']"
    enter_email_xpath= "//input[@placeholder='Enter Email']"
    cashout_btn_xpath= "//button[normalize-space()='Cashout']"

    def __init__(self,driver):
        self.driver= driver

    def clickmenuwithdrawbutton(self):
        #element=self.driver.find_element(By.XPATH, self.menu_withdraw_xpath).click()
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.menu_withdraw_xpath)))
        element.click()

    def clicksubmenuwithdrawbtn(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.sub_menu_withdraw_tab_class)))
        element.click()

    def selectgame(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.game_dropdown_xpath)))
        element.click()
        checkbox= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.game_checbox_xpath)))
        checkbox.click()
        game_save_btn= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.game_dropdown_save_btn_xpath)))
        game_save_btn.click()

    def clickmaxbutton(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.max_btn_xpath)))
        self.driver.execute_script('arguments[0].click()', element)

    def selectpayout(self):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.payput_image_xpath)))
        self.driver.execute_script('arguments[0].click()', element)
        select_symbol= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, self.select_currency_id)))
        self.driver.execute_script('arguments[0].click()', select_symbol)
        save_changes_btn= WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.payout_save_changes_btn_xpath)))
        self.driver.execute_script('arguments[0].click()', save_changes_btn)

    def enterEmail(self, email):
        self.driver.find_element(By.XPATH,self.enter_email_xpath).send_keys(email)

    def clickcashout(self):
        self.driver.find_element(By.XPATH, self.cashout_btn_xpath).click()