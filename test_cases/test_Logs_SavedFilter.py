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
# class Test_Logs_SavedFilter:
#     loginpage_url = Read_Config.get_loginpage_url()
#     email = Read_Config.get_email()
#     password = Read_Config.get_password()
#     logger = Log_Maker.log_gen()
#
#
#     def test_savedfilter_verifytabledata_1(self, setup):
#         self.logger.info("*************** Test_SavedFilter verify table_data_1 *********************")
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
#         self.logs.click_on_savedfilter_tab()
#         time.sleep(3)
#
#         formatted_table = self.logs.table_data_11()
#
#         # Write the formatted table to a text file
#         with open('Logs_savedfilter_table.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'Logs_savedfilter_table.txt'.")
#
#         # formatted_table = self.logs.table_data_11()
#         #
#         # # Write the formatted table to a text file
#         # with open('Logs_SavedFilter_table1.txt', 'w', encoding='utf-8') as file:
#         #     file.write(formatted_table)
#         #
#         # print("Table data has been saved to 'Logs_SavedFilter_table1.txt'.")
#
#         # def save_table_to_txt(formatted_table, filename):
#         #     with open(filename, 'w', encoding='utf-8') as file:
#         #         file.write(formatted_table)
#         #
#         # # Example usage within your test function
#         # formatted_table = self.logs.table_data_11()
#         # print(formatted_table)  # To see the formatted table output in the console
#         # save_table_to_txt(formatted_table, 'Logs_SavedFilter_table1.txt')
#
#
#     def test_savedfilter_verifytabledata_2(self, setup):
#         self.logger.info("*************** Test_SavedFilter verify table_data_2 *********************")
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
#         self.logs.click_on_savedfilter_tab()
#         time.sleep(3)
#         # self.logs.click_on_time_interval_dropdown()
#         # time.sleep(3)
#         # self.logs.click_on_interval_dropdown_options()
#         # time.sleep(7)
#
#
#
#         formatted_table = self.logs.table_data_3()
#
#         # Write the formatted table to a text file
#         with open('Logs_SavedFilter_ttable2.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'Logs_SavedFilter_ttable2.txt'.")
#
#
#     def test_savedfilter_verify_graph(self, setup):
#         self.logger.info("*************** Test_SavedFilter verify graph *********************")
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
#         self.logs.click_on_savedfilter_tab()
#         time.sleep(3)
#         # self.logs.click_on_time_interval_dropdown()
#         # time.sleep(3)
#         # self.logs.click_on_interval_dropdown_options()
#         # time.sleep(7)
#         try:
#             savedfilter_graph = self.driver.find_element(By.XPATH, self.logs.savedfilter_graph_xpath)
#             if savedfilter_graph.is_displayed():
#                 print("Saved Filter Graph is there")
#             else:
#                 print("No Graph Data for Saved Filter")
#
#         except:
#
#             no_savedfilter_graph = self.driver.find_element(By.XPATH, self.logs.savedfilter_no_graph_xpath)
#             print("SavedFilter Graph :- ",no_savedfilter_graph.text)
#
#     @pytest.mark.tulasi
#     def test_savedfilter_verify_searchbox(self, setup):
#         self.logger.info("*************** Test_SavedFilter verify searchbox *********************")
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
#         self.logs.click_on_savedfilter_tab()
#         time.sleep(3)
#         self.logs.enter_text_into_savedfilter_searchbox("tulasi")
#         time.sleep(4)
#         allrowsforsearchbox=self.driver.find_elements(By.XPATH, "(//div[@class='ant-spin-container'])[1]//tbody//tr")
#         print("Total searched Result :" , len(allrowsforsearchbox))
#
#
#
#
#
#
#
#
# #saved filter some problem in table printing for 1st table and second table
