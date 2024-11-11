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
# class Test_Infrastructure_Metrices:
#     loginpage_url = Read_Config.get_loginpage_url()
#     email = Read_Config.get_email()
#     password = Read_Config.get_password()
#     logger = Log_Maker.log_gen()
#
#     def test_metrices_listofmetrices(self, setup):
#         self.logger.info("*************** Test_Infrastructure Here printing all list of metrices *********************")
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
#         self.driver.find_element(By.XPATH, "//div[text()='Metrics']").click()
#         time.sleep(7)
#
#         # Locate all metric elements
#         metrics_elements = self.driver.find_elements(By.XPATH,
#                                                      "//article[contains(@class,'ant-typography font-semibold tablet-md:text-xs text-gray-800')]")
#         metrics_count = len(metrics_elements)
#
#         for index in range(metrics_count):
#             try:
#                 # Locate all metric elements again
#                 metrics_elements = self.driver.find_elements(By.XPATH,
#                                                              "//article[contains(@class,'ant-typography font-semibold tablet-md:text-xs text-gray-800')]")
#                 element = metrics_elements[index]
#                 print(element.text)
#                 time.sleep(2)
#                 # Click on the element
#                 element.click()
#                 time.sleep(5)  # Adjust sleep if necessary
#
#                 # Check for the presence of the graph
#                 try:
#                     self.driver.find_element(By.XPATH,
#                                              "//div[@class='ant-card-body']//descendant::div[@class='tablet-sm:h-[130px] w-full pt-2']")
#                     print(f"Graph is visible for element {index + 1}")
#                 except NoSuchElementException:
#                     print(f"No graph for element {index + 1}")
#
#                 # Click the back button to return to the list of metrics
#                 self.driver.find_element(By.XPATH, "//span[text()='Back']").click()
#                 time.sleep(2)
#             except Exception as e:
#                 self.logger.error(f"Error processing element {index + 1}: {e}")
#                 continue
#
