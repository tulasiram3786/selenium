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
# class Test_Logs_AddData:
#     loginpage_url = Read_Config.get_loginpage_url()
#     email = Read_Config.get_email()
#     password = Read_Config.get_password()
#     logger = Log_Maker.log_gen()
#
#
#     def test_configure_for_Nginx(self, setup):
#         self.logger.info("*************** Test_Logs_AddData configure Nginx *********************")
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
#         self.logs.click_on_Logs_AddData()
#         time.sleep(3)
#         self.logs.click_on_Nginx()
#         time.sleep(2)
#         self.logs.click_on_AddData_continuebutton()
#         time.sleep(2)
#         self.logs.click_on_selectcontroldevices_on_a_Host()
#         time.sleep(3)
#         self.logs.click_on_AddData_continuebutton()
#         time.sleep(2)
#         self.logs.click_on_installation_option_is_your_application_running_on_windows()
#         time.sleep(2)
#         self.logs.click_on_AddData_continuebutton()
#         time.sleep(2)
#         self.logs.select_host_dropdown_by_index(0)
#         time.sleep(3)
#         self.logs.click_on_AddData_continuebutton()
#         time.sleep(3)
#         self.logs.enter_text_into_addData_filepath("C\zcsu016\Downloads.log")
#         time.sleep(2)
#         self.logs.enter_text_into_addData_tag("Testtulasi11")
#         time.sleep(2)
#         self.logs.click_on_AddData_continuebutton()
#         time.sleep(2)
#         self.logs.click_addData_Finish_button()
#         time.sleep(4)
#         act_status_text = self.driver.find_element(By.XPATH,
#                                                   "//p[text()='success']").text
#         time.sleep(3)
#
#         if act_status_text == "success":
#             self.logger.info("*************** Nginx adding server is success *********************")
#             assert True
#
#         else:
#
#             self.logger.info("*************** Nginx adding server is Failed *********************")
#             self.driver.close()
#             assert False
#
#
#     def test_configure_for_Tomcat(self, setup):
#         self.logger.info("*************** Test_Logs_AddData configure Nginx *********************")
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
#         self.logs.click_on_Logs_AddData()
#         time.sleep(3)
#         self.logs.click_on_Tomcat()
#         time.sleep(2)
#         self.logs.click_on_AddData_continuebutton()
#         time.sleep(2)
#         self.logs.click_on_selectcontroldevices_on_a_Host()
#         time.sleep(3)
#         self.logs.click_on_AddData_continuebutton()
#         time.sleep(2)
#         self.logs.click_on_installation_option_is_your_application_running_on_windows()
#         time.sleep(2)
#         self.logs.click_on_AddData_continuebutton()
#         time.sleep(2)
#         self.logs.select_host_dropdown_by_index(0)
#         time.sleep(3)
#         self.logs.click_on_AddData_continuebutton()
#         time.sleep(3)
#         self.logs.enter_text_into_addData_filepath("C\zcsu016\Downloads.log")
#         time.sleep(2)
#         self.logs.enter_text_into_addData_tag("Testtulasi123")
#         time.sleep(2)
#         self.logs.click_on_AddData_continuebutton()
#         time.sleep(2)
#         self.logs.click_addData_Finish_button()
#         time.sleep(4)
#         act_status_text = self.driver.find_element(By.XPATH,
#                                                   "//p[text()='success']").text
#         time.sleep(3)
#
#         if act_status_text == "success":
#             self.logger.info("*************** Tomcat adding server is success *********************")
#             assert True
#
#         else:
#
#             self.logger.info("*************** Tomcat adding server is Failed *********************")
#             self.driver.close()
#             assert False
#
#     @pytest.mark.tulasi
#     def test_configure_for_CustomLog(self, setup):
#         self.logger.info("*************** Test_Logs_AddData configure Nginx *********************")
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
#         self.logs.click_on_Logs_AddData()
#         time.sleep(3)
#         self.logs.click_on_Customlog()
#         time.sleep(2)
#         self.logs.click_on_AddData_continuebutton()
#         time.sleep(2)
#         self.logs.click_on_selectcontroldevices_on_a_Host()
#         time.sleep(3)
#         self.logs.click_on_AddData_continuebutton()
#         time.sleep(2)
#         self.logs.click_on_installation_option_is_your_application_running_on_windows()
#         time.sleep(2)
#         self.logs.click_on_AddData_continuebutton()
#         time.sleep(2)
#         self.logs.select_host_dropdown_by_index(0)
#         time.sleep(3)
#         self.logs.click_on_AddData_continuebutton()
#         time.sleep(3)
#         self.logs.enter_text_into_addData_filepath("C\zcsu016\Downloads.log")
#         time.sleep(2)
#         self.logs.enter_text_into_addData_tag("Testram12")
#         time.sleep(2)
#         self.logs.click_on_AddData_continuebutton()
#         time.sleep(2)
#         self.logs.click_addData_Finish_button()
#         time.sleep(4)
#         act_status_text = self.driver.find_element(By.XPATH,
#                                                    "//p[text()='success']").text
#         time.sleep(3)
#
#         if act_status_text == "success":
#             self.logger.info("*************** Tomcat adding server is success *********************")
#             assert True
#
#         else:
#
#             self.logger.info("*************** Tomcat adding server is Failed *********************")
#             self.driver.close()
#             assert False
#
#
#
#
#
