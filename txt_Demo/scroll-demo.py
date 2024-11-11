import time

import pytest
from selenium.webdriver.common.by import By


class Test_scroll:

    @pytest.mark.tulasidd
    def test_scroll_page(self, setup):

        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.gsmarena.com/makers.php3")

        self.driver.execute_script("window.scrollBy(0,1000);")
        time.sleep(4)
        print(self.driver.execute_script("return window.pageYOffset;"))

    @pytest.mark.tulasieter
    def test_scroll_page_upto_elementview(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.gsmarena.com/makers.php3")
        oscal = self.driver.find_element(By.XPATH, "//table/tbody/tr[39]/td[2]")
        self.driver.execute_script("arguments[0].scrollIntoView();", oscal)
        time.sleep(5)

    @pytest.mark.tulasi
    def test_scroll_page_upto_endofthepage_startofthepage(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.gsmarena.com/makers.php3")
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,-document.body.scrollHeight);")
