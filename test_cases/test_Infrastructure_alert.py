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
# class Test_Infrastructure_Storage:
#     loginpage_url = Read_Config.get_loginpage_url()
#     email = Read_Config.get_email()
#     password = Read_Config.get_password()
#     logger = Log_Maker.log_gen()
#
#     def test_verify_alert_table_data(self, setup):
#         self.logger.info("*************** Test_Infrastructure alert table data *********************")
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
#         self.driver.find_element(By.XPATH, "//div[text()='Alert']").click()
#         time.sleep(7)
#
#         # Locate the table element
#         table = self.driver.find_element(By.XPATH, "//div[@class='ant-spin-container']")
#
#         # Capture the header row
#         header = table.find_elements(By.XPATH, ".//thead//th")
#         header_row = [cell.text for cell in header]
#
#         table_data = []
#
#         while True:
#             # Locate all rows in the table
#             rows = table.find_elements(By.XPATH, ".//tbody//tr")
#
#             # Prepare data for DataFrame
#             for row in rows:
#                 # Locate all cells in the current row
#                 cells = row.find_elements(By.XPATH, ".//td")
#                 row_data = [cell.text for cell in cells]
#                 if row_data not in table_data:  # Avoid adding duplicate rows
#                     table_data.append(row_data)
#
#             # Check if the next page button is enabled
#             try:
#                 next_button = self.driver.find_element(By.XPATH, "//li[@class='ant-pagination-next']//button")
#                 if 'disabled' in next_button.get_attribute('class'):
#                     break
#             except:
#                 break
#
#             # Click the next page button
#             next_button.click()
#             time.sleep(2)
#
#             # Refresh the table element after clicking next button
#             table = self.driver.find_element(By.XPATH, "//div[@class='ant-spin-container']")
#
#         # Ensure all rows have the same number of columns
#         max_columns = max(len(row) for row in table_data)
#         for row in table_data:
#             while len(row) < max_columns:
#                 row.append('')
#
#         # Create DataFrame
#         df = pd.DataFrame(table_data, columns=header_row)
#
#         # Generate the formatted table output using tabulate
#         formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
#
#         # Write the formatted table to a text file
#         with open('table_alert.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'table_alert.txt'.")