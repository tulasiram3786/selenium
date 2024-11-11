# import time
# import pandas as pd
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from tabulate import tabulate
#
# from base_pages.Login_Page import Zoomview_Login_Page
# from base_pages.Logs_Page import Zoomview_Logs_Page
# from base_pages.Settings_Page import Zoomview_Settings_Page
# from base_pages.Settings_ProfilePage import Zoomview_Settings_Profile_Page
# from utilities.random import generate_random_text
# from utilities.read_properties import Read_Config
# from utilities.custom_logger import Log_Maker
#
#
# class Test_Settins_NotificationGroup:
#     loginpage_url = Read_Config.get_loginpage_url()
#     email = Read_Config.get_email()
#     password = Read_Config.get_password()
#     logger = Log_Maker.log_gen()
#
#     def test_profile_title_verification(self, setup):
#         self.logger.info("*************** Test_Infrastructure *********************")
#         self.logger.info("*************** verification of Infrastructure page title *********************")
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#         # --------- calling login page ------------#
#         self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#         self.login.enter_email(self.email)
#         self.login.enter_password(self.password)
#         self.login.click_login()
#         time.sleep(5)  # Wait for the login to process
#         # -------- calling settings page --------------#
#         self.settings = Zoomview_Settings_Page(self.driver)
#         self.settings.click_settings_dropdown()
#
#         #---------- calling settings_profile page --------------------------
#         self.profile = Zoomview_Settings_Profile_Page(self.driver)
#         self.profile.click_settings_profile()
#         time.sleep(4)
#         act_title = self.driver.title
#         exp_title = "ZoomView | Profile"
#         print("Settings_Profile Title :- ", act_title)
#
#         if act_title == exp_title:
#             self.logger.info(
#                 "*************** test_profile_title_verification - Title Matched *********************")
#             assert True
#             self.driver.close()
#         else:
#             self.driver.save_screenshot(".\\screenshots\\test_profile_title_verification.png")
#             self.logger.info(
#                 "*************** test_profile_title_verification - Title not matched *********************")
#             self.driver.close()
#             assert False
#
#     def test_settings_profile_Authentication(self,setup):
#         self.logger.info("*************** test_settings_profile_Authentication started *********************")
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#         self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#         self.login.enter_email(self.email)
#         self.login.enter_password(self.password)
#         self.login.click_login()
#         time.sleep(5)  # Wait for the login to process
#         self.settings = Zoomview_Settings_Page(self.driver)
#         self.settings.click_settings_dropdown()
#         time.sleep(4)
#         self.profile = Zoomview_Settings_Profile_Page(self.driver)
#         self.profile.click_settings_profile()
#         time.sleep(2)
#         self.driver.find_element(By.XPATH, "//div[@class='ant-switch-handle']").click()
#         self.settings.click_settings_dropdown()
#         time.sleep(2)
#         self.login.click_logout()
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#         self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#         self.login.enter_email(self.email)
#         self.login.enter_password(self.password)
#         self.login.click_login()
#         time.sleep(5)  # Wait for the login to process
#         # Find all OTP input fields using class name (you can also use XPath)
#         otp_inputs = self.driver.find_elements(By.XPATH, "//input[contains(@class, 'ant-input-outlined input-otp__field')]")
#
#         # Loop through each input field and send the value "1"
#         for otp_input in otp_inputs:
#             otp_input.send_keys("1")
#
#         # Optional: Wait and then close the browser
#         time.sleep(3)
#         self.driver.find_element(By.XPATH, "//span[text()='Verify']").click()
#         time.sleep(2)
#         self.settings = Zoomview_Settings_Page(self.driver)
#         self.settings.click_settings_dropdown()
#         time.sleep(4)
#         self.profile = Zoomview_Settings_Profile_Page(self.driver)
#         self.profile.click_settings_profile()
#         time.sleep(2)
#         self.driver.find_element(By.XPATH, "//div[@class='ant-switch-handle']").click()
#         self.settings.click_settings_dropdown()
#         time.sleep(2)
#         self.login.click_logout()
#         self.login.enter_email(self.email)
#         self.login.enter_password(self.password)
#         self.login.click_login()
#         time.sleep(5)  # Wait for the login to process
#         self.driver.quit()
#
#     @pytest.mark.df
#     def test_settings_profile_accountdetails_edit(self, setup):
#
#         self.logger.info("*************** test_settings_profile_accountdetails_edit *********************")
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#         # --------- calling login page ------------#
#         self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#         self.login.enter_email(self.email)
#         self.login.enter_password(self.password)
#         self.login.click_login()
#         time.sleep(5)  # Wait for the login to process
#         # -------- calling settings page --------------#
#         self.settings = Zoomview_Settings_Page(self.driver)
#         self.settings.click_settings_dropdown()
#
#         # ---------- calling settings_profile page --------------------------
#         self.profile = Zoomview_Settings_Profile_Page(self.driver)
#         self.profile.click_settings_profile()
#         time.sleep(4)
#
#         self.profile.click_settings_profile_edit()
#         time.sleep(3)
#         self.profile.enter_text_into_profile_position("Test Engineer")
#         self.profile.click_settings_profile_update()
#         time.sleep(3)
#
#     @pytest.mark.tulasi
#     def test_settings_profile_companydetails_edit(self, setup):
#
#         self.logger.info("*************** test_settings_profile_edit *********************")
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#         # --------- calling login page ------------#
#         self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#         self.login.enter_email(self.email)
#         self.login.enter_password(self.password)
#         self.login.click_login()
#         time.sleep(5)  # Wait for the login to process
#         # -------- calling settings page --------------#
#         self.settings = Zoomview_Settings_Page(self.driver)
#         self.settings.click_settings_dropdown()
#
#         # ---------- calling settings_profile page --------------------------
#         self.profile = Zoomview_Settings_Profile_Page(self.driver)
#         self.profile.click_settings_profile()
#         time.sleep(4)
#
#         self.profile.click_settings_profile_edit_companydetails()
#         self.profile.enter_text_into_profile_companyname("Zybisys Consulting Services")
#         time.sleep(4)
#         self.profile.click_settings_profile_companydetails_update()
#         time.sleep(3)
#
#
#
#
#
#
