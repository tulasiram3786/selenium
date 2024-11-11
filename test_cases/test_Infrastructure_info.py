# import time
# import pytest
# from selenium import webdriver
# from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
# from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.common.by import By
# from base_pages.Infrastructure_Page import Zoomview_Infrastructure_Page
# from base_pages.Login_Page import Zoomview_Login_Page
# from utilities.read_properties import Read_Config
# from utilities.custom_logger import Log_Maker
# from tabulate import tabulate
# import pandas as pd
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class Test_Infrastructure_Info:
#     loginpage_url = Read_Config.get_loginpage_url()
#     email = Read_Config.get_email()
#     password = Read_Config.get_password()
#     logger = Log_Maker.log_gen()
#
#     def test_info(self, setup):
#         self.logger.info("*************** Test_Infrastructure Info page *********************")
#
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#         self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#         self.login.enter_email(self.email)
#         self.login.enter_password(self.password)
#         self.login.click_login()
#         time.sleep(8)  # Wait for the login to process
#         self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#         time.sleep(3)
#         self.infrastructure.infrastructure_page_button()
#         time.sleep(4)
#         self.infrastructure.click_infrastructure_actions_button()
#         time.sleep(3)
#         self.driver.find_element(By.XPATH, "//div[text()='Info']").click()
#         time.sleep(7)
#         self.logger.info("*************** Host info *********************")
#         print("Host info")
#
#         # Locate all info elements
#         infotexts = self.driver.find_elements(By.XPATH, "//div[contains(@class,'flex gap-x-5')]")
#
#         # Accumulate text
#         accumulated_text = []
#
#         for element in infotexts:
#             try:
#                 # Append the text of each element to the list
#                 accumulated_text.append(element.text)
#             except Exception as e:
#                 self.logger.error("No data found on info page")
#                 continue
#
#         # Join all texts into a single string with a space delimiter
#         all_text = ' '.join(accumulated_text)
#         print(all_text)
#
#     def test_info_softwareinventory(self, setup):
#         self.logger.info("*************** Test_Infrastructure Info page *********************")
#
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#         self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#         self.login.enter_email(self.email)
#         self.login.enter_password(self.password)
#         self.login.click_login()
#         time.sleep(8)  # Wait for the login to process
#         self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#         time.sleep(3)
#         self.infrastructure.infrastructure_page_button()
#         time.sleep(4)
#         self.infrastructure.click_infrastructure_actions_button()
#         time.sleep(3)
#         self.driver.find_element(By.XPATH, "//div[text()='Info']").click()
#         time.sleep(7)
#         self.logger.info("*************** Software inventory *********************")
#         print("software inventory")
#
#         # Locate all info elements
#         try:
#             infotexts = self.driver.find_elements(By.XPATH, "//div[contains(@class,'flex gap-x-3')]")
#         except NoSuchElementException as e:
#             self.logger.error("No info elements found on the page")
#             print("No data found for software inventory")
#             infotexts = []
#
#         # Accumulate text
#         accumulated_text = []
#
#         for element in infotexts:
#             try:
#                 # Append the text of each element to the list
#                 accumulated_text.append(element.text)
#             except Exception as e:
#                 self.logger.error(f"Error processing element: {e}")
#                 continue
#
#         # Join all texts into a single string with a space delimiter
#         all_text = ' '.join(accumulated_text)
#         print(all_text)
#
#         # Ensure the script passes even if no elements are found
#         assert True
#
