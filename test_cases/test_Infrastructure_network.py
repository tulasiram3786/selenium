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
#     def test_verify_network_graph(self, setup):
#         self.logger.info("*************** Test_Infrastructure Network Graph *********************")
#
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#         self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#         self.login.enter_email(self.email)
#         self.login.enter_password(self.password)
#         self.login.click_login()
#         time.sleep(5)  # Wait for the login to process
#         self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#         self.infrastructure.infrastructure_page_button()
#         time.sleep(4)
#         self.infrastructure.click_infrastructure_actions_button()
#         time.sleep(3)
#         self.driver.find_element(By.XPATH, "//div[text()='Network']").click()
#         time.sleep(3)
#
#         # Wait for the dropdown to be clickable and click to open it
#         wait = WebDriverWait(self.driver, 10)
#         dropdown_xpath = "(//div[@class='ant-select-selector'])[3]"
#         dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#         dropdown.click()
#
#         # Collect all options in the dropdown
#         options_xpath = "//div[@class='rc-virtual-list-holder-inner']//descendant::div[@class='ant-select-item ant-select-item-option']"
#
#         while True:
#             options = wait.until(
#                 EC.presence_of_all_elements_located((By.XPATH, options_xpath)))  # Adjust the XPath as needed
#             initial_count = len(options)
#
#             for option in options:
#                 try:
#                     # Re-open the dropdown if necessary
#                     dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#                     dropdown.click()
#                     time.sleep(2)
#
#                     # Re-collect options to avoid stale elements
#                     options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#
#                     # Scroll the current option into view
#                     self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
#
#                     # Use JavaScript to click
#                     self.driver.execute_script("arguments[0].click();", option)
#                     print(option.text)
#                     time.sleep(3)  # Optional: wait to observe the click action
#
#                     # Verify the graph is displayed
#                     graph_xpath = "(//div[@class='relative']//descendant::div[@class='h-[150px] w-full pt-2'])[1]"
#                     try:
#                         graph = wait.until(EC.presence_of_element_located((By.XPATH, graph_xpath)))
#                         assert graph.is_displayed(), f"Graph not displayed for option: {option.text}"
#                         print(f"Graph displayed : {option.text}")
#                     except TimeoutException:
#                         print(f"Graph not displayed: {option.text}")
#
#                 except (StaleElementReferenceException, IndexError):
#                     continue
#
#             # Re-collect options to check if new options are loaded
#             options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#             new_count = len(options)
#
#             if new_count == initial_count:
#                 break  # Break the loop if no new options are loaded
#
#         # Optionally, perform any additional actions or assertions
#
#         # Close the WebDriver
#         self.driver.quit()
#
#     def test_verify_network_graph_child1(self, setup):
#         self.logger.info("*************** Test_Infrastructure Network Graph child1 *********************")
#
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#         self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#         self.login.enter_email(self.email)
#         self.login.enter_password(self.password)
#         self.login.click_login()
#         time.sleep(5)  # Wait for the login to process
#         self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#         self.infrastructure.infrastructure_page_button()
#         time.sleep(4)
#         self.infrastructure.click_infrastructure_actions_button()
#         time.sleep(3)
#         self.driver.find_element(By.XPATH, "//div[text()='Network']").click()
#         time.sleep(3)
#
#         # Wait for the dropdown to be clickable and click to open it
#         wait = WebDriverWait(self.driver, 10)
#         dropdown_xpath = "(//div[@class='ant-select-selector'])[4]"
#         dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#         dropdown.click()
#
#         # Collect all options in the dropdown
#         options_xpath = "//div[@class='rc-virtual-list-holder-inner']//descendant::div[@class='ant-select-item ant-select-item-option']"
#
#         while True:
#             options = wait.until(
#                 EC.presence_of_all_elements_located((By.XPATH, options_xpath)))  # Adjust the XPath as needed
#             initial_count = len(options)
#
#             for option in options:
#                 try:
#                     # Re-open the dropdown if necessary
#                     dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#                     dropdown.click()
#                     time.sleep(2)
#
#                     # Re-collect options to avoid stale elements
#                     options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#
#                     # Scroll the current option into view
#                     self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
#
#                     # Use JavaScript to click
#                     self.driver.execute_script("arguments[0].click();", option)
#                     print(option.text)
#                     time.sleep(3)  # Optional: wait to observe the click action
#
#                     # Verify the graph is displayed
#                     graph_xpath = "(//div[@class='relative']//descendant::div[@class='h-[150px] w-full pt-2'])[2]"
#                     try:
#                         graph = wait.until(EC.presence_of_element_located((By.XPATH, graph_xpath)))
#                         assert graph.is_displayed(), f"Graph not displayed for option: {option.text}"
#                         print(f"Graph displayed : {option.text}")
#                     except TimeoutException:
#                         print(f"Graph not displayed: {option.text}")
#
#                 except (StaleElementReferenceException, IndexError):
#                     continue
#
#             # Re-collect options to check if new options are loaded
#             options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#             new_count = len(options)
#
#             if new_count == initial_count:
#                 break  # Break the loop if no new options are loaded
#
#         # Optionally, perform any additional actions or assertions
#
#         # Close the WebDriver
#         self.driver.quit()
#
#     def test_verify_network_graph_child2(self, setup):
#         self.logger.info("*************** Test_Infrastructure Network Graph child 2 *********************")
#
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#         self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#         self.login.enter_email(self.email)
#         self.login.enter_password(self.password)
#         self.login.click_login()
#         time.sleep(5)  # Wait for the login to process
#         self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#         self.infrastructure.infrastructure_page_button()
#         time.sleep(4)
#         self.infrastructure.click_infrastructure_actions_button()
#         time.sleep(3)
#         self.driver.find_element(By.XPATH, "//div[text()='Network']").click()
#         time.sleep(3)
#
#         # Wait for the dropdown to be clickable and click to open it
#         wait = WebDriverWait(self.driver, 10)
#         dropdown_xpath = "(//div[@class='ant-select-selector'])[5]"
#         dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#         dropdown.click()
#
#         # Collect all options in the dropdown
#         options_xpath = "//div[@class='rc-virtual-list-holder-inner']//descendant::div[@class='ant-select-item ant-select-item-option']"
#
#         while True:
#             options = wait.until(
#                 EC.presence_of_all_elements_located((By.XPATH, options_xpath)))  # Adjust the XPath as needed
#             initial_count = len(options)
#
#             for option in options:
#                 try:
#                     # Re-open the dropdown if necessary
#                     dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#                     dropdown.click()
#                     time.sleep(2)
#
#                     # Re-collect options to avoid stale elements
#                     options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#
#                     # Scroll the current option into view
#                     self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
#
#                     # Use JavaScript to click
#                     self.driver.execute_script("arguments[0].click();", option)
#                     print(option.text)
#                     time.sleep(3)  # Optional: wait to observe the click action
#
#                     # Verify the graph is displayed
#                     graph_xpath = "(//div[@class='relative']//descendant::div[@class='h-[150px] w-full pt-2'])[3]"
#                     try:
#                         graph = wait.until(EC.presence_of_element_located((By.XPATH, graph_xpath)))
#                         assert graph.is_displayed(), f"Graph not displayed for option: {option.text}"
#                         print(f"Graph displayed : {option.text}")
#                     except TimeoutException:
#                         print(f"Graph not displayed: {option.text}")
#
#                 except (StaleElementReferenceException, IndexError):
#                     continue
#
#             # Re-collect options to check if new options are loaded
#             options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#             new_count = len(options)
#
#             if new_count == initial_count:
#                 break  # Break the loop if no new options are loaded
#
#         # Optionally, perform any additional actions or assertions
#
#         # Close the WebDriver
#         self.driver.quit()
#
#     def test_verify_network_table_data(self, setup):
#         self.logger.info("*************** Test_Infrastructure storage table data *********************")
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
#         self.driver.find_element(By.XPATH, "//div[text()='Network']").click()
#         time.sleep(7)
#
#         # Locate the table element
#         table = self.driver.find_element(By.XPATH, "(//div[@class='ant-spin-container'])[4]")
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
#             table = self.driver.find_element(By.XPATH, "(//div[@class='ant-spin-container'])[7]")
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
#         with open('table_network.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'table_network.txt'.")
#
#