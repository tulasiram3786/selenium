# import time
#
# import pytest
# from selenium.webdriver.common.by import By
#
#
# class Test_AlertsorPopups:
#
#     def test_alertsorpopus(self,setup):
#
#         self.driver = setup
#         self.driver.implicitly_wait(10)
#         self.driver.get("https://testautomationpractice.blogspot.com/")
#         self.driver.find_element(By.XPATH, "//button[@id='promptBtn']").click()
#         myalert = self.driver.switch_to.alert
#         print(myalert.text)
#
#         myalert.send_keys("tulasiram")
#         time.sleep(10)
#         myalert.accept()
#         myalert.dismiss()
#
#         name = self.driver.find_element(By.XPATH, "//p[@id='demo']")
#         print(name.text)
#
#     @pytest.mark.tulasi
#     def test_authenticationpopup(self, setup):
#         self.driver= setup
#         self.driver.implicitly_wait(10)
#         self.driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
#         time.sleep(3)




#________________________________

import paramiko
import requests

# Define server connection details
hostname = '192.168.1.81'
port = 20202
username = 'tulasi'
password = 'Nop@ssw0rd'

# API details
api_url = 'https://staging-api-zoomview.zybisys.com/saas-zoomview/api/v1/infra/infra-livestate'  # Replace with your API endpoint

def execute_remote_command(command):
    try:
        # Create an SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        if error:
            print(f"Error: {error}")
        return output.strip()  # Stripping extra newlines/whitespace
    except Exception as e:
        print(f"Failed to connect: {e}")
    finally:
        client.close()


# Fetch system storage data via SSH
def fetch_system_data():
    # Fetch Disk usage in bytes and percentage (for root partition "/")
    disk_bytes_command = "df --block-size=1 / | grep '/' | awk '{print $3}'"  # Fetch the used space in bytes
    disk_used_bytes = execute_remote_command(disk_bytes_command)

    disk_percentage_command = "df -h / | grep '/' | awk '{print $5}'"  # Fetch the usage percentage directly
    disk_usage_percentage = execute_remote_command(disk_percentage_command).replace('%', '')  # Remove %

    return {
        "disk_used_bytes": disk_used_bytes,  # Disk used in bytes
        "disk_usage_percentage": disk_usage_percentage  # Disk usage in percentage
    }


# Fetch storage data from API
def fetch_api_data():
    payload = {'host_name': 'zcsit', 'service_name': 'disk'}
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI4ODc4ODYxNzUyLCJpYXQiOjE3Mjg4Nzg4NjEsImV4cCI6MTcyODk2NTI2MX0.Ef_o8MKUV3NuDN1w8QnqoK6esImiA6kghiTDzm_vJt8ZyWojlpGft4rnKv1LmdQD-WuwJNlpO09oLDIqUNhLjA"
        # Replace with your actual token
    }
    response = requests.get(url=api_url, params=payload, headers=headers)
    if response.status_code == 200:
        api_data = response.json()
        api_data2 = api_data['message']

        storage_data = {}
        for serviceData in api_data2:
            service_data = serviceData['service_data']
            for service_data2 in service_data:
                if 'disk_used_bytes' in service_data2['metrix_name']:
                    storage_data['disk_used_bytes'] = service_data2['metrix_value']
                elif 'disk_usage_percentage' in service_data2['metrix_name']:
                    storage_data['disk_usage_percentage'] = service_data2['metrix_value']

        return storage_data
    else:
        print(f"API Request Failed: {response.status_code}")
        return None


# Compare Disk (Storage) data for both bytes and percentage
def compare_data(ssh_data, api_data):
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(f"SSH DATA: {ssh_data}")
    print(f"API DATA: {api_data}")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    # Disk Usage Bytes Comparison
    ssh_disk_used_bytes = int(ssh_data.get('disk_used_bytes', 0))
    api_disk_used_bytes = int(api_data.get('disk_used_bytes', 0))

    if api_disk_used_bytes:
        if abs(ssh_disk_used_bytes - api_disk_used_bytes) <= (ssh_disk_used_bytes * 0.05):  # Allow 5% tolerance
            print(f"Disk used bytes matches: SSH={ssh_disk_used_bytes} bytes, API={api_disk_used_bytes} bytes (within 5%)")
        else:
            print(f"Disk used bytes mismatch: SSH={ssh_disk_used_bytes} bytes, API={api_disk_used_bytes} bytes (difference > 5%)")
    else:
        print("Disk used bytes data missing from API.")

    # Disk Usage Percentage Comparison
    ssh_disk_usage_percentage = float(ssh_data.get('disk_usage_percentage', 0))
    api_disk_usage_percentage = float(api_data.get('disk_usage_percentage', 0))

    if api_disk_usage_percentage:
        if abs(ssh_disk_usage_percentage - api_disk_usage_percentage) <= 5:  # Allow 5% tolerance
            print(f"Disk usage percentage matches: SSH={ssh_disk_usage_percentage}%, API={api_disk_usage_percentage}% (within 5%)")
        else:
            print(f"Disk usage percentage mismatch: SSH={ssh_disk_usage_percentage}%, API={api_disk_usage_percentage}% (difference > 5%)")
    else:
        print("Disk usage percentage data missing from API.")


# Main execution
if __name__ == "__main__":
    print("Fetching system storage data from SSH...")
    ssh_data = fetch_system_data()
    print(ssh_data)
    print("Fetching storage data from API...")
    api_data = fetch_api_data()
    print(api_data)

    if api_data:
        print("Comparing storage data for disk_used_bytes and disk_usage_percentage...")
        compare_data(ssh_data, api_data)
    else:
        print("Failed to fetch API data.")
