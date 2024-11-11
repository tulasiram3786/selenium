import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Test_Mousehover:

    @pytest.mark.tulasi
    def test_mousehoverdemo(self,setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://the-internet.herokuapp.com/hovers")
        time.sleep(3)
        all_users = self.driver.find_elements(By.XPATH, "//*[@class='figure']")
        user1=all_users[0]
        viewprofile1 = self.driver.find_element(By.XPATH, "//a[@href='/users/1']")

        act = ActionChains(self.driver)
        act.move_to_element(user1).move_to_element(viewprofile1).click().perform()

        self.driver.back()
        time.sleep(3)
        user2=all_users[1]
        viewprofile2 = self.driver.find_element(By.XPATH, "//a[@href='/users/2']")
        act.move_to_element(user2).move_to_element(viewprofile2).click().perform()


