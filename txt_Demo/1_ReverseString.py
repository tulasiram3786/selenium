

# input_string = "tulasiram"
# output_string = ""
#
# for i in range(len(input_string) - 1, -1, -1):
#     c1 = input_string[i]
#     output_string += c1
#
# print(output_string)



# input_string = "mom"
# output_string =""
#
# for i in range(len(input_string)-1, -1, -1):
#     c1= input_string[i]
#     output_string = output_string+c1
#
# print(output_string)
#
# if input_string == output_string:
#     print("palindrom")
# else:
#     print("not palindrom")





#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#super
import paramiko
import requests
from prettytable import PrettyTable
from jinja2 import Environment, FileSystemLoader

# Define server connection details
hostname = '192.168.1.81'
port = 20202
username = 'tulasi'
password = 'Nop@ssw0rd'

# API details
api_url = 'https://staging-api-zoomview.zybisys.com/saas-zoomview/api/v1/infra/infra-livestate'  # Replace with your API endpoint

def execute_remote_command(command):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')
        if error:
            print(f"Error: {error}")
        return output.strip()
    except Exception as e:
        print(f"Failed to connect: {e}")
    finally:
        client.close()

# Fetch disk data via SSH
def fetch_disk_data():
    # Fetch disk usage data for root partition
    disk_command = "df -B1 / | awk 'NR==2{printf \"%s %s %s\", $2, $3, $4}'"
    disk_usage = execute_remote_command(disk_command).split()
    disk_total, disk_used, disk_free = map(int, disk_usage)

    return {
        "disk_total": round(disk_total / 1e9, 2),  # Convert to GB
        "disk_used": round(disk_used / 1e9, 2),    # Convert to GB
        "disk_free": round(disk_free / 1e9, 2),    # Convert to GB
    }

def fetch_api_data():
    payload = {'host_name': 'zcsit', 'service_name': 'disk'}
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI5MTU2OTgzODUwLCJpYXQiOjE3MjkxNTY5ODMsImV4cCI6MTcyOTI0MzM4M30.ZDvzBZbxVkbJeuvawRPqHrQTnWLAmGLvej_bm2mWeyZdjCzEnPhjcBQG4TJBDsx4BJXBbIZCD89QxeTpUkO1ZQ"  # Replace with your actual token
    }
    response = requests.get(url=api_url, params=payload, headers=headers)
    if response.status_code == 200:
        api_data = response.json()
        api_data2 = api_data['message']

        disk_data = {}
        for serviceData in api_data2:
            service_data = serviceData['service_data']
            for service_data2 in service_data:
                if service_data2['metrix_name'] == 'disk_used':
                    disk_data['disk_used'] = float(service_data2['metrix_value'])
                if service_data2['metrix_name'] == 'disk_total':
                    disk_data['disk_total'] = float(service_data2['metrix_value'])
                if service_data2['metrix_name'] == 'disk_free':
                    disk_data['disk_free'] = float(service_data2['metrix_value'])

        return disk_data
    else:
        print(f"API Request Failed: {response.status_code}")
        return None

def compare_values(ssh_value, api_value):
    if api_value is None:
        return "fail"  # If API value is missing, mark as fail
    difference = abs(ssh_value - api_value) / ssh_value * 100
    if difference <= 10:
        return "pass"
    elif difference > 20:
        return "fail"
    else:
        return "pass with warning"  # Could be used if needed

def generate_report(ssh_data, api_data):
    table = PrettyTable()
    table.field_names = ["Metrics", "SSH Value", "API Value", "Status"]

    # Disk Report
    ssh_disk_total = ssh_data['disk_total']
    api_disk_total = api_data.get('disk_total', None)
    total_disk_status = compare_values(ssh_disk_total, api_disk_total)
    table.add_row(["Total Disk", f"{ssh_disk_total} GB", f"{api_disk_total} GB", total_disk_status])

    ssh_disk_used = ssh_data['disk_used']
    api_disk_used = api_data.get('disk_used', None)
    used_disk_status = compare_values(ssh_disk_used, api_disk_used)
    table.add_row(["Used Disk", f"{ssh_disk_used} GB", f"{api_disk_used} GB", used_disk_status])

    ssh_disk_free = ssh_data['disk_free']
    api_disk_free = api_data.get('disk_free', None)
    free_disk_status = compare_values(ssh_disk_free, api_disk_free)
    table.add_row(["Free Disk", f"{ssh_disk_free} GB", f"{api_disk_free} GB", free_disk_status])

    print(table)
    return table

def generate_html_report(table):
    # Load Jinja2 template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('report_template1.html')  # Your HTML template file

    # Generate HTML content
    html_content = template.render(table=table)

    # Save to a file
    with open('report.html', 'w') as f:
        f.write(html_content)

    print("HTML report generated: report.html")

# Main execution
if __name__ == "__main__":
    print("Fetching disk data from SSH...")
    ssh_data = fetch_disk_data()
    print(ssh_data)
    print("Fetching disk data from API...")
    api_data = fetch_api_data()
    print(api_data)

    if api_data:
        print("Generating report...")
        table = generate_report(ssh_data, api_data)
        generate_html_report(table)
    else:
        print("Failed to fetch API data.")

#____________________
#fine but api values is same for both

# import paramiko
# import requests
# from prettytable import PrettyTable
# from jinja2 import Environment, FileSystemLoader
# import psutil  # Import psutil for Windows disk data retrieval
#
# # Define server connection details for Linux
# linux_hostname = '192.168.1.81'
# linux_port = 20202
# linux_username = 'tulasi'
# linux_password = 'Nop@ssw0rd'
#
# # Define server connection details for Windows
# windows_hostname = '10.192.1.77'
# windows_username = 'tulsiram'
# windows_password = 'nMuZ3XcF87zq4tsG65NfkA'
#
# # API details
# api_url = 'https://staging-api-zoomview.zybisys.com/saas-zoomview/api/v1/infra/infra-livestate'  # Replace with your API endpoint
#
# # Function to execute commands on a Linux server via SSH
# def execute_remote_command(command, hostname, port, username, password):
#     try:
#         client = paramiko.SSHClient()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect(hostname, port=port, username=username, password=password)
#         stdin, stdout, stderr = client.exec_command(command)
#         output = stdout.read().decode('utf-8')
#         error = stderr.read().decode('utf-8')
#         if error:
#             print(f"Error: {error}")
#         return output.strip()
#     except Exception as e:
#         print(f"Failed to connect: {e}")
#     finally:
#         client.close()
#
# # Fetch disk data via SSH for Linux
# def fetch_linux_disk_data():
#     # Fetch disk usage data for root partition
#     disk_command = "df -B1 / | awk 'NR==2{printf \"%s %s %s\", $2, $3, $4}'"
#     disk_usage = execute_remote_command(disk_command, linux_hostname, linux_port, linux_username, linux_password).split()
#     disk_total, disk_used, disk_free = map(int, disk_usage)
#
#     return {
#         "disk_total": round(disk_total / 1e9, 2),  # Convert to GB
#         "disk_used": round(disk_used / 1e9, 2),    # Convert to GB
#         "disk_free": round(disk_free / 1e9, 2),    # Convert to GB
#     }
#
# # Fetch disk data for Windows
# def fetch_windows_disk_data():
#     # Get disk usage for the C: drive
#     disk_usage = psutil.disk_usage('C:/')
#     total = disk_usage.total / (1024 ** 3)  # Convert bytes to GB
#     used = disk_usage.used / (1024 ** 3)    # Convert bytes to GB
#     free = disk_usage.free / (1024 ** 3)    # Convert bytes to GB
#     return {
#         "disk_total": round(total, 2),
#         "disk_used": round(used, 2),
#         "disk_free": round(free, 2),
#     }
#
# # Fetch disk data from API
# def fetch_api_data():
#     payload = {'host_name': 'zcsit', 'service_name': 'disk'}
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI5MTU2OTgzODUwLCJpYXQiOjE3MjkxNTY5ODMsImV4cCI6MTcyOTI0MzM4M30.ZDvzBZbxVkbJeuvawRPqHrQTnWLAmGLvej_bm2mWeyZdjCzEnPhjcBQG4TJBDsx4BJXBbIZCD89QxeTpUkO1ZQ"  # Replace with your actual token
#     }
#     response = requests.get(url=api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()
#         api_data2 = api_data['message']
#
#         disk_data = {}
#         for serviceData in api_data2:
#             service_data = serviceData['service_data']
#             for service_data2 in service_data:
#                 if service_data2['metrix_name'] == 'disk_used':
#                     disk_data['disk_used'] = float(service_data2['metrix_value'])
#                 if service_data2['metrix_name'] == 'disk_total':
#                     disk_data['disk_total'] = float(service_data2['metrix_value'])
#                 if service_data2['metrix_name'] == 'disk_free':
#                     disk_data['disk_free'] = float(service_data2['metrix_value'])
#
#         return disk_data
#     else:
#         print(f"API Request Failed: {response.status_code}")
#         return None
#
# # Compare SSH and API values
# def compare_values(ssh_value, api_value):
#     if api_value is None:
#         return "fail"  # If API value is missing, mark as fail
#     difference = abs(ssh_value - api_value) / ssh_value * 100
#     if difference <= 10:
#         return "pass"
#     elif difference > 20:
#         return "fail"
#     else:
#         return "pass with warning"  # Could be used if needed
#
# # Generate report
# def generate_report(linux_data, windows_data, api_data):
#     table = PrettyTable()
#     table.field_names = ["Metrics", "Linux Value", "Windows Value", "API Value", "Status"]
#
#     # Linux Disk Report
#     linux_disk_total = linux_data['disk_total']
#     api_linux_disk_total = api_data.get('disk_total', None)
#     total_disk_status = compare_values(linux_disk_total, api_linux_disk_total)
#     table.add_row(["Total Disk (Linux)", f"{linux_disk_total} GB", "", f"{api_linux_disk_total} GB", total_disk_status])
#
#     linux_disk_used = linux_data['disk_used']
#     api_linux_disk_used = api_data.get('disk_used', None)
#     used_disk_status = compare_values(linux_disk_used, api_linux_disk_used)
#     table.add_row(["Used Disk (Linux)", f"{linux_disk_used} GB", "", f"{api_linux_disk_used} GB", used_disk_status])
#
#     linux_disk_free = linux_data['disk_free']
#     api_linux_disk_free = api_data.get('disk_free', None)
#     free_disk_status = compare_values(linux_disk_free, api_linux_disk_free)
#     table.add_row(["Free Disk (Linux)", f"{linux_disk_free} GB", "", f"{api_linux_disk_free} GB", free_disk_status])
#
#     # Windows Disk Report
#     windows_disk_data = fetch_windows_disk_data()
#     windows_disk_total = windows_disk_data['disk_total']
#     api_windows_disk_total = api_data.get('disk_total', None)
#     total_disk_status = compare_values(windows_disk_total, api_windows_disk_total)
#     table.add_row(["Total Disk (Windows)", "", f"{windows_disk_total} GB", f"{api_windows_disk_total} GB", total_disk_status])
#
#     windows_disk_used = windows_disk_data['disk_used']
#     api_windows_disk_used = api_data.get('disk_used', None)
#     used_disk_status = compare_values(windows_disk_used, api_windows_disk_used)
#     table.add_row(["Used Disk (Windows)", "", f"{windows_disk_used} GB", f"{api_windows_disk_used} GB", used_disk_status])
#
#     windows_disk_free = windows_disk_data['disk_free']
#     api_windows_disk_free = api_data.get('disk_free', None)
#     free_disk_status = compare_values(windows_disk_free, api_windows_disk_free)
#     table.add_row(["Free Disk (Windows)", "", f"{windows_disk_free} GB", f"{api_windows_disk_free} GB", free_disk_status])
#
#     print(table)
#     return table
#
# def generate_html_report(table):
#     # Load Jinja2 template
#     env = Environment(loader=FileSystemLoader('.'))
#     template = env.get_template('report_template.html')  # Your HTML template file
#
#     # Generate HTML content
#     html_content = template.render(table=table)
#
#     # Save to a file
#     with open('report.html', 'w') as f:
#         f.write(html_content)
#
#     print("HTML report generated: report.html")
#
# # Main execution
# if __name__ == "__main__":
#     print("Fetching disk data from Linux server...")
#     linux_data = fetch_linux_disk_data()
#     print(linux_data)
#
#     print("Fetching disk data from API...")
#     api_data = fetch_api_data()
#     print(api_data)
#
#     if api_data:
#         print("Generating report...")
#         table = generate_report(linux_data, None, api_data)
#         generate_html_report(table)
#
#     print("Fetching disk data from Windows server...")
#     windows_data = fetch_windows_disk_data()
#     print(windows_data)
#
#     print("Generating Windows report...")
#     table = generate_report(None, windows_data, api_data)
#     generate_html_report(table)


import requests
from prettytable import PrettyTable
from jinja2 import Environment, FileSystemLoader
import psutil  # Import psutil for Windows disk data retrieval

# Define server connection details for Windows
windows_hostname = '10.192.1.77'
windows_username = 'tulsiram'
windows_password = 'nMuZ3XcF87zq4tsG65NfkA'

# API details
api_url = 'https://staging-api-zoomview.zybisys.com/saas-zoomview/api/v1/infra/infra-livestate'  # Replace with your API endpoint

# Fetch disk data for Windows
def fetch_windows_disk_data():
    # Get disk usage for the C: drive
    disk_usage = psutil.disk_usage('C:/')
    total = disk_usage.total / (1024 ** 3)  # Convert bytes to GB
    used = disk_usage.used / (1024 ** 3)    # Convert bytes to GB
    free = disk_usage.free / (1024 ** 3)    # Convert bytes to GB
    return {
        "disk_total": round(total, 2),
        "disk_used": round(used, 2),
        "disk_free": round(free, 2),
    }

# Fetch disk data from API
def fetch_api_data():
    payload = {'host_name': 'ZCS-SERVER', 'service_name': 'disk'}
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzMwNzkyMjc3ODE0LCJpYXQiOjE3MzA3OTIyNzcsImV4cCI6MTczMDg3ODY3N30.GtL77IGMqmQuXqcjdETjKSeoe2hyrTwyqOPJajmZhycnShelxFIdX5mQucVGCm1Y8Yvmqye58ONp7iybE66ZjQ"  # Replace with your actual token
    }
    response = requests.get(url=api_url, params=payload, headers=headers)
    if response.status_code == 200:
        api_data = response.json()
        api_data2 = api_data['message']

        disk_data = {}
        for serviceData in api_data2:
            service_data = serviceData['service_data']
            for service_data2 in service_data:
                if service_data2['metrix_name'] == 'disk_used':
                    disk_data['disk_used'] = float(service_data2['metrix_value'])
                if service_data2['metrix_name'] == 'disk_total':
                    disk_data['disk_total'] = float(service_data2['metrix_value'])
                if service_data2['metrix_name'] == 'disk_free':
                    disk_data['disk_free'] = float(service_data2['metrix_value'])

        return disk_data
    else:
        print(f"API Request Failed: {response.status_code}")
        return None

# Compare SSH and API values
def compare_values(ssh_value, api_value):
    if api_value is None:
        return "fail"  # If API value is missing, mark as fail
    difference = abs(ssh_value - api_value) / ssh_value * 100
    if difference <= 10:
        return "pass"
    elif difference > 20:
        return "fail"
    else:
        return "pass with warning"  # Could be used if needed

# Generate report
def generate_report(windows_data, api_data):
    table = PrettyTable()
    table.field_names = ["Metrics", "Windows Value", "API Value", "Status"]

    # Windows Disk Report
    windows_disk_total = windows_data['disk_total']
    api_windows_disk_total = api_data.get('disk_total', None)
    total_disk_status = compare_values(windows_disk_total, api_windows_disk_total)
    table.add_row(["Total Disk (Windows)", f"{windows_disk_total} GB", f"{api_windows_disk_total} GB", total_disk_status])

    windows_disk_used = windows_data['disk_used']
    api_windows_disk_used = api_data.get('disk_used', None)
    used_disk_status = compare_values(windows_disk_used, api_windows_disk_used)
    table.add_row(["Used Disk (Windows)", f"{windows_disk_used} GB", f"{api_windows_disk_used} GB", used_disk_status])

    windows_disk_free = windows_data['disk_free']
    api_windows_disk_free = api_data.get('disk_free', None)
    free_disk_status = compare_values(windows_disk_free, api_windows_disk_free)
    table.add_row(["Free Disk (Windows)", f"{windows_disk_free} GB", f"{api_windows_disk_free} GB", free_disk_status])

    print(table)
    return table

def generate_html_report(table):
    # Load Jinja2 template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('report_template1.html')  # Your HTML template file

    # Generate HTML content
    html_content = template.render(table=table)

    # Save to a file
    with open('report.html', 'w') as f:
        f.write(html_content)

    print("HTML report generated: report.html")

# Main execution
if __name__ == "__main__":
    print("Fetching disk data from Windows server...")
    windows_data = fetch_windows_disk_data()
    print(windows_data)

    print("Fetching disk data from API...")
    api_data = fetch_api_data()
    print(api_data)

    if api_data:
        print("Generating report...")
        table = generate_report(windows_data, api_data)
        generate_html_report(table)
    else:
        print("Failed to fetch API data.")




