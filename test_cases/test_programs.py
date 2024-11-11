# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# def test_sort():
#     list = [2, 5, 1, 8, 9]
#
#     # Initial list of strings
#     #string_list = ["2", "5", "1", "8", "9"]
#
#     # Convert strings to integers and sort
#     sorted_list = sorted(list)
#     print(sorted_list)
#
# def toastmessage_verification():
#     toast_message = self.driver.find_element(By.XPATH, "//div[@class='ant-notification-notice-message']")
#     act_toast = toast_message.text
#     print(act_toast)
#     time.sleep(3)
#
#     exp_toast = "Removed filter successfully"
#
#     if act_toast == exp_toast:
#         self.logger.info(
#             "*************** test_tuning_delete_tablerow - Tuning table row deleted successfully *********************")
#         assert True
#         self.driver.close()
#     else:
#         self.driver.save_screenshot(".\\screenshots\\test_tuning_delete_tablerow.png")
#         self.logger.info(
#             "*************** test_tuning_delete_tablerow - Tuning table row not deleted *********************")
#         self.driver.close()
#         assert False
#
#
# def toast():
#     # Wait for the toast message to appear
#     toast_message_xpath = "//div[text()='Log view created successfully']"
#     try:
#         # Wait for the toast message to be present and visible
#         toast_message = WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located((By.XPATH, toast_message_xpath))
#         )
#         # Print the text of the toast message
#         print("Toast Message :- ", toast_message.text)
#     except Exception as e:
#         self.logger.error("Toast message not found or not visible")
#         print("Toast message not found or not visible")
#
