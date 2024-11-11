# import time
#
# import pytest
# from selenium.common import TimeoutException
# from selenium.webdriver.chrome import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options  # Correct import for ChromeOptions
#
# from base_pages.Forgot_Password_Page import Zoomview_Forgotpassword_Page
# from base_pages.Gmail_email import Gmail_Email
# from base_pages.Login_Page import Zoomview_Login_Page
# from base_pages.zoho_email import Zoho_email
# from utilities.custom_logger import Log_Maker
# from utilities.read_properties import Read_Config
#
#
# class Test_ForgotPassword:
#     forgotpasswordpage_url = Read_Config.get_forgotpasswordpage_url()
#     fp_email = Read_Config.get_forgotpassword_email()
#     logger = Log_Maker.log_gen()
#     loginpage_url = Read_Config.get_loginpage_url()
#
#     def test_Forgotpassword_title_verification(self, setup):
#
#         self.logger.info("*************** Test_ForgotPassword *********************")
#         self.logger.info("*************** verification of ForgotPassword page title *********************")
#         self.driver = setup
#         self.driver.get(self.forgotpasswordpage_url)
#         self.driver.maximize_window()
#         time.sleep(3)
#         act_title = self.driver.title
#         exp_title = "ZoomView | ForgotPassword"
#         print("Title :- ", act_title)
#
#         if act_title == exp_title:
#             self.logger.info(
#                 "*************** test_Forgotpassword_title_verification - Title Matched *********************")
#             assert True
#             self.driver.close()
#         else:
#             self.driver.save_screenshot(".\\screenshots\\test_Forgotpassword_title_verification.png")
#             self.logger.info(
#                 "*************** test_Forgotpassword_title_verification - Title not matched *********************")
#             self.driver.close()
#             assert False
#
#         self.driver.quit()
#
#     def test_forgotpassword_page_validation(self, setup):
#         self.logger.info("*************** test_forgotpassword_page_validation started *********************")
#         self.driver = setup
#         self.driver.get(self.forgotpasswordpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#
#         act_dashboard_text = self.driver.find_element(By.XPATH,
#                                                       "//p[text()='Find Your Account']").text
#         time.sleep(3)
#
#         if act_dashboard_text == "Find Your Account":
#             self.logger.info("*************** Forgotpassword page verification text found *********************")
#             assert True
#             self.driver.close()
#         else:
#             self.driver.save_screenshot(".\\screenshots\\test_forgotpassword_page_validation.png")
#             self.logger.info("*************** Forgotpassword page verification text not found *********************")
#             self.driver.close()
#             assert False
#
#         self.driver.quit()
#
#     def test_forgotpassword_page_valid_email(self, setup):
#         self.logger.info("*************** test_forgotpassword_page_valid_email started *********************")
#         self.driver = setup
#         self.driver.get(self.forgotpasswordpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#         self.forgotpassword = Zoomview_Forgotpassword_Page(self.driver)  # Corrected instantiation
#         self.forgotpassword.enter_forgotpasswordpage_email(self.fp_email)
#         self.forgotpassword.click_forgotpasswordpage_submit()
#         time.sleep(5)  # Wait for the login to process
#         act_forgotpassword_text = self.driver.find_element(By.XPATH, "//p[text()='Authentication']").text
#         time.sleep(3)
#
#         if act_forgotpassword_text == "Authentication":
#             self.logger.info("*************** Forgotpassword text found *********************")
#             assert True
#             self.driver.close()
#         else:
#             self.driver.save_screenshot(".\\screenshots\\test_forgotpassword_page_valid_email.png")
#             self.logger.info("*************** Forgotpassword text not found *********************")
#             self.driver.close()
#             assert False
#
#     @pytest.mark.tulasi
#     def test_forgotpassword_email_invaliddetails(self, setup):
#
#         self.logger.info("*************** test_forgotpassword_email_invaliddetails started *********************")
#         self.driver = setup
#
#         test_cases = [
#
#             ("123@gmail.com", "Enter a valid email"),
#             ("tulasiram", "Enter a valid email"),
#             ("@no-local-part.com", "Enter a valid email"),
#             ("tulasiram@.com", "Enter a valid email"),
#             ("tulasiram@gmail..com", "Enter a valid email"),
#             ("tulasiram@gmail.com.123", "Enter a valid email"),
#             ("tulasiram.gmail.com", "Enter a valid email"),
#             ("tulasiram@", "Enter a valid email"),
#             ("tulasi ram@gmail.com", "Enter a valid email"),
#             ("tulasiram@ gmail.com", "Enter a valid email"),
#             ("tulasiram!@gmail.com", "Enter a valid email"),
#             ("tulasiram@gmail@gmail.com", "Enter a valid email"),
#             ("tulasi<>ram@gmail.com", "Enter a valid email"),
#             ("@gmail.com", "Enter a valid email"),
#             ("tulasiram@gmail", "Enter a valid email"),
#             (
#             "tulasirdddddddddddffkdddddddddddddddddddddddddddddddddddddddddssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssffffffffhddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddam.r@gmail.com",
#             "Enter a valid email"),
#             ("tulasiram.r@gmail.commmmmmmmmmmmm", "Enter a valid email"),
#             ("tulasiram.r@gmail,com", "Enter a valid email"),
#             ("tulasiram@192.168.1.81", "Enter a valid email"),
#             ("tulasiram@gma$il.com", "Enter a valid email"),
#             ("tulasiram@gmailcom", "Enter a valid email")
#
#         ]
#
#         for fp_email, expected_text in test_cases:
#             self.logger.info(f"*************** Testing Forgotpassword_email: {fp_email} *********************")
#             self.driver.get(self.forgotpasswordpage_url)
#             self.driver.maximize_window()
#             time.sleep(2)
#
#             forgotpassword_page = Zoomview_Forgotpassword_Page(self.driver)
#             forgotpassword_page.enter_forgotpasswordpage_email(fp_email)
#             time.sleep(3)
#
#             act_signuppage_text = self.driver.find_element(By.XPATH,
#                                                            "//span[text()='Email']")
#             act_signuppage_text.click()
#             time.sleep(2)
#
#             act_email_error_text = self.driver.find_element(By.XPATH, "//span[text()='Enter a valid email']").text
#             time.sleep(3)
#
#             if act_email_error_text == expected_text:
#                 self.logger.info(
#                     f"*************** forgotpassword page '{fp_email}' validation text found *********************")
#                 assert True
#             else:
#                 self.driver.save_screenshot(f".\\screenshots\\test_forgotpassword_email_invaliddetails_{fp_email}.png")
#                 self.logger.info(
#                     f"*************** forgotpassword page '{fp_email}' validation text not found *********************")
#                 assert False
#
#         self.driver.quit()
#
#
#     def test_forgotpassword_verify_otp(self, setup):
#         self.logger.info("*************** forgotpassword_verify_otp started *********************")
#
#         # Set up the driver
#         self.driver = setup
#         self.driver.get(self.forgotpasswordpage_url)
#         self.driver.maximize_window()
#         time.sleep(3)
#
#         # Interact with the Forgot Password page
#         self.forgotpassword = Zoomview_Forgotpassword_Page(self.driver)
#         self.forgotpassword.enter_forgotpasswordpage_email(self.fp_email)
#         self.forgotpassword.click_forgotpasswordpage_submit()
#         time.sleep(5)
#
#         # Set Chrome options
#         chrome_options = Options()  # Use Options instead of webdriver.ChromeOptions()
#         chrome_options.add_argument("--disable-notifications")
#
#         # Open a new tab and navigate to Zoho Mail
#         self.driver.execute_script("window.open('');")
#         self.driver.switch_to.window(self.driver.window_handles[1])
#         self.driver.get("https://www.zoho.com/mail/login.html")
#         time.sleep(2)
#         self.driver.maximize_window()
#         time.sleep(4)
#
#         # Interact with Zoho Mail to extract OTP
#         zoho = Zoho_email(self.driver)
#         zoho.signup_for_zoho_for_verify_otp()
#         time.sleep(5)
#
#         # Extract the OTP and ensure it's correctly formatted
#         otp = zoho.extract_otp()
#         otp = otp[:6]  # Adjust this based on the correct OTP length
#         print(f"The OTP is: {otp}")
#
#         # Close the Zoho Mail tab and switch back to the original tab
#         zoho.close_current_window()
#         self.driver.switch_to.window(self.driver.window_handles[0])
#         time.sleep(2)
#
#         # Enter the OTP in the forgot password page
#         forgotpassword_page = Zoomview_Forgotpassword_Page(self.driver)
#         try:
#             otp_field = WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//input[contains(@aria-label,'character')]"))
#             )
#             forgotpassword_page.enter_otp_digit_by_digit(otp)
#         except TimeoutException:
#             self.logger.error("OTP field was not found on the page.")
#             self.driver.save_screenshot(".\\screenshots\\otp_field_not_found.png")
#             assert False, "OTP field not found within the time limit"
#
#         time.sleep(5)
#         print("OTP entered successfully")
#
#         # Continue with the authentication and password reset process
#         try:
#             act_text = WebDriverWait(self.driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, "//p[text()='Authentication']"))
#             )
#             act_text.click()
#             time.sleep(2)
#             print("Clicked on Authentication")
#
#             forgotpassword_page.authentication_submit_button()
#             time.sleep(5)
#
#             # Enter new password details
#             forgotpassword_page.enter_text_createpassword("Zybisys@128")
#             time.sleep(2)
#             forgotpassword_page.click_hidden_button_for_create()
#             time.sleep(2)
#             forgotpassword_page.enter_text_conformpassword("Zybisys@128")
#             time.sleep(2)
#             forgotpassword_page.click_hidden_button_for_conform()
#             time.sleep(2)
#             forgotpassword_page.click_setpassword_button()
#             time.sleep(5)
#         except TimeoutException:
#             self.logger.error("Element not found during the authentication process.")
#             self.driver.save_screenshot(".\\screenshots\\auth_process_error.png")
#             assert False, "Element not found during the authentication process"
#
#         # Login verification
#         self.driver.get(self.loginpage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#         self.login = Zoomview_Login_Page(self.driver)
#         self.login.enter_email("tulasiram.r@zybisys.com")
#         self.login.enter_password("Zybisys@128")
#         self.driver.find_element(By.XPATH, "//span[@class='ant-input-suffix']").click()
#         time.sleep(2)
#         self.login.click_login()
#         time.sleep(5)
#
#         # Check if login was successful
#         try:
#             act_dashboard_text = WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "//a[text()='Dashboard']"))
#             ).text
#             time.sleep(3)
#
#             if act_dashboard_text == "Dashboard":
#                 self.logger.info("*************** Dashboard text found *********************")
#                 assert True
#             else:
#                 self.driver.save_screenshot(".\\screenshots\\test_valid_login.png")
#                 self.logger.info("*************** Dashboard text not found *********************")
#                 assert False
#         except TimeoutException:
#             self.logger.error("Dashboard text not found.")
#             self.driver.save_screenshot(".\\screenshots\\dashboard_text_not_found.png")
#             assert False, "Dashboard text not found within the time limit"
#
#         self.driver.close()
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
