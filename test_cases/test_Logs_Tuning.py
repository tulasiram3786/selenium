# import time
# import pytest
# from selenium import webdriver
# from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
# from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.common.by import By
# from base_pages.Infrastructure_Page import Zoomview_Infrastructure_Page
# from base_pages.Login_Page import Zoomview_Login_Page
# from base_pages.Logs_Page import Zoomview_Logs_Page
# from utilities.read_properties import Read_Config
# from utilities.custom_logger import Log_Maker
# from tabulate import tabulate
# import pandas as pd
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class Test_Logs_Tuning:
#     loginpage_url = Read_Config.get_loginpage_url()
#     email = Read_Config.get_email()
#     password = Read_Config.get_password()
#     logger = Log_Maker.log_gen()
#
#
#     def test_add_tuning(self, setup):
#         self.logger.info("*************** Test_Tuning *********************")
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
#         self.logs = Zoomview_Logs_Page(self.driver)
#         self.logs.click_Logs()
#         time.sleep(2)
#         self.logs.click_AllLogs()
#         time.sleep(5)
#         self.logs.click_tuningbutton()
#         time.sleep(3)
#         self.logs.click_tuning_addbutton()
#         time.sleep(2)
#         self.logs.enter_text_into_nameofrule("testTulasiramm")
#         time.sleep(2)
#         # self.logs.click_fieldtotune_listbox()
#         # time.sleep(3)
#         self.logs.arrow_button()
#         time.sleep(2)
#         self.logs.hostname_dropdown()
#         time.sleep(2)
#         self.logs.enter_text_into_tuningrule("testad")
#         time.sleep(2)
#         self.logs.click_on_createrule()
#         time.sleep(2)
#
#     @pytest.mark.tulasi
#     def test_tuning_verifytabledata(self, setup):
#         self.logger.info("*************** Test_Tuning verify table_data *********************")
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
#         self.logs = Zoomview_Logs_Page(self.driver)
#         self.logs.click_Logs()
#         time.sleep(2)
#         self.logs.click_AllLogs()
#         time.sleep(5)
#         self.logs.click_tuningbutton()
#         time.sleep(3)
#
#         formatted_table = self.logs.table_data_1()
#
#         # Write the formatted table to a text file
#         with open('Logs_Tuning_table.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'Logs_Tuning_table.txt'.")
#
#     @pytest.mark.tulasi
#     def test_tuning_delete_tablerow(self, setup):
#         self.logger.info("*************** Test_Tuning verify table_data *********************")
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
#         self.logs = Zoomview_Logs_Page(self.driver)
#         self.logs.click_Logs()
#         time.sleep(2)
#         self.logs.click_AllLogs()
#         time.sleep(5)
#         self.logs.click_tuningbutton()
#         time.sleep(3)
#         self.logs.click_on_tuning_actions_button()
#         time.sleep(3)
#         self.logs.click_on_tuning_table_row_delete()
#         time.sleep(5)
#         self.logs.click_on_tuning_table_row_delete_popup()
#         time.sleep(4)
#
#         toast_message = self.driver.find_element(By.XPATH, "//div[@class='ant-notification-notice-message']")
#         act_toast = toast_message.text
#         print(act_toast)
#         time.sleep(3)
#
#         exp_toast = "Removed filter successfully"
#
#         if act_toast == exp_toast:
#             self.logger.info("*************** test_tuning_delete_tablerow - Tuning table row deleted successfully *********************")
#             assert True
#             self.driver.close()
#         else:
#             self.driver.save_screenshot(".\\screenshots\\test_tuning_delete_tablerow.png")
#             self.logger.info("*************** test_tuning_delete_tablerow - Tuning table row not deleted *********************")
#             self.driver.close()
#             assert False
#
#
#
#
#
#
#
#
#
