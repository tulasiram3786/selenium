import random
import time
from selenium.webdriver.common.by import By

class Zoomview_Settings_Roles_Page:

    button_Roles_xpath = "//a[text()='Roles']"
    button_Roles_AddRole_xpath = "//span[text()='Add Role']"
    textbox_Roles_RoleName_xpath = "//input[@label='Role Name*']"
    checkbox_Roles_selectall_xpath = "(//input[@class='ant-checkbox-input'])[1]"
    button_Roles_submit_xpath = "//span[text()='Submit']"
    #-------------------------- Add User ----------------------------------
    button_Roles_AddUser_xpath = "//span[text()='Add User']"
    button_Roles_AddUser_uploadphoto_xpath = "//span[text()='+ Upload Photo']"
    textbox_Roles_AddUser_firstname_xpath = "//input[@name='first_name']"
    textbox_Roles_AddUser_lastname_xpath = "//input[@name='last_name']"
    textbox_Roles_AddUser_Email_xpath = "//input[@name='email']"
    textbox_Roles_AddUser_phonenumber_xpath = "//input[@name='phone']"

    button_Roles_AddUser_Add_xpath = "//span[text()='Add']"










    def __init__(self, driver):  # Corrected constructor
        self.driver = driver



