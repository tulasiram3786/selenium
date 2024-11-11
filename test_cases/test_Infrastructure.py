# import time
#
# import allure
# import pytest
# from allure_commons.types import AttachmentType
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
# class Test_Infrastructure:
#     loginpage_url = Read_Config.get_loginpage_url()
#     email = Read_Config.get_email()
#     password = Read_Config.get_password()
#     logger = Log_Maker.log_gen()
#
#     @pytest.mark.tulasi
#     @allure.severity(allure.severity_level.CRITICAL)
#
#     def test_title_verification_for_infrastructure_page(self, setup):
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
#         #------------------ calling zoomview infrastructure page ------------------------
#         self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#         self.infrastructure.infrastructure_page_button()
#         time.sleep(3)
#         act_title = self.driver.title
#         exp_title = "ZoomView | Infrastructure"
#         print("Infrastructure Title :- ", act_title)
#
#         allure.attach(self.driver.get_screenshot_as_png(),name="test_title_verification_for_infrastructure_page",attachment_type=AttachmentType.PNG)
#
#         if act_title == exp_title:
#             self.logger.info(
#                 "*************** test_title_verification_for_infrastructure_page - Title Matched *********************")
#             assert True
#             self.driver.close()
#         else:
#             self.driver.save_screenshot(".\\screenshots\\test_title_verification_for_infrastructure_page.png")
#             self.logger.info(
#                 "*************** test_title_verification_for_infrastructure_page - Title not matched *********************")
#             self.driver.close()
#             assert False
#
#     def test_infrastructure_for_validationofHosts(self, setup):
#
#         self.logger.info("*************** Test_Infrastructure verify hosts count *********************")
#         self.logger.info("*************** hosts count = live+offline+stale *********************")
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
#         time.sleep(3)
#         self.infrastructure.verify_infrastructure_hosts()
#         self.logger.info(
#             "*************** Infrastructure hosts count matched with live,offline,stale *********************")
#         self.driver.close()
#
#     def test_infrastructure_for_validationofServices(self, setup):
#
#         self.logger.info("*************** Test_Infrastructure verify Services count *********************")
#         self.logger.info("*************** services count = ok + crit + warn *********************")
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
#         self.infrastructure.verify_infrastructure_services()
#         self.logger.info(
#             "*************** Infrastructure Services count matched with ok, warn, crit *********************")
#         self.driver.close()
#
#
#     def test_print_infrastructure_table(self, setup):
#         self.logger.info("*************** Test_Infrastructure printing table data *********************")
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
#
#         # Locate the table element
#         table = self.driver.find_element(By.XPATH, "//table")
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
#         # Create DataFrame
#         df = pd.DataFrame(table_data[1:], columns=table_data[0])
#
#         # Generate the formatted table output using tabulate
#         formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
#
#         # Write the formatted table to a text file
#         with open('zoomview_infrastructure_table.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'zoomview_infrastructure_table.txt'.")
#         self.driver.close()
#
#     def test_infrastructure_performence(self,setup):
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
#         self.url=self.driver.current_url
#         print("zoomview_Infrastructure_performence url:",self.url)
#
#
#
#     def test_verify_cpu_graph(self, setup):
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
#         time.sleep(6)
#
#         self.infrastructure.click_infrastructure_actions_button()
#         time.sleep(6)
#
#
#         try:
#             cpu_graph = self.driver.find_element(By.XPATH, self.infrastructure.infrastructure_cpu_graph_xpath)
#             if cpu_graph.is_displayed():
#                 print("cpu graph is there")
#             else:
#                 print("No Data for Cpu")
#
#         except:
#             no_cpu_graph = self.driver.find_element(By.XPATH, self.infrastructure.infrastructure_no_cpu_graph_xpath)
#             print("Cpu Graph :- ", no_cpu_graph.text)
#
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
#
#     def test_verify_memory_graph(self,setup):
#         self.logger.info("*************** Test_Infrastructure *********************")
#
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#
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
#
#     def test_verify_network_graph(self,setup):
#         self.logger.info("*************** Test_Infrastructure *********************")
#
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#
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
#
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
#
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
#
#     # def test_verify_system(self, setup):
#     #     self.logger.info("*************** Test_Infrastructure *********************")
#     #
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(5)  # Wait for the login to process
#     #     self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#     #     self.infrastructure.infrastructure_page_button()
#     #     time.sleep(4)
#     #     self.infrastructure.click_infrastructure_actions_button()
#     #     time.sleep(3)
#     #     self.driver.find_element(By.XPATH, "//div[text()='System']").click()
#     #     time.sleep(3)
#     #
#     #     # Wait for the dropdown to be clickable and click to open it
#     #     wait = WebDriverWait(self.driver, 10)
#     #     dropdown_xpath = "(//div[@class='ant-select-selector'])[3]"
#     #     dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #     dropdown.click()
#     #
#     #     # Collect all options in the dropdown
#     #     options_xpath = "//div[@class='rc-virtual-list-holder-inner']//descendant::div[@class='ant-select-item ant-select-item-option']"
#     #
#     #     while True:
#     #         options = wait.until(
#     #             EC.presence_of_all_elements_located((By.XPATH, options_xpath)))  # Adjust the XPath as needed
#     #         initial_count = len(options)
#     #
#     #         for option in options:
#     #             try:
#     #                 # Re-open the dropdown if necessary
#     #                 dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #                 dropdown.click()
#     #                 time.sleep(2)
#     #
#     #                 # Re-collect options to avoid stale elements
#     #                 options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #
#     #                 # Scroll the current option into view
#     #                 self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
#     #
#     #                 # Use JavaScript to click
#     #                 self.driver.execute_script("arguments[0].click();", option)
#     #                 print(option.text)
#     #                 time.sleep(3)  # Optional: wait to observe the click action
#     #
#     #             except (StaleElementReferenceException, IndexError):
#     #                 continue
#     #
#     #         # Re-collect options to check if new options are loaded
#     #         options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #         new_count = len(options)
#     #
#     #         if new_count == initial_count:
#     #             break  # Break the loop if no new options are loaded
#     #
#     #     # Close the WebDriver
#     #     self.driver.quit()
#     #
#     # def test_verify_system(self, setup):
#     #     self.logger.info("*************** Test_Infrastructure *********************")
#     #
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(5)  # Wait for the login to process
#     #     self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#     #     self.infrastructure.infrastructure_page_button()
#     #     time.sleep(4)
#     #     self.infrastructure.click_infrastructure_actions_button()
#     #     time.sleep(3)
#     #     self.driver.find_element(By.XPATH, "//div[text()='System']").click()
#     #     time.sleep(3)
#     #
#     #     # Wait for the dropdown to be clickable and click to open it
#     #     wait = WebDriverWait(self.driver, 10)
#     #     dropdown_xpath = "(//div[@class='ant-select-selector'])[3]"
#     #     dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #     dropdown.click()
#     #
#     #     # Collect all options in the dropdown
#     #     options_xpath = "//div[@class='rc-virtual-list-holder-inner']//descendant::div[@class='ant-select-item ant-select-item-option']"
#     #
#     #     while True:
#     #         options = wait.until(
#     #             EC.presence_of_all_elements_located((By.XPATH, options_xpath)))  # Adjust the XPath as needed
#     #         initial_count = len(options)
#     #
#     #         for option in options:
#     #             try:
#     #                 # Re-open the dropdown if necessary
#     #                 dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #                 dropdown.click()
#     #                 time.sleep(2)
#     #
#     #                 # Re-collect options to avoid stale elements
#     #                 options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #
#     #                 # Scroll the current option into view
#     #                 self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
#     #
#     #                 # Use JavaScript to click
#     #                 self.driver.execute_script("arguments[0].click();", option)
#     #                 print(option.text)
#     #                 time.sleep(3)  # Optional: wait to observe the click action
#     #
#     #                 # Verify the graph is displayed
#     #                 graph_xpath = "(//div[@class='relative']//descendant::div[@class='h-[150px] w-full pt-2'])[1]"
#     #                 try:
#     #                     graph = wait.until(EC.presence_of_element_located((By.XPATH, graph_xpath)))
#     #                     assert graph.is_displayed(), f"Graph not displayed for option: {option.text}"
#     #                     print(f"Graph displayed : {option.text}")
#     #                 except TimeoutException:
#     #                     print(f"Graph not displayed: {option.text}")
#     #
#     #             except (StaleElementReferenceException, IndexError):
#     #                 continue
#     #
#     #         # Re-collect options to check if new options are loaded
#     #         options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #         new_count = len(options)
#     #
#     #         if new_count == initial_count:
#     #             break  # Break the loop if no new options are loaded
#     #
#     #     # Optionally, perform any additional actions or assertions
#     #
#     #     # Close the WebDriver
#     #     self.driver.quit()
#     #
#     # def test_verify_system_child1_graph(self, setup):
#     #     self.logger.info("*************** Test_Infrastructure *********************")
#     #
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(5)  # Wait for the login to process
#     #     self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#     #     self.infrastructure.infrastructure_page_button()
#     #     time.sleep(4)
#     #     self.infrastructure.click_infrastructure_actions_button()
#     #     time.sleep(3)
#     #     self.driver.find_element(By.XPATH, "//div[text()='System']").click()
#     #     time.sleep(3)
#     #
#     #     # Wait for the dropdown to be clickable and click to open it
#     #     wait = WebDriverWait(self.driver, 10)
#     #     dropdown_xpath = "(//div[@class='ant-select-selector'])[4]"
#     #     dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #     dropdown.click()
#     #
#     #     # Collect all options in the dropdown
#     #     options_xpath = "//div[@class='rc-virtual-list-holder-inner']//descendant::div[@class='ant-select-item ant-select-item-option']"
#     #
#     #     while True:
#     #         options = wait.until(
#     #             EC.presence_of_all_elements_located((By.XPATH, options_xpath)))  # Adjust the XPath as needed
#     #         initial_count = len(options)
#     #
#     #         for option in options:
#     #             try:
#     #                 # Re-open the dropdown if necessary
#     #                 dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #                 dropdown.click()
#     #                 time.sleep(2)
#     #
#     #                 # Re-collect options to avoid stale elements
#     #                 options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #
#     #                 # Scroll the current option into view
#     #                 self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
#     #
#     #                 # Use JavaScript to click
#     #                 self.driver.execute_script("arguments[0].click();", option)
#     #                 print(option.text)
#     #                 time.sleep(3)  # Optional: wait to observe the click action
#     #
#     #                 # Verify the graph is displayed
#     #                 graph_xpath = "(//div[@class='relative']//descendant::div[@class='h-[150px] w-full pt-2'])[2]"
#     #                 try:
#     #                     graph = wait.until(EC.presence_of_element_located((By.XPATH, graph_xpath)))
#     #                     assert graph.is_displayed(), f"Graph not displayed for option: {option.text}"
#     #                     print(f"Graph displayed : {option.text}")
#     #                 except TimeoutException:
#     #                     print(f"Graph not displayed: {option.text}")
#     #
#     #             except (StaleElementReferenceException, IndexError):
#     #                 continue
#     #
#     #         # Re-collect options to check if new options are loaded
#     #         options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #         new_count = len(options)
#     #
#     #         if new_count == initial_count:
#     #             break  # Break the loop if no new options are loaded
#     #
#     #     # Optionally, perform any additional actions or assertions
#     #
#     #     # Close the WebDriver
#     #     self.driver.quit()
#     #
#     # def test_verify_system_child2_graph(self, setup):
#     #     self.logger.info("*************** Test_Infrastructure *********************")
#     #
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(5)  # Wait for the login to process
#     #     self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#     #     self.infrastructure.infrastructure_page_button()
#     #     time.sleep(4)
#     #     self.infrastructure.click_infrastructure_actions_button()
#     #     time.sleep(3)
#     #     self.driver.find_element(By.XPATH, "//div[text()='System']").click()
#     #     time.sleep(3)
#     #
#     #     # Wait for the dropdown to be clickable and click to open it
#     #     wait = WebDriverWait(self.driver, 10)
#     #     dropdown_xpath = "(//div[@class='ant-select-selector'])[5]"
#     #     dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #     dropdown.click()
#     #
#     #     # Collect all options in the dropdown
#     #     options_xpath = "//div[@class='rc-virtual-list-holder-inner']//descendant::div[@class='ant-select-item ant-select-item-option']"
#     #
#     #     while True:
#     #         options = wait.until(
#     #             EC.presence_of_all_elements_located((By.XPATH, options_xpath)))  # Adjust the XPath as needed
#     #         initial_count = len(options)
#     #
#     #         for option in options:
#     #             try:
#     #                 # Re-open the dropdown if necessary
#     #                 dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #                 dropdown.click()
#     #                 time.sleep(2)
#     #
#     #                 # Re-collect options to avoid stale elements
#     #                 options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #
#     #                 # Scroll the current option into view
#     #                 self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
#     #
#     #                 # Use JavaScript to click
#     #                 self.driver.execute_script("arguments[0].click();", option)
#     #                 print(option.text)
#     #                 time.sleep(3)  # Optional: wait to observe the click action
#     #
#     #                 # Verify the graph is displayed
#     #                 graph_xpath = "(//div[@class='relative']//descendant::div[@class='h-[150px] w-full pt-2'])[3]"
#     #                 try:
#     #                     graph = wait.until(EC.presence_of_element_located((By.XPATH, graph_xpath)))
#     #                     assert graph.is_displayed(), f"Graph not displayed for option: {option.text}"
#     #                     print(f"Graph displayed : {option.text}")
#     #                 except TimeoutException:
#     #                     print(f"Graph not displayed: {option.text}")
#     #
#     #             except (StaleElementReferenceException, IndexError):
#     #                 continue
#     #
#     #         # Re-collect options to check if new options are loaded
#     #         options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #         new_count = len(options)
#     #
#     #         if new_count == initial_count:
#     #             break  # Break the loop if no new options are loaded
#     #
#     #     # Optionally, perform any additional actions or assertions
#     #
#     #     # Close the WebDriver
#     #     self.driver.quit()
#     #
#     # def test_verify_storage_graph(self, setup):
#     #     self.logger.info("*************** Test_Infrastructure *********************")
#     #
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(5)  # Wait for the login to process
#     #     self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#     #     self.infrastructure.infrastructure_page_button()
#     #     time.sleep(4)
#     #     self.infrastructure.click_infrastructure_actions_button()
#     #     time.sleep(3)
#     #     self.driver.find_element(By.XPATH, "//div[text()='Storage']").click()
#     #     time.sleep(3)
#     #
#     #     # Wait for the dropdown to be clickable and click to open it
#     #     wait = WebDriverWait(self.driver, 10)
#     #     dropdown_xpath = "(//div[@class='ant-select-selector'])[3]"
#     #     dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #     dropdown.click()
#     #
#     #     # Collect all options in the dropdown
#     #     options_xpath = "//div[@class='rc-virtual-list-holder-inner']//descendant::div[@class='ant-select-item ant-select-item-option']"
#     #
#     #     while True:
#     #         options = wait.until(
#     #             EC.presence_of_all_elements_located((By.XPATH, options_xpath)))  # Adjust the XPath as needed
#     #         initial_count = len(options)
#     #
#     #         for option in options:
#     #             try:
#     #                 # Re-open the dropdown if necessary
#     #                 dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #                 dropdown.click()
#     #                 time.sleep(2)
#     #
#     #                 # Re-collect options to avoid stale elements
#     #                 options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #
#     #                 # Scroll the current option into view
#     #                 self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
#     #
#     #                 # Use JavaScript to click
#     #                 self.driver.execute_script("arguments[0].click();", option)
#     #                 print(option.text)
#     #                 time.sleep(3)  # Optional: wait to observe the click action
#     #
#     #                 # Verify the graph is displayed
#     #                 graph_xpath = "(//div[@class='relative']//descendant::div[@class='h-[150px] w-full pt-2'])[1]"
#     #                 try:
#     #                     graph = wait.until(EC.presence_of_element_located((By.XPATH, graph_xpath)))
#     #                     assert graph.is_displayed(), f"Graph not displayed for option: {option.text}"
#     #                     print(f"Graph displayed : {option.text}")
#     #                 except TimeoutException:
#     #                     print(f"Graph not displayed: {option.text}")
#     #
#     #             except (StaleElementReferenceException, IndexError):
#     #                 continue
#     #
#     #         # Re-collect options to check if new options are loaded
#     #         options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #         new_count = len(options)
#     #
#     #         if new_count == initial_count:
#     #             break  # Break the loop if no new options are loaded
#     #
#     #     # Optionally, perform any additional actions or assertions
#     #
#     #     # Close the WebDriver
#     #     self.driver.quit()
#     #
#     # def test_verify_storage_graph_child1(self, setup):
#     #     self.logger.info("*************** Test_Infrastructure *********************")
#     #
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(5)  # Wait for the login to process
#     #     self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#     #     self.infrastructure.infrastructure_page_button()
#     #     time.sleep(4)
#     #     self.infrastructure.click_infrastructure_actions_button()
#     #     time.sleep(3)
#     #     self.driver.find_element(By.XPATH, "//div[text()='Storage']").click()
#     #     time.sleep(3)
#     #
#     #     # Wait for the dropdown to be clickable and click to open it
#     #     wait = WebDriverWait(self.driver, 10)
#     #     dropdown_xpath = "(//div[@class='ant-select-selector'])[4]"
#     #     dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #     dropdown.click()
#     #
#     #     # Collect all options in the dropdown
#     #     options_xpath = "//div[@class='rc-virtual-list-holder-inner']//descendant::div[@class='ant-select-item ant-select-item-option']"
#     #
#     #     while True:
#     #         options = wait.until(
#     #             EC.presence_of_all_elements_located((By.XPATH, options_xpath)))  # Adjust the XPath as needed
#     #         initial_count = len(options)
#     #
#     #         for option in options:
#     #             try:
#     #                 # Re-open the dropdown if necessary
#     #                 dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #                 dropdown.click()
#     #                 time.sleep(2)
#     #
#     #                 # Re-collect options to avoid stale elements
#     #                 options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #
#     #                 # Scroll the current option into view
#     #                 self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
#     #
#     #                 # Use JavaScript to click
#     #                 self.driver.execute_script("arguments[0].click();", option)
#     #                 print(option.text)
#     #                 time.sleep(3)  # Optional: wait to observe the click action
#     #
#     #                 # Verify the graph is displayed
#     #                 graph_xpath = "(//div[@class='relative']//descendant::div[@class='h-[150px] w-full pt-2'])[2]"
#     #                 try:
#     #                     graph = wait.until(EC.presence_of_element_located((By.XPATH, graph_xpath)))
#     #                     assert graph.is_displayed(), f"Graph not displayed for option: {option.text}"
#     #                     print(f"Graph displayed : {option.text}")
#     #                 except TimeoutException:
#     #                     print(f"Graph not displayed: {option.text}")
#     #
#     #             except (StaleElementReferenceException, IndexError):
#     #                 continue
#     #
#     #         # Re-collect options to check if new options are loaded
#     #         options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #         new_count = len(options)
#     #
#     #         if new_count == initial_count:
#     #             break  # Break the loop if no new options are loaded
#     #
#     #     # Optionally, perform any additional actions or assertions
#     #
#     #     # Close the WebDriver
#     #     self.driver.quit()
#     #
#     # def test_verify_storage_graph_child2(self, setup):
#     #     self.logger.info("*************** Test_Infrastructure *********************")
#     #
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(5)  # Wait for the login to process
#     #     self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#     #     self.infrastructure.infrastructure_page_button()
#     #     time.sleep(4)
#     #     self.infrastructure.click_infrastructure_actions_button()
#     #     time.sleep(3)
#     #     self.driver.find_element(By.XPATH, "//div[text()='Storage']").click()
#     #     time.sleep(3)
#     #
#     #     # Wait for the dropdown to be clickable and click to open it
#     #     wait = WebDriverWait(self.driver, 10)
#     #     dropdown_xpath = "(//div[@class='ant-select-selector'])[5]"
#     #     dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #     dropdown.click()
#     #
#     #     # Collect all options in the dropdown
#     #     options_xpath = "//div[@class='rc-virtual-list-holder-inner']//descendant::div[@class='ant-select-item ant-select-item-option']"
#     #
#     #     while True:
#     #         options = wait.until(
#     #             EC.presence_of_all_elements_located((By.XPATH, options_xpath)))  # Adjust the XPath as needed
#     #         initial_count = len(options)
#     #
#     #         for option in options:
#     #             try:
#     #                 # Re-open the dropdown if necessary
#     #                 dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #                 dropdown.click()
#     #                 time.sleep(2)
#     #
#     #                 # Re-collect options to avoid stale elements
#     #                 options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #
#     #                 # Scroll the current option into view
#     #                 self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
#     #
#     #                 # Use JavaScript to click
#     #                 self.driver.execute_script("arguments[0].click();", option)
#     #                 print(option.text)
#     #                 time.sleep(3)  # Optional: wait to observe the click action
#     #
#     #                 # Verify the graph is displayed
#     #                 graph_xpath = "(//div[@class='relative']//descendant::div[@class='h-[150px] w-full pt-2'])[3]"
#     #                 try:
#     #                     graph = wait.until(EC.presence_of_element_located((By.XPATH, graph_xpath)))
#     #                     assert graph.is_displayed(), f"Graph not displayed for option: {option.text}"
#     #                     print(f"Graph displayed : {option.text}")
#     #                 except TimeoutException:
#     #                     print(f"Graph not displayed: {option.text}")
#     #
#     #             except (StaleElementReferenceException, IndexError):
#     #                 continue
#     #
#     #         # Re-collect options to check if new options are loaded
#     #         options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #         new_count = len(options)
#     #
#     #         if new_count == initial_count:
#     #             break  # Break the loop if no new options are loaded
#     #
#     #     # Optionally, perform any additional actions or assertions
#     #
#     #     # Close the WebDriver
#     #     self.driver.quit()
#     #
#     # def test_verify_network_graph(self, setup):
#     #     self.logger.info("*************** Test_Infrastructure Network Graph *********************")
#     #
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(5)  # Wait for the login to process
#     #     self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#     #     self.infrastructure.infrastructure_page_button()
#     #     time.sleep(4)
#     #     self.infrastructure.click_infrastructure_actions_button()
#     #     time.sleep(3)
#     #     self.driver.find_element(By.XPATH, "//div[text()='Network']").click()
#     #     time.sleep(3)
#     #
#     #     # Wait for the dropdown to be clickable and click to open it
#     #     wait = WebDriverWait(self.driver, 10)
#     #     dropdown_xpath = "(//div[@class='ant-select-selector'])[3]"
#     #     dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #     dropdown.click()
#     #
#     #     # Collect all options in the dropdown
#     #     options_xpath = "//div[@class='rc-virtual-list-holder-inner']//descendant::div[@class='ant-select-item ant-select-item-option']"
#     #
#     #     while True:
#     #         options = wait.until(
#     #             EC.presence_of_all_elements_located((By.XPATH, options_xpath)))  # Adjust the XPath as needed
#     #         initial_count = len(options)
#     #
#     #         for option in options:
#     #             try:
#     #                 # Re-open the dropdown if necessary
#     #                 dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #                 dropdown.click()
#     #                 time.sleep(2)
#     #
#     #                 # Re-collect options to avoid stale elements
#     #                 options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #
#     #                 # Scroll the current option into view
#     #                 self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
#     #
#     #                 # Use JavaScript to click
#     #                 self.driver.execute_script("arguments[0].click();", option)
#     #                 print(option.text)
#     #                 time.sleep(3)  # Optional: wait to observe the click action
#     #
#     #                 # Verify the graph is displayed
#     #                 graph_xpath = "(//div[@class='relative']//descendant::div[@class='h-[150px] w-full pt-2'])[1]"
#     #                 try:
#     #                     graph = wait.until(EC.presence_of_element_located((By.XPATH, graph_xpath)))
#     #                     assert graph.is_displayed(), f"Graph not displayed for option: {option.text}"
#     #                     print(f"Graph displayed : {option.text}")
#     #                 except TimeoutException:
#     #                     print(f"Graph not displayed: {option.text}")
#     #
#     #             except (StaleElementReferenceException, IndexError):
#     #                 continue
#     #
#     #         # Re-collect options to check if new options are loaded
#     #         options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #         new_count = len(options)
#     #
#     #         if new_count == initial_count:
#     #             break  # Break the loop if no new options are loaded
#     #
#     #     # Optionally, perform any additional actions or assertions
#     #
#     #     # Close the WebDriver
#     #     self.driver.quit()
#     #
#     # def test_verify_network_graph_child1(self, setup):
#     #     self.logger.info("*************** Test_Infrastructure Network Graph child1 *********************")
#     #
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(5)  # Wait for the login to process
#     #     self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#     #     self.infrastructure.infrastructure_page_button()
#     #     time.sleep(4)
#     #     self.infrastructure.click_infrastructure_actions_button()
#     #     time.sleep(3)
#     #     self.driver.find_element(By.XPATH, "//div[text()='Network']").click()
#     #     time.sleep(3)
#     #
#     #     # Wait for the dropdown to be clickable and click to open it
#     #     wait = WebDriverWait(self.driver, 10)
#     #     dropdown_xpath = "(//div[@class='ant-select-selector'])[4]"
#     #     dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #     dropdown.click()
#     #
#     #     # Collect all options in the dropdown
#     #     options_xpath = "//div[@class='rc-virtual-list-holder-inner']//descendant::div[@class='ant-select-item ant-select-item-option']"
#     #
#     #     while True:
#     #         options = wait.until(
#     #             EC.presence_of_all_elements_located((By.XPATH, options_xpath)))  # Adjust the XPath as needed
#     #         initial_count = len(options)
#     #
#     #         for option in options:
#     #             try:
#     #                 # Re-open the dropdown if necessary
#     #                 dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #                 dropdown.click()
#     #                 time.sleep(2)
#     #
#     #                 # Re-collect options to avoid stale elements
#     #                 options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #
#     #                 # Scroll the current option into view
#     #                 self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
#     #
#     #                 # Use JavaScript to click
#     #                 self.driver.execute_script("arguments[0].click();", option)
#     #                 print(option.text)
#     #                 time.sleep(3)  # Optional: wait to observe the click action
#     #
#     #                 # Verify the graph is displayed
#     #                 graph_xpath = "(//div[@class='relative']//descendant::div[@class='h-[150px] w-full pt-2'])[2]"
#     #                 try:
#     #                     graph = wait.until(EC.presence_of_element_located((By.XPATH, graph_xpath)))
#     #                     assert graph.is_displayed(), f"Graph not displayed for option: {option.text}"
#     #                     print(f"Graph displayed : {option.text}")
#     #                 except TimeoutException:
#     #                     print(f"Graph not displayed: {option.text}")
#     #
#     #             except (StaleElementReferenceException, IndexError):
#     #                 continue
#     #
#     #         # Re-collect options to check if new options are loaded
#     #         options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #         new_count = len(options)
#     #
#     #         if new_count == initial_count:
#     #             break  # Break the loop if no new options are loaded
#     #
#     #     # Optionally, perform any additional actions or assertions
#     #
#     #     # Close the WebDriver
#     #     self.driver.quit()
#     #
#     # def test_verify_network_graph_child2(self, setup):
#     #     self.logger.info("*************** Test_Infrastructure Network Graph child 2 *********************")
#     #
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(5)  # Wait for the login to process
#     #     self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#     #     self.infrastructure.infrastructure_page_button()
#     #     time.sleep(4)
#     #     self.infrastructure.click_infrastructure_actions_button()
#     #     time.sleep(3)
#     #     self.driver.find_element(By.XPATH, "//div[text()='Network']").click()
#     #     time.sleep(3)
#     #
#     #     # Wait for the dropdown to be clickable and click to open it
#     #     wait = WebDriverWait(self.driver, 10)
#     #     dropdown_xpath = "(//div[@class='ant-select-selector'])[5]"
#     #     dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #     dropdown.click()
#     #
#     #     # Collect all options in the dropdown
#     #     options_xpath = "//div[@class='rc-virtual-list-holder-inner']//descendant::div[@class='ant-select-item ant-select-item-option']"
#     #
#     #     while True:
#     #         options = wait.until(
#     #             EC.presence_of_all_elements_located((By.XPATH, options_xpath)))  # Adjust the XPath as needed
#     #         initial_count = len(options)
#     #
#     #         for option in options:
#     #             try:
#     #                 # Re-open the dropdown if necessary
#     #                 dropdown = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
#     #                 dropdown.click()
#     #                 time.sleep(2)
#     #
#     #                 # Re-collect options to avoid stale elements
#     #                 options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #
#     #                 # Scroll the current option into view
#     #                 self.driver.execute_script("arguments[0].scrollIntoView(true);", option)
#     #
#     #                 # Use JavaScript to click
#     #                 self.driver.execute_script("arguments[0].click();", option)
#     #                 print(option.text)
#     #                 time.sleep(3)  # Optional: wait to observe the click action
#     #
#     #                 # Verify the graph is displayed
#     #                 graph_xpath = "(//div[@class='relative']//descendant::div[@class='h-[150px] w-full pt-2'])[3]"
#     #                 try:
#     #                     graph = wait.until(EC.presence_of_element_located((By.XPATH, graph_xpath)))
#     #                     assert graph.is_displayed(), f"Graph not displayed for option: {option.text}"
#     #                     print(f"Graph displayed : {option.text}")
#     #                 except TimeoutException:
#     #                     print(f"Graph not displayed: {option.text}")
#     #
#     #             except (StaleElementReferenceException, IndexError):
#     #                 continue
#     #
#     #         # Re-collect options to check if new options are loaded
#     #         options = wait.until(EC.presence_of_all_elements_located((By.XPATH, options_xpath)))
#     #         new_count = len(options)
#     #
#     #         if new_count == initial_count:
#     #             break  # Break the loop if no new options are loaded
#     #
#     #     # Optionally, perform any additional actions or assertions
#     #
#     #     # Close the WebDriver
#     #     self.driver.quit()
#     #
#     # def test_verify_system_cpu_table_data(self, setup):
#     #     self.logger.info("*************** Test_Infrastructure system cpu table data *********************")
#     #
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(5)  # Wait for the login to process
#     #     self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#     #     time.sleep(3)
#     #     self.infrastructure.infrastructure_page_button()
#     #     time.sleep(4)
#     #     self.infrastructure.click_infrastructure_actions_button()
#     #     time.sleep(3)
#     #     self.driver.find_element(By.XPATH, "//div[text()='System']").click()
#     #     time.sleep(7)
#     #
#     #     # Locate the table element
#     #     table = self.driver.find_element(By.XPATH, "(//div[@class='ant-spin-container'])[6]")
#     #
#     #     # Capture the header row
#     #     header = table.find_elements(By.XPATH, ".//thead//th")
#     #     header_row = [cell.text for cell in header]
#     #
#     #     # Get the initial row count
#     #     rows = table.find_elements(By.XPATH, ".//tbody//tr")
#     #     initial_row_count = len(rows)
#     #
#     #     # Scroll the table and gather all rows
#     #     table_data = []
#     #     previous_row_count = 0
#     #
#     #     while True:
#     #         # Locate all rows in the table
#     #         rows = table.find_elements(By.XPATH, ".//tbody//tr")
#     #
#     #         # If the row count hasn't changed after scrolling, break the loop
#     #         if len(rows) == previous_row_count:
#     #             break
#     #
#     #         previous_row_count = len(rows)
#     #
#     #         # Prepare data for DataFrame
#     #         for row in rows:
#     #             # Locate all cells in the current row
#     #             cells = row.find_elements(By.XPATH, ".//td")
#     #             time.sleep(1)
#     #             row_data = [cell.text for cell in cells]
#     #             if row_data not in table_data:  # Avoid adding duplicate rows
#     #                 table_data.append(row_data)
#     #
#     #         # Scroll to the last row to load more rows
#     #         actions = ActionChains(self.driver)
#     #         actions.move_to_element(rows[-1]).perform()
#     #         time.sleep(2)
#     #
#     #     # Ensure all rows have the same number of columns
#     #     max_columns = max(len(row) for row in table_data)
#     #     for row in table_data:
#     #         while len(row) < max_columns:
#     #             row.append('')
#     #
#     #     # Create DataFrame
#     #     df = pd.DataFrame(table_data, columns=header_row)
#     #
#     #     # Generate the formatted table output using tabulate
#     #     formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
#     #
#     #     # Write the formatted table to a text file
#     #     with open('table_system_cpu.txt', 'w', encoding='utf-8') as file:
#     #         file.write(formatted_table)
#     #
#     #     print("Table data has been saved to 'table_system_cpu.txt'.")
#     #
#     #
#     # def test_verify_system_cpu_table2_data(self, setup):
#     #     self.logger.info("*************** Test_Infrastructure system cpu table2 data *********************")
#     #
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(5)  # Wait for the login to process
#     #     self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#     #     time.sleep(3)
#     #     self.infrastructure.infrastructure_page_button()
#     #     time.sleep(4)
#     #     self.infrastructure.click_infrastructure_actions_button()
#     #     time.sleep(3)
#     #     self.driver.find_element(By.XPATH, "//div[text()='System']").click()
#     #     time.sleep(7)
#     #
#     #     # Locate the table element
#     #     table = self.driver.find_element(By.XPATH, "(//div[@class='ant-spin-container'])[7]")
#     #
#     #     # Capture the header row
#     #     header = table.find_elements(By.XPATH, ".//thead//th")
#     #     header_row = [cell.text for cell in header]
#     #
#     #     table_data = []
#     #
#     #     while True:
#     #         # Locate all rows in the table
#     #         rows = table.find_elements(By.XPATH, ".//tbody//tr")
#     #
#     #         # Prepare data for DataFrame
#     #         for row in rows:
#     #             # Locate all cells in the current row
#     #             cells = row.find_elements(By.XPATH, ".//td")
#     #             row_data = [cell.text for cell in cells]
#     #             if row_data not in table_data:  # Avoid adding duplicate rows
#     #                 table_data.append(row_data)
#     #
#     #         # Check if the next page button is enabled
#     #         try:
#     #             next_button = self.driver.find_element(By.XPATH, "//li[@class='ant-pagination-next']//button")
#     #             if 'disabled' in next_button.get_attribute('class'):
#     #                 break
#     #         except:
#     #             break
#     #
#     #         # Click the next page button
#     #         next_button.click()
#     #         time.sleep(2)
#     #
#     #         # Refresh the table element after clicking next button
#     #         table = self.driver.find_element(By.XPATH, "(//div[@class='ant-spin-container'])[7]")
#     #
#     #     # Ensure all rows have the same number of columns
#     #     max_columns = max(len(row) for row in table_data)
#     #     for row in table_data:
#     #         while len(row) < max_columns:
#     #             row.append('')
#     #
#     #     # Create DataFrame
#     #     df = pd.DataFrame(table_data, columns=header_row)
#     #
#     #     # Generate the formatted table output using tabulate
#     #     formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
#     #
#     #     # Write the formatted table to a text file
#     #     with open('table2_system_cpu.txt', 'w', encoding='utf-8') as file:
#     #         file.write(formatted_table)
#     #
#     #     print("Table data has been saved to 'table2_system_cpu.txt'.")
#     #
#     # def test_verify_system_memorytable_data(self, setup):
#     #     self.logger.info("*************** Test_Infrastructure system cpu table2 data *********************")
#     #
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(8)  # Wait for the login to process
#     #     self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#     #     time.sleep(3)
#     #     self.infrastructure.infrastructure_page_button()
#     #     time.sleep(4)
#     #     self.infrastructure.click_infrastructure_actions_button()
#     #     time.sleep(3)
#     #     self.driver.find_element(By.XPATH, "//div[text()='System']").click()
#     #     time.sleep(7)
#     #     self.driver.find_element(By.XPATH, "//div[text()='Memory']").click()
#     #     time.sleep(5)
#     #
#     #     # Locate the table element
#     #     table = self.driver.find_element(By.XPATH, "(//div[@class='ant-spin-container'])[6]")
#     #
#     #     # Capture the header row
#     #     header = table.find_elements(By.XPATH, ".//thead//th")
#     #     header_row = [cell.text for cell in header]
#     #
#     #     table_data = []
#     #
#     #     while True:
#     #         # Locate all rows in the table
#     #         rows = table.find_elements(By.XPATH, ".//tbody//tr")
#     #
#     #         # Prepare data for DataFrame
#     #         for row in rows:
#     #             # Locate all cells in the current row
#     #             cells = row.find_elements(By.XPATH, ".//td")
#     #             row_data = [cell.text for cell in cells]
#     #             if row_data not in table_data:  # Avoid adding duplicate rows
#     #                 table_data.append(row_data)
#     #
#     #         # Check if the next page button is enabled
#     #         try:
#     #             next_button = self.driver.find_element(By.XPATH, "//li[@class='ant-pagination-next']//button")
#     #             if 'disabled' in next_button.get_attribute('class'):
#     #                 break
#     #         except:
#     #             break
#     #
#     #         # Click the next page button
#     #         next_button.click()
#     #         time.sleep(2)
#     #
#     #         # Refresh the table element after clicking next button
#     #         table = self.driver.find_element(By.XPATH, "(//div[@class='ant-spin-container'])[7]")
#     #
#     #     # Ensure all rows have the same number of columns
#     #     max_columns = max(len(row) for row in table_data)
#     #     for row in table_data:
#     #         while len(row) < max_columns:
#     #             row.append('')
#     #
#     #     # Create DataFrame
#     #     df = pd.DataFrame(table_data, columns=header_row)
#     #
#     #     # Generate the formatted table output using tabulate
#     #     formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
#     #
#     #     # Write the formatted table to a text file
#     #     with open('table_system_memory.txt', 'w', encoding='utf-8') as file:
#     #         file.write(formatted_table)
#     #
#     #     print("Table data has been saved to 'table_system_memory.txt'.")
#     #
#     # # execution is pending
#     #
#     # def test_verify_storage_table_data(self, setup):
#     #     self.logger.info("*************** Test_Infrastructure storage table data *********************")
#     #
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(8)  # Wait for the login to process
#     #     self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#     #     time.sleep(3)
#     #     self.infrastructure.infrastructure_page_button()
#     #     time.sleep(4)
#     #     self.infrastructure.click_infrastructure_actions_button()
#     #     time.sleep(3)
#     #     self.driver.find_element(By.XPATH, "//div[text()='Storage']").click()
#     #     time.sleep(7)
#     #
#     #     # Locate the table element
#     #     table = self.driver.find_element(By.XPATH, "(//div[@class='ant-spin-container'])[7]")
#     #
#     #     # Capture the header row
#     #     header = table.find_elements(By.XPATH, ".//thead//th")
#     #     header_row = [cell.text for cell in header]
#     #
#     #     table_data = []
#     #
#     #     while True:
#     #         # Locate all rows in the table
#     #         rows = table.find_elements(By.XPATH, ".//tbody//tr")
#     #
#     #         # Prepare data for DataFrame
#     #         for row in rows:
#     #             # Locate all cells in the current row
#     #             cells = row.find_elements(By.XPATH, ".//td")
#     #             row_data = [cell.text for cell in cells]
#     #             if row_data not in table_data:  # Avoid adding duplicate rows
#     #                 table_data.append(row_data)
#     #
#     #         # Check if the next page button is enabled
#     #         try:
#     #             next_button = self.driver.find_element(By.XPATH, "//li[@class='ant-pagination-next']//button")
#     #             if 'disabled' in next_button.get_attribute('class'):
#     #                 break
#     #         except:
#     #             break
#     #
#     #         # Click the next page button
#     #         next_button.click()
#     #         time.sleep(2)
#     #
#     #         # Refresh the table element after clicking next button
#     #         table = self.driver.find_element(By.XPATH, "(//div[@class='ant-spin-container'])[7]")
#     #
#     #     # Ensure all rows have the same number of columns
#     #     max_columns = max(len(row) for row in table_data)
#     #     for row in table_data:
#     #         while len(row) < max_columns:
#     #             row.append('')
#     #
#     #     # Create DataFrame
#     #     df = pd.DataFrame(table_data, columns=header_row)
#     #
#     #     # Generate the formatted table output using tabulate
#     #     formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
#     #
#     #     # Write the formatted table to a text file
#     #     with open('table_storage.txt', 'w', encoding='utf-8') as file:
#     #         file.write(formatted_table)
#     #
#     #     print("Table data has been saved to 'table_storage.txt'.")
#     #
#     # #execution is pending
#     # def test_verify_network_table_data(self, setup):
#     #     self.logger.info("*************** Test_Infrastructure storage table data *********************")
#     #
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(8)  # Wait for the login to process
#     #     self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#     #     time.sleep(3)
#     #     self.infrastructure.infrastructure_page_button()
#     #     time.sleep(4)
#     #     self.infrastructure.click_infrastructure_actions_button()
#     #     time.sleep(3)
#     #     self.driver.find_element(By.XPATH, "//div[text()='Network']").click()
#     #     time.sleep(7)
#     #
#     #     # Locate the table element
#     #     table = self.driver.find_element(By.XPATH, "(//div[@class='ant-spin-container'])[4]")
#     #
#     #     # Capture the header row
#     #     header = table.find_elements(By.XPATH, ".//thead//th")
#     #     header_row = [cell.text for cell in header]
#     #
#     #     table_data = []
#     #
#     #     while True:
#     #         # Locate all rows in the table
#     #         rows = table.find_elements(By.XPATH, ".//tbody//tr")
#     #
#     #         # Prepare data for DataFrame
#     #         for row in rows:
#     #             # Locate all cells in the current row
#     #             cells = row.find_elements(By.XPATH, ".//td")
#     #             row_data = [cell.text for cell in cells]
#     #             if row_data not in table_data:  # Avoid adding duplicate rows
#     #                 table_data.append(row_data)
#     #
#     #         # Check if the next page button is enabled
#     #         try:
#     #             next_button = self.driver.find_element(By.XPATH, "//li[@class='ant-pagination-next']//button")
#     #             if 'disabled' in next_button.get_attribute('class'):
#     #                 break
#     #         except:
#     #             break
#     #
#     #         # Click the next page button
#     #         next_button.click()
#     #         time.sleep(2)
#     #
#     #         # Refresh the table element after clicking next button
#     #         table = self.driver.find_element(By.XPATH, "(//div[@class='ant-spin-container'])[7]")
#     #
#     #     # Ensure all rows have the same number of columns
#     #     max_columns = max(len(row) for row in table_data)
#     #     for row in table_data:
#     #         while len(row) < max_columns:
#     #             row.append('')
#     #
#     #     # Create DataFrame
#     #     df = pd.DataFrame(table_data, columns=header_row)
#     #
#     #     # Generate the formatted table output using tabulate
#     #     formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
#     #
#     #     # Write the formatted table to a text file
#     #     with open('table_network.txt', 'w', encoding='utf-8') as file:
#     #         file.write(formatted_table)
#     #
#     #     print("Table data has been saved to 'table_network.txt'.")
#     #
#     # # execution is pending
#     # def test_verify_alert_table_data(self, setup):
#     #     self.logger.info("*************** Test_Infrastructure alert table data *********************")
#     #
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(8)  # Wait for the login to process
#     #     self.infrastructure = Zoomview_Infrastructure_Page(self.driver)
#     #     time.sleep(3)
#     #     self.infrastructure.infrastructure_page_button()
#     #     time.sleep(4)
#     #     self.infrastructure.click_infrastructure_actions_button()
#     #     time.sleep(3)
#     #     self.driver.find_element(By.XPATH, "//div[text()='Alert']").click()
#     #     time.sleep(7)
#     #
#     #     # Locate the table element
#     #     table = self.driver.find_element(By.XPATH, "//div[@class='ant-spin-container']")
#     #
#     #     # Capture the header row
#     #     header = table.find_elements(By.XPATH, ".//thead//th")
#     #     header_row = [cell.text for cell in header]
#     #
#     #     table_data = []
#     #
#     #     while True:
#     #         # Locate all rows in the table
#     #         rows = table.find_elements(By.XPATH, ".//tbody//tr")
#     #
#     #         # Prepare data for DataFrame
#     #         for row in rows:
#     #             # Locate all cells in the current row
#     #             cells = row.find_elements(By.XPATH, ".//td")
#     #             row_data = [cell.text for cell in cells]
#     #             if row_data not in table_data:  # Avoid adding duplicate rows
#     #                 table_data.append(row_data)
#     #
#     #         # Check if the next page button is enabled
#     #         try:
#     #             next_button = self.driver.find_element(By.XPATH, "//li[@class='ant-pagination-next']//button")
#     #             if 'disabled' in next_button.get_attribute('class'):
#     #                 break
#     #         except:
#     #             break
#     #
#     #         # Click the next page button
#     #         next_button.click()
#     #         time.sleep(2)
#     #
#     #         # Refresh the table element after clicking next button
#     #         table = self.driver.find_element(By.XPATH, "//div[@class='ant-spin-container']")
#     #
#     #     # Ensure all rows have the same number of columns
#     #     max_columns = max(len(row) for row in table_data)
#     #     for row in table_data:
#     #         while len(row) < max_columns:
#     #             row.append('')
#     #
#     #     # Create DataFrame
#     #     df = pd.DataFrame(table_data, columns=header_row)
#     #
#     #     # Generate the formatted table output using tabulate
#     #     formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
#     #
#     #     # Write the formatted table to a text file
#     #     with open('table_alert.txt', 'w', encoding='utf-8') as file:
#     #         file.write(formatted_table)
#     #
#     #     print("Table data has been saved to 'table_alert.txt'.")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
