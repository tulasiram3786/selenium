# import allure
# import pytest
# from selenium.webdriver.common.by import By
#
# @pytest.mark.usefixtures("setup_and_teardown","log_on_failure")
# @allure.severity(allure.severity_level.CRITICAL)
# class TestSearch:
#
#     def test_search_fo_a_valid_product(self):
#         self.driver.find_element(By.NAME,"search").send_keys("HP")
#         self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
#         assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
