import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

class Test_keyboard_demo:

    @pytest.mark.tulasi
    def test_keyboard_actions(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.onlinenotepad.io")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//div[@class='ql-editor ql-blank']").send_keys("welcome tulasiram")

        act = ActionChains(self.driver)
        #select text ctrl+A
        act.key_down(Keys.CONTROL)
        act.send_keys("a")
        act.key_up(Keys.CONTROL)
        act.perform()

        #copy the text ctrl+c
        act.key_down(Keys.CONTROL)
        act.send_keys("c")
        act.key_up(Keys.CONTROL)
        act.perform()

        #press right arrow key
        act.send_keys(Keys.ARROW_RIGHT)

        #press Enter key
        act.send_keys(Keys.ENTER)

        #paste the text
        act.key_down(Keys.CONTROL)
        act.send_keys("v")
        act.key_up(Keys.CONTROL)
        act.perform()

