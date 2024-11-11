import time

import pytest
from selenium.webdriver.common.by import By


class Test_frames:

    def test_framesoriframes(self, setup):

        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.maths.surrey.ac.uk/explore/nigelspages/frame2.htm")
        #my_frame1 = self.driver.find_element(By.XPATH, "/html/frameset/frame[1]")
        self.driver.switch_to(0) #id or name or frame webelement or index
        self.driver.find_element(By.XPATH, "Tables").click()
        self.driver.switch_to.default_content() #move focus back to parent page

        #my_frame2 = self.driver.find_element(By.XPATH, "/html/frameset/frame[2]")
        self.driver.switch_to(1)
        self.driver.find_element(By.XPATH,"abc").send_keys("adfassfdf")
        self.driver.switch_to.default_content()

        #my_frame3 = self.driver.find_element(By.XPATH, "/html/frameset/frame[3]")
        self.driver.switch_to(2)
        self.driver.find_element(By.XPATH, "xyz").click()
        self.driver.switch_to.default_content()

    @pytest.mark.tulasiewe
    def test_iframes(self,setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://seleniumbase.io/demo_page")

        self.driver.switch_to.frame("myFrame2")
        iframe_text = self.driver.find_element(By.XPATH, "//h4[text()='iFrame Text']")
        print(iframe_text.text)
        self.driver.switch_to.default_content()

        self.driver.switch_to.frame("frameName3")
        checkbox= self.driver.find_element(By.XPATH, "//input[@id='checkBox6']")
        checkbox.click()
        self.driver.switch_to.default_content()

        self.driver.find_element(By.ID, "myTextInput").send_keys("tulasi")
        time.sleep(3)

    @pytest.mark.tulasi
    def test_nested_iframes(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.dezlearn.com/nested-iframes-example/")
        self.driver.maximize_window()

        self.driver.switch_to.frame("parent_iframe")    #imp

        self.driver.switch_to.frame("iframe1")
        self.driver.find_element(By.XPATH, "//button[@id='u_5_6']").click()
        time.sleep(3)
        self.driver.switch_to.parent_frame()
        self.driver.find_element(By.XPATH, "//button[@id='u_5_5']").click()
        time.sleep(3)








