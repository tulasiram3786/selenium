import time
import pytest
from selenium.webdriver.common.by import By


class Test_Bootstrap_dropdowns:

    def test_bootstrapdropdown(self,setup):

        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("httsp://www.ib.com/planetwide/select/selector.html")
        self.driver.maximize_window()

        self.driver.find_element(By.ID, "select2-ibm_select-container").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "truste-consent-button").click()
        countries = self.driver.find_elements(By.XPATH, "//*[@class='select2-results__option']")

        for country in countries:

            if "India" in country.text:
                country.click()
