import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Test_rightclick_demo:


    def test_righgclick(self, setup):

        self.driver = setup

        chr_options = Options()
        chr_options.add_experimental_option("detach", True)

        self.driver.implicitly_wait(10)
        self.driver.get("https://the-internet.herokuapp.com/context_menu")
        time.sleep(2)
        ele = self.driver.find_element(By.XPATH, "//div[@id='hot-spot']")

        act = ActionChains(self.driver)
        act.context_click(ele).perform()


    def test_righgclick1(self, setup):

        self.driver = setup

        chr_options = Options()
        chr_options.add_experimental_option("detach", True)

        self.driver.implicitly_wait(10)
        self.driver.get("https://the-internet.herokuapp.com/context_menu")
        time.sleep(2)
        ele = self.driver.find_element(By.XPATH, "//div[@id='hot-spot']")

        act = ActionChains(self.driver)
        act.context_click(ele).perform()

    def test_righgclick2(self, setup):

        self.driver = setup

        chr_options = Options()
        chr_options.add_experimental_option("detach", True)

        self.driver.implicitly_wait(10)
        self.driver.get("https://the-internet.herokuapp.com/context_menu")
        time.sleep(2)
        ele = self.driver.find_element(By.XPATH, "//div[@id='hot-spot']")

        act = ActionChains(self.driver)
        act.context_click(ele).perform()

