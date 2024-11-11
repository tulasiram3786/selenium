import time

import pytest
from selenium.webdriver.common.by import By


class Test_browsers_window_switching:

    @pytest.mark.tulasi
    def test_browserswindowswitching(self, setup):

        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://demo.nopcommerce.com/")

        self.driver.find_element(By.XPATH, "//a[text()='Facebook']").click()
        time.sleep(4)
        window_ids = self.driver.window_handles
        parent_window_id = window_ids[0]
        child_window_id = window_ids[1]
        print(parent_window_id)
        print(child_window_id)

        self.driver.switch_to.window(child_window_id)
        print(self.driver.title)
        self.driver.switch_to.window(parent_window_id)

        for win_id in window_ids:
            self.driver.switch_to.window(win_id)
            time.sleep(3)
            if self.driver.title == "nopCommerce (@nopCommerce) / X":
                self.driver.close()