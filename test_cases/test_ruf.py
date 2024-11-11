# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # import time
# #
# #
# # class Zoomview_Logs_Page:
# #     def __init__(self, driver):
# #         self.driver = driver
# #         self.logpartition_button_xpath = "YOUR_XPATH"
# #         self.logpartition_actions_button_xpath = "YOUR_XPATH"
# #         self.logpartition_table_row_edit_xpath = "YOUR_XPATH"
# #         self.logpartition_name_xpath = "YOUR_XPATH"
# #         self.logpartition_retention_xpath = "YOUR_XPATH"
# #         self.logpartition_description_xpath = "YOUR_XPATH"
# #         self.logpartition_condition_xpath = "YOUR_XPATH"
# #
# #     def click_logpartition_button(self):
# #         self.driver.find_element(By.XPATH, self.logpartition_button_xpath).click()
# #
# #     def click_on_logpartition_actions_button(self):
# #         self.driver.find_element(By.XPATH, self.logpartition_actions_button_xpath).click()
# #
# #     def click_on_logpartition_table_row_edit(self):
# #         self.driver.find_element(By.XPATH, self.logpartition_table_row_edit_xpath).click()
# #
# #     def get_logpartition_name(self):
# #         return self.driver.find_element(By.XPATH, self.logpartition_name_xpath).get_attribute("value")
# #
# #     def get_logpartition_retention(self):
# #         return self.driver.find_element(By.XPATH, self.logpartition_retention_xpath).get_attribute("value")
# #
# #     def get_logpartition_description(self):
# #         return self.driver.find_element(By.XPATH, self.logpartition_description_xpath).get_attribute("value")
# #
# #     def get_logpartition_condition(self):
# #         return self.driver.find_element(By.XPATH, self.logpartition_condition_xpath).get_attribute("value")
# #
# #     def set_logpartition_name(self, name):
# #         element = self.driver.find_element(By.XPATH, self.logpartition_name_xpath)
# #         element.clear()
# #         element.send_keys(name)
# #
# #     def set_logpartition_retention(self, retention):
# #         element = self.driver.find_element(By.XPATH, self.logpartition_retention_xpath)
# #         element.clear()
# #         element.send_keys(retention)
# #
# #     def set_logpartition_description(self, description):
# #         element = self.driver.find_element(By.XPATH, self.logpartition_description_xpath)
# #         element.clear()
# #         element.send_keys(description)
# #
# #     def set_logpartition_condition(self, condition):
# #         element = self.driver.find_element(By.XPATH, self.logpartition_condition_xpath)
# #         element.clear()
# #         element.send_keys(condition)
# #
# #
# # def test_logpartition_edit_tablerow(setup):
# #     logger.info("*************** Test_Tuning verify table_data *********************")
# #     driver = setup
# #     driver.get("YOUR_LOGIN_PAGE_URL")
# #     driver.maximize_window()
# #     time.sleep(2)
# #
# #     # Perform login steps
# #     login = Zoomview_Login_Page(driver)  # Corrected instantiation
# #     login.enter_email("YOUR_EMAIL")
# #     login.enter_password("YOUR_PASSWORD")
# #     login.click_login()
# #     time.sleep(5)  # Wait for the login to process
# #
# #     logs = Zoomview_Logs_Page(driver)
# #     logs.click_Logs()
# #     time.sleep(2)
# #     logs.click_AllLogs()
# #     time.sleep(5)
# #     logs.click_logpartition_button()
# #     time.sleep(4)
# #     logs.click_on_logpartition_actions_button()
# #     time.sleep(2)
# #     logs.click_on_logpartition_table_row_edit()
# #     time.sleep(2)
# #
# #     # Store original values
# #     original_name = logs.get_logpartition_name()
# #     original_retention = logs.get_logpartition_retention()
# #     original_description = logs.get_logpartition_description()
# #     original_condition = logs.get_logpartition_condition()
# #
# #     print(f"Original Name: {original_name}")
# #     print(f"Original Retention: {original_retention}")
# #     print(f"Original Description: {original_description}")
# #     print(f"Original Condition: {original_condition}")
# #
# #     # Enter new values
# #     new_name = "New Name"
# #     new_retention = "New Retention"
# #     new_description = "New Description"
# #     new_condition = "New Condition"
# #
# #     logs.set_logpartition_name(new_name)
# #     logs.set_logpartition_retention(new_retention)
# #     logs.set_logpartition_description(new_description)
# #     logs.set_logpartition_condition(new_condition)
# #
# #     time.sleep(2)
# #
# #     # Verify new values
# #     updated_name = logs.get_logpartition_name()
# #     updated_retention = logs.get_logpartition_retention()
# #     updated_description = logs.get_logpartition_description()
# #     updated_condition = logs.get_logpartition_condition()
# #
# #     assert updated_name == new_name, "Name did not update correctly."
# #     assert updated_retention == new_retention, "Retention did not update correctly."
# #     assert updated_description == new_description, "Description did not update correctly."
# #     assert updated_condition == new_condition, "Condition did not update correctly."
# #
# #     print(f"Updated Name: {updated_name}")
# #     print(f"Updated Retention: {updated_retention}")
# #     print(f"Updated Description: {updated_description}")
# #     print(f"Updated Condition: {updated_condition}")
# #
# #     # Compare old and new values
# #     assert original_name != updated_name, "Original and updated names are the same."
# #     assert original_retention != updated_retention, "Original and updated retentions are the same."
# #     assert original_description != updated_description, "Original and updated descriptions are the same."
# #     assert original_condition != updated_condition, "Original and updated conditions are the same."
# #
# #     print("Test passed. Values updated and verified successfully.")
# #
# #     self.logs = Zoomview_Logs_Page(self.driver)
# #
# #     formatted_table = self.logs.table2_data()
# #
# #     # Write the formatted table to a text file
# #     with open('Settings_NotificationGroup.txt', 'w', encoding='utf-8') as file:
# #         file.write(formatted_table)
# #
# #     print("Table data has been saved to 'Settings_NotificationGroup.txt'.")
#
#
#
# # import pandas as pd
# #
# # # Define match and player data
# # data = {
# #     "Players": ["ZEESHAN ALI", "ANSHUMAN RATH", "NIZAKAT KHAN", "BABAR HAYAT", "AIZAZ KHAN",
# #                 "MARTIN COETZEE", "NASRULLA RANA", "YASIM MURTAZA", "ANAS KHAN"],
# #     "VS OMAN": [3, "61", "34", 10, "1/1(4)", 19, "4/1(4)", "10/1(3)", "0/0(2)"],
# #     "VS AFG A": [4, "5/0(2)", 21, 4, 15, 0, "42/0(1)", "0/2(3)", "1/0(1)"],
# #     "VS BAN A": [4, "2/0(2)", 25, 85, "2/0(1)", 15, "0/1(3)", "7/0(3)", "0/1(4)"],
# #     "VS SL A": [18, 6, 11, 38, "0/1(2)", 15, "1/0(4)", "44/1(4)", "1/0(3)"],
# #     "VS AFG A (2)": [12, 0, 1, 39, 12, 15, "2/0(2)", "1/0(3)", ""]
# # }
# #
# # # Define match result row
# # match_results = ["152/8(W)", "111/9(L)", "150/8(L)", "136/7(L)", "133/5(W)"]
# #
# # # Create DataFrame
# # df = pd.DataFrame(data)
# # df.loc[-1] = ["Match Results"] + match_results  # Insert match results at the top
# # df.index = df.index + 1  # Shift index
# # df = df.sort_index()  # Sort index to place results at the top
# #
# # # Print the DataFrame
# # print(df)
# #
# # # Save to an Excel file (optional)
# # df.to_excel("cricket_scores11.xlsx", index=False)
#
#
# import time
#
# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
#
# from utilities.custom_logger import Log_Maker
# from utilities.read_properties import Read_Config
#
#
# class Test_auto:
#     signuppage_url = Read_Config.get_signuppage_url()
#     firstname = Read_Config.get_signuppage_firstname()
#     lastname = Read_Config.get_signuppage_lastname()
#     companyname = Read_Config.get_signuppage_companyname()
#     signuppageemail = Read_Config.get_signuppage_email()
#     phonenumber = Read_Config.get_signuppage_phonenumber()
#     designation = Read_Config.get_signuppage_designation()
#     createpassword = Read_Config.get_signuppage_createpassword()
#     conformpassword = Read_Config.get_signuppage_conformpassword()
#     logger = Log_Maker.log_gen()
#
#     @pytest.mark.tulasi
#     def test_signup_title_verification(self, setup):
#
#         self.logger.info("*************** Test_Signup *********************")
#         self.logger.info("*************** verification of signup page title *********************")
#         self.driver = setup
#         self.driver.get(self.signuppage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#         act_title = self.driver.title
#         exp_title = "ZoomView | Signup"
#         print("Title :- ", act_title)
#         if act_title == exp_title:
#             self.logger.info("*************** test_signup_title_verification - Title Matched *********************")
#             assert True
#             self.driver.close()
#         else:
#             self.driver.save_screenshot(".\\screenshots\\test_signup_title_verification.png")
#             self.logger.info(
#                 "*************** test_signup_title_verification - Title not matched *********************")
#             self.driver.close()
#             assert False
#
#         self.driver.quit()
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
