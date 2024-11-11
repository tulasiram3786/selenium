# import time
# import pytest
# import allure
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
# class Test_Infrastructure_Summary:
#     loginpage_url = Read_Config.get_loginpage_url()
#     email = Read_Config.get_email()
#     password = Read_Config.get_password()
#     logger = Log_Maker.log_gen()
#     @allure.title("TC#1- Verifying cpu graph")
#     @pytest.mark.smoke
#     def test_verify_cpu_graph(self,setup):
#         self.logger.info("*************** Test_Infrastructure *********************")
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
#
#         try:
#             cpu_graph = self.driver.find_element(By.XPATH, self.infrastructure.infrastructure_cpu_graph_xpath)
#             if cpu_graph.is_displayed():
#                 print("cpu graph is there")
#             else:
#                 print("No Data for Cpu")
#
#         except:
#
#             no_cpu_graph = self.driver.find_element(By.XPATH, self.infrastructure.infrastructure_no_cpu_graph_xpath)
#             print("Cpu Graph :- ",no_cpu_graph.text)
#     @pytest.mark.sanity
#     def test_verify_cpuloadaverage_graph(self,setup):
#         self.logger.info("*************** Test_Infrastructure *********************")
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
#
#         try:
#             cpu_load_average_graph = self.driver.find_element(By.XPATH, self.infrastructure.infrastructure_cpuload_average_graph_xpath)
#             if cpu_load_average_graph.is_displayed():
#                 print("cpu load average graph is there")
#             else:
#                 print("No Data for Cpu Load")
#
#         except:
#
#             no_cpu_load_average_graph = self.driver.find_element(By.XPATH, self.infrastructure.infrastructure_no_cpu_graph_xpath)
#             print("Cpu Load Average Graph :- ",no_cpu_load_average_graph.text)
#     @pytest.mark.regression
#     def test_verify_memory_graph(self,setup):
#         self.logger.info("*************** Test_Infrastructure *********************")
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
#
#         try:
#             memory_graph = self.driver.find_element(By.XPATH, self.infrastructure.infrastructure_memory_graph_xpath)
#             if memory_graph.is_displayed():
#                 print("memory graph is there")
#             else:
#                 print("No Data for memory")
#
#         except:
#
#             no_memory_graph = self.driver.find_element(By.XPATH, self.infrastructure.infrastructure_no_memory_graph_xpath)
#             print("Memory Graph :- ",no_memory_graph.text)
#     @pytest.mark.sanity
#     def test_verify_network_graph(self,setup):
#         self.logger.info("*************** Test_Infrastructure *********************")
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
#
#         try:
#             network_graph = self.driver.find_element(By.XPATH, self.infrastructure.infrastructure_network_graph_xpath)
#             if network_graph.is_displayed():
#                 print("network graph is there")
#             else:
#                 print("No Data for network")
#
#         except:
#
#             no_network_graph = self.driver.find_element(By.XPATH, self.infrastructure.infrastructure_no_network_graph_xpath)
#             print("Network Graph :- ",no_network_graph.text)
#
#
#     @pytest.mark.regression
#     def test_verify_disk_table_data(self, setup):
#         self.logger.info("*************** Test_Infrastructure *********************")
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
#
#         # Locate the table element
#         table = self.driver.find_element(By.XPATH, self.infrastructure.infrastructure_summarypage_disk_table_xpath)
#
#         # Locate all rows in the table
#         rows = table.find_elements(By.XPATH, ".//tr")
#
#         # Prepare data for DataFrame
#         table_data = []
#         for row in rows:
#             # Locate all cells in the current row
#             cells = row.find_elements(By.XPATH, ".//td | .//th")
#             row_data = [cell.text for cell in cells]
#             table_data.append(row_data)
#
#         # Ensure all rows have the same number of columns
#         max_columns = max(len(row) for row in table_data)
#         for row in table_data:
#             while len(row) < max_columns:
#                 row.append('')
#
#         # Create DataFrame
#         df = pd.DataFrame(table_data[1:], columns=table_data[0])
#
#         # Generate the formatted table output using tabulate
#         formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
#
#         # Write the formatted table to a text file
#         with open('table_Disk.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'table_Disk.txt'.")
#     @pytest.mark.skip
#     def test_verify_processrunning_topcpu_table_data(self, setup):
#         self.logger.info("*************** Test_Infrastructure *********************")
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
#
#         # Locate the table element
#         table = self.driver.find_element(By.XPATH, self.infrastructure.infrastructure_summarypage_process_running_table_xpath)
#
#         # Locate all rows in the table
#         rows = table.find_elements(By.XPATH, ".//tr")
#
#         # Prepare data for DataFrame
#         table_data = []
#         for row in rows:
#             # Locate all cells in the current row
#             cells = row.find_elements(By.XPATH, ".//td | .//th")
#             row_data = [cell.text for cell in cells]
#             table_data.append(row_data)
#
#         # Ensure all rows have the same number of columns
#         max_columns = max(len(row) for row in table_data)
#         for row in table_data:
#             while len(row) < max_columns:
#                 row.append('')
#
#         # Create DataFrame
#         df = pd.DataFrame(table_data[1:], columns=table_data[0])
#
#         # Generate the formatted table output using tabulate
#         formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
#
#         # Write the formatted table to a text file
#         with open('table_ProcessRunningTopCPU.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'table_ProcessRunningTopCPU.txt'.")
#     @pytest.mark.sanity
#     def test_verify_processrunning_topmemory_table_data(self, setup):
#         self.logger.info("*************** Test_Infrastructure *********************")
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
#         self.infrastructure.click_infrastructure_topmemory()
#         time.sleep(4)
#
#         # Locate the table element
#         table = self.driver.find_element(By.XPATH, self.infrastructure.infrastructure_summarypage_process_running_table_xpath)
#
#         # Locate all rows in the table
#         rows = table.find_elements(By.XPATH, ".//tr")
#
#         # Prepare data for DataFrame
#         table_data = []
#         for row in rows:
#             # Locate all cells in the current row
#             cells = row.find_elements(By.XPATH, ".//td | .//th")
#             row_data = [cell.text for cell in cells]
#             table_data.append(row_data)
#
#         # Ensure all rows have the same number of columns
#         max_columns = max(len(row) for row in table_data)
#         for row in table_data:
#             while len(row) < max_columns:
#                 row.append('')
#
#         # Create DataFrame
#         df = pd.DataFrame(table_data[1:], columns=table_data[0])
#
#         # Generate the formatted table output using tabulate
#         formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
#
#         # Write the formatted table to a text file
#         with open('table_ProcessRunningTopMemory.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'table_ProcessRunningTopMemory.txt'.")
