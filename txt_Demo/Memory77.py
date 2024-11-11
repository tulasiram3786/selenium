# import requests
# from prettytable import PrettyTable
# from jinja2 import Environment, FileSystemLoader
# import os
# import winrm  # For connecting to the Windows server
#
# # Server connection details
# windows_hostname = '10.192.1.77'  # Replace with your Windows server IP
# username = 'tulsiram'  # Replace with your Windows server username
# password = 'nMuZ3XcF87zq4tsG65NfkA'  # Replace with your Windows server password
#
# # API details
# api_url = 'https://staging-api-zoomview.zybisys.com/saas-zoomview/api/v1/infra/infra-livestate'
#
# # Create a session to connect to the Windows server
# session = winrm.Session(f'http://{windows_hostname}:5985/wsman', auth=(username, password), transport='ntlm')
#
# # PowerShell command to fetch CPU usage
# cpu_command = """
# Get-WmiObject -Query "SELECT LoadPercentage FROM Win32_Processor" |
# ForEach-Object { $_.LoadPercentage }
# """
#
# # PowerShell command to fetch memory usage
# memory_command = """
# $mem = Get-CimInstance -ClassName Win32_OperatingSystem
# @{
#     TotalMemoryGB = [math]::round($mem.TotalVisibleMemorySize / 1MB, 2)
#     FreeMemoryGB = [math]::round($mem.FreePhysicalMemory / 1MB, 2)
#     UsedMemoryGB = [math]::round(($mem.TotalVisibleMemorySize - $mem.FreePhysicalMemory) / 1MB, 2)
# }
# """
#
#
# # Function to execute commands on Windows server
# def execute_windows_command(command):
#     try:
#         result = session.run_ps(command)
#         output = result.std_out.decode('utf-8').strip()
#         return output
#     except Exception as e:
#         print(f"Failed to connect or execute command: {e}")
#         return None
#
#
# # Function to fetch system data from Windows server (CPU and memory)
# def fetch_windows_system_data():
#     print("Fetching CPU usage from Windows server...")
#     cpu_usage = execute_windows_command(cpu_command)
#
#     print("Fetching memory usage from Windows server...")
#     memory_usage = execute_windows_command(memory_command)
#
#     # Debug print for memory_usage to see if it contains the expected data
#     print("Memory usage raw output:", memory_usage)
#
#     # Parsing the memory data manually as it's a dictionary-like output with spaces
#     if memory_usage:
#         memory_lines = memory_usage.splitlines()
#         memory_data = {}
#         for line in memory_lines:
#             if 'TotalMemoryGB' in line:
#                 memory_data['TotalMemoryGB'] = float(line.split()[-1])  # Last part is the value
#             elif 'FreeMemoryGB' in line:
#                 memory_data['FreeMemoryGB'] = float(line.split()[-1])  # Last part is the value
#             elif 'UsedMemoryGB' in line:
#                 memory_data['UsedMemoryGB'] = float(line.split()[-1])  # Last part is the value
#
#         ram_total = memory_data['TotalMemoryGB']
#         ram_used = memory_data['UsedMemoryGB']
#         ram_free = memory_data['FreeMemoryGB']
#         ram_free_bytes = ram_free * 1024 ** 3  # Convert to bytes
#
#         return {
#             "ram_total": round(ram_total, 2),
#             "ram_used": round(ram_used, 2),
#             "ram_free_bytes": round(ram_free_bytes),
#             "cpu_usage": cpu_usage
#         }
#     else:
#         return None
#
#
# # Function to fetch API data
# def fetch_api_data():
#     payload = {'host_name': 'ZCS-SERVER', 'service_name': 'ram'}
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI5MDU4MTY2ODU1LCJpYXQiOjE3MjkwNTgxNjYsImV4cCI6MTcyOTE0NDU2Nn0.SORIz8sCOjPenGt1Hj6eIsgChwiUXQ4lBPj5jgd3oQuzdGD5XnXmDs6p1VcwLpItLpGG0-dF8ZpEcL93BqgjVg"
#     }
#     response = requests.get(url=api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()
#         api_data2 = api_data['message']
#
#         ram_data = {}
#         for serviceData in api_data2:
#             service_data = serviceData['service_data']
#             for service_data2 in service_data:
#                 if service_data2['metrix_name'] == 'ram_used':
#                     ram_data['ram_used'] = float(service_data2['metrix_value'])
#                 if service_data2['metrix_name'] == 'ram_total':
#                     ram_data['ram_total'] = float(service_data2['metrix_value'])
#                 if service_data2['metrix_name'] == 'ram_free_bytes':
#                     ram_data['ram_free_bytes'] = float(service_data2['metrix_value'])
#
#         return ram_data
#     else:
#         print(f"API Request Failed: {response.status_code}")
#         return None
#
#
# # Function to compare system and API values
# def compare_values(ssh_value, api_value):
#     if api_value is None:
#         return "fail"
#     difference = abs(ssh_value - api_value) / ssh_value * 100
#     if difference <= 10:
#         return "passed"
#     else:
#         return "failed"
#
#
# # Function to generate report
# def generate_report(ssh_data, api_data):
#     table = PrettyTable()
#     table.field_names = ["Metrics", "SSH Value", "API Value", "Status"]
#
#     report_data = []
#
#     ssh_ram_total = ssh_data['ram_total']
#     api_ram_total = api_data.get('ram_total', None)
#     total_memory_status = compare_values(ssh_ram_total, api_ram_total)
#     report_data.append({
#         "metric": "Total Memory",
#         "ssh_value": f"{ssh_ram_total} GB",
#         "api_value": f"{api_ram_total} GB",
#         "status": total_memory_status
#     })
#
#     ssh_ram_used = ssh_data['ram_used']
#     api_ram_used = api_data.get('ram_used', None)
#     used_memory_status = compare_values(ssh_ram_used, api_ram_used)
#     report_data.append({
#         "metric": "Used Memory",
#         "ssh_value": f"{ssh_ram_used} GB",
#         "api_value": f"{api_ram_used} GB",
#         "status": used_memory_status
#     })
#
#     ssh_ram_free_bytes = ssh_data['ram_free_bytes']
#     api_ram_free_bytes = api_data.get('ram_free_bytes', None)
#     free_memory_status = compare_values(ssh_ram_free_bytes / 1e9, api_ram_free_bytes / 1e9)
#     report_data.append({
#         "metric": "Free Memory",
#         "ssh_value": f"{ssh_ram_free_bytes / 1e9:.2f} GB",
#         "api_value": f"{api_ram_free_bytes / 1e9:.2f} GB",
#         "status": free_memory_status
#     })
#
#     for row in report_data:
#         table.add_row([row['metric'], row['ssh_value'], row['api_value'], row['status']])
#
#     print(table)
#     return report_data
#
#
# # Function to generate HTML report
# def generate_html_report(report_data):
#     env = Environment(loader=FileSystemLoader('.'))
#     template = env.get_template('report_template.html')
#
#     total_tests = len(report_data)
#     pass_count = sum(1 for row in report_data if row['status'] == "passed")
#     fail_count = total_tests - pass_count
#
#     pass_percentage = (pass_count / total_tests) * 100
#     fail_percentage = (fail_count / total_tests) * 100
#
#     html_content = template.render(
#         table=report_data,
#         pass_percentage=round(pass_percentage, 2),
#         fail_percentage=round(fail_percentage, 2)
#     )
#
#     with open('report.html', 'w') as f:
#         f.write(html_content)
#
#     print("HTML report generated: report.html")
#
#
# # Main execution
# if __name__ == "__main__":
#     print("Fetching system data from Windows Server...")
#     windows_data = fetch_windows_system_data()
#     print(windows_data)
#
#     print("Fetching system data from API...")
#     api_data = fetch_api_data()
#     print(api_data)
#
#     if api_data and windows_data:
#         print("Generating report...")
#         report_data = generate_report(windows_data, api_data)
#         generate_html_report(report_data)
#     else:
#         print("Failed to fetch necessary data.")

# import winrm
#
# # Server connection details
# windows_hostname = '10.192.1.77'  # Replace with your Windows server IP
# username = 'tulsiram'             # Replace with your Windows server username
# password = 'nMuZ3XcF87zq4tsG65NfkA'         # Replace with your Windows server password
#
# # Create a session to connect to the Windows server
# session = winrm.Session(f'http://{windows_hostname}:5985/wsman', auth=(username, password), transport='ntlm')
#
# # PowerShell command to fetch CPU usage
# cpu_command = """
# Get-WmiObject -Query "SELECT LoadPercentage FROM Win32_Processor" |
# ForEach-Object { $_.LoadPercentage }
# """
#
# # PowerShell command to fetch memory usage
# memory_command = """
# $mem = Get-CimInstance -ClassName Win32_OperatingSystem
# @{
#     TotalMemoryGB = [math]::round($mem.TotalVisibleMemorySize / 1MB, 2)
#     FreeMemoryGB = [math]::round($mem.FreePhysicalMemory / 1MB, 2)
#     UsedMemoryGB = [math]::round(($mem.TotalVisibleMemorySize - $mem.FreePhysicalMemory) / 1MB, 2)
# }
# """
#
# def fetch_cpu_usage():
#     try:
#         result = session.run_ps(cpu_command)
#         cpu_usage = result.std_out.decode('utf-8').strip()
#         print(f"CPU Usage: {cpu_usage}%")
#         return cpu_usage
#     except Exception as e:
#         print(f"Failed to fetch CPU usage: {e}")
#         return None
#
# def fetch_memory_usage():
#     try:
#         result = session.run_ps(memory_command)
#         memory_usage = result.std_out.decode('utf-8').strip()
#         print(f"Memory Usage: {memory_usage}")
#         return memory_usage
#     except Exception as e:
#         print(f"Failed to fetch memory usage: {e}")
#         return None
#
# # Fetch and print CPU and memory usage
# if __name__ == "__main__":
#     print("Fetching CPU usage from Windows server...")
#     cpu_usage = fetch_cpu_usage()
#
#     print("Fetching memory usage from Windows server...")
#     memory_usage = fetch_memory_usage()



#---------------

# import requests
# from prettytable import PrettyTable
# from jinja2 import Environment, FileSystemLoader
# import os
# import winrm  # For connecting to the Windows server
# import paramiko  # For connecting to the Linux server
#
# # Server connection details for Windows
# windows_hostname = '10.192.1.77'  # Replace with your Windows server IP
# windows_username = 'tulsiram'  # Replace with your Windows server username
# windows_password = 'nMuZ3XcF87zq4tsG65NfkA'  # Replace with your Windows server password
#
# # Server connection details for Linux
# linux_hostname = '192.168.1.81'  # Replace with your Linux server IP
# linux_port = 20202  # Replace with your Linux server SSH port
# linux_username = 'tulasi'  # Replace with your Linux server username
# linux_password = 'Nop@ssw0rd'  # Replace with your Linux server password
#
# # API details
# api_url = 'https://staging-api-zoomview.zybisys.com/saas-zoomview/api/v1/infra/infra-livestate'  # Replace with your API endpoint
# api_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI5MDU4MTY2ODU1LCJpYXQiOjE3MjkwNTgxNjYsImV4cCI6MTcyOTE0NDU2Nn0.SORIz8sCOjPenGt1Hj6eIsgChwiUXQ4lBPj5jgd3oQuzdGD5XnXmDs6p1VcwLpItLpGG0-dF8ZpEcL93BqgjVg"  # Replace with your valid API token
#
# # Windows Commands
# windows_cpu_command = """
# Get-WmiObject -Query "SELECT LoadPercentage FROM Win32_Processor" |
# ForEach-Object { $_.LoadPercentage }
# """
#
# windows_memory_command = """
# $mem = Get-CimInstance -ClassName Win32_OperatingSystem
# @{
#     TotalMemoryGB = [math]::round($mem.TotalVisibleMemorySize / 1MB, 2)
#     FreeMemoryGB = [math]::round($mem.FreePhysicalMemory / 1MB, 2)
#     UsedMemoryGB = [math]::round(($mem.TotalVisibleMemorySize - $mem.FreePhysicalMemory) / 1MB, 2)
# }
# """
#
#
# # Function to execute Windows commands
# def execute_windows_command(command):
#     session = winrm.Session(f'http://{windows_hostname}:5985/wsman', auth=(windows_username, windows_password),
#                             transport='ntlm')
#     try:
#         result = session.run_ps(command)
#         return result.std_out.decode('utf-8').strip()
#     except Exception as e:
#         print(f"Failed to connect to Windows server: {e}")
#         return None
#
#
# # Fetch system data from Windows server
# def fetch_windows_system_data():
#     print("Fetching CPU usage from Windows server...")
#     cpu_usage = execute_windows_command(windows_cpu_command)
#
#     print("Fetching memory usage from Windows server...")
#     memory_usage = execute_windows_command(windows_memory_command)
#
#     if memory_usage:
#         memory_data = {}
#         for line in memory_usage.splitlines():
#             if 'TotalMemoryGB' in line:
#                 memory_data['TotalMemoryGB'] = float(line.split()[-1])
#             elif 'FreeMemoryGB' in line:
#                 memory_data['FreeMemoryGB'] = float(line.split()[-1])
#             elif 'UsedMemoryGB' in line:
#                 memory_data['UsedMemoryGB'] = float(line.split()[-1])
#
#         ram_total = memory_data['TotalMemoryGB']
#         ram_used = memory_data['UsedMemoryGB']
#         ram_free_bytes = memory_data['FreeMemoryGB'] * 1024 ** 3
#
#         return {
#             "ram_total": round(ram_total, 2),
#             "ram_used": round(ram_used, 2),
#             "ram_free_bytes": round(ram_free_bytes),
#             "cpu_usage": cpu_usage
#         }
#     else:
#         return None
#
#
# # Function to execute Linux commands
# def execute_linux_command(command):
#     try:
#         client = paramiko.SSHClient()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect(linux_hostname, port=linux_port, username=linux_username, password=linux_password)
#         stdin, stdout, stderr = client.exec_command(command)
#         output = stdout.read().decode('utf-8')
#         client.close()
#         return output.strip()
#     except Exception as e:
#         print(f"Failed to connect to Linux server: {e}")
#         return None
#
#
# # Fetch system data from Linux server
# def fetch_linux_system_data():
#     cpu_command = "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'"
#     memory_command = "free -m | awk 'NR==2{printf \"%s %s %s %.2f\", $2,$3,$4,$3*100/$2 }'"
#
#     print("Fetching CPU usage from Linux server...")
#     cpu_usage = execute_linux_command(cpu_command)
#
#     print("Fetching memory usage from Linux server...")
#     memory_usage = execute_linux_command(memory_command).split()
#     ram_total, ram_used, ram_free, ram_percent_used = map(float, memory_usage)
#     ram_free_bytes = ram_free * 1000 * 1000
#
#     return {
#         "ram_total": round(ram_total / 1000, 2),
#         "ram_used": round(ram_used / 1000, 2),
#         "ram_free_bytes": round(ram_free_bytes)
#     }
#
#
# # Fetch API data
# def fetch_api_data():
#     payload = {'host_name': 'zcsit', 'service_name': 'ram'}
#     headers = {
#         "Authorization": f"Bearer {api_token}"
#     }
#     response = requests.get(api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()['message']
#         ram_data = {}
#         for serviceData in api_data:
#             for service_data in serviceData['service_data']:
#                 if service_data['metrix_name'] == 'ram_used':
#                     ram_data['ram_used'] = float(service_data['metrix_value'])
#                 if service_data['metrix_name'] == 'ram_total':
#                     ram_data['ram_total'] = float(service_data['metrix_value'])
#                 if service_data['metrix_name'] == 'ram_free_bytes':
#                     ram_data['ram_free_bytes'] = float(service_data['metrix_value'])
#         return ram_data
#     else:
#         print(f"API Request Failed: {response.status_code}")
#         return None
#
#
# # Function to compare values
# def compare_values(ssh_value, api_value):
#     if api_value is None:
#         return "fail"
#     difference = abs(ssh_value - api_value) / ssh_value * 100
#     return "passed" if difference <= 10 else "failed"
#
#
# # Generate report
# def generate_report(ssh_data, api_data):
#     table = PrettyTable()
#     table.field_names = ["Metrics", "SSH Value", "API Value", "Status"]
#     report_data = []
#
#     for metric in ["ram_total", "ram_used", "ram_free_bytes"]:
#         ssh_value = ssh_data[metric]
#         api_value = api_data.get(metric)
#         status = compare_values(ssh_value, api_value)
#         report_data.append({
#             "metric": metric.replace("_", " ").capitalize(),
#             "ssh_value": f"{ssh_value / 1e9:.2f} GB" if "bytes" in metric else f"{ssh_value} GB",
#             "api_value": f"{api_value / 1e9:.2f} GB" if "bytes" in metric else f"{api_value} GB",
#             "status": status
#         })
#
#     for row in report_data:
#         table.add_row([row['metric'], row['ssh_value'], row['api_value'], row['status']])
#
#     print(table)
#     return report_data
#
#
# # Generate HTML report
# def generate_html_report(report_data):
#     env = Environment(loader=FileSystemLoader('.'))
#     template = env.get_template('report_template.html')
#
#     total_tests = len(report_data)
#     pass_count = sum(1 for row in report_data if row['status'] == "passed")
#     fail_count = total_tests - pass_count
#
#     html_content = template.render(
#         table=report_data,
#         pass_percentage=round((pass_count / total_tests) * 100, 2),
#         fail_percentage=round((fail_count / total_tests) * 100, 2)
#     )
#
#     with open('report.html', 'w') as f:
#         f.write(html_content)
#     print("HTML report generated: report.html")
#
#
# # Main execution
# if __name__ == "__main__":
#     print("Fetching data from Windows Server...")
#     windows_data = fetch_windows_system_data()
#     print(windows_data)
#
#     print("Fetching data from Linux Server...")
#     linux_data = fetch_linux_system_data()
#     print(linux_data)
#
#     print("Fetching system data from API...")
#     api_data = fetch_api_data()
#     print(api_data)
#
#     if windows_data and linux_data and api_data:
#         print("Generating report for Windows data...")
#         windows_report_data = generate_report(windows_data, api_data)
#
#         print("Generating report for Linux data...")
#         linux_report_data = generate_report(linux_data, api_data)
#
#         # Combine both reports and generate final HTML report
#         full_report_data = windows_report_data + linux_report_data
#         generate_html_report(full_report_data)
#     else:
#         print("Failed to fetch necessary data.")


#----------------

#Good working code but the problem is report not generating


# import requests
# from prettytable import PrettyTable
# from jinja2 import Environment, FileSystemLoader
# import os
# import winrm  # For connecting to the Windows server
# import paramiko  # For connecting to the Linux server
#
# # Server connection details for Windows
# windows_hostname = '10.192.1.77'  # Replace with your Windows server IP
# windows_username = 'tulsiram'  # Replace with your Windows server username
# windows_password = 'nMuZ3XcF87zq4tsG65NfkA'  # Replace with your Windows server password
#
# # Server connection details for Linux
# linux_hostname = '192.168.1.81'  # Replace with your Linux server IP
# linux_port = 20202  # Replace with your Linux server SSH port
# linux_username = 'tulasi'  # Replace with your Linux server username
# linux_password = 'Nop@ssw0rd'  # Replace with your Linux server password
#
# # API details
# api_url = 'https://staging-api-zoomview.zybisys.com/saas-zoomview/api/v1/infra/infra-livestate'  # Replace with your API endpoint
# api_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI5MDU4MTY2ODU1LCJpYXQiOjE3MjkwNTgxNjYsImV4cCI6MTcyOTE0NDU2Nn0.SORIz8sCOjPenGt1Hj6eIsgChwiUXQ4lBPj5jgd3oQuzdGD5XnXmDs6p1VcwLpItLpGG0-dF8ZpEcL93BqgjVg"  # Replace with your valid API token
#
# # Windows Commands
# windows_cpu_command = """
# Get-WmiObject -Query "SELECT LoadPercentage FROM Win32_Processor" |
# ForEach-Object { $_.LoadPercentage }
# """
#
# windows_memory_command = """
# $mem = Get-CimInstance -ClassName Win32_OperatingSystem
# @{
#     TotalMemoryGB = [math]::round($mem.TotalVisibleMemorySize / 1MB, 2)
#     FreeMemoryGB = [math]::round($mem.FreePhysicalMemory / 1MB, 2)
#     UsedMemoryGB = [math]::round(($mem.TotalVisibleMemorySize - $mem.FreePhysicalMemory) / 1MB, 2)
# }
# """
#
#
# # Function to execute Windows commands
# def execute_windows_command(command):
#     session = winrm.Session(f'http://{windows_hostname}:5985/wsman', auth=(windows_username, windows_password),
#                             transport='ntlm')
#     try:
#         result = session.run_ps(command)
#         return result.std_out.decode('utf-8').strip()
#     except Exception as e:
#         print(f"Failed to connect to Windows server: {e}")
#         return None
#
#
# # Fetch system data from Windows server
# def fetch_windows_system_data():
#     print("Fetching CPU usage from Windows server...")
#     cpu_usage = execute_windows_command(windows_cpu_command)
#
#     print("Fetching memory usage from Windows server...")
#     memory_usage = execute_windows_command(windows_memory_command)
#
#     if memory_usage:
#         memory_data = {}
#         for line in memory_usage.splitlines():
#             if 'TotalMemoryGB' in line:
#                 memory_data['TotalMemoryGB'] = float(line.split()[-1])
#             elif 'FreeMemoryGB' in line:
#                 memory_data['FreeMemoryGB'] = float(line.split()[-1])
#             elif 'UsedMemoryGB' in line:
#                 memory_data['UsedMemoryGB'] = float(line.split()[-1])
#
#         ram_total = memory_data['TotalMemoryGB']
#         ram_used = memory_data['UsedMemoryGB']
#         ram_free_bytes = memory_data['FreeMemoryGB'] * 1024 ** 3
#
#         return {
#             "ram_total": round(ram_total, 2),
#             "ram_used": round(ram_used, 2),
#             "ram_free_bytes": round(ram_free_bytes),
#             "cpu_usage": cpu_usage
#         }
#     else:
#         return None
#
#
# # Function to execute Linux commands
# def execute_linux_command(command):
#     try:
#         client = paramiko.SSHClient()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect(linux_hostname, port=linux_port, username=linux_username, password=linux_password)
#         stdin, stdout, stderr = client.exec_command(command)
#         output = stdout.read().decode('utf-8')
#         client.close()
#         return output.strip()
#     except Exception as e:
#         print(f"Failed to connect to Linux server: {e}")
#         return None
#
#
# # Fetch system data from Linux server
# def fetch_linux_system_data():
#     cpu_command = "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'"
#     memory_command = "free -m | awk 'NR==2{printf \"%s %s %s %.2f\", $2,$3,$4,$3*100/$2 }'"
#
#     print("Fetching CPU usage from Linux server...")
#     cpu_usage = execute_linux_command(cpu_command)
#
#     print("Fetching memory usage from Linux server...")
#     memory_usage = execute_linux_command(memory_command).split()
#     ram_total, ram_used, ram_free, ram_percent_used = map(float, memory_usage)
#     ram_free_bytes = ram_free * 1000 * 1000
#
#     return {
#         "ram_total": round(ram_total / 1000, 2),
#         "ram_used": round(ram_used / 1000, 2),
#         "ram_free_bytes": round(ram_free_bytes)
#     }
#
#
# # Fetch API data for each server
# def fetch_api_data(server_name):
#     payload = {'host_name': server_name, 'service_name': 'ram'}
#     headers = {
#         "Authorization": f"Bearer {api_token}"
#     }
#     response = requests.get(api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()['message']
#         ram_data = {}
#         for serviceData in api_data:
#             for service_data in serviceData['service_data']:
#                 if service_data['metrix_name'] == 'ram_used':
#                     ram_data['ram_used'] = float(service_data['metrix_value'])
#                 if service_data['metrix_name'] == 'ram_total':
#                     ram_data['ram_total'] = float(service_data['metrix_value'])
#                 if service_data['metrix_name'] == 'ram_free_bytes':
#                     ram_data['ram_free_bytes'] = float(service_data['metrix_value'])
#         return ram_data
#     else:
#         print(f"API Request Failed: {response.status_code}")
#         return None
#
#
# # Function to compare values
# def compare_values(ssh_value, api_value):
#     if api_value is None:
#         return "fail"
#     difference = abs(ssh_value - api_value) / ssh_value * 100
#     return "passed" if difference <= 10 else "failed"
#
#
# # Generate report
# def generate_report(ssh_data, api_data):
#     table = PrettyTable()
#     table.field_names = ["Metrics", "SSH Value", "API Value", "Status"]
#     report_data = []
#
#     for metric in ["ram_total", "ram_used", "ram_free_bytes"]:
#         ssh_value = ssh_data[metric]
#         api_value = api_data.get(metric)
#         status = compare_values(ssh_value, api_value)
#         report_data.append({
#             "metric": metric.replace("_", " ").capitalize(),
#             "ssh_value": f"{ssh_value / 1e9:.2f} GB" if "bytes" in metric else f"{ssh_value} GB",
#             "api_value": f"{api_value / 1e9:.2f} GB" if "bytes" in metric else f"{api_value} GB",
#             "status": status
#         })
#
#     for row in report_data:
#         table.add_row([row['metric'], row['ssh_value'], row['api_value'], row['status']])
#
#     print(table)
#     return report_data
#
#
# # Generate HTML report
# def generate_html_report(windows_report_data, linux_report_data):
#     env = Environment(loader=FileSystemLoader('.'))
#     template = env.get_template('report_template.html')
#
#     windows_total_tests = len(windows_report_data)
#     windows_pass_count = sum(1 for row in windows_report_data if row['status'] == "passed")
#     windows_fail_count = windows_total_tests - windows_pass_count
#
#     linux_total_tests = len(linux_report_data)
#     linux_pass_count = sum(1 for row in linux_report_data if row['status'] == "passed")
#     linux_fail_count = linux_total_tests - linux_pass_count
#
#     html_content = template.render(
#         windows_table=windows_report_data,
#         linux_table=linux_report_data,
#         windows_pass_percentage=round((windows_pass_count / windows_total_tests) * 100, 2),
#         windows_fail_percentage=round((windows_fail_count / windows_total_tests) * 100, 2),
#         linux_pass_percentage=round((linux_pass_count / linux_total_tests) * 100, 2),
#         linux_fail_percentage=round((linux_fail_count / linux_total_tests) * 100, 2)
#     )
#
#     with open('report.html', 'w') as f:
#         f.write(html_content)
#     print("HTML report generated: report.html")
#
#
# # Main execution
# if __name__ == "__main__":
#     print("Fetching data from Windows Server...")
#     windows_data = fetch_windows_system_data()
#     print(windows_data)
#
#     print("Fetching data from Linux Server...")
#     linux_data = fetch_linux_system_data()
#     print(linux_data)
#
#     print("Fetching system data from API for Windows Server...")
#     windows_api_data = fetch_api_data('ZCS-SERVER')  # Replace with your Windows server name
#     print(windows_api_data)
#
#     print("Fetching system data from API for Linux Server...")
#     linux_api_data = fetch_api_data('zcsit')
#     print(linux_api_data)
#
#     # Generate reports for both servers
#     windows_report_data = generate_report(windows_data, windows_api_data)
#     linux_report_data = generate_report(linux_data, linux_api_data)
#
#     # Generate HTML report
#     generate_html_report(windows_report_data, linux_report_data)

#
import requests
from prettytable import PrettyTable
from jinja2 import Environment, FileSystemLoader
import os
import winrm  # For connecting to the Windows server
import paramiko  # For connecting to the Linux server
import datetime

# Server connection details for Windows
windows_hostname = '10.192.1.77'  # Replace with your Windows server IP
windows_username = 'tulsiram'  # Replace with your Windows server username
windows_password = 'nMuZ3XcF87zq4tsG65NfkA'  # Replace with your Windows server password

# Server connection details for Linux
linux_hostname = '192.168.1.81'  # Replace with your Linux server IP
linux_port = 20202  # Replace with your Linux server SSH port
linux_username = 'tulasi'  # Replace with your Linux server username
linux_password = 'Nop@ssw0rd'  # Replace with your Linux server password

# API details
api_url = 'https://staging-api-zoomview.zybisys.com/saas-zoomview/api/v1/infra/infra-livestate'  # Replace with your API endpoint
api_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzMwMDkxMzY3NzIxLCJpYXQiOjE3MzAwOTEzNjcsImV4cCI6MTczMDE3Nzc2N30.R7X-UqhpsSlE7mNg7S6lzsxZTJxGzgbQ7NvDPxWOrfM0GDmW6ZStN0LHiA0qSlEiV-mmSpNdoASUMI9YQaEzEA"  # Replace with your valid API token

# Windows Commands
windows_cpu_command = """
Get-WmiObject -Query "SELECT LoadPercentage FROM Win32_Processor" |
ForEach-Object { $_.LoadPercentage }
"""

windows_memory_command = """
$mem = Get-CimInstance -ClassName Win32_OperatingSystem
@{
    TotalMemoryGB = [math]::round($mem.TotalVisibleMemorySize / 1MB, 2)
    FreeMemoryGB = [math]::round($mem.FreePhysicalMemory / 1MB, 2)
    UsedMemoryGB = [math]::round(($mem.TotalVisibleMemorySize - $mem.FreePhysicalMemory) / 1MB, 2)
}
"""

# Function to execute Windows commands
def execute_windows_command(command):
    session = winrm.Session(f'http://{windows_hostname}:5985/wsman', auth=(windows_username, windows_password),
                            transport='ntlm')
    try:
        result = session.run_ps(command)
        return result.std_out.decode('utf-8').strip()
    except Exception as e:
        print(f"Failed to connect to Windows server: {e}")
        return None

# Fetch system data from Windows server
def fetch_windows_system_data():
    print("Fetching CPU usage from Windows server...")
    cpu_usage = execute_windows_command(windows_cpu_command)

    print("Fetching memory usage from Windows server...")
    memory_usage = execute_windows_command(windows_memory_command)

    if memory_usage:
        memory_data = {}
        for line in memory_usage.splitlines():
            if 'TotalMemoryGB' in line:
                memory_data['TotalMemoryGB'] = float(line.split()[-1])
            elif 'FreeMemoryGB' in line:
                memory_data['FreeMemoryGB'] = float(line.split()[-1])
            elif 'UsedMemoryGB' in line:
                memory_data['UsedMemoryGB'] = float(line.split()[-1])

        ram_total = memory_data['TotalMemoryGB']
        ram_used = memory_data['UsedMemoryGB']
        ram_free_bytes = memory_data['FreeMemoryGB'] * 1024 ** 3

        return {
            "ram_total": round(ram_total, 2),
            "ram_used": round(ram_used, 2),
            "ram_free_bytes": round(ram_free_bytes),
            "cpu_usage": cpu_usage
        }
    else:
        return None

# Function to execute Linux commands
def execute_linux_command(command):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(linux_hostname, port=linux_port, username=linux_username, password=linux_password)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode('utf-8')
        client.close()
        return output.strip()
    except Exception as e:
        print(f"Failed to connect to Linux server: {e}")
        return None

# Fetch system data from Linux server
def fetch_linux_system_data():
    cpu_command = "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'"
    memory_command = "free -m | awk 'NR==2{printf \"%s %s %s %.2f\", $2,$3,$4,$3*100/$2 }'"

    print("Fetching CPU usage from Linux server...")
    cpu_usage = execute_linux_command(cpu_command)

    print("Fetching memory usage from Linux server...")
    memory_usage = execute_linux_command(memory_command).split()
    ram_total, ram_used, ram_free, ram_percent_used = map(float, memory_usage)
    ram_free_bytes = ram_free * 1000 * 1000

    return {
        "ram_total": round(ram_total / 1000, 2),
        "ram_used": round(ram_used / 1000, 2),
        "ram_free_bytes": round(ram_free_bytes)
    }

# Fetch API data for each server
def fetch_api_data(server_name):
    payload = {'host_name': server_name, 'service_name': 'ram'}
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(api_url, params=payload, headers=headers)
    if response.status_code == 200:
        api_data = response.json()['message']
        ram_data = {}
        for serviceData in api_data:
            for service_data in serviceData['service_data']:
                if service_data['metrix_name'] == 'ram_used':
                    ram_data['ram_used'] = float(service_data['metrix_value'])
                if service_data['metrix_name'] == 'ram_total':
                    ram_data['ram_total'] = float(service_data['metrix_value'])
                if service_data['metrix_name'] == 'ram_free_bytes':
                    ram_data['ram_free_bytes'] = float(service_data['metrix_value'])
        return ram_data
    else:
        print(f"API Request Failed: {response.status_code}")
        return None

# Function to compare values
def compare_values(ssh_value, api_value):
    if api_value is None:
        return "fail"
    difference = abs(ssh_value - api_value) / ssh_value * 100
    return "passed" if difference <= 10 else "failed"

# Generate report
def generate_report(ssh_data, api_data):
    table = PrettyTable()
    table.field_names = ["Metrics", "SSH Value", "API Value", "Status"]
    report_data = []

    for metric in ["ram_total", "ram_used", "ram_free_bytes"]:
        ssh_value = ssh_data[metric]
        api_value = api_data.get(metric)
        status = compare_values(ssh_value, api_value)
        report_data.append({
            "metric": metric.replace("_", " ").capitalize(),
            "ssh_value": f"{ssh_value / 1e9:.2f} GB" if "bytes" in metric else f"{ssh_value} GB",
            "api_value": f"{api_value / 1e9:.2f} GB" if "bytes" in metric else f"{api_value} GB",
            "status": status
        })

    for row in report_data:
        table.add_row([row['metric'], row['ssh_value'], row['api_value'], row['status']])

    print(table)
    return report_data

# Generate HTML report
def generate_html_report(windows_report_data, linux_report_data,windows_fetch_time, linux_fetch_time):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('report_template.html')

    windows_total_tests = len(windows_report_data)
    windows_pass_count = sum(1 for row in windows_report_data if row['status'] == "passed")
    windows_fail_count = windows_total_tests - windows_pass_count

    linux_total_tests = len(linux_report_data)
    linux_pass_count = sum(1 for row in linux_report_data if row['status'] == "passed")
    linux_fail_count = linux_total_tests - linux_pass_count

    html_content = template.render(
        windows_table=windows_report_data,
        linux_table=linux_report_data,
        windows_pass_percentage=round((windows_pass_count / windows_total_tests) * 100, 2),
        windows_fail_percentage=round((windows_fail_count / windows_total_tests) * 100, 2),
        linux_pass_percentage=round((linux_pass_count / linux_total_tests) * 100, 2),
        linux_fail_percentage=round((linux_fail_count / linux_total_tests) * 100, 2),
        windows_fetch_time=windows_fetch_time,  # Pass Windows fetch time to the template
        linux_fetch_time=linux_fetch_time  # Pass Linux fetch time to the template
    )

    with open("system_report.html", "w") as f:
        f.write(html_content)
    print("HTML report generated successfully.")

# Main execution
# if __name__ == "__main__":
#     print("Fetching data from Windows Server...")
#     windows_data = fetch_windows_system_data()
#     print("Windows Data:", windows_data)
#
#     print("Fetching data from Linux Server...")
#     linux_data = fetch_linux_system_data()
#     print("Linux Data:", linux_data)
#
#     print("Fetching system data from API for Windows Server...")
#     windows_api_data = fetch_api_data('ZCS-SERVER')  # Replace with your Windows server name
#     print("Windows API Data:", windows_api_data)
#
#     print("Fetching system data from API for Linux Server...")
#     linux_api_data = fetch_api_data('zcsit')  # Replace with your Linux server name
#     print("Linux API Data:", linux_api_data)
#
#     # Generate reports for both servers
#     windows_report_data = generate_report(windows_data, windows_api_data)
#     linux_report_data = generate_report(linux_data, linux_api_data)
#
#     print("Windows Report Data:", windows_report_data)
#     print("Linux Report Data:", linux_report_data)
#
#     # Generate HTML report
#     generate_html_report(windows_report_data, linux_report_data)



if __name__ == "__main__":
    # Capture the time just before fetching data from Windows server
    windows_fetch_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Fetching data from Windows Server at {windows_fetch_time}...")
    windows_data = fetch_windows_system_data()  # Assuming you want to keep the original function name
    print("Windows Data:", windows_data)

    # Capture the time just before fetching data from Linux server
    linux_fetch_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Fetching data from Linux Server at {linux_fetch_time}...")
    linux_data = fetch_linux_system_data()  # Assuming you want to keep the original function name
    print("Linux Data:", linux_data)

    # Fetch API data
    print(f"Fetching system data from API for Windows Server at {windows_fetch_time}...")
    windows_api_data = fetch_api_data('ZCS-SERVER')  # Replace with your Windows server name
    print("Windows API Data:", windows_api_data)

    print(f"Fetching system data from API for Linux Server at {linux_fetch_time}...")
    linux_api_data = fetch_api_data('zcsit')  # Replace with your Linux server name
    print("Linux API Data:", linux_api_data)

    # Generate reports for both servers
    windows_report_data = generate_report(windows_data, windows_api_data)
    linux_report_data = generate_report(linux_data, linux_api_data)

    # Generate final HTML report
    generate_html_report(windows_report_data, linux_report_data, windows_fetch_time, linux_fetch_time)







