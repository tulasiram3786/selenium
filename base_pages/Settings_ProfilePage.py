import random
import time
from selenium.webdriver.common.by import By

class Zoomview_Settings_Profile_Page:

    button_profile_xpath = "//a[text()='Profile']"
    button_profile_uploadimaga_xpath = "//span[text()='Upload Image']"
    button_profile_removeimaga_xpath = "//span[text()='Remove Image']"
    button_profile_inside_remove_xpath = "//span[text()='Remove']"
    button_profile_accountdetails_edit_xpath = "(//span[text()=' Edit '])[1]"
    button_profile_companydetails_edit_xpath = "(//span[text()=' Edit '])[2]"
    textbox_profile_firstname_xpath = "//input[@label='First Name']"
    textbox_profile_lastname_xpath = "//input[@label='Last Name']"

    textbox_profile_postition_xpath = "//input[@label='Position']"
    button_profile_update_xpath = "(//span[text()='Update'])[1]"
    button_profile_companydetails_update_xpath = "(//span[text()='Update'])[1]"

    textbox_profile_companyname_xpath = "//input[@label='Company Name']"
    textbox_profile_address_xpath = "//input[@label='Address']"
    textbox_profile_pincode_xpath = "//input[@label='pincode']"
    textbox_profile_phoneno_xpath = "//input[@label='Phone No']"
    textbox_profile_GST_xpath = "//input[@label='GST']"



    def __init__(self, driver):  # Corrected constructor
        self.driver = driver

    def click_settings_profile(self):
        self.driver.find_element(By.XPATH, self.button_profile_xpath).click()

    def click_settings_profile_edit(self):
        self.driver.find_element(By.XPATH, self.button_profile_accountdetails_edit_xpath).click()

    def click_settings_profile_edit_companydetails(self):
        self.driver.find_element(By.XPATH, self.button_profile_companydetails_edit_xpath).click()

    def click_settings_profile_upload_image(self):
        self.driver.find_element(By.XPATH, self.button_profile_uploadimaga_xpath).click()

    def click_settings_profile_remove_image(self):
        self.driver.find_element(By.XPATH, self.button_profile_removeimaga_xpath).click()

    def click_profile_remove_inside(self):
        self.driver.find_element(By.XPATH, self.button_profile_inside_remove_xpath).click()

    def enter_text_into_profile_firstname(self, firstname):
        self.driver.find_element(By.XPATH, self.textbox_profile_firstname_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_profile_firstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_profile_firstname_xpath).send_keys(firstname)

    def enter_text_into_profile_lastname(self, lastname):
        self.driver.find_element(By.XPATH, self.textbox_profile_lastname_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_profile_lastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_profile_lastname_xpath).send_keys(lastname)

    def enter_text_into_profile_position(self, position):
        self.driver.find_element(By.XPATH, self.textbox_profile_postition_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.textbox_profile_postition_xpath).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.textbox_profile_postition_xpath).send_keys(position)

    def click_settings_profile_update(self):
        self.driver.find_element(By.XPATH, self.button_profile_update_xpath).click()



    def enter_text_into_profile_companyname(self, companyname):
        self.driver.find_element(By.XPATH, self.textbox_profile_companyname_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_profile_companyname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_profile_companyname_xpath).send_keys(companyname)

    def click_settings_profile_companydetails_update(self):
        self.driver.find_element(By.XPATH, self.button_profile_companydetails_update_xpath).click()







