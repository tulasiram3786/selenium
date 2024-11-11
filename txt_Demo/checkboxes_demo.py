import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_checkboxes:


    def test_checkboxes_selecting_multiple_checkboxes_basedonchoice(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.ironspider.ca/forms/checkradio.htm")
        self.driver.maximize_window()

        my_elements=self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")


        for ele in my_elements:
            value = ele.get_attribute("value")
            print(value)
            if (value == "red") or (value == "blue") or (value == "orange"):
                ele.click()
                time.sleep(2)

    @pytest.mark.tulasidf
    def test_checkboxes_select_lasttwo(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.ironspider.ca/forms/checkradio.htm")
        self.driver.maximize_window()

        my_elements = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")

        print(len(my_elements))

        for i in range(len(my_elements)-2,len(my_elements)):
            my_elements[i].click()
            time.sleep(2)

    @pytest.mark.tulasiwd
    def test_checkboxes_select_firsttwo(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.ironspider.ca/forms/checkradio.htm")
        self.driver.maximize_window()

        my_elements = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")

        print(len(my_elements))

        for i in range(len(my_elements)):
            if i<2:
                my_elements[i].click()
                time.sleep(2)

    @pytest.mark.tulasiddd
    def test_checkboxes_unselect_checkboxes(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.ironspider.ca/forms/checkradio.htm")
        self.driver.maximize_window()

        my_elements = self.driver.find_elements(By.XPATH, "//input[@type='checkbox']")

        print(len(my_elements))

        for ele in my_elements:
            if ele.is_selected():
                ele.click()
        time.sleep(2)

























