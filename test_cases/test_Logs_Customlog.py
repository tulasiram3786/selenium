# import time
# import pytest
# from base_pages.Login_Page import Zoomview_Login_Page
# from base_pages.Logs_Page import Zoomview_Logs_Page
# from utilities.custom_logger import Log_Maker
# from utilities.read_properties import Read_Config
# import pyautogui
#
#
# class Test_Logs_CustomLog:
#     loginpage_url = Read_Config.get_loginpage_url()
#     email = Read_Config.get_email()
#     password = Read_Config.get_password()
#     logger = Log_Maker.log_gen()
#
#
#     def test_add_Customlog(self, setup):
#         self.logger.info("*************** Test_CustomLog *********************")
#         self.driver = setup
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#
#         # --------- calling login page ------------#
#         self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#         self.login.enter_email(self.email)
#         self.login.enter_password(self.password)
#         self.login.click_login()
#         time.sleep(10)  # Wait for the login to process
#
#         # Navigate to the Logs page
#         self.logs = Zoomview_Logs_Page(self.driver)
#         self.logs.click_Logs()
#         time.sleep(3)
#         self.logs.click_AllLogs()
#         time.sleep(3)
#         self.logs.click_custom_log_button()
#         time.sleep(3)
#         self.logs.click_custom_log_add_button()
#         time.sleep(2)
#
#         # Enter custom log details
#         self.logs.enter_text_into_custom_log_name_field("test")
#         time.sleep(2)
#         self.logs.enter_text_into_custom_log_description("Testing")
#         time.sleep(2)
#
#         # Browse for file and use pyautogui to handle the file upload
#         self.logs.click_custom_log_Browsefile_button()
#         time.sleep(4)
#
#         # Set the path to your file (using raw string or escaped backslashes)
#         file_path = r"C:\Users\zcsu016\Downloads\data_suites (3).csv"  # Using raw string
#
#         # Use pyautogui to interact with the file dialog (simulate typing the file path)
#         pyautogui.write(file_path)
#         pyautogui.press('enter')
#         time.sleep(3)
#
#         self.logs.click_custom_log_save_button()
#         time.sleep(3)
#
#
#     def test_customlog_verifytabledata(self, setup):
#         self.logger.info("*************** Test_CustomLog verify table_data *********************")
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
#         self.logs.click_custom_log_button()
#         time.sleep(3)
#
#
#         formatted_table = self.logs.table_data_1()
#
#         # Write the formatted table to a text file
#         with open('txt_files/CustomLog_table.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'txt_files/CustomLog_table.txt'.")
#
#     @pytest.mark.tulasi
#     def test_customlog_delete_tablerow(self, setup):
#         self.logger.info("*************** Test_CustomLog Delete table_row *********************")
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
#         self.logs.click_custom_log_button()
#         time.sleep(3)
#         self.logs.click_on_custom_log_actions_button()
#         time.sleep(2)
#         self.logs.click_on_custom_log_table_row_delete()
#         time.sleep(3)
#         self.logs.click_on_custom_log_table_row_delete_popup()
#         time.sleep(5)
#
#
#
#
#
