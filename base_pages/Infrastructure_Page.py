import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Zoomview_Infrastructure_Page:
    #click on infrastructure button
    infrastructure_button_xpath = "//span[@class='ant-menu-title-content']//a[text()='Infrastructure']"

    #infrastructure Hosts
    infrastructure_total_hosts_xpath = "(//article[text()='Hosts'])[1]//ancestor::div[@class='ant-card-body']//descendant::div[@class='h-[30px]']"
    infrastructure_live_hosts_xpath = "((//article[text()='Hosts'])[1]//ancestor::div[@class='ant-card-body']//descendant::article)[4]"
    infrastructure_offline_host_xpath = "((//article[text()='Hosts'])[1]//ancestor::div[@class='ant-card-body']//descendant::article)[6]"
    infrastructure_stale_host_xpath = "((//article[text()='Hosts'])[1]//ancestor::div[@class='ant-card-body']//descendant::article)[8]"

    #infrastructure Services
    infrastructure_total_service_xpath = "(//article[text()='Service'])[1]//ancestor::div[@class='ant-card-body']//descendant::div[@class='h-[30px]']"
    infrastructur_service_ok_xpath = "((//article[text()='Service'])[1]//ancestor::div[@class='ant-card-body']//descendant::article)[4]"
    infrastructur_service_critical_xpath = "((//article[text()='Service'])[1]//ancestor::div[@class='ant-card-body']//descendant::article)[6]"
    infrastructur_service_warning_xpath = "((//article[text()='Service'])[1]//ancestor::div[@class='ant-card-body']//descendant::article)[8]"

    #click on actions
    button_infrastructure_actions_xpath = "(//table//tbody//tr[@class='ant-table-row ant-table-row-level-0']//td)[11]"

    #click on performence
    button_infrastructure_performence_xpath = "//span[text()='Performance']"

    #xpath for infrastructure cpu graph
    infrastructure_cpu_graph_xpath = "(//div[@class='relative']//descendant::div[@class=' tablet-sm:h-[130px] w-full pt-2'])[1]"
    infrastructure_no_cpu_graph_xpath = "//div[text()='No CPU Data']"

    # xpath for infrastructure Cpu Load Average graph
    infrastructure_cpuload_average_graph_xpath = "(//div[@class='relative']//descendant::div[@class=' tablet-sm:h-[130px] w-full pt-2'])[2]"
    infrastructure_no_cpuload_average_graph_xpath = "//div[text()='No CPU Data']"

    # xpath for infrastructure memory graph
    infrastructure_memory_graph_xpath = "(//div[@class='relative']//descendant::div[@class=' tablet-sm:h-[130px] w-full pt-2'])[3]"
    infrastructure_no_memory_graph_xpath = "//div[text()='No Memory Data']"

    # xpath for infrastructure network graph
    infrastructure_network_graph_xpath = "(//div[@class='relative']//descendant::div[@class=' tablet-sm:h-[130px] w-full pt-2'])[4]"
    infrastructure_no_network_graph_xpath = "//div[text()='No Network Data']"

    #xpath for infrastructure summary Disk,process running(top cpu, top memory) table
    infrastructure_summarypage_disk_table_xpath = "(//div[contains(@class,'ant-table ant-table-small')])[1]"
    infrastructure_summarypage_process_running_table_xpath = "(//div[contains(@class,'ant-table ant-table-small')])[2]"

    #xpath for click on topmemory in summary page
    button_top_memory_xpath = "//p[text()='Top Memory']"

    #------------------------------------------------------------------------------------
    #=================== System page ========================
    

    def __init__(self, driver):  # Corrected constructor
        self.driver = driver

    def infrastructure_page_button(self):
        self.driver.find_element(By.XPATH, self.infrastructure_button_xpath).click()

    def verify_infrastructure_hosts(self):
        total_hosts = int(self.driver.find_element(By.XPATH, self.infrastructure_total_hosts_xpath).text)
        live = int(self.driver.find_element(By.XPATH, self.infrastructure_live_hosts_xpath).text)
        offline = int(self.driver.find_element(By.XPATH, self.infrastructure_offline_host_xpath).text)
        stale = int(self.driver.find_element(By.XPATH, self.infrastructure_stale_host_xpath).text)
        print("Totals hosts", total_hosts)
        print("Live hosts:", live)
        print("Offline hosts:", offline)
        print("Stale hosts:", stale)
        total_Hosts = live + offline + stale
        print("The sum of Live, offline and stale hosts:", total_Hosts)

        class Color:
            RED = '\033[91m'
            END = '\033[0m'
            GREEN = '\033[92m'

        if total_hosts == total_Hosts:
            print(Color.GREEN + "successfully matched" + Color.END)
        else:
            print(Color.RED + "not matched" + Color.END)

    def verify_infrastructure_services(self):
        total_service = int(self.driver.find_element(By.XPATH, self.infrastructure_total_service_xpath).text)
        ok = int(self.driver.find_element(By.XPATH, self.infrastructur_service_ok_xpath).text)
        warn = int(self.driver.find_element(By.XPATH, self.infrastructur_service_warning_xpath).text)
        critical = int(self.driver.find_element(By.XPATH, self.infrastructur_service_critical_xpath).text)
        print("Totals services", total_service)
        print("ok services:", ok)
        print("warn services:", warn)
        print("crit services:", critical)
        total_services = ok + warn + critical
        print("The sum of ok, warn and crit services:", total_services)

        class Color:
            RED = '\033[91m'
            END = '\033[0m'
            GREEN = '\033[92m'

        if total_service == total_services:
            print(Color.GREEN + "Infrastructure Services count is succssfully matched with ok,warn,crit" + Color.END)
        else:
            print(Color.RED + "Infrastructure Services count is not matched with ok,warn,crit" + Color.END)

    def click_infrastructure_actions_button(self):

        scrollable_element = self.driver.find_element(By.XPATH, "//div[@class='ant-table-content']")

        # Scroll the specific element horizontally to the right
        self.driver.execute_script("arguments[0].scrollLeft += 1000;", scrollable_element)  # Scroll 1000px to the right

        self.driver.find_element(By.XPATH, self.button_infrastructure_actions_xpath).click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, self.button_infrastructure_performence_xpath).click()
        time.sleep(3)

    def click_infrastructure_topmemory(self):
        self.driver.find_element(By.XPATH, self.button_top_memory_xpath).click()

    def current_url(self):
        current_url = self.driver.current_url
        print("url:-", current_url)


