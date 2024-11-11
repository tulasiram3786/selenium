# import time
# import pytest
# from selenium import webdriver
# from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
# from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.common.by import By
# from base_pages.Infrastructure_Page import Zoomview_Infrastructure_Page
# from base_pages.Login_Page import Zoomview_Login_Page
# from base_pages.Logs_Page import Zoomview_Logs_Page
# from base_pages.Signup_Page import Zoomview_Signup_Page
# from utilities.read_properties import Read_Config
# from utilities.custom_logger import Log_Maker
# from tabulate import tabulate
# import pandas as pd
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class Test_Logs_AllLogs:
#     loginpage_url = Read_Config.get_loginpage_url()
#     email = Read_Config.get_email()
#     password = Read_Config.get_password()
#     logger = Log_Maker.log_gen()
#
#     def test_title_verification_for_logs_page(self, setup):
#         self.logger.info("*************** Test_Logs *********************")
#         self.logger.info("*************** verification of Logs page title *********************")
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
#         act_title = self.driver.title
#         exp_title = "ZoomView | Logs | All Logs"
#         print("Logs page Title :- ", act_title)
#
#         if act_title == exp_title:
#             self.logger.info(
#                 "*************** test_title_verification_for_logs_page - Title Matched *********************")
#             assert True
#             self.driver.close()
#         else:
#             self.driver.save_screenshot(".\\screenshots\\test_title_verification_for_logs_page.png")
#             self.logger.info(
#                 "*************** test_title_verification_for_logs_page - Title not matched *********************")
#             self.driver.close()
#             assert False
#
#     @pytest.mark.tulasi
#     def test_verify_all_logs_tab_graph(self,setup):
#         self.logger.info("*************** Test_Logs verifying all logs tab graph *********************")
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
#         self.logs = Zoomview_Logs_Page(self.driver)
#         self.logs.click_Logs()
#         time.sleep(2)
#         self.logs.click_AllLogs()
#         time.sleep(5)
#         # self.logs.click_on_time_interval_dropdown()
#         # time.sleep(3)
#         # self.logs.click_on_interval_dropdown_options()
#         # time.sleep(7)
#
#         try:
#             alllogs_graph = self.driver.find_element(By.XPATH, self.logs.logspage_all_logs_graph_xpath)
#             if alllogs_graph.is_displayed():
#                 print("All Logs Tab Graph is there")
#             else:
#                 print("No Graph for all logs tab")
#
#         except:
#
#             no_alllogs_graph = self.driver.find_element(By.XPATH, self.logs.logspage_all_logs_no_graph_xpath)
#             print("all logs Graph :- ",no_alllogs_graph.text)
#
#     #its working fine
#     def test_verify_alllogs_tabledata(self, setup):
#         self.logger.info(
#             "*************** Test_Logs_AllLogs verifying and printing all logs table data *********************"
#         )
#
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#
#         # Login process
#         self.login = Zoomview_Login_Page(self.driver)
#         self.login.enter_email(self.email)
#         self.login.enter_password(self.password)
#         self.login.click_login()
#         time.sleep(5)
#
#         # Navigate to the Logs page
#         self.logs = Zoomview_Logs_Page(self.driver)
#         self.logs.click_Logs()
#         time.sleep(2)
#         self.logs.click_AllLogs()
#         time.sleep(5)
#
#         # Wait until the table rows are present
#         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table/tbody/tr")))
#
#         # Locate the table element
#         table = self.driver.find_element(By.XPATH, "//table")
#
#         # Capture the header row
#         header = table.find_elements(By.XPATH, ".//thead//th")
#         header_row = [cell.text for cell in header]
#
#         # Initialize variables for collecting data
#         table_data = []
#         previous_row_count = 0
#         start_time = time.time()  # Start timer
#
#         # Set a max duration to run the loop (15 seconds)
#         while time.time() - start_time < 15:
#             # Get the current rows
#             rows = table.find_elements(By.XPATH, ".//tbody//tr")
#             current_row_count = len(rows)
#
#             # If no new rows are loaded, stop scrolling
#             if current_row_count == previous_row_count:
#                 break
#
#             # Gather data from new rows
#             for row in rows[previous_row_count:]:
#                 cells = row.find_elements(By.XPATH, ".//td")
#                 row_data = [cell.text for cell in cells]
#                 if row_data:  # Only append if the row has data
#                     table_data.append(row_data)
#
#             previous_row_count = current_row_count
#
#             # Scroll to the last row to load more data
#             if rows:
#                 actions = ActionChains(self.driver)
#                 actions.move_to_element(rows[-1]).perform()
#             time.sleep(1)  # Wait for more rows to load
#
#         # After collecting data for 15 seconds or until no more rows are loaded
#         # Add logic to ensure that table header and body are processed correctly
#
#         # Locate the table header and all rows in the table (both header and body)
#         rows = table.find_elements(By.XPATH, ".//tr")
#
#         # Prepare data for DataFrame
#         for row in rows:
#             # Locate all cells in the current row (both header and body)
#             cells = row.find_elements(By.XPATH, ".//td | .//th")
#             row_data = [cell.text for cell in cells]
#             table_data.append(row_data)
#
#         # Create DataFrame from table_data
#         df = pd.DataFrame(table_data[1:], columns=table_data[0])
#
#         # Generate the formatted table output using tabulate
#         formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
#
#         # Write the formatted table to a text file
#         with open('table_Zoomview_all_logs.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'table_Zoomview_all_logs.txt'.")
#
#     #its working fine
#     def test_verify_search_and_table_data(self, setup):
#         self.logger.info(
#             "*************** Test_Logs_AllLogs verifying search and printing table data *********************")
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
#         self.logs = Zoomview_Logs_Page(self.driver)
#         self.logs.click_Logs()
#         time.sleep(2)
#         self.logs.click_AllLogs()
#         time.sleep(5)
#
#         self.logs.enter_logs_searchbox("Log=500")
#         time.sleep(3)
#         self.logs.click_enterbutton()
#         time.sleep(5)
#
#         formatted_table = self.logs.table_data()
#
#         # Write the formatted table to a text file
#         with open('table_all_logs_savedfilter_table11.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'table_all_logs_savedfilter_table11.txt'.")
#
#         self.logs.click_savebutton()
#         time.sleep(2)
#
#
#
#         self.logs.enter_text_into_savebutton("Tulasiram-10")
#         time.sleep(2)
#
#         self.logs.click_savebutton_inside_savebutton()
#         time.sleep(4)
#
#         # Wait for the toast message to appear
#         toast_message_xpath = "//div[text()='Log view created successfully']"
#         try:
#             # Wait for the toast message to be present and visible
#             toast_message = WebDriverWait(self.driver, 10).until(
#                 EC.visibility_of_element_located((By.XPATH, toast_message_xpath))
#             )
#             # Print the text of the toast message
#             print("Toast Message :- ", toast_message.text)
#         except Exception as e:
#             self.logger.error("Toast message not found or not visible")
#             print("Toast message not found or not visible")
#
#
#     def test_logs_verify_alllogsdata(self, setup):
#         self.logger.info("*************** Test_Logs_AllLogs  *********************")
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
#         self.logs = Zoomview_Logs_Page(self.driver)
#         self.logs.click_Logs()
#         time.sleep(2)
#         self.logs.click_AllLogs()
#         time.sleep(5)
#         self.logs.click_alllogdata()
#         time.sleep(3)
#         formatted_table = self.logs.table2_data()
#
#         # Write the formatted table to a text file
#         with open('table_all_logs_alllogData.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'table_all_logs_alllogData.txt'.")
#
#
#     def test_logs_verify_export_json(self, setup):
#         self.logger.info("*************** Test_Logs_AllLogs verify Export Json Option data *********************")
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
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
#         # self.logs.click_on_time_interval_dropdown()
#         # time.sleep(3)
#         # self.logs.click_on_interval_dropdown_options()
#         time.sleep(7)
#         self.logs.click_exportbutton()
#         time.sleep(2)
#         self.logs.click_exportbutton_json()
#         time.sleep(2)
#         self.logs.click_on_export_limit_dropdown()
#         time.sleep(3)
#         self.logs.export_limit_dropdown_json()
#         time.sleep(3)
#         self.logs.click_download_button()
#         time.sleep(5)
#
#
#     def test_logs_verify_export_csv(self, setup):
#         self.logger.info("*************** Test_Logs_AllLogs verify Export csv Option data *********************")
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
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
#         # self.logs.click_on_time_interval_dropdown()
#         # time.sleep(3)
#         # self.logs.click_on_interval_dropdown_options()
#         # time.sleep(7)
#         self.logs.click_exportbutton()
#         time.sleep(2)
#         self.logs.click_exportbutton_csv()
#         time.sleep(2)
#         self.logs.click_on_export_limit_dropdown()
#         time.sleep(3)
#         self.logs.export_limit_dropdown_csv()
#         time.sleep(3)
#         self.logs.click_download_button()
#         time.sleep(3)
#
#
#     def test_logs_verify_settings(self, setup):
#         self.logger.info("*************** Test_Logs_AllLogs verify settings *********************")
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
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
#         self.logs.click_on_logs_settings()
#         time.sleep(2)
#         self.logs.click_on_logs_selectall_checkbox()
#         time.sleep(2)
#         # self.logs.click_on_logs_empty_selectall_checkbox()
#         # time.sleep(2)
#         self.logs.click_on_logs_settings_save()
#         time.sleep(3)
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
#
#
