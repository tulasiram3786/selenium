import time

import pytest
from selenium.webdriver.common.by import By


class Test_screenshots:

    @pytest.mark.tulasi
    def test_screenshot(self,setup):

        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.ibm.com/contact/global")
        self.driver.maximize_window()
        #self.driver.save_screenshot(".\\screenshots\\home.png")
        time.sleep(3)

        self.driver.get_screenshot_as_file(".\\screenshots\\home1.png")
        self.driver.get_screenshot_as_png()
        self.driver.get_screenshot_as_base64()

        #taking a screenshot of specific webelement

        button = self.driver.find_element(By.XPATH, "//div[@id='adff']")
        button.screenshot()