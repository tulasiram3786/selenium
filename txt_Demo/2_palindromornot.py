


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


#nice code but only 1 table

# import paramiko
# import requests
# from prettytable import PrettyTable
# from jinja2 import Environment, FileSystemLoader
# import psutil  # Import psutil for Windows disk data retrieval
#
# #Define server connection details for Linux
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
#
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
#
# # Fetch disk data via SSH (Linux)
# def fetch_linux_disk_data():
#     disk_command = "df -B1 / | awk 'NR==2{printf \"%s %s %s\", $2, $3, $4}'"
#     disk_usage = execute_remote_command(disk_command, linux_hostname, linux_port, linux_username,
#                                         linux_password).split()
#     disk_total, disk_used, disk_free = map(int, disk_usage)
#
#     return {
#         "disk_total": round(disk_total / 1e9, 2),  # Convert to GB
#         "disk_used": round(disk_used / 1e9, 2),  # Convert to GB
#         "disk_free": round(disk_free / 1e9, 2),  # Convert to GB
#     }
#
#
# # Fetch disk data for Windows
# def fetch_windows_disk_data():
#     disk_usage = psutil.disk_usage('C:/')
#     total = disk_usage.total / (1024 ** 3)  # Convert bytes to GB
#     used = disk_usage.used / (1024 ** 3)  # Convert bytes to GB
#     free = disk_usage.free / (1024 ** 3)  # Convert bytes to GB
#     return {
#         "disk_total": round(total, 2),
#         "disk_used": round(used, 2),
#         "disk_free": round(free, 2),
#     }
#
#
# # Fetch disk data from API
# def fetch_api_data(host_name):
#     payload = {'host_name': host_name, 'service_name': 'disk'}
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
#
# # Generate report
# def generate_report(linux_data, windows_data, api_data_linux, api_data_windows):
#     table = PrettyTable()
#     table.field_names = ["Metrics", "Linux Value", "Windows Value", "API Value (Linux)", "API Value (Windows)",
#                          "Status"]
#
#     # Linux Disk Report
#     linux_disk_total = linux_data['disk_total']
#     api_linux_disk_total = api_data_linux.get('disk_total', None)
#     total_linux_disk_status = compare_values(linux_disk_total, api_linux_disk_total)
#
#     windows_disk_total = windows_data['disk_total']
#     api_windows_disk_total = api_data_windows.get('disk_total', None)
#     total_windows_disk_status = compare_values(windows_disk_total, api_windows_disk_total)
#
#     table.add_row(["Total Disk", f"{linux_disk_total} GB", f"{windows_disk_total} GB", f"{api_linux_disk_total} GB",
#                    f"{api_windows_disk_total} GB", total_linux_disk_status + " / " + total_windows_disk_status])
#
#     # Used Disk Report
#     linux_disk_used = linux_data['disk_used']
#     api_linux_disk_used = api_data_linux.get('disk_used', None)
#     used_linux_disk_status = compare_values(linux_disk_used, api_linux_disk_used)
#
#     windows_disk_used = windows_data['disk_used']
#     api_windows_disk_used = api_data_windows.get('disk_used', None)
#     used_windows_disk_status = compare_values(windows_disk_used, api_windows_disk_used)
#
#     table.add_row(["Used Disk", f"{linux_disk_used} GB", f"{windows_disk_used} GB", f"{api_linux_disk_used} GB",
#                    f"{api_windows_disk_used} GB", used_linux_disk_status + " / " + used_windows_disk_status])
#
#     # Free Disk Report
#     linux_disk_free = linux_data['disk_free']
#     api_linux_disk_free = api_data_linux.get('disk_free', None)
#     free_linux_disk_status = compare_values(linux_disk_free, api_linux_disk_free)
#
#     windows_disk_free = windows_data['disk_free']
#     api_windows_disk_free = api_data_windows.get('disk_free', None)
#     free_windows_disk_status = compare_values(windows_disk_free, api_windows_disk_free)
#
#     table.add_row(["Free Disk", f"{linux_disk_free} GB", f"{windows_disk_free} GB", f"{api_linux_disk_free} GB",
#                    f"{api_windows_disk_free} GB", free_linux_disk_status + " / " + free_windows_disk_status])
#
#     print(table)
#     return table
#
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
#
# # Main execution
# if __name__ == "__main__":
#     # Fetch Linux disk data
#     print("Fetching disk data from Linux server...")
#     linux_data = fetch_linux_disk_data()
#     print(linux_data)
#
#     print("Fetching disk data from API for Linux...")
#     api_data_linux = fetch_api_data('zcsit')
#     print(api_data_linux)
#
#     # Fetch Windows disk data
#     print("Fetching disk data from Windows server...")
#     windows_data = fetch_windows_disk_data()
#     print(windows_data)
#
#     print("Fetching disk data from API for Windows...")
#     api_data_windows = fetch_api_data('ZCS-SERVER')
#     print(api_data_windows)
#
#     if api_data_linux and api_data_windows:
#         print("Generating report...")
#         table = generate_report(linux_data, windows_data, api_data_linux, api_data_windows)
#         generate_html_report(table)
#     else:
#         print("Failed to fetch API data.")


#good working
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
#
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
#
# # Fetch disk data via SSH (Linux)
# def fetch_linux_disk_data():
#     disk_command = "df -B1 / | awk 'NR==2{printf \"%s %s %s\", $2, $3, $4}'"
#     disk_usage = execute_remote_command(disk_command, linux_hostname, linux_port, linux_username,
#                                         linux_password).split()
#     disk_total, disk_used, disk_free = map(int, disk_usage)
#
#     return {
#         "disk_total": round(disk_total / 1e9, 2),  # Convert to GB
#         "disk_used": round(disk_used / 1e9, 2),    # Convert to GB
#         "disk_free": round(disk_free / 1e9, 2),    # Convert to GB
#     }
#
#
# # Fetch disk data for Windows
# def fetch_windows_disk_data():
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
#
# # Fetch disk data from API
# def fetch_api_data(host_name):
#     payload = {'host_name': host_name, 'service_name': 'disk'}
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI5MTY1MTY5Mjc4LCJpYXQiOjE3MjkxNjUxNjksImV4cCI6MTcyOTI1MTU2OX0.c0CKP9YlMYH2CVs61VgpAvTk0QkaHpf0jBOCv5jVK7rNa84RNVoC4knLPJ70bz1_CFJiF1lF9t-rIKZ-RJQZog"  # Replace with your actual token
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
#
# # Generate report
# def generate_report(linux_data, windows_data, api_data_linux, api_data_windows):
#     report_data = []
#
#     # Linux Disk Report
#     total_linux_disk_status = compare_values(linux_data['disk_total'], api_data_linux.get('disk_total', None))
#     report_data.append([
#         "Total Disk",
#         f"{linux_data['disk_total']} GB",
#         f"{windows_data['disk_total']} GB",
#         f"{api_data_linux.get('disk_total', None)} GB",
#         f"{api_data_windows.get('disk_total', None)} GB",
#         total_linux_disk_status + " / " + compare_values(windows_data['disk_total'], api_data_windows.get('disk_total', None))
#     ])
#
#     # Used Disk Report
#     used_linux_disk_status = compare_values(linux_data['disk_used'], api_data_linux.get('disk_used', None))
#     report_data.append([
#         "Used Disk",
#         f"{linux_data['disk_used']} GB",
#         f"{windows_data['disk_used']} GB",
#         f"{api_data_linux.get('disk_used', None)} GB",
#         f"{api_data_windows.get('disk_used', None)} GB",
#         used_linux_disk_status + " / " + compare_values(windows_data['disk_used'], api_data_windows.get('disk_used', None))
#     ])
#
#     # Free Disk Report
#     free_linux_disk_status = compare_values(linux_data['disk_free'], api_data_linux.get('disk_free', None))
#     report_data.append([
#         "Free Disk",
#         f"{linux_data['disk_free']} GB",
#         f"{windows_data['disk_free']} GB",
#         f"{api_data_linux.get('disk_free', None)} GB",
#         f"{api_data_windows.get('disk_free', None)} GB",
#         free_linux_disk_status + " / " + compare_values(windows_data['disk_free'], api_data_windows.get('disk_free', None))
#     ])
#
#     return report_data  # Return a list of rows instead
#
#
# def generate_html_report(report_data):
#     # Load Jinja2 template
#     env = Environment(loader=FileSystemLoader('.'))
#     template = env.get_template('report_template1.html')  # Your HTML template file
#
#     # Generate HTML content
#     html_content = template.render(rows=report_data)  # Pass rows instead
#
#     # Save to a file
#     with open('report.html', 'w') as f:
#         f.write(html_content)
#
#     print("HTML report generated: report.html")
#
#
# # Main execution
# if __name__ == "__main__":
#     # Fetch Linux disk data
#     print("Fetching disk data from Linux server...")
#     linux_data = fetch_linux_disk_data()
#     print(linux_data)
#
#     print("Fetching disk data from API for Linux...")
#     api_data_linux = fetch_api_data('zcsit')
#     print(api_data_linux)
#
#     # Fetch Windows disk data
#     print("Fetching disk data from Windows server...")
#     windows_data = fetch_windows_disk_data()
#     print(windows_data)
#
#     print("Fetching disk data from API for Windows...")
#     api_data_windows = fetch_api_data('ZCS-SERVER')
#     print(api_data_windows)
#
#     if api_data_linux and api_data_windows:
#         print("Generating report...")
#         report_data = generate_report(linux_data, windows_data, api_data_linux, api_data_windows)
#         generate_html_report(report_data)
#     else:
#         print("Failed to fetch API data.")

#super duper code

import paramiko
import requests
from prettytable import PrettyTable
from jinja2 import Environment, FileSystemLoader
import psutil

# Define server connection details for Linux
linux_hostname = '192.168.1.81'
linux_port = 20202
linux_username = 'tulasi'
linux_password = 'Nop@ssw0rd'

# Define server connection details for Windows
windows_hostname = '10.192.1.77'
windows_username = 'tulsiram'
windows_password = 'nMuZ3XcF87zq4tsG65NfkA'

# API details
api_url = 'https://staging-api-zoomview.zybisys.com/saas-zoomview/api/v1/infra/infra-livestate'

def execute_remote_command(command, hostname, port, username, password):
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

# Fetch disk data via SSH (Linux)
def fetch_linux_disk_data():
    disk_command = "df -B1 / | awk 'NR==2{printf \"%s %s %s\", $2, $3, $4}'"
    disk_usage = execute_remote_command(disk_command, linux_hostname, linux_port, linux_username,
                                        linux_password).split()
    disk_total, disk_used, disk_free = map(int, disk_usage)

    return {
        "disk_total": round(disk_total / 1e9, 2),  # Convert to GB
        "disk_used": round(disk_used / 1e9, 2),  # Convert to GB
        "disk_free": round(disk_free / 1e9, 2),  # Convert to GB
    }

# Fetch disk data for Windows
def fetch_windows_disk_data():
    disk_usage = psutil.disk_usage('C:/')
    total = disk_usage.total / (1024 ** 3)  # Convert bytes to GB
    used = disk_usage.used / (1024 ** 3)  # Convert bytes to GB
    free = disk_usage.free / (1024 ** 3)  # Convert bytes to GB
    return {
        "disk_total": round(total, 2),
        "disk_used": round(used, 2),
        "disk_free": round(free, 2),
    }

# Fetch disk data from API
def fetch_api_data(host_name):
    payload = {'host_name': host_name, 'service_name': 'disk'}
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
        return "pass with warning"

# Convert PrettyTable to a list of dictionaries
def convert_table_to_list(table):
    return [dict(zip(table.field_names, row)) for row in table.rows]

# Generate report
def generate_report(linux_data, windows_data, api_data_linux, api_data_windows):
    linux_table = PrettyTable()
    linux_table.field_names = ["Metrics", "Linux Value", "API Value", "Status"]

    windows_table = PrettyTable()
    windows_table.field_names = ["Metrics", "Windows Value", "API Value", "Status"]

    # Linux Disk Report
    linux_disk_total = linux_data['disk_total']
    api_linux_disk_total = api_data_linux.get('disk_total', None)
    total_linux_disk_status = compare_values(linux_disk_total, api_linux_disk_total)

    linux_table.add_row(["Total Disk", f"{linux_disk_total} GB", f"{api_linux_disk_total} GB", total_linux_disk_status])

    linux_disk_used = linux_data['disk_used']
    api_linux_disk_used = api_data_linux.get('disk_used', None)
    used_linux_disk_status = compare_values(linux_disk_used, api_linux_disk_used)

    linux_table.add_row(["Used Disk", f"{linux_disk_used} GB", f"{api_linux_disk_used} GB", used_linux_disk_status])

    linux_disk_free = linux_data['disk_free']
    api_linux_disk_free = api_data_linux.get('disk_free', None)
    free_linux_disk_status = compare_values(linux_disk_free, api_linux_disk_free)

    linux_table.add_row(["Free Disk", f"{linux_disk_free} GB", f"{api_linux_disk_free} GB", free_linux_disk_status])

    # Windows Disk Report
    windows_disk_total = windows_data['disk_total']
    api_windows_disk_total = api_data_windows.get('disk_total', None)
    total_windows_disk_status = compare_values(windows_disk_total, api_windows_disk_total)

    windows_table.add_row(["Total Disk", f"{windows_disk_total} GB", f"{api_windows_disk_total} GB", total_windows_disk_status])

    windows_disk_used = windows_data['disk_used']
    api_windows_disk_used = api_data_windows.get('disk_used', None)
    used_windows_disk_status = compare_values(windows_disk_used, api_windows_disk_used)

    windows_table.add_row(["Used Disk", f"{windows_disk_used} GB", f"{api_windows_disk_used} GB", used_windows_disk_status])

    windows_disk_free = windows_data['disk_free']
    api_windows_disk_free = api_data_windows.get('disk_free', None)
    free_windows_disk_status = compare_values(windows_disk_free, api_windows_disk_free)

    windows_table.add_row(["Free Disk", f"{windows_disk_free} GB", f"{api_windows_disk_free} GB", free_windows_disk_status])

    return convert_table_to_list(linux_table), convert_table_to_list(windows_table)


def generate_html_report(linux_table, windows_table):
    # Load Jinja2 template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('report_template1.html')

    # Generate HTML content
    html_content = template.render(linux_table=linux_table, windows_table=windows_table)

    # Save to a file
    with open('report.html', 'w') as f:
        f.write(html_content)

    print("HTML report generated: report.html")


# Main execution
if __name__ == "__main__":
    # Fetch Linux disk data
    print("Fetching disk data from Linux server...")
    linux_data = fetch_linux_disk_data()
    print(linux_data)

    print("Fetching disk data from API for Linux...")
    api_data_linux = fetch_api_data('zcsit')
    print(api_data_linux)

    # Fetch Windows disk data
    print("Fetching disk data from Windows server...")
    windows_data = fetch_windows_disk_data()
    print(windows_data)

    print("Fetching disk data from API for Windows...")
    api_data_windows = fetch_api_data('ZCS-SERVER')
    print(api_data_windows)

    if api_data_linux and api_data_windows:
        print("Generating report...")
        linux_table, windows_table = generate_report(linux_data, windows_data, api_data_linux, api_data_windows)
        generate_html_report(linux_table, windows_table)
    else:
        print("Failed to fetch API data.")













