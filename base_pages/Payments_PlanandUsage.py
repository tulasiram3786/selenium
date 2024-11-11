from selenium.webdriver.common.by import By


class Zoomview_Payments_Page:

    link_PlanandUsage_xpath = "//a[text()='Plan & Usage']"
    button_planandpricing_xpath = "//div[text()='Plan & pricing']"
    button_billinghistory_xpath = "//div[text()='Billing history']"
    button_planandpricing_Storage_xpath = "//span[text()='Storage']"
    textbox_planandpricing_storage_GB_xpath = "(//input[@type='text'])[1]"
    button_planandpricing_ContinuetoPayment = "//span[text()='Continue to payment']"
    textbox_billingContactname_xpath = "//input[@name='billing_name']"
    textbox_billingCompanyname_xpath = "//input[@name='billing_company_name']"
    textbox_billingAddress_xpath = "//input[@name='billing_address']"
    textbox_billingCity_xpath = "//input[@name='billing_city']"
    textbox_billingPostalcode_xpath = "//input[@name='billing_postal_code']"
    textbox_billingCountry_xpath = "//input[@name='billing_country']"
    button_billing_processoffline_xpath = "//span[text()='Process offline']"

    def __init__(self, driver):
        self.driver = driver

    def click_PlanandUsage_link(self):
        self.driver.find_element(By.XPATH, self.link_PlanandUsage_xpath).click()

    def click_PlanandUsage_PlanandPricing(self):
        self.driver.find_element(By.XPATH, self.button_planandpricing_xpath).click()

    def click_PlanandUsage_BillingHistory(self):
        self.driver.find_element(By.XPATH, self.button_billinghistory_xpath).click()

    def click_Storage(self):
        self.driver.find_element(By.XPATH, self.button_planandpricing_Storage_xpath).click()

    def enter_text_into_storage_GB(self, gb):
        self.driver.find_element(By.XPATH, self.textbox_planandpricing_storage_GB_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_planandpricing_storage_GB_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_planandpricing_storage_GB_xpath).send_keys(gb)

    def click_continuetopayment(self):
        self.driver.find_element(By.XPATH, self.button_planandpricing_ContinuetoPayment).click()

    def enter_text_into_Billing_Contact_Name(self, contactname):
        self.driver.find_element(By.XPATH, self.textbox_billingContactname_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_billingContactname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_billingContactname_xpath).send_keys(contactname)

    def enter_text_into_Billing_Company_Name(self, companyname):
        self.driver.find_element(By.XPATH, self.textbox_billingCompanyname_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_billingCompanyname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_billingCompanyname_xpath).send_keys(companyname)

    def enter_text_into_Billing_Address(self, address):
        self.driver.find_element(By.XPATH, self.textbox_billingAddress_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_billingAddress_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_billingAddress_xpath).send_keys(address)

    def enter_text_into_Billing_City(self, city):
        self.driver.find_element(By.XPATH, self.textbox_billingCity_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_billingCity_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_billingCity_xpath).send_keys(city)

    def enter_text_into_Billing_PostalCode(self, postalcode):
        self.driver.find_element(By.XPATH, self.textbox_billingPostalcode_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_billingPostalcode_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_billingPostalcode_xpath).send_keys(postalcode)

    def enter_text_into_Billing_Country(self, country):
        self.driver.find_element(By.XPATH, self.textbox_billingCountry_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_billingCountry_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_billingCountry_xpath).send_keys(country)

    def click_processofflinebutton(self):
        self.driver.find_element(By.XPATH, self.button_billing_processoffline_xpath).click()








