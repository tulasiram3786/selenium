# import time
# import pandas as pd
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from tabulate import tabulate
# from base_pages.Login_Page import Zoomview_Login_Page
# from base_pages.Logs_Page import Zoomview_Logs_Page
# from base_pages.Payments_PlanandUsage import Zoomview_Payments_Page
# from utilities.random import generate_random_text
# from utilities.read_properties import Read_Config
# from utilities.custom_logger import Log_Maker
#
#
# class Test_Billing_PlanandUsage:
#     loginpage_url = Read_Config.get_loginpage_url()
#     email = Read_Config.get_email()
#     password = Read_Config.get_password()
#     logger = Log_Maker.log_gen()
#
#     @pytest.mark.tulasidfgfdg
#     def test_title_verification_for_PlanandUsage(self, setup):
#         self.logger.info("*************** test_title_verification_for_PlanandUsage *********************")
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#
#         try:
#             # --------- calling login page ------------#
#             self.login = Zoomview_Login_Page(self.driver)
#             self.login.enter_email(self.email)
#             self.login.enter_password(self.password)
#             self.login.click_login()
#
#             # Wait for the page to load after login
#             WebDriverWait(self.driver, 10).until(EC.title_contains("Dashboard"))  # Adjust the title as necessary
#
#             self.payments = Zoomview_Payments_Page(self.driver)
#             self.payments.click_PlanandUsage_link()
#             time.sleep(3)
#
#             # Wait until the Notification Group page is loaded
#             WebDriverWait(self.driver, 10).until(EC.title_contains("Payment Usage"))
#
#             act_title = self.driver.title
#             exp_title = "ZoomView | Payment Usage"
#             print("Plan and Usage Page Title :- ", act_title)
#
#             if act_title == exp_title:
#                 self.logger.info(
#                     "*************** test_title_verification_for_PlanandUsage - Title Matched *********************")
#                 assert True
#             else:
#                 self.driver.save_screenshot(".\\screenshots\\test_title_verification_for_PlanandUsage.png")
#                 self.logger.info(
#                     "*************** test_title_verification_for_PlanandUsage - Title not matched *********************")
#                 assert False
#
#         except Exception as e:
#             self.logger.error(f"An error occurred: {e}")
#             self.driver.save_screenshot(".\\screenshots\\test_title_verification_for_PlanandUsage.png")
#             assert False
#         finally:
#             self.driver.quit()  # Ensure the driver is closed in all cases
#
#     @pytest.mark.tulasisdfsdf
#     def test_print_PlanandUsage_table(self, setup):
#         self.logger.info("*************** test_print_PlanandUsage_table printing table data *********************")
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
#
#         self.payments = Zoomview_Payments_Page(self.driver)
#         self.payments.click_PlanandUsage_link()
#         time.sleep(3)
#
#         self.logs = Zoomview_Logs_Page(self.driver)
#
#         formatted_table = self.logs.table_data()
#
#         # Write the formatted table to a text file
#         with open('PlanandUsage_table.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'PlanandUsage_table.txt'.")
#
#     @pytest.mark.tulasi
#     def test_PlanandPricing(self, setup):
#         self.logger.info("*************** test_PlanandPricing  *********************")
#
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#         self.login = Zoomview_Login_Page(self.driver)
#         self.login.enter_email(self.email)
#         self.login.enter_password(self.password)
#         self.login.click_login()
#         time.sleep(5)  # Wait for the login to process
#
#         self.payments = Zoomview_Payments_Page(self.driver)
#         self.payments.click_PlanandUsage_link()
#         time.sleep(3)
#         self.payments.click_PlanandUsage_PlanandPricing()
#         time.sleep(2)
#         self.payments.click_Storage()
#         time.sleep(3)
#         self.payments.enter_text_into_storage_GB("2")
#         time.sleep(2)
#         self.payments.click_continuetopayment()
#         self.payments.enter_text_into_Billing_Contact_Name("Tulasiram")
#         self.payments.enter_text_into_Billing_Company_Name("zybisys")
#         self.payments.enter_text_into_Billing_Address("jayanagar")
#         self.payments.enter_text_into_Billing_City("Bengaluru")
#         self.payments.enter_text_into_Billing_PostalCode("560041")
#         self.payments.enter_text_into_Billing_Country("India")
#         time.sleep(2)
#         self.payments.click_processofflinebutton()
#         time.sleep(3)
#
#         alert_button = self.driver.find_element(By.XPATH, "//div[@class='Toastify']/div/div/div/div[2]")
#         print("Toast Message :- ", alert_button.text)
#         time.sleep(3)
#
#
#
#
#
#     @pytest.mark.tulasi1
#     def test_print_PlanandUsage_BillingHistory_table(self, setup):
#         self.logger.info("*************** test_print_NotificationGroup_table printing table data *********************")
#
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#         self.login = Zoomview_Login_Page(self.driver)
#         self.login.enter_email(self.email)
#         self.login.enter_password(self.password)
#         self.login.click_login()
#         time.sleep(5)  # Wait for the login to process
#
#         self.payments = Zoomview_Payments_Page(self.driver)
#         self.payments.click_PlanandUsage_link()
#         time.sleep(3)
#
#         self.payments.click_PlanandUsage_BillingHistory()
#         time.sleep(2)
#
#         # Locate the table element
#         table = self.driver.find_element(By.XPATH, "(//table)[2]")
#
#         # Capture the header row
#         header = table.find_elements(By.XPATH, ".//thead//th")
#         header_row = [cell.text for cell in header]
#
#         # Log the headers for debugging
#         self.logger.info(f"Extracted headers: {header_row}")
#
#         # Fallback in case headers are not captured
#         if not header_row:
#             self.logger.warning("No headers found, using default headers.")
#             # Assuming 9 columns based on your data
#             header_row = [f"Column {i + 1}" for i in range(9)]
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
#             try:
#                 table = WebDriverWait(self.driver, 10).until(
#                     EC.presence_of_element_located((By.XPATH, "(//table)[2]"))
#                 )
#             except Exception as e:
#                 self.logger.error(f"Error locating table after clicking next button: {e}")
#                 self.driver.save_screenshot(".\\screenshots\\test_print_PlanandUsage_BillingHistory_table.png")
#                 assert False
#
#         # Ensure all rows have the same number of columns
#         max_columns = max(len(row) for row in table_data)
#         for row in table_data:
#             while len(row) < max_columns:
#                 row.append('')
#
#         # Create DataFrame
#         try:
#             df = pd.DataFrame(table_data, columns=header_row)
#         except ValueError as e:
#             self.logger.error(f"Error creating DataFrame: {e}")
#             self.driver.save_screenshot(".\\screenshots\\test_dataframe_creation_error.png")
#             assert False, "DataFrame creation failed due to header mismatch."
#
#         # Generate the formatted table output using tabulate
#         formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
#
#         # Write the formatted table to a text file
#         with open('table_billinghistory.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'table_billinghistory.txt'.")
#
