import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_dropdown:


    def test_selectclass_dropdowns(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.facebook.com/r.php")
        self.driver.maximize_window()
        month_dropdown=self.driver.find_element(By.XPATH, "//*[@id='month']")
        month = Select(month_dropdown)
        #month.select_by_visible_text("Aug")
        #month.select_by_index(11)
        month.select_by_value("10")
        time.sleep(3)


    def test_selectclass_dropdowns_options(self, setup):

        #dont select by dropdown using index, visible text, value then how you can select the dropdown
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.facebook.com/r.php")
        self.driver.maximize_window()
        month_dropdown=self.driver.find_element(By.XPATH, "//*[@id='month']")
        month = Select(month_dropdown)
        time.sleep(3)
        all_months = month.options
        print(len(all_months))

        for mon in all_months:
            print(mon.text)

        for mon in all_months:
            if(mon.text == "Aug"):
                mon.click()
                break

    @pytest.mark.tulasi
    def test_noselectclass_dropdowns(self, setup):

        #dont select by dropdown using index, visible text, value then how you can select the dropdown
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.facebook.com/r.php")
        self.driver.maximize_window()
        all_months = self.driver.find_elements(By.XPATH, "//*[@id='month']//option")

        for mon in all_months:
            if mon.text == "Oct":
                mon.click()
                time.sleep(3)
                break



