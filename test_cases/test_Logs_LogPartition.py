# import time
# import pytest
# from selenium import webdriver
# from selenium.common import NoSuchElementException, StaleElementReferenceException, TimeoutException
# from selenium.webdriver import Keys, ActionChains
# from selenium.webdriver.common.by import By
# from base_pages.Infrastructure_Page import Zoomview_Infrastructure_Page
# from base_pages.Login_Page import Zoomview_Login_Page
# from base_pages.Logs_Page import Zoomview_Logs_Page
# from utilities.read_properties import Read_Config
# from utilities.custom_logger import Log_Maker
# from tabulate import tabulate
# import pandas as pd
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class Test_Logs_LogPartition:
#     loginpage_url = Read_Config.get_loginpage_url()
#     email = Read_Config.get_email()
#     password = Read_Config.get_password()
#     logger = Log_Maker.log_gen()
#
#
#     def test_add_logpartition(self, setup):
#         self.logger.info("*************** Test_LogPartition *********************")
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
#         self.logs.click_logpartition_button()
#         time.sleep(3)
#         self.logs.click_logpartition_add_button()
#         time.sleep(2)
#         self.logs.enter_text_into_logpartition_name_field("Tulasiramtestt")
#         time.sleep(2)
#         self.logs.click_on_listbox_chooseretentionforthispartition()
#         time.sleep(4)
#         self.logs.click_on_listbox_dropdown_for_chooseretentionforthispartition()
#         time.sleep(2)
#         self.logs.enter_text_into_logpartition_description("This is for log partition")
#         time.sleep(2)
#         self.logs.enter_text_into_logpartition_conditionforlog("log=500")
#         time.sleep(2)
#         self.logs.click_on_logpartition_createrule()
#         time.sleep(5)
#
#     @pytest.mark.tulasi
#     def test_logpartition_verifytabledata(self, setup):
#         self.logger.info("*************** Test_LogPartition verify table_data *********************")
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
#         self.logs.click_logpartition_button()
#         time.sleep(3)
#
#         formatted_table = self.logs.table_data_1()
#
#         # Write the formatted table to a text file
#         with open('txt_files/Logs_LogPartition_table.txt', 'w', encoding='utf-8') as file:
#             file.write(formatted_table)
#
#         print("Table data has been saved to 'txt_files/Logs_LogPartition_table.txt'.")
#
#
#     def test_logpartition_delete_tablerow(self, setup):
#         self.logger.info("*************** Test_LogPartition Delete table_row *********************")
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
#         self.logs.click_logpartition_button()
#         time.sleep(4)
#         self.logs.click_on_logpartition_actions_button()
#         time.sleep(2)
#         self.logs.click_on_logpartition_table_row_delete()
#         time.sleep(3)
#         self.logs.click_on_logpartition_table_row_delete_popup()
#         time.sleep(5)
#
#     # def test_logpartition_edit_tablerow(self, setup):
#     #     self.logger.info("*************** Test_Tuning verify table_data *********************")
#     #     self.driver = setup
#     #     self.driver.get(self.loginpage_url)
#     #     self.driver.maximize_window()
#     #     time.sleep(2)
#     #     # --------- calling login page ------------#
#     #     self.login = Zoomview_Login_Page(self.driver)  # Corrected instantiation
#     #     self.login.enter_email(self.email)
#     #     self.login.enter_password(self.password)
#     #     self.login.click_login()
#     #     time.sleep(5)  # Wait for the login to process
#     #     self.logs = Zoomview_Logs_Page(self.driver)
#     #     self.logs.click_Logs()
#     #     time.sleep(2)
#     #     self.logs.click_AllLogs()
#     #     time.sleep(5)
#     #     self.logs.click_logpartition_button()
#     #     time.sleep(4)
#     #     self.logs.click_on_logpartition_actions_button()
#     #     time.sleep(2)
#     #     self.logs.click_on_logpartition_table_row_edit()
#     #     time.sleep(2)
#     #     # Store original values
#     #     original_name = self.logs.get_logpartition_name()
#     #     #original_retention = self.logs.get_logpartition_retention()
#     #     original_description = self.logs.get_logpartition_description()
#     #     original_condition = self.logs.get_logpartition_condition()
#     #
#     #     print(f"Original Name: {original_name}")
#     #     #print(f"Original Retention: {original_retention}")
#     #     print(f"Original Description: {original_description}")
#     #     print(f"Original Condition: {original_condition}")
#     #
#     #     # Enter new values
#     #     new_name = "Tulasiram"
#     #     #new_retention = "New Retention"
#     #     new_description = "keep all 200 logs"
#     #     new_condition = "log=200"
#     #
#     #     self.logs.set_logpartition_name(new_name)
#     #     #self.logs.set_logpartition_retention(new_retention)
#     #     self.logs.set_logpartition_description(new_description)
#     #     self.logs.set_logpartition_condition(new_condition)
#     #
#     #     time.sleep(2)
#     #
#     #     # Verify new values
#     #     updated_name = self.logs.get_logpartition_name()
#     #     #updated_retention = self.logs.get_logpartition_retention()
#     #     updated_description = self.logs.get_logpartition_description()
#     #     updated_condition = self.logs.get_logpartition_condition()
#     #
#     #     assert updated_name == new_name, "Name did not update correctly."
#     #     #assert updated_retention == new_retention, "Retention did not update correctly."
#     #     assert updated_description == new_description, "Description did not update correctly."
#     #     assert updated_condition == new_condition, "Condition did not update correctly."
#     #
#     #     print(f"Updated Name: {updated_name}")
#     #     #print(f"Updated Retention: {updated_retention}")
#     #     print(f"Updated Description: {updated_description}")
#     #     print(f"Updated Condition: {updated_condition}")
#     #
#     #     # Compare old and new values
#     #     assert original_name != updated_name, "Original and updated names are the same."
#     #     #assert original_retention != updated_retention, "Original and updated retentions are the same."
#     #     assert original_description != updated_description, "Original and updated descriptions are the same."
#     #     assert original_condition != updated_condition, "Original and updated conditions are the same."
#     #
#     #     print("Test passed. Values updated and verified successfully.")
#
#
#     def test_logpartition_edit_tablerow(self, setup):
#         self.logger.info("*************** Test_Tuning verify table_data *********************")
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
#         time.sleep(5)  # Wait for the login to process
#
#         self.logs = Zoomview_Logs_Page(self.driver)
#         self.logs.click_Logs()
#         time.sleep(2)
#         self.logs.click_AllLogs()
#         time.sleep(5)
#         self.logs.click_logpartition_button()
#         time.sleep(4)
#         self.logs.click_on_logpartition_actions_button()
#         time.sleep(2)
#         self.logs.click_on_logpartition_table_row_edit()
#         time.sleep(5)
#
#         self.name=self.logs.enter_text_into_logpartition_name_field("tulasii")
#         time.sleep(2)
#         self.logs.update_button()
#         time.sleep(3)
#
#
#
#
#
#         # # Store original values
#         # original_name = self.logs.get_logpartition_name()
#         # original_description = self.logs.get_logpartition_description()
#         # original_condition = self.logs.get_logpartition_condition()
#         #
#         # print(f"Original Name: {original_name}")
#         # print(f"Original Description: {original_description}")
#         # print(f"Original Condition: {original_condition}")
#         #
#         # # Clear text boxes before entering new values
#         # self.logs.clear_logpartition_name()  # Clear the name field
#         # self.logs.clear_logpartition_description()  # Clear the description field
#         # self.logs.clear_logpartition_condition()  # Clear the condition field
#         #
#         # # Alternatively, use the `send_keys(Keys.CONTROL + 'a')` and `send_keys(Keys.BACKSPACE)` to select and clear the text
#         # name_field = self.logs.get_logpartition_name()  # Locate the name input field
#         # name_field.send_keys(Keys.CONTROL + 'a')
#         # name_field.send_keys(Keys.BACKSPACE)
#         #
#         # description_field = self.logs.get_logpartition_description()  # Locate the description input field
#         # description_field.send_keys(Keys.CONTROL + 'a')
#         # description_field.send_keys(Keys.BACKSPACE)
#         #
#         # condition_field = self.logs.get_logpartition_condition()  # Locate the condition input field
#         # condition_field.send_keys(Keys.CONTROL + 'a')
#         # condition_field.send_keys(Keys.BACKSPACE)
#         #
#         # # Enter new values
#         # new_name = "Tulasiramm"
#         # new_description = "keep all 200 logs"
#         # new_condition = "log=200"
#         #
#         # self.logs.set_logpartition_name(new_name)
#         # self.logs.set_logpartition_description(new_description)
#         # self.logs.set_logpartition_condition(new_condition)
#         #
#         # time.sleep(2)
#         #
#         # # Verify new values
#         # updated_name = self.logs.get_logpartition_name()
#         # updated_description = self.logs.get_logpartition_description()
#         # updated_condition = self.logs.get_logpartition_condition()
#         #
#         # # Asserts to check if the values are updated correctly
#         # assert updated_name == new_name, "Name did not update correctly."
#         # assert updated_description == new_description, "Description did not update correctly."
#         # assert updated_condition == new_condition, "Condition did not update correctly."
#         #
#         # print(f"Updated Name: {updated_name}")
#         # print(f"Updated Description: {updated_description}")
#         # print(f"Updated Condition: {updated_condition}")
#         #
#         # # Asserts to compare old and new values
#         # assert original_name != updated_name, "Original and updated names are the same."
#         # assert original_description != updated_description, "Original and updated descriptions are the same."
#         # assert original_condition != updated_condition, "Original and updated conditions are the same."
#         #
#         # print("Test passed. Values updated and verified successfully.")
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
