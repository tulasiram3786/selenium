# import time
# import pytest
# from selenium.webdriver.common.by import By
# from base_pages.Signup_Page import Zoomview_Signup_Page
# from utilities.custom_logger import Log_Maker
# from utilities.read_properties import Read_Config
#
# class Test_Signup:
#
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
#     @pytest.mark.sanity
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
#     @pytest.mark.regression
#     def test_signup_page_validation(self, setup):
#         self.logger.info("*************** test_signup_page_validation started *********************")
#         self.driver = setup
#         self.driver.get(self.signuppage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#
#         act_dashboard_text = self.driver.find_element(By.XPATH,
#                                                       "//p[text()='Create your account']").text
#         time.sleep(3)
#
#         if act_dashboard_text == "Create your account":
#             self.logger.info("*************** signup page verification text found *********************")
#             assert True
#             self.driver.close()
#         else:
#             self.driver.save_screenshot(".\\screenshots\\test_signup_page_validation.png")
#             self.logger.info("*************** signup page verification text not found *********************")
#             self.driver.close()
#             assert False
#
#         self.driver.quit()
#
#     @pytest.mark.regression
#     @pytest.mark.sanity
#
#     def test_signup_valid_login(self, setup):
#         self.logger.info("*************** test_signup_valid_login started *********************")
#         self.driver = setup
#         self.driver.get(self.signuppage_url)
#         self.driver.maximize_window()
#         time.sleep(2)
#         self.signup = Zoomview_Signup_Page(self.driver)  # Corrected instantiation
#         self.signup.enter_signup_firstname(self.firstname)
#         self.signup.enter_signup_lastname(self.lastname)
#         self.signup.enter_signup_email(self.signuppageemail)
#         self.signup.enter_signup_companyname(self.companyname)
#         self.signup.enter_signup_phonenumber(self.phonenumber)
#         time.sleep(3)
#         act_signuppage_text = self.driver.find_element(By.XPATH,
#                                                        "//p[text()='Create your account']")
#         act_signuppage_text.click()
#         time.sleep(2)
#         self.driver.find_element(By.XPATH, "(//span[@class='ant-input-suffix'])[1]").click()
#         time.sleep(3)
#         # Find all OTP input fields using class name (you can also use XPath)
#         otp_inputs = self.driver.find_elements(By.XPATH,
#                                                "//input[contains(@aria-label,'Please enter OTP character')]")
#
#         # Loop through each input field and send the value "1"
#         for otp_input in otp_inputs:
#             otp_input.send_keys("1")
#
#         # Optional: Wait and then close the browser
#         time.sleep(3)
#         self.driver.find_element(By.XPATH, "//span[text()='Submit']").click()
#         time.sleep(2)
#
#
#         self.signup.enter_signup_designation(self.designation)
#         self.signup.enter_signup_createpassword(self.createpassword)
#         self.signup.enter_signup_conformpassword(self.conformpassword)
#         time.sleep(2)
#         self.signup.click_signup_createaccount()
#         time.sleep(5)  # Wait for the login to process
#         act_dashboard_text = self.driver.find_element(By.XPATH,
#                                                       "//p[text()='Check your email for the verification link sent to']").text
#         time.sleep(3)
#
#         if act_dashboard_text == "Check your email for the verification link sent to":
#             self.logger.info("*************** signup page verification text found *********************")
#             assert True
#             self.driver.close()
#         else:
#             self.driver.save_screenshot(".\\screenshots\\test_signup_valid_login.png")
#             self.logger.info("*************** signup page verification text not found *********************")
#             self.driver.close()
#             assert False
#
#         self.driver.quit()
#
#     def test_firstname_invaliddetails(self,setup):
#
#         self.logger.info("*************** test_firstname_invaliddetails started *********************")
#         self.driver = setup
#
#         test_cases = [
#             ("Tulasiram111", "First name must be at least 3 characters long"),
#             ("tu", "First name must be at least 3 characters long"),
#             (
#                 "Tulasiram here iam entering more than 30 characters",
#                 "First name must be at least 3 characters long"),
#             ("tuDJD12$%", "First name must be at least 3 characters long"),
#             ("          ", "First name must be at least 3 characters long"),
#             ("at name last space  ", "First name must be at least 3 characters long"),
#
#             ("9865478922", "First name must be at least 3 characters long"),
#             ("$*$&#*#-#_@", "First name must be at least 3 characters long")
#
#         ]
#
#         for first_name, expected_text in test_cases:
#             self.logger.info(f"*************** Testing first name: {first_name} *********************")
#             self.driver.get(self.signuppage_url)
#             self.driver.maximize_window()
#             time.sleep(2)
#
#             signup_page = Zoomview_Signup_Page(self.driver)
#             signup_page.enter_signup_firstname(first_name)
#             time.sleep(3)
#             act_signuppage_text = self.driver.find_element(By.XPATH,
#                                                           "//p[text()='Create your account']")
#             act_signuppage_text.click()
#             time.sleep(2)
#
#             act_firstname_error_text = self.driver.find_element(By.XPATH, "//span[text()='First name must be at least 3 characters long']").text
#             time.sleep(3)
#
#             if act_firstname_error_text == expected_text:
#                 self.logger.info(
#                     f"*************** First name '{first_name}' validation text found *********************")
#                 assert True
#             else:
#                 self.driver.save_screenshot(f".\\screenshots\\test_firstname_invaliddetails_{first_name}.png")
#                 self.logger.info(
#                     f"*************** First name '{first_name}' validation text not found *********************")
#                 assert False
#
#         self.driver.close()
#
#
#
#
#
#     def test_lastname_invaliddetails(self,setup):
#
#         self.logger.info("*************** test_lastaname_invaliddetails strted *********************")
#         self.driver = setup
#
#         test_cases = [
#
#             (
#                 "Tulasiram here iam entering more than 30 characters",
#                 "Last name must be at least 1 characters long"),
#             ("tuDJD12$%", "Last name must be at least 1 characters long"),
#             ("          ", "Last name must be at least 1 characters long"),
#             ("at name last space  ", "Last name must be at least 1 characters long"),
#
#             ("9865478922", "Last name must be at least 1 characters long"),
#             ("$*$&#*#-#_@", "Last name must be at least 1 characters long")
#
#         ]
#
#         for last_name, expected_text in test_cases:
#             self.logger.info(f"*************** Testing last name: {last_name} *********************")
#             self.driver.get(self.signuppage_url)
#             self.driver.maximize_window()
#             time.sleep(2)
#
#             signup_page = Zoomview_Signup_Page(self.driver)
#             signup_page.enter_signup_lastname(last_name)
#             time.sleep(3)
#
#             act_signuppage_text = self.driver.find_element(By.XPATH,
#                                                            "//p[text()='Create your account']")
#             act_signuppage_text.click()
#             time.sleep(2)
#
#             act_lastname_error_text = self.driver.find_element(By.XPATH, "//span[text()='Last name must be at least 1 characters long']").text
#             time.sleep(3)
#
#             if act_lastname_error_text == expected_text:
#                 self.logger.info(
#                     f"*************** Last name '{last_name}' validation text found *********************")
#                 assert True
#             else:
#                 self.driver.save_screenshot(f".\\screenshots\\test_lastname_invaliddetails_{last_name}.png")
#                 self.logger.info(
#                     f"*************** Last name '{last_name}' validation text not found *********************")
#                 assert False
#
#         self.driver.quit()
#
#
#     def test_email_invaliddetails(self,setup):
#
#         self.logger.info("*************** test_email_invaliddetails strted *********************")
#         self.driver = setup
#
#         test_cases = [
#
#             ("123@gmail.com", "Enter valid email"),
#             ("tulasiram", "Enter valid email"),
#             ("@no-local-part.com", "Enter valid email"),
#             ("tulasiram@.com", "Enter valid email"),
#             ("tulasiram@gmail..com", "Enter valid email"),
#             ("tulasiram@gmail.com.123", "Enter valid email"),
#             ("tulasiram.gmail.com", "Enter valid email"),
#             ("tulasiram@", "Enter valid email"),
#             ("tulasi ram@gmail.com", "Enter valid email"),
#             ("tulasiram@ gmail.com", "Enter valid email"),
#             ("tulasiram!@gmail.com", "Enter valid email"),
#             ("tulasiram@gmail@gmail.com", "Enter valid email"),
#             ("tulasi<>ram@gmail.com", "Enter valid email"),
#             ("@gmail.com", "Enter valid email"),
#             ("tulasiram@gmail", "Enter valid email"),
#             (
#                 "tulasirdddddddddddffkdddddddddddddddddddddddddddddddddddddddddssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssffffffffhddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddam.r@gmail.com",
#                 "Enter valid email"),
#             ("tulasiram.r@gmail.commmmmmmmmmmmm", "Enter valid email"),
#             ("tulasiram.r@gmail,com", "Enter valid email"),
#             ("tulasiram@192.168.1.81", "Enter valid email"),
#             ("tulasiram@gma$il.com", "Enter valid email"),
#             ("tulasiram@gmailcom", "Enter valid email")
#
#         ]
#
#         for email, expected_text in test_cases:
#             self.logger.info(f"*************** Testing Email: {email} *********************")
#             self.driver.get(self.signuppage_url)
#             self.driver.maximize_window()
#             time.sleep(2)
#
#             signup_page = Zoomview_Signup_Page(self.driver)
#             signup_page.enter_signup_email(email)
#             time.sleep(3)
#
#             act_signuppage_text = self.driver.find_element(By.XPATH,
#                                                            "//p[text()='Create your account']")
#             act_signuppage_text.click()
#             time.sleep(2)
#
#             act_email_error_text = self.driver.find_element(By.XPATH, "//span[text()='Enter valid email']").text
#             time.sleep(3)
#
#             if act_email_error_text == expected_text:
#                 self.logger.info(
#                     f"*************** Email '{email}' validation text found *********************")
#                 assert True
#             else:
#                 self.driver.save_screenshot(f".\\screenshots\\test_email_invaliddetails_{email}.png")
#                 self.logger.info(
#                     f"*************** Email '{email}' validation text not found *********************")
#                 assert False
#
#         self.driver.quit()
#
#     def test_companyname_invaliddetails(self,setup):
#
#         self.logger.info("*************** test_companyname_invaliddetails strted *********************")
#         self.driver = setup
#
#         test_cases = [
#
#             (
#                 "tulasiram testing company name here iam entering more than 50 characters","Company name cannot include dot and exceed 50 characters"),
#             ("..........", "Company name cannot include dot and exceed 50 characters"),
#
#
#         ]
#
#         for companyname, expected_text in test_cases:
#             self.logger.info(f"*************** Testing Companyname: {companyname} *********************")
#             self.driver.get(self.signuppage_url)
#             self.driver.maximize_window()
#             time.sleep(2)
#
#             signup_page = Zoomview_Signup_Page(self.driver)
#             signup_page.enter_signup_companyname(companyname)
#             time.sleep(3)
#
#             act_signuppage_text = self.driver.find_element(By.XPATH,
#                                                            "//p[text()='Create your account']")
#             act_signuppage_text.click()
#             time.sleep(2)
#
#             act_company_error_text = self.driver.find_element(By.XPATH, "//span[text()='Company name cannot include dot and exceed 50 characters']").text
#             time.sleep(3)
#
#             if act_company_error_text == expected_text:
#                 self.logger.info(
#                     f"*************** Companyname '{companyname}' validation text found *********************")
#                 assert True
#             else:
#                 self.driver.save_screenshot(f".\\screenshots\\test_companyname_invaliddetails_{companyname}.png")
#                 self.logger.info(
#                     f"*************** Companyname '{companyname}' validation text not found *********************")
#                 assert False
#
#         self.driver.quit()
#
#     @pytest.mark.tulasi
#     def test_phonenumber_invaliddetails(self,setup):
#
#         self.logger.info("*************** test_phonenumber_invaliddetails strted *********************")
#         self.driver = setup
#
#         test_cases = [
#
#             ("9847","Enter valid phone number"),
#             ("959574653333375", "Enter valid phone number"),
#             ("984hdfjdjj34", "Enter valid phone number"),
#             ("9f@E899937", "Enter valid phone number"),
#             ("1196859874", "Enter valid phone number"),
#             ("9876 5665 34", "Enter valid phone number"),
#             ("09876566534", "Enter valid phone number"),
#             ("+8222 8989898989", "Enter valid phone number"),
#             ("1111111111", "Enter valid phone number")
#
#
#
#         ]
#
#         for phonenumber, expected_text in test_cases:
#             self.logger.info(f"*************** Testing Phonenumber: {phonenumber} *********************")
#             self.driver.get(self.signuppage_url)
#             self.driver.maximize_window()
#             time.sleep(2)
#
#             signup_page = Zoomview_Signup_Page(self.driver)
#             signup_page.enter_signup_phonenumber(phonenumber)
#             time.sleep(3)
#
#             act_signuppage_text = self.driver.find_element(By.XPATH,
#                                                            "//p[text()='Create your account']")
#             act_signuppage_text.click()
#             time.sleep(2)
#
#             act_phonenumber_error_text = self.driver.find_element(By.XPATH, "//span[text()='Enter valid phone number']").text
#             time.sleep(3)
#
#             if act_phonenumber_error_text == expected_text:
#                 self.logger.info(
#                     f"*************** Phonenumber '{phonenumber}' validation text found *********************")
#                 assert True
#             else:
#                 self.driver.save_screenshot(f".\\screenshots\\test_phonenumber_invaliddetails_{phonenumber}.png")
#                 self.logger.info(
#                     f"*************** Phonenumber '{phonenumber}' validation text not found *********************")
#                 assert False
#
#         self.driver.quit()
#
#
#     def test_designation_invaliddetails(self,setup):
#
#         self.logger.info("*************** test_designation_invaliddetails started *********************")
#         self.driver = setup
#
#         test_cases = [
#
#             (
#                 "Tulasiram testing designation feild and here iam entering more than 50 characters",
#                 "Enter 3-50 chars with letters and single spaces only."),
#             ("          ", "Enter 3-50 chars with letters and single spaces only."),
#             ("jj", "Enter 3-50 chars with letters and single spaces only.")
#
#         ]
#
#         for designation, expected_text in test_cases:
#             self.logger.info(f"*************** Testing Designation: {designation} *********************")
#             self.driver.get(self.signuppage_url)
#             self.driver.maximize_window()
#             time.sleep(2)
#
#             signup_page = Zoomview_Signup_Page(self.driver)
#             signup_page.enter_signup_designation(designation)
#             time.sleep(3)
#
#             act_signuppage_text = self.driver.find_element(By.XPATH,
#                                                            "//p[text()='Create your account']")
#             act_signuppage_text.click()
#             time.sleep(2)
#
#             act_designation_error_text = self.driver.find_element(By.XPATH, "//span[text()='Enter 3-50 chars with letters and single spaces only.']").text
#             time.sleep(3)
#
#             if act_designation_error_text == expected_text:
#                 self.logger.info(
#                     f"*************** Designation '{designation}' validation text found *********************")
#                 assert True
#             else:
#                 self.driver.save_screenshot(f".\\screenshots\\test_designation_invaliddetails_{designation}.png")
#                 self.logger.info(
#                     f"*************** Designation '{designation}' validation text not found *********************")
#                 assert False
#
#         self.driver.quit()
#
#
#
#
#
#
#
#     def test_createpassword_invaliddetails(self, setup):
#
#         self.logger.info("*************** test_createpassword_invaliddetails started *********************")
#         self.driver = setup
#
#         test_cases = [
#             ("Tulasiram111", "Password must be 8-50 characters with lowercase, uppercase, digit, and special character."),
#             ("tu", "Password must be 8-50 characters with lowercase, uppercase, digit, and special character."),
#             (
#                 "Tulasiram djdkfkjfjfkf fkdfjfjjfjfjf fjfjfhere iam entering more than 50 characters",
#                 "Password must be 8-50 characters with lowercase, uppercase, digit, and special character."),
#             ("          ", "Password must be 8-50 characters with lowercase, uppercase, digit, and special character."),
#             ("at last space  ", "Password must be 8-50 characters with lowercase, uppercase, digit, and special character."),
#             ("PasswordNoNumber", "Password must be 8-50 characters with lowercase, uppercase, digit, and special character."),
#             ("password123", "Password must be 8-50 characters with lowercase, uppercase, digit, and special character."),
#             ("TULASIRAM123", "Password must be 8-50 characters with lowercase, uppercase, digit, and special character."),
#             ("Password 123!", "Password must be 8-50 characters with lowercase, uppercase, digit, and special character."),
#             ("123456789", "Password must be 8-50 characters with lowercase, uppercase, digit, and special character."),
#             ("jack.demo@gmail.com", "Password must be 8-50 characters with lowercase, uppercase, digit, and special character.")
#
#         ]
#
#         for createpassword, expected_text in test_cases:
#             self.logger.info(f"*************** Testing Createpassword: {createpassword} *********************")
#             self.driver.get(self.signuppage_url)
#             self.driver.maximize_window()
#             time.sleep(2)
#
#             signup_page = Zoomview_Signup_Page(self.driver)
#             signup_page.enter_signup_createpassword(createpassword)
#             time.sleep(3)
#
#             act_signuppage_text = self.driver.find_element(By.XPATH,
#                                                            "//p[text()='Create your account']")
#             act_signuppage_text.click()
#             time.sleep(2)
#
#             act_createpassword_error_text = self.driver.find_element(By.XPATH, "//span[text()='Password must be 8-50 characters with lowercase, uppercase, digit, and special character.']").text
#             time.sleep(3)
#
#             if act_createpassword_error_text == expected_text:
#                 self.logger.info(
#                     f"*************** Createpassword '{createpassword}' validation text found *********************")
#                 assert True
#             else:
#                 self.driver.save_screenshot(f".\\screenshots\\test_createpassword_invaliddetails_{createpassword}.png")
#                 self.logger.info(
#                     f"*************** Createpassword '{createpassword}' validation text not found *********************")
#                 assert False
#
#         self.driver.quit()
#
#
#
#     # def test_conformpassword_invaliddetails(self,setup):
#     #
#     #     self.logger.info("*************** test_conformpassword_invaliddetails started *********************")
#     #     self.driver = setup
#     #
#     #     test_cases = [
#     #         ("Tulasiram111", "Mismatched Password"),
#     #         ("tu", "Mismatched Password"),
#     #         (
#     #             "Tulasiram djdkfkjfjfkf fkdfjfjjfjfjf fjfjfhere iam entering more than 50 characters",
#     #             "Mismatched Password"),
#     #         ("          ", "Mismatched Password"),
#     #         ("at name last space  ", "Mismatched Password"),
#     #         ("9865478922", "Mismatched Password"),
#     #         ("$*$&#*#-#_@", "Mismatched Password")
#     #
#     #     ]
#     #
#     #     for conformpassword, expected_text in test_cases:
#     #         self.logger.info(f"*************** Testing Conformpassword: {conformpassword} *********************")
#     #         self.driver.get(self.signuppage_url)
#     #         self.driver.maximize_window()
#     #         time.sleep(2)
#     #
#     #         signup_page = Zoomview_Signup_Page(self.driver)
#     #         signup_page.enter_signup_conformpassword(conformpassword)
#     #         time.sleep(3)
#     #
#     #         act_conformpassword_text = self.driver.find_element(By.XPATH, "//span[text()='Mismatched Password']").text
#     #         time.sleep(3)
#     #
#     #         if act_conformpassword_text == expected_text:
#     #             self.logger.info(
#     #                 f"*************** Conformpassword '{conformpassword}' validation text found *********************")
#     #             assert True
#     #         else:
#     #             self.driver.save_screenshot(f".\\screenshots\\test_conformpassword_invaliddetails_{conformpassword}.png")
#     #             self.logger.info(
#     #                 f"*************** Conformpassword '{conformpassword}' validation text not found *********************")
#     #             assert False
#     #
#     #     self.driver.quit()
#
#
#     #=============================================
#     #company name
#     #valid login
#
