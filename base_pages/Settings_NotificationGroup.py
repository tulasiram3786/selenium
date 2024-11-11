import random
import time
from selenium.webdriver.common.by import By

class Zoomview_Settings_NotificationGroup_Page:

    button_notificationgroup_xpath = "//a[text()='Notifications Group']"
    button_add_xpath = "//span[text()='Add']"
    textbox_Groupname_xpath = "//input[@label='Group Name']"
    textbox_Description_xpath = "//input[@label='Description']"
    button_addemails_xpath = "//span[text()='ADD EMAILS +']"
    button_save_xpath = "//span[text()='SAVE ']"
    NotificationGroup_toast_message_xpath = "//div[text()='Inserted Notification successfully']"
    button_notificationgroup_table_row_clone_xpath = "(//span[text()='Clone'])[1]"







    def __init__(self, driver):  # Corrected constructor
        self.driver = driver

    def click_settings_NotificationGroup(self):
        self.driver.find_element(By.XPATH, self.button_notificationgroup_xpath).click()

    def click_add(self):
        self.driver.find_element(By.XPATH, self.button_add_xpath).click()

    def enter_text_into_GroupName(self, groupname):
        self.driver.find_element(By.XPATH, self.textbox_Groupname_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_Groupname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_Groupname_xpath).send_keys(groupname)

    def enter_text_into_Description(self, description):
        self.driver.find_element(By.XPATH, self.textbox_Description_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_Description_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_Description_xpath).send_keys(description)

    def click_AddEmails(self):
        self.driver.find_element(By.XPATH, self.button_addemails_xpath).click()

    def click_savebutton(self):
        self.driver.find_element(By.XPATH, self.button_save_xpath).click()


    def click_on_notificationgroup_table_row_clone(self):
        self.driver.find_element(By.XPATH, self.button_notificationgroup_table_row_clone_xpath).click()





