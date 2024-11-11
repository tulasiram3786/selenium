import time
import pandas as pd
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from tabulate import tabulate
from selenium.webdriver.support import expected_conditions as EC


class Zoomview_Logs_Page:
    button_Logs_xpath = "(//span[text()='Logs'])[1]"
    button_AllLogs_xpath = "//a[text()='All Logs']"
    button_AddData_xpath = "//a[text()='Add Data']"
    textbox_searchbox_xpath = "(//input[@class='ant-select-selection-search-input'])[2]"
    button_logs_enter_xpath = "//span[text()='Enter']"
    button_logs_save_xpath = "(//*[local-name()='svg' and @stroke='currentColor'])[14]"
    textbox_logs_savebutton_input_xpath = "//input[@placeholder='Save']"
    button_logs_savebutton_input_againsavebutton_xpath = "//span[text()='Save']"
    savefilter_toast_message_xpath = "//div[text()='Log view created successfully']"
    button_logs_alllogdata_xpath = "(//*[local-name()='svg' and @stroke='currentColor'])[15]"
    logspage_all_logs_graph_xpath = "//div[@class='ant-card-body']"
    logspage_all_logs_no_graph_xpath = "//div[@description='No data']"
    button_export_xpath = "//span[text()='Export ']"
    radio_button_alllogs_json_xpath = "(//span[@class='ant-radio ant-wave-target'])[1]"
    radio_button_alllogs_csv_xpath = "(//span[@class='ant-radio ant-wave-target'])[2]"
    button_export_dropdown = "(//input[@aria-haspopup='listbox'])[3]"
    listbox_dropdown_elements_json_xpath = "//div[@class='rc-virtual-list-holder-inner']//descendant::div[text()='200']"
    listbox_dropdown_elements_csv_xpath = "//div[@class='rc-virtual-list-holder-inner']//descendant::div[text()='300']"
    button_logs_download_xpath = "//span[text()='Download']"
    button_logs_settings_xpath = "//span[text()='Settings ']"
    button_logs_settings_checkbox_xpath = "(//input[@class='ant-checkbox-input'])[9]"
    button_logs_settings_uncheckbox_xpath = "//label[@class='ant-checkbox-wrapper flex items-center css-i56btq']//input"
    button_logs_settings_save_xpath = "//span[text()='Save']"




    # --------------------- Tuning ---------------------------------
    button_tuning_xpath = "//div[text()='Tuning']"
    button_tuning_add_xpath = "//span[text()='Add']"
    textbox_tuning_nameofrule_xpath = "//input[@id='tuning_name']"
    # listbox_tuning_fieldtotune_xpath = "//span[@class='ant-select-selection-search']"
    listbox_tuning_fieldtotune_xpath = "//input[contains(@aria-haspopup,'listbox')]"
    textbox_tuning_tuningrule_xpath = "//textarea[@placeholder='Tuning rules are written in Grok or Regex']"
    button_tuning_pastelog_xpath = "//div[text()='Paste Log']"
    button_tuning_Createrule_xpath = "//span[text()='Create Rule']"
    button_tuning_table_row_actions_xpath = "(//div[@class='text-center '])[1]"
    button_tuning_table_row_delete_xpath = "(//span[text()='Delete'])[1]"
    button_tuning_table_row_delete_popup_xpath = "(//span[text()='Delete'])[2]"

    # -------------------------- Drop Filter ------------------------------------------------
    button_dropfilter_xpath = "//div[text()='Drop Filter']"
    button_dropfilter_add_xpath = "//span[text()='Add']"
    textbox_dropfilter_name_xpath = "//input[@label='Name']"
    listbox_dropfilter_selectlogpartition_xpath = "(//input[@class='ant-select-selection-search-input'])[1]"
    textbox_dropfilter_conditionforlog_xpath = "(//input[@class='ant-select-selection-search-input'])[2]"
    button_dropfilter_submit_xpath = "//span[text()='Submit']"
    button_dropfilter_table_row_actions_xpath = "(//div[@class='text-center '])[1]"
    button_dropfilter_table_row_delete_xpath = "(//span[text()='Delete'])"
    button_dropfilter_table_row_delete_popup_xpath = "(//span[text()='Delete'])[2]"

    # ------------------------ Log Partition --------------------------------------
    button_log_partition_xpath = "//div[text()='Log Partition']"
    button_log_partition_add_xpath = "//span[text()='Add']"
    textbox_log_partition_name_xpath = "//input[@placeholder='Name of the partition']"
    listbox_log_partition_chooseretentionforthispartition_xpath = "//span[@class='ant-select-selection-item']"
    textbox_log_partition_description_xpath = "//input[@placeholder='Description of the partition']"
    textbox_log_partition_conditionforlog_xpath = "(//input[contains(@aria-haspopup,'listbox')])[2]"
    button_log_partition_createrule_xpath = "//span[text()='Create rule']"
    button_logpartition_table_row_actions_xpath = "(//div[@class='text-center '])[1]"
    button_logpartition_table_row_delete_xpath = "(//span[text()='Delete'])[1]"
    button_logpartition_table_row_delete_popup_xpath = "(//span[text()='Delete'])[2]"
    button_logpartition_table_row_edit_xpath = "(//span[text()='Edit'])[1]"
    button_update_xpath = "//span[text()='Update']"

    #---------------------------- Saved Filter ---------------------------------------
    button_savedfilter_xpath = "//div[text()='Saved Filter']"
    savedfilter_graph_xpath = "(//div[@class='ant-spin-container'])[2]"
    savedfilter_no_graph_xpath = "//div[text()='No CPU Data']"         # this xpath is correct or not we dont know
    savedfilter_searchbox_xpath = "//input[@placeholder='Search']"
    time_interval_dropdown_xpath = "//span[@class='ant-select-selection-item']"

    #----------------------------- Custom Log -----------------------------------------
    button_custom_log_xpath = "//div[text()='Custom Log']"
    button_custom_log_add_xpath = "//span[text()='Add']"
    textbox_custom_log_name_xpath = "//input[@placeholder='Name for the partition']"
    textbox_custom_log_description_xpath = "//input[@placeholder='Description for the partition']"
    button_custom_log_browsefile_xpath = "//span[text()='Browse File']"
    button_custom_log_save_xpath = "//span[text()='Save']"
    button_custom_log_table_row_actions_xpath = "(//div[@class='text-center '])[1]"
    button_custom_log_table_row_delete_xpath = "(//span[text()='Delete'])[1]"
    button_custom_log_table_row_delete_popup_xpath = "(//span[text()='Delete'])[2]"

    #------------------------------------ Add Data ------------------------------------

    link_logs_addData_xpath = "//a[text()='Add Data']"
    AddData_searchbox_xpath = "//input[@type='text']"
    AddData_Nginx_xpath = "(//div[@class='ant-card-body'])[1]"
    AddData_Tomcat_xpath = "(//div[@class='ant-card-body'])[2]"
    AddData_customLog_xpath = "(//div[@class='ant-card-body'])[3]"
    AddData_continue_button_xpath = "//span[text()='Continue']"
    AddData_selectcontroldevices_xpath = "//div[@class='ant-card-body']"
    AddData_installationoption_xpath = "(//div[@class='ant-card-body'])[1]"
    AddData_selectyourhost_dropdown_xpath = "//span[contains(@class,'ant-select-selection-s')]"
    AddData_addfilepath_xpath = "//input[@placeholder='Enter the file path']"
    AddData_tag_xpath = "//input[@placeholder='Tag']"
    AddData_button_finish_xpath = "//span[text()='Finish']"




















    def __init__(self, driver):  # Corrected constructor
        self.driver = driver

    def click_Logs(self):
        self.driver.find_element(By.XPATH, self.button_Logs_xpath).click()

    def click_AllLogs(self):
        self.driver.find_element(By.XPATH, self.button_AllLogs_xpath).click()

    def click_addData(self):
        self.driver.find_element(By.XPATH, self.button_AddData_xpath).click()

    def enter_logs_searchbox(self, data):
        self.driver.find_element(By.XPATH, self.textbox_searchbox_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_searchbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_searchbox_xpath).send_keys(data)

    def click_enterbutton(self):
        self.driver.find_element(By.XPATH, self.button_logs_enter_xpath).click()

    def click_savebutton(self):
        self.driver.find_element(By.XPATH, self.button_logs_save_xpath).click()

    def enter_text_into_savebutton(self, text):
        self.driver.find_element(By.XPATH, self.textbox_logs_savebutton_input_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_logs_savebutton_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_logs_savebutton_input_xpath).send_keys(text)

    def click_savebutton_inside_savebutton(self):
        self.driver.find_element(By.XPATH, self.button_logs_savebutton_input_againsavebutton_xpath).click()

    def click_alllogdata(self):
        self.driver.find_element(By.XPATH, self.button_logs_alllogdata_xpath).click()

    def click_exportbutton(self):
        self.driver.find_element(By.XPATH, self.button_export_xpath).click()

    def click_exportbutton_json(self):
        self.driver.find_element(By.XPATH, self.radio_button_alllogs_json_xpath).click()

    def click_exportbutton_csv(self):
        self.driver.find_element(By.XPATH, self.radio_button_alllogs_csv_xpath).click()

    def click_on_export_limit_dropdown(self):
        self.driver.find_element(By.XPATH, self.button_export_dropdown).click()

    def export_limit_dropdown_json(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.listbox_dropdown_elements_json_xpath)))
        print("Element found:", element.text)
        element.click()

    def export_limit_dropdown_csv(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.listbox_dropdown_elements_csv_xpath)))
        print("Element found:", element.text)
        element.click()

    def click_download_button(self):
        self.driver.find_element(By.XPATH, self.button_logs_download_xpath).click()

    def click_on_logs_settings(self):
        self.driver.find_element(By.XPATH, self.button_logs_settings_xpath).click()

    def click_on_logs_selectall_checkbox(self):
        self.driver.find_element(By.XPATH, self.button_logs_settings_checkbox_xpath).click()

    def click_on_logs_empty_selectall_checkbox(self):
        self.driver.find_element(By.XPATH, self.button_logs_settings_uncheckbox_xpath).click()

    def click_on_logs_settings_save(self):
        self.driver.find_element(By.XPATH, self.button_logs_settings_save_xpath).click()

    # ---------------------- Tuning ----------------------------

    def click_tuningbutton(self):
        self.driver.find_element(By.XPATH, self.button_tuning_xpath).click()

    def click_tuning_addbutton(self):
        self.driver.find_element(By.XPATH, self.button_tuning_add_xpath).click()

    def enter_text_into_nameofrule(self, text):
        self.driver.find_element(By.XPATH, self.textbox_tuning_nameofrule_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_tuning_nameofrule_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_tuning_nameofrule_xpath).send_keys(text)

    def arrow_button(self):
        self.driver.find_element(By.XPATH, self.listbox_tuning_fieldtotune_xpath).click()

    def hostname_dropdown(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Host Name']")))
        print("Element found:", element.text)
        element.click()

    def log_dropdown(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Log']")))
        print("Element found:", element.text)
        element.click()

    def click_fieldtotune_listbox1111(self):
        self.driver.find_element(By.XPATH, self.listbox_tuning_fieldtotune_xpath).click()
        time.sleep(5)

        allintervals = self.driver.find_elements(By.XPATH,
                                                 "rc_select_0_list_")

        for element in allintervals:
            if element.text == "Log":
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(element)
                )
                self.driver.execute_script("arguments[0].click();", element)
                break
        time.sleep(2)

    def enter_text_into_tuningrule(self, text):
        self.driver.find_element(By.XPATH, self.textbox_tuning_tuningrule_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_tuning_tuningrule_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_tuning_tuningrule_xpath).send_keys(text)

    def click_on_pastelog(self):
        self.driver.find_element(By.XPATH, self.button_tuning_pastelog_xpath).click()

    def click_on_createrule(self):
        self.driver.find_element(By.XPATH, self.button_tuning_Createrule_xpath).click()

    def click_on_tuning_actions_button(self):

        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, self.button_tuning_table_row_actions_xpath))
        action.perform()

    def click_on_tuning_table_row_delete(self):
        self.driver.find_element(By.XPATH, self.button_tuning_table_row_delete_xpath).click()

    def click_on_tuning_table_row_delete_popup(self):
        self.driver.find_element(By.XPATH, self.button_tuning_table_row_delete_popup_xpath).click()

    # ------------------------------ Drop Filter -------------------------------------
    def click_on_dropfilter_tag(self):
        self.driver.find_element(By.XPATH, self.button_dropfilter_xpath).click()

    def click_on_dropfilter_add(self):
        self.driver.find_element(By.XPATH, self.button_dropfilter_add_xpath).click()

    def enter_text_into_dropfilter_name(self, text):
        self.driver.find_element(By.XPATH, self.textbox_dropfilter_name_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_dropfilter_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_dropfilter_name_xpath).send_keys(text)

    def click_on_selectlogpartition_dropdown(self):  # pending
        self.driver.find_element(By.XPATH, self.listbox_dropfilter_selectlogpartition_xpath).click()

    def enter_text_into_conditionforlog(self, text):
        self.driver.find_element(By.XPATH, self.textbox_dropfilter_conditionforlog_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_dropfilter_conditionforlog_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_dropfilter_conditionforlog_xpath).send_keys(text)

    def click_on_dropfilter_submit(self):
        self.driver.find_element(By.XPATH, self.button_dropfilter_submit_xpath).click()

    def click_on_dropfilter_actions_button(self):

        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, self.button_dropfilter_table_row_actions_xpath))
        action.perform()

    def click_on_dropfilter_table_row_delete(self):
        self.driver.find_element(By.XPATH, self.button_dropfilter_table_row_delete_xpath).click()

    def click_on_dropfilter_table_row_delete_popup(self):
        self.driver.find_element(By.XPATH, self.button_dropfilter_table_row_delete_popup_xpath).click()

    #----------------------------- Log Partition ----------------------------------------------------

    def click_logpartition_button(self):
        self.driver.find_element(By.XPATH, self.button_log_partition_xpath).click()

    def click_logpartition_add_button(self):
        self.driver.find_element(By.XPATH, self.button_log_partition_add_xpath).click()

    def enter_text_into_logpartition_name_field(self, text):
        self.driver.find_element(By.XPATH, self.textbox_log_partition_name_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_log_partition_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_log_partition_name_xpath).send_keys(text)



    def click_on_listbox_chooseretentionforthispartition(self):
        self.driver.find_element(By.XPATH, self.listbox_log_partition_chooseretentionforthispartition_xpath).click()

    def click_on_listbox_dropdown_for_chooseretentionforthispartition(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='60 days']")))
        print("Element found:", element.text)
        element.click()

    def enter_text_into_logpartition_description(self, text):
        self.driver.find_element(By.XPATH, self.textbox_log_partition_description_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_log_partition_description_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_log_partition_description_xpath).send_keys(text)

    def enter_text_into_logpartition_conditionforlog(self, text):
        self.driver.find_element(By.XPATH, self.textbox_log_partition_conditionforlog_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_log_partition_conditionforlog_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_log_partition_conditionforlog_xpath).send_keys(text)

    def click_on_logpartition_createrule(self):
        self.driver.find_element(By.XPATH, self.button_log_partition_createrule_xpath).click()

    def click_on_logpartition_actions_button(self):

        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, self.button_logpartition_table_row_actions_xpath))
        action.perform()

    def click_on_logpartition_table_row_delete(self):
        self.driver.find_element(By.XPATH, self.button_logpartition_table_row_delete_xpath).click()

    def click_on_logpartition_table_row_delete_popup(self):
        self.driver.find_element(By.XPATH, self.button_logpartition_table_row_delete_popup_xpath).click()

    def click_on_logpartition_table_row_edit(self):
        self.driver.find_element(By.XPATH, self.button_logpartition_table_row_edit_xpath).click()

    def get_logpartition_name(self):
        return self.driver.find_element(By.XPATH, self.textbox_log_partition_name_xpath).get_attribute("value")

    # def get_logpartition_retention(self):
    #     return self.driver.find_element(By.XPATH, self.listbox_log_partition_chooseretentionforthispartition_xpath).get_attribute("value")

    def get_logpartition_description(self):
        return self.driver.find_element(By.XPATH, self.textbox_log_partition_description_xpath).get_attribute("value")

    def get_logpartition_condition(self):
        return self.driver.find_element(By.XPATH, self.textbox_log_partition_conditionforlog_xpath).get_attribute("value")

    def set_logpartition_name(self, name):
        element = self.driver.find_element(By.XPATH, self.textbox_log_partition_name_xpath)
        element.clear()
        element.send_keys(name)

    # def set_logpartition_retention(self, retention):
    #     element = self.driver.find_element(By.XPATH, self.listbox_log_partition_chooseretentionforthispartition_xpath)
    #     element.clear()
    #     element.send_keys(retention)

    def set_logpartition_description(self, description):
        element = self.driver.find_element(By.XPATH, self.textbox_log_partition_description_xpath)
        element.clear()
        element.send_keys(description)

    def set_logpartition_condition(self, condition):
        element = self.driver.find_element(By.XPATH, self.textbox_log_partition_conditionforlog_xpath)
        element.clear()
        element.send_keys(condition)

    def clear_logpartition_name(self):
        element = self.driver.find_element(By.XPATH, self.textbox_log_partition_name_xpath)
        element.click()
        time.sleep(3)
        element.clear()

    def clear_logpartition_description(self):
        element = self.driver.find_element(By.XPATH, self.textbox_log_partition_description_xpath)
        element.click()
        time.sleep(3)
        element.clear()

    def clear_logpartition_condition(self):
        element = self.driver.find_element(By.XPATH, self.textbox_log_partition_conditionforlog_xpath)
        element.click()
        time.sleep(3)
        element.clear()

    def update_button(self):
        self.driver.find_element(By.XPATH, self.button_update_xpath).click()

    #---------------------------------- Saved Filter -----------------------------------------------
    def click_on_savedfilter_tab(self):
        self.driver.find_element(By.XPATH, self.button_savedfilter_xpath).click()

    def enter_text_into_savedfilter_searchbox(self, searchbox_text):
        self.driver.find_element(By.XPATH, self.savedfilter_searchbox_xpath).click()
        self.driver.find_element(By.XPATH, self.savedfilter_searchbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.savedfilter_searchbox_xpath).send_keys(searchbox_text)

    def click_on_time_interval_dropdown(self):
        self.driver.find_element(By.XPATH, self.time_interval_dropdown_xpath).click()

    # def click_on_interval_dropdown_options(self):
    #     element = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, "//span[text()='Today']")))
    #     print("Element found:", element.text)
    #     element.click()

    #------------------------------------ Custome Log --------------------------------------

    def click_custom_log_button(self):
        self.driver.find_element(By.XPATH, self.button_custom_log_xpath).click()

    def click_custom_log_add_button(self):
        self.driver.find_element(By.XPATH, self.button_custom_log_add_xpath).click()

    def enter_text_into_custom_log_name_field(self, text):
        self.driver.find_element(By.XPATH, self.textbox_custom_log_name_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_custom_log_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_custom_log_name_xpath).send_keys(text)

    def enter_text_into_custom_log_description(self, text):
        self.driver.find_element(By.XPATH, self.textbox_custom_log_description_xpath).click()
        self.driver.find_element(By.XPATH, self.textbox_custom_log_description_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_custom_log_description_xpath).send_keys(text)

    def click_custom_log_Browsefile_button(self):
        self.driver.find_element(By.XPATH, self.button_custom_log_browsefile_xpath).click()

    def click_custom_log_save_button(self):
        self.driver.find_element(By.XPATH, self.button_custom_log_save_xpath).click()

    def click_on_custom_log_actions_button(self):

        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.XPATH, self.button_custom_log_table_row_actions_xpath))
        action.perform()

    def click_on_custom_log_table_row_delete(self):
        self.driver.find_element(By.XPATH, self.button_custom_log_table_row_delete_xpath).click()

    def click_on_custom_log_table_row_delete_popup(self):
        self.driver.find_element(By.XPATH, self.button_custom_log_table_row_delete_popup_xpath).click()


    #------------------------------------ Add Data ---------------------------------------------

    def click_on_Logs_AddData(self):
        self.driver.find_element(By.XPATH, self.link_logs_addData_xpath).click()

    def click_on_Nginx(self):
        self.driver.find_element(By.XPATH, self.AddData_Nginx_xpath).click()

    def click_on_Tomcat(self):
        self.driver.find_element(By.XPATH, self.AddData_Tomcat_xpath).click()

    def click_on_Customlog(self):
        self.driver.find_element(By.XPATH, self.AddData_customLog_xpath).click()

    def click_on_AddData_continuebutton(self):
        self.driver.find_element(By.XPATH, self.AddData_continue_button_xpath).click()

    def click_on_selectcontroldevices_on_a_Host(self):
        self.driver.find_element(By.XPATH, self.AddData_selectcontroldevices_xpath).click()

    def click_on_installation_option_is_your_application_running_on_windows(self):
        self.driver.find_element(By.XPATH, self.AddData_installationoption_xpath).click()

    def click_on_selectyourhost_dropdown(self):
        self.driver.find_element(By.XPATH, self.AddData_selectyourhost_dropdown_xpath).click()

    def addData_dropdown(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='ZCS-SERVER']")))
        print("Element found:", element.text)
        element.click()

    def enter_text_into_addData_filepath(self, filepath):
        self.driver.find_element(By.XPATH, self.AddData_addfilepath_xpath).click()
        self.driver.find_element(By.XPATH, self.AddData_addfilepath_xpath).clear()
        self.driver.find_element(By.XPATH, self.AddData_addfilepath_xpath).send_keys(filepath)

    def enter_text_into_addData_tag(self, tag):
        self.driver.find_element(By.XPATH, self.AddData_tag_xpath).click()
        self.driver.find_element(By.XPATH, self.AddData_tag_xpath).clear()
        self.driver.find_element(By.XPATH, self.AddData_tag_xpath).send_keys(tag)

    def click_addData_Finish_button(self):
        self.driver.find_element(By.XPATH, self.AddData_button_finish_xpath).click()



    def select_host_dropdown_by_index(self, index):
        # Wait for the dropdown to be clickable and click it to expand the options
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'ant-select-selector')]"))
        )
        dropdown.click()  # Clicks to open the dropdown
        time.sleep(3)
        print("alexasdksalkfj;lksjflkjl;sdjf;ljsdfjlksjd;lfjlsdjflkjds111111111111111")

        # Wait for the options to be visible
        options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='ant-select-item-option-content']"))
        )
        print("alexasdksalkfj;lksjflkjl;sdjf;ljsdfjlksjd;lfjlsdjflkjds")
        print(len(options))

        # Check if index is valid
        if index < len(options):
            # Select option by index
            options[index].click()
            time.sleep(4)
        else:
            print(f"Index {index} is out of range for the dropdown options")

        time.sleep(2)  # Small delay to allow the option to be selected


    def table_data(self):
        # Locate the table element
        table = self.driver.find_element(By.XPATH, "//table")

        # Capture the header row
        header = table.find_elements(By.XPATH, ".//thead//th")
        header_row = [cell.text for cell in header]

        # Get the initial row count
        rows = table.find_elements(By.XPATH, ".//tbody//tr")
        initial_row_count = len(rows)

        # Scroll the table and gather all rows
        table_data = []
        previous_row_count = 0

        while True:
            # Locate all rows in the table
            rows = table.find_elements(By.XPATH, ".//tbody//tr")

            # If the row count hasn't changed after scrolling, break the loop
            if len(rows) == previous_row_count:
                break

            previous_row_count = len(rows)

            # Prepare data for DataFrame
            for row in rows:
                # Locate all cells in the current row
                cells = row.find_elements(By.XPATH, ".//td")
                time.sleep(1)
                row_data = [cell.text for cell in cells]
                if row_data not in table_data:  # Avoid adding duplicate rows
                    table_data.append(row_data)

        # Ensure all rows have the same number of columns
        max_columns = max(len(row) for row in table_data)
        for row in table_data:
            while len(row) < max_columns:
                row.append('')

        # Create DataFrame
        df = pd.DataFrame(table_data, columns=header_row)

        # Generate the formatted table output using tabulate
        formatted_table = tabulate(df, headers='keys', tablefmt='pretty')

        return formatted_table

    def table_data_1(self):
        # Locate the table element
        table = self.driver.find_element(By.XPATH, "//div[@class='ant-table-container']")

        # Capture the header row
        header = table.find_elements(By.XPATH, ".//thead//th")
        header_row = [cell.text for cell in header]

        # Get the initial row count
        rows = table.find_elements(By.XPATH, ".//tbody//tr")
        initial_row_count = len(rows)

        # Scroll the table and gather all rows
        table_data = []
        previous_row_count = 0

        while True:
            # Locate all rows in the table
            rows = table.find_elements(By.XPATH, ".//tbody//tr")

            # If the row count hasn't changed after scrolling, break the loop
            if len(rows) == previous_row_count:
                break

            previous_row_count = len(rows)

            # Prepare data for DataFrame
            for row in rows:
                # Locate all cells in the current row
                cells = row.find_elements(By.XPATH, ".//td")
                time.sleep(1)
                row_data = [cell.text for cell in cells]
                if row_data not in table_data:  # Avoid adding duplicate rows
                    table_data.append(row_data)

        # Ensure all rows have the same number of columns
        max_columns = max(len(row) for row in table_data)
        for row in table_data:
            while len(row) < max_columns:
                row.append('')

        # Create DataFrame
        df = pd.DataFrame(table_data, columns=header_row)

        # Generate the formatted table output using tabulate
        formatted_table = tabulate(df, headers='keys', tablefmt='pretty')

        return formatted_table

    # def table_data_11(self):
    #     # Locate the table element
    #     table = self.driver.find_element(By.XPATH, "(//div[@class='ant-table-container'])[1]")
    #
    #     # Capture the header row
    #     header = table.find_elements(By.XPATH, ".//thead//th")
    #     header_row = [cell.text for cell in header]
    #
    #     print("Header Row: ", header_row)  # Debugging print
    #
    #     # Get the initial row count
    #     rows = table.find_elements(By.XPATH, ".//tbody//tr")
    #     initial_row_count = len(rows)
    #
    #     # Scroll the table and gather all rows
    #     table_data = []
    #     previous_row_count = 0
    #
    #     while True:
    #         # Locate all rows in the table
    #         rows = table.find_elements(By.XPATH, ".//tbody//tr")
    #
    #         # If the row count hasn't changed after scrolling, break the loop
    #         if len(rows) == previous_row_count:
    #             break
    #
    #         previous_row_count = len(rows)
    #
    #         # Prepare data for DataFrame
    #         for row in rows:
    #             # Locate all cells in the current row
    #             cells = row.find_elements(By.XPATH, ".//td")
    #             time.sleep(1)
    #             row_data = [cell.text for cell in cells]
    #             print("Row Data: ", row_data)  # Debugging print
    #             if row_data not in table_data:  # Avoid adding duplicate rows
    #                 table_data.append(row_data)
    #
    #     # Get the maximum number of columns in any row
    #     max_columns = max(len(row) for row in table_data)
    #
    #     # Adjust the header row to match the number of columns in table_data
    #     while len(header_row) < max_columns:
    #         header_row.append('')
    #
    #     # Ensure all rows have the same number of columns
    #     for row in table_data:
    #         while len(row) < max_columns:
    #             row.insert(0, '')  # Add empty string to the beginning to align columns
    #
    #     # Create DataFrame
    #     df = pd.DataFrame(table_data, columns=header_row)
    #
    #     # Generate the formatted table output using tabulate
    #     formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
    #
    #     return formatted_table

    def table_data_11(self):
        # Locate the table element
        table = self.driver.find_element(By.XPATH, "(//div[@class='ant-table-container'])[1]")

        # Capture the header row
        header = table.find_elements(By.XPATH, ".//thead//th")
        header_row = [cell.text.strip() for cell in header]

        # Filter out any empty header columns (optional, if you want to skip empty headers)
        header_row = [col for col in header_row if col]

        print("Header Row: ", header_row)  # Debugging print

        # Get the initial row count
        rows = table.find_elements(By.XPATH, ".//tbody//tr")
        previous_row_count = 0

        # Scroll the table and gather all rows
        table_data = []

        while True:
            # Locate all rows in the table
            rows = table.find_elements(By.XPATH, ".//tbody//tr")

            # If the row count hasn't changed after scrolling, break the loop
            if len(rows) == previous_row_count:
                break

            previous_row_count = len(rows)

            # Prepare data for DataFrame
            for row in rows:
                # Locate all cells in the current row
                cells = row.find_elements(By.XPATH, ".//td")
                row_data = [cell.text.strip() for cell in cells]
                print("Row Data: ", row_data)  # Debugging print

                # Ensure row_data has the same number of elements as header_row
                while len(row_data) < len(header_row):
                    row_data.append('')  # Pad with empty strings if needed

                # Avoid adding duplicate rows
                if row_data not in table_data:
                    table_data.append(row_data)

        # Get the maximum number of columns in any row
        max_columns = max(len(row) for row in table_data)

        # Adjust the header row to match the number of columns in table_data (if needed)
        while len(header_row) < max_columns:
            header_row.append('')

        # Ensure all rows have the same number of columns
        for row in table_data:
            while len(row) < max_columns:
                row.append('')  # Add empty strings to align the columns

        # Create DataFrame
        df = pd.DataFrame(table_data, columns=header_row)

        # Generate the formatted table output using tabulate
        formatted_table = tabulate(df, headers='keys', tablefmt='pretty')

        return formatted_table

    def table_data_2(self):
        # Locate the table element
        table = self.driver.find_element(By.XPATH, "(//div[@class='ant-table-container'])[2]")

        # Capture the header row
        header = table.find_elements(By.XPATH, ".//thead//th")
        header_row = [cell.text for cell in header]

        # Get the initial row count
        rows = table.find_elements(By.XPATH, ".//tbody//tr")

        # Check if there is any data
        if len(rows) == 1 and rows[0].text == "No data":
            print("No data available in the table.")
            return "No data"

        # Scroll the table and gather all rows
        table_data = []
        previous_row_count = 0

        while True:
            # Locate all rows in the table
            rows = table.find_elements(By.XPATH, ".//tbody//tr")

            # If the row count hasn't changed after scrolling, break the loop
            if len(rows) == previous_row_count:
                break

            previous_row_count = len(rows)

            # Prepare data for DataFrame
            for row in rows:
                # Locate all cells in the current row
                cells = row.find_elements(By.XPATH, ".//td")
                time.sleep(1)
                row_data = [cell.text for cell in cells]
                if row_data not in table_data:  # Avoid adding duplicate rows
                    table_data.append(row_data)

        # Ensure all rows have the same number of columns
        max_columns = max(len(row) for row in table_data)
        for row in table_data:
            while len(row) < max_columns:
                row.append('')

        # Create DataFrame
        df = pd.DataFrame(table_data, columns=header_row)

        # Generate the formatted table output using tabulate
        formatted_table = tabulate(df, headers='keys', tablefmt='pretty')

        return formatted_table

    # def table_data_2(self):
    #     # Locate the table element
    #     table = self.driver.find_element(By.XPATH, "(//div[@class='ant-table-container'])[2]")
    #
    #     # Capture the header row
    #     header = table.find_elements(By.XPATH, ".//thead//th")
    #     header_row = [cell.text for cell in header]
    #
    #     # Get the initial row count
    #     rows = table.find_elements(By.XPATH, ".//tbody//tr")
    #     initial_row_count = len(rows)
    #
    #     # Scroll the table and gather all rows
    #     table_data = []
    #     previous_row_count = 0
    #
    #     while True:
    #         # Locate all rows in the table
    #         rows = table.find_elements(By.XPATH, ".//tbody//tr")
    #
    #         # If the row count hasn't changed after scrolling, break the loop
    #         if len(rows) == previous_row_count:
    #             break
    #
    #         previous_row_count = len(rows)
    #
    #         # Prepare data for DataFrame
    #         for row in rows:
    #             # Locate all cells in the current row
    #             cells = row.find_elements(By.XPATH, ".//td")
    #             time.sleep(1)
    #             row_data = [cell.text for cell in cells]
    #             if row_data not in table_data:  # Avoid adding duplicate rows
    #                 table_data.append(row_data)
    #
    #     # Ensure all rows have the same number of columns
    #     max_columns = max(len(row) for row in table_data)
    #     for row in table_data:
    #         while len(row) < max_columns:
    #             row.append('')
    #
    #     # Create DataFrame
    #     df = pd.DataFrame(table_data, columns=header_row)
    #
    #     # Generate the formatted table output using tabulate
    #     formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
    #
    #     return formatted_table

    # def table2_data(self):
    #     # Locate the table element
    #     table = self.driver.find_element(By.XPATH, "(//table)[2]")
    #
    #     # Capture the header row
    #     header = table.find_elements(By.XPATH, ".//thead//th")
    #     header_row = [cell.text for cell in header]
    #
    #     # Get the initial row count
    #     rows = table.find_elements(By.XPATH, ".//tbody//tr")
    #     initial_row_count = len(rows)
    #
    #     # Scroll the table and gather all rows
    #     table_data = []
    #     previous_row_count = 0
    #
    #     while True:
    #         # Locate all rows in the table
    #         rows = table.find_elements(By.XPATH, ".//tbody//tr")
    #
    #         # If the row count hasn't changed after scrolling, break the loop
    #         if len(rows) == previous_row_count:
    #             break
    #
    #         previous_row_count = len(rows)
    #
    #         # Prepare data for DataFrame
    #         for row in rows:
    #             # Locate all cells in the current row
    #             cells = row.find_elements(By.XPATH, ".//td")
    #             time.sleep(1)
    #             row_data = [cell.text for cell in cells]
    #             if row_data not in table_data:  # Avoid adding duplicate rows
    #                 table_data.append(row_data)
    #
    #     # Ensure all rows have the same number of columns
    #     max_columns = max(len(row) for row in table_data)
    #     for row in table_data:
    #         while len(row) < max_columns:
    #             row.append('')
    #
    #     # Create DataFrame
    #     df = pd.DataFrame(table_data, columns=header_row)
    #
    #     # Generate the formatted table output using tabulate
    #     formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
    #
    #     return formatted_table

    def table2_data(self):
        # Locate the table element
        table = self.driver.find_element(By.XPATH, "(//table)[2]")

        # Capture the header row
        header = table.find_elements(By.XPATH, ".//thead//th")
        header_row = [cell.text for cell in header]

        # Fallback headers if header_row is empty
        if not header_row:
            rows = table.find_elements(By.XPATH, ".//tbody//tr")
            if rows:
                sample_row = rows[0].find_elements(By.XPATH, ".//td")
                header_row = [f"Column {i + 1}" for i in range(len(sample_row))]

        # Log headers and initial row count
        print(f"Headers: {header_row}")

        # Get the initial row count
        rows = table.find_elements(By.XPATH, ".//tbody//tr")
        initial_row_count = len(rows)

        # Scroll the table and gather all rows
        table_data = []
        previous_row_count = 0

        while True:
            # Locate all rows in the table
            rows = table.find_elements(By.XPATH, ".//tbody//tr")

            # If the row count hasn't changed after scrolling, break the loop
            if len(rows) == previous_row_count:
                break

            previous_row_count = len(rows)

            # Prepare data for DataFrame
            for row in rows:
                # Locate all cells in the current row
                cells = row.find_elements(By.XPATH, ".//td")
                time.sleep(1)  # Adjust sleep as needed
                row_data = [cell.text for cell in cells]
                if row_data not in table_data:  # Avoid adding duplicate rows
                    table_data.append(row_data)

        # Ensure all rows have the same number of columns
        max_columns = max(len(row) for row in table_data)
        for row in table_data:
            while len(row) < max_columns:
                row.append('')

        # Recheck header length against row length
        if len(header_row) != max_columns:
            print(f"Warning: Header length ({len(header_row)}) does not match row length ({max_columns}).")
            # Adjust header_row length to match max_columns
            header_row = header_row[:max_columns] + [f"Column {i + 1}" for i in range(len(header_row), max_columns)]

        # Create DataFrame
        df = pd.DataFrame(table_data, columns=header_row)

        # Generate the formatted table output using tabulate
        formatted_table = tabulate(df, headers='keys', tablefmt='pretty')

        return formatted_table


    def table_data_3(self):
        # Wait until the table rows are present
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//table)[3]/tbody/tr")))

        # Locate the table element
        table = self.driver.find_element(By.XPATH, "(//table)[3]")

        # Capture the header row
        header = table.find_elements(By.XPATH, ".//thead//th")
        header_row = [cell.text for cell in header]

        # Initialize variables for collecting data
        table_data = []
        previous_row_count = 0
        start_time = time.time()  # Start timer

        # Set a max duration to run the loop (15 seconds)
        while time.time() - start_time < 15:
            # Get the current rows
            rows = table.find_elements(By.XPATH, ".//tbody//tr")
            current_row_count = len(rows)

            # If no new rows are loaded, stop scrolling
            if current_row_count == previous_row_count:
                break

            # Gather data from new rows
            for row in rows[previous_row_count:]:
                cells = row.find_elements(By.XPATH, ".//td")
                row_data = [cell.text for cell in cells]
                if row_data:  # Only append if the row has data
                    table_data.append(row_data)

            previous_row_count = current_row_count

            # Scroll to the last row to load more data
            if rows:
                actions = ActionChains(self.driver)
                actions.move_to_element(rows[-1]).perform()
            time.sleep(1)  # Wait for more rows to load

        # After collecting data for 15 seconds or until no more rows are loaded
        # Add logic to ensure that table header and body are processed correctly

        # Locate the table header and all rows in the table (both header and body)
        rows = table.find_elements(By.XPATH, ".//tr")

        # Prepare data for DataFrame
        for row in rows:
            # Locate all cells in the current row (both header and body)
            cells = row.find_elements(By.XPATH, ".//td | .//th")
            row_data = [cell.text for cell in cells]
            table_data.append(row_data)

        # Create DataFrame from table_data
        df = pd.DataFrame(table_data[1:], columns=table_data[0])

        # Generate the formatted table output using tabulate
        formatted_table = tabulate(df, headers='keys', tablefmt='pretty')
        return formatted_table


