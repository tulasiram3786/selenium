# import time
# import pandas as pd
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from tabulate import tabulate
#
# from base_pages.Login_Page import Zoomview_Login_Page
# from base_pages.Logs_Page import Zoomview_Logs_Page
# from base_pages.Settings_NotificationGroup import Zoomview_Settings_NotificationGroup_Page
# from base_pages.Settings_Page import Zoomview_Settings_Page
# from utilities.random import generate_random_text
# from utilities.read_properties import Read_Config
# from utilities.custom_logger import Log_Maker
#
#
# class Test_Settins_NotificationGroup:
#     loginpage_url = Read_Config.get_loginpage_url()
#     email = Read_Config.get_email()
#     password = Read_Config.get_password()
#     logger = Log_Maker.log_gen()
#
#     def test_notificationgroup_title_verification(self, setup):
#         self.logger.info("*************** Test_Settings_NotificationGroup *********************")
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
#             # -------- calling settings page --------------#
#             self.settings = Zoomview_Settings_Page(self.driver)
#             self.settings.click_settings_dropdown()
#
#             # --------- calling Notification Group page ----------- #
#             self.notificationgroup = Zoomview_Settings_NotificationGroup_Page(self.driver)
#             self.notificationgroup.click_settings_NotificationGroup()
#
#             # Wait until the Notification Group page is loaded
#             WebDriverWait(self.driver, 10).until(EC.title_contains("Notifications Group"))
#
#             act_title = self.driver.title
#             exp_title = "ZoomView | Notifications Group"
#             print("Notification Group Page Title :- ", act_title)
#
#             if act_title == exp_title:
#                 self.logger.info(
#                     "*************** test_notificationgroup_title_verification - Title Matched *********************")
#                 assert True
#             else:
#                 self.driver.save_screenshot(".\\screenshots\\test_notificationgroup_title_verification.png")
#                 self.logger.info(
#                     "*************** test_notificationgroup_title_verification - Title not matched *********************")
#                 assert False
#
#         except Exception as e:
#             self.logger.error(f"An error occurred: {e}")
#             self.driver.save_screenshot(".\\screenshots\\test_notificationgroup_error.png")
#             assert False
#         finally:
#             self.driver.quit()  # Ensure the driver is closed in all cases
#
#
#     def test_notificationgroup_add(self, setup):
#         self.logger.info("*************** Test_Settings_NotificationGroup_Add *********************")
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
#             # Wait for the Dashboard page to load after login
#             WebDriverWait(self.driver, 10).until(EC.title_contains("Dashboard"))  # Adjust the title as necessary
#
#             # -------- calling settings page --------------#
#             self.settings = Zoomview_Settings_Page(self.driver)
#             self.settings.click_settings_dropdown()
#             time.sleep(3)
#
#             # --------- calling Notification Group page ----------- #
#             self.notificationgroup = Zoomview_Settings_NotificationGroup_Page(self.driver)
#             self.notificationgroup.click_settings_NotificationGroup()
#
#             # Wait until the Notification Group page is loaded
#             WebDriverWait(self.driver, 10).until(EC.title_contains("Notifications Group"))
#
#             # Click on Add button
#             self.notificationgroup.click_add()
#
#             # Wait until the 'Group Name' input is present
#             WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//input[@label='Group Name']"))
#             )
#
#             # Enter Group Name and Description using random text generator
#             random_group_name = generate_random_text()  # Generate random group name
#             self.notificationgroup.enter_text_into_GroupName(random_group_name)
#             time.sleep(2)
#             self.notificationgroup.enter_text_into_Description("testing for notification group")
#
#             # Click on Add Emails and enter each email separately
#             email_list = ["tulasiram1704@gmail.com", "tulasi4333@gmail.com", "tulasiram1111@gmail.com"]
#
#             for email in email_list:
#                 # Click on Add Emails button
#                 self.notificationgroup.click_AddEmails()
#
#                 # Wait for email input fields to appear and find the last one
#                 email_inputs = WebDriverWait(self.driver, 10).until(
#                     EC.presence_of_all_elements_located((By.XPATH, "//input[contains(@name, 'email')]"))
#                 )
#
#                 if email_inputs:
#                     # Find the last email input field and enter the email address
#                     last_email_input = email_inputs[-1]
#                     last_email_input.click()
#                     last_email_input.send_keys(email)
#                 else:
#                     self.logger.error(
#                         "*************** test_notificationgroup_add - No email input fields found *********************")
#                     assert False
#
#             # Click on Save button
#             self.notificationgroup.click_savebutton()
#
#             # Wait for the toast message to appear and verify it
#             act_toast_message = WebDriverWait(self.driver, 10).until(
#                 EC.visibility_of_element_located(
#                     (By.XPATH, self.notificationgroup.NotificationGroup_toast_message_xpath))
#             ).text
#
#             exp_toast_message = "Inserted Notification successfully"
#
#             if act_toast_message == exp_toast_message:
#                 self.logger.info(
#                     "*************** test_notificationgroup_add - Emails entered successfully *********************")
#                 assert True
#             else:
#                 self.driver.save_screenshot(".\\screenshots\\test_notificationgroup_add.png")
#                 self.logger.error(
#                     "*************** test_notificationgroup_add - Emails not entered as expected *********************")
#                 assert False
#
#         except Exception as e:
#             self.logger.error(f"An error occurred: {e}")
#             self.driver.save_screenshot(".\\screenshots\\test_notificationgroup_add_error.png")
#             assert False
#         finally:
#             self.driver.quit()  # Ensure the driver is closed in all cases
#
#     @pytest.mark.tula
#     def test_print_NotificationGroup_table(self, setup):
#         self.logger.info("*************** test_print_NotificationGroup_table printing table data *********************")
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
#         # -------- calling settings page --------------#
#         self.settings = Zoomview_Settings_Page(self.driver)
#         self.settings.click_settings_dropdown()
#         time.sleep(3)
#
#         # --------- calling Notification Group page ----------- #
#         self.notificationgroup = Zoomview_Settings_NotificationGroup_Page(self.driver)
#         self.notificationgroup.click_settings_NotificationGroup()
#         time.sleep(3)
#
#         self.logs = Zoomview_Logs_Page(self.driver)
#
#
#         formatted_table = self.logs.table2_data()
#
#         # Write the formatted table to a text file
#         with open('notificationgroup_table.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'notificationgroup_table.txt'.")
#
#         # # Locate the table element
#         # table = self.driver.find_element(By.XPATH, "(//table)[2]")
#         #
#         # # Locate all rows in the table
#         # rows = table.find_elements(By.XPATH, ".//tr")
#         #
#         # # Prepare data for DataFrame
#         # table_data = []
#         # for row in rows:
#         #     # Locate all cells in the current row
#         #     cells = row.find_elements(By.XPATH, ".//td | .//th")
#         #     row_data = [cell.text for cell in cells]
#         #     table_data.append(row_data)
#         #
#         # # Create DataFrame
#         # df = pd.DataFrame(table_data[1:], columns=table_data[0])
#         #
#         # # Generate the formatted table output using tabulate
#         # formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
#         #
#         # # Write the formatted table to a text file
#         # with open('Settings_NotificationGroup_table.txt', 'w', encoding='utf-8') as file:
#         #     file.write(formatted_table)
#         #
#         # print("Table data has been saved to 'Settings_NotificationGroup_table.txt'.")
#
#     @pytest.mark.tul
#     def test_NotificationGroup_delete_tablerow(self, setup):
#         self.logger.info("*************** test_NotificationGroup_delete_tablerow deleting table row *********************")
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
#         # -------- calling settings page --------------#
#         self.settings = Zoomview_Settings_Page(self.driver)
#         self.settings.click_settings_dropdown()
#         time.sleep(3)
#
#         # --------- calling Notification Group page ----------- #
#         self.notificationgroup = Zoomview_Settings_NotificationGroup_Page(self.driver)
#         self.notificationgroup.click_settings_NotificationGroup()
#         time.sleep(3)
#
#         self.logs = Zoomview_Logs_Page(self.driver)
#         self.logs.click_on_logpartition_actions_button()
#         time.sleep(2)
#         self.logs.click_on_logpartition_table_row_delete()
#         time.sleep(3)
#         self.logs.click_on_logpartition_table_row_delete_popup()
#         time.sleep(5)
#
#     @pytest.mark.tulasi
#     def test_NotificationGroup_clone_tablerow(self, setup):
#         self.logger.info(
#             "*************** test_NotificationGroup_clone_tablerow clone table row *********************")
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
#         # -------- calling settings page --------------#
#         self.settings = Zoomview_Settings_Page(self.driver)
#         self.settings.click_settings_dropdown()
#         time.sleep(3)
#
#         # --------- calling Notification Group page ----------- #
#         self.notificationgroup = Zoomview_Settings_NotificationGroup_Page(self.driver)
#         self.notificationgroup.click_settings_NotificationGroup()
#         time.sleep(3)
#
#         self.logs = Zoomview_Logs_Page(self.driver)
#         self.logs.click_on_logpartition_actions_button()
#         time.sleep(2)
#         self.notificationgroup.click_on_notificationgroup_table_row_clone()
#         time.sleep(2)
#         self.notificationgroup.enter_text_into_GroupName("Test")
#         time.sleep(3)
#         self.notificationgroup.click_savebutton()
#
#
#
#
#
#
#
