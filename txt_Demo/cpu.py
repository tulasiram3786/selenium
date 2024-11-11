# import psutil
#
# # Get CPU usage percentage
# cpu_usage = psutil.cpu_percent(interval=1)
# print(f"CPU Usage: {cpu_usage}%")
#
# # Get memory usage statistics
# memory_info = psutil.virtual_memory()
# total_memory = memory_info.total / (1024 ** 3)  # Convert to GB
# available_memory = memory_info.available / (1024 ** 3)  # Convert to GB
# memory_usage_percentage = memory_info.percent
#
# print(f"Total Memory: {total_memory:.2f} GB")
# print(f"Available Memory: {available_memory:.2f} GB")
# print(f"Memory Usage: {memory_usage_percentage}%")

####################

# import requests
#
# api_url = 'https://staging-api-zoomview.zybisys.com/saas-zoomview/api/v1/infra/infra-livestate?host_name=zcsit&service_name=cpu'  # Replace with your API endpoint
# response = requests.get(api_url)
#
# # Assuming the response is JSON and contains CPU, memory, and disk usage
# if response.status_code == 200:
#     api_data = response.json()
#     api_cpu = api_data['cpu']  # Modify this based on your API's structure
#     api_memory = api_data['memory']  # Modify as per the API structure
#     api_disk = api_data['disk']  # Modify as per the API structure
# else:
#     print(f"API Request Failed: {response.status_code}")



#===================

# import paramiko
# import requests
#
# # Define server connection details
# hostname = '192.168.1.81'
# port = 20202
# username = 'tulasi'
# password = 'Nop@ssw0rd'
#
# # API details
# api_url = 'https://staging-api-zoomview.zybisys.com/saas-zoomview/api/v1/infra/infra-livestate'  # Replace with your API endpoint
#
#
# def execute_remote_command(command):
#     try:
#         # Create an SSH client
#         client = paramiko.SSHClient()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect(hostname, port=port, username=username, password=password)
#         stdin, stdout, stderr = client.exec_command(command)
#         output = stdout.read().decode('utf-8')
#         error = stderr.read().decode('utf-8')
#         if error:
#             print(f"Error: {error}")
#         return output.strip()  # Stripping extra newlines/whitespace
#     except Exception as e:
#         print(f"Failed to connect: {e}")
#     finally:
#         client.close()
#
#
# # Fetch system data via SSH
# def fetch_system_data():
#     # Fetch CPU usage
#     cpu_command = "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'"
#     cpu_usage = execute_remote_command(cpu_command)
#
#     return {
#         "cpu": round(float(cpu_usage), 2)  # Round to 2 decimal places
#     }
#
#
# # Fetch API data
# def fetch_api_data():
#     payload = {'host_name': 'zcsit', 'service_name': 'cpu'}
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI4ODc4ODYxNzUyLCJpYXQiOjE3Mjg4Nzg4NjEsImV4cCI6MTcyODk2NTI2MX0.Ef_o8MKUV3NuDN1w8QnqoK6esImiA6kghiTDzm_vJt8ZyWojlpGft4rnKv1LmdQD-WuwJNlpO09oLDIqUNhLjA"
#         # Replace with your actual token
#     }
#     response = requests.get(url=api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()
#         api_data2 = api_data['message']
#
#         cpu_data = {}
#         for serviceData in api_data2:
#             service_data = serviceData['service_data']
#             for service_data2 in service_data:
#                 if service_data2['metrix_name'] == 'cpu_usage':
#                     cpu_data['cpu'] = float(service_data2['metrix_value'])  # Assuming API returns in percentage
#
#         return cpu_data
#     else:
#         print(f"API Request Failed: {response.status_code}")
#         return None
#
#
# # Compare CPU data only
# def compare_data(ssh_data, api_data):
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#     print(f"SSH DATA: {ssh_data}")
#     print(f"API DATA: {api_data}")
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#
#     # Fetch CPU data from SSH and API
#     ssh_cpu_usage = ssh_data['cpu']
#     api_cpu_usage = api_data.get('cpu', None)
#
#     # CPU Usage Comparison
#     if api_cpu_usage is not None:
#         tolerance_10_cpu = 0.1 * ssh_cpu_usage  # 10% tolerance
#         tolerance_20_cpu = 0.2 * ssh_cpu_usage  # 20% tolerance
#         difference_cpu = abs(ssh_cpu_usage - api_cpu_usage)
#
#         if difference_cpu <= tolerance_10_cpu:
#             print(f"CPU usage matches: SSH={ssh_cpu_usage}%, API={api_cpu_usage}% (within 10%)")
#         elif difference_cpu <= tolerance_20_cpu:
#             print(f"CPU usage partially matches: SSH={ssh_cpu_usage}%, API={api_cpu_usage}% (between 10%-20%)")
#         else:
#             print(f"CPU usage mismatch: SSH={ssh_cpu_usage}%, API={api_cpu_usage}% (difference > 20%)")
#     else:
#         print("CPU data missing from API.")
#
#
# # Main execution
# if __name__ == "__main__":
#     print("Fetching system data from SSH...")
#     ssh_data = fetch_system_data()
#     print(ssh_data)
#     print("Fetching system data from API...")
#     api_data = fetch_api_data()
#     print(api_data)
#
#     if api_data:
#         print("Comparing system data...")
#         compare_data(ssh_data, api_data)
#     else:
#         print("Failed to fetch API data.")



#-----------------

# import paramiko
# import requests
#
# # Define server connection details
# hostname = '192.168.1.81'
# port = 20202
# username = 'tulasi'
# password = 'Nop@ssw0rd'
#
# # API details
# api_url = 'https://staging-api-zoomview.zybisys.com/saas-zoomview/api/v1/infra/infra-livestate'  # Replace with your API endpoint
#
#
# def execute_remote_command(command):
#     try:
#         # Create an SSH client
#         client = paramiko.SSHClient()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect(hostname, port=port, username=username, password=password)
#         stdin, stdout, stderr = client.exec_command(command)
#         output = stdout.read().decode('utf-8')
#         error = stderr.read().decode('utf-8')
#         if error:
#             print(f"Error: {error}")
#         return output.strip()  # Stripping extra newlines/whitespace
#     except Exception as e:
#         print(f"Failed to connect: {e}")
#     finally:
#         client.close()
#
#
# # Fetch system data via SSH
# def fetch_system_data():
#     # Fetch core-wise CPU usage (CPU0, CPU1, CPU2, CPU3, etc.)
#     cpu_command = "top -bn1 | grep 'Cpu' | awk -F',' '{for (i=1;i<=NF;i++) print $i}' | grep 'id' | awk '{print 100 - $1}'"
#     cpu_usage_output = execute_remote_command(cpu_command)
#
#     # Parse core-wise CPU usage from SSH
#     cpu_usage_data = {}
#     cores = cpu_usage_output.splitlines()
#     for i, usage in enumerate(cores):
#         cpu_usage_data[f'cpu{i}'] = round(float(usage), 2)
#
#     return cpu_usage_data
#
#
# # Fetch API data
# def fetch_api_data():
#     payload = {'host_name': 'zcsit', 'service_name': 'cpu'}
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI4ODc4ODYxNzUyLCJpYXQiOjE3Mjg4Nzg4NjEsImV4cCI6MTcyODk2NTI2MX0.Ef_o8MKUV3NuDN1w8QnqoK6esImiA6kghiTDzm_vJt8ZyWojlpGft4rnKv1LmdQD-WuwJNlpO09oLDIqUNhLjA"
#         # Replace with your actual token
#     }
#     response = requests.get(url=api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()
#         api_data2 = api_data['message']
#
#         cpu_data = {}
#         for serviceData in api_data2:
#             service_data = serviceData['service_data']
#             for service_data2 in service_data:
#                 if 'cpu' in service_data2['metrix_name']:
#                     core = service_data2['metrix_name'].replace('cpu', '')  # e.g., "cpu0", "cpu1"
#                     cpu_data[f'cpu{core}'] = float(service_data2['metrix_value'])  # Assuming API returns in percentage
#
#         return cpu_data
#     else:
#         print(f"API Request Failed: {response.status_code}")
#         return None
#
#
# # Compare core-wise CPU data
# def compare_data(ssh_data, api_data):
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#     print(f"SSH DATA: {ssh_data}")
#     print(f"API DATA: {api_data}")
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#
#     for core, ssh_cpu_usage in ssh_data.items():
#         api_cpu_usage = api_data.get(core, None)
#
#         # CPU Usage Comparison
#         if api_cpu_usage is not None:
#             tolerance_10_cpu = 0.1 * ssh_cpu_usage  # 10% tolerance
#             tolerance_20_cpu = 0.2 * ssh_cpu_usage  # 20% tolerance
#             difference_cpu = abs(ssh_cpu_usage - api_cpu_usage)
#
#             if difference_cpu <= tolerance_10_cpu:
#                 print(f"{core} usage matches: SSH={ssh_cpu_usage}%, API={api_cpu_usage}% (within 10%)")
#             elif difference_cpu <= tolerance_20_cpu:
#                 print(f"{core} usage partially matches: SSH={ssh_cpu_usage}%, API={api_cpu_usage}% (between 10%-20%)")
#             else:
#                 print(f"{core} usage mismatch: SSH={ssh_cpu_usage}%, API={api_cpu_usage}% (difference > 20%)")
#         else:
#             print(f"CPU data for {core} missing from API.")
#
#
# # Main execution
# if __name__ == "__main__":
#     print("Fetching system data from SSH...")
#     ssh_data = fetch_system_data()
#     print(ssh_data)
#     print("Fetching system data from API...")
#     api_data = fetch_api_data()
#     print(api_data)
#
#     if api_data:
#         print("Comparing system data...")
#         compare_data(ssh_data, api_data)
#     else:
#         print("Failed to fetch API data.")


#--------------

# import paramiko
# import requests
# from datetime import datetime
#
# # Define server connection details
# hostname = '192.168.1.81'
# port = 20202
# username = 'tulasi'
# password = 'Nop@ssw0rd'
#
# # API details
# api_url = 'https://staging-api-zoomview.zybisys.com/saas-zoomview/api/v1/infra/infra-livestate'  # Replace with your API endpoint
#
#
# def execute_remote_command(command):
#     try:
#         # Create an SSH client
#         client = paramiko.SSHClient()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect(hostname, port=port, username=username, password=password)
#         stdin, stdout, stderr = client.exec_command(command)
#         output = stdout.read().decode('utf-8')
#         error = stderr.read().decode('utf-8')
#         if error:
#             print(f"Error: {error}")
#         return output.strip()  # Stripping extra newlines/whitespace
#     except Exception as e:
#         print(f"Failed to connect: {e}")
#     finally:
#         client.close()
#
#
# # Fetch system data via SSH
# def fetch_system_data():
#     # Fetch CPU usage
#     cpu_command = "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'"
#     cpu_usage = execute_remote_command(cpu_command)
#
#     return {
#         "cpu": round(float(cpu_usage), 2)  # Round to 2 decimal places
#     }
#
#
# # Fetch API data
# def fetch_api_data():
#     payload = {'host_name': 'zcsit', 'service_name': 'cpu'}
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI4ODc4ODYxNzUyLCJpYXQiOjE3Mjg4Nzg4NjEsImV4cCI6MTcyODk2NTI2MX0.Ef_o8MKUV3NuDN1w8QnqoK6esImiA6kghiTDzm_vJt8ZyWojlpGft4rnKv1LmdQD-WuwJNlpO09oLDIqUNhLjA"
#         # Replace with your actual token
#     }
#     response = requests.get(url=api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()
#         api_data2 = api_data['message']
#
#         cpu_data = {}
#         for serviceData in api_data2:
#             service_data = serviceData['service_data']
#             for service_data2 in service_data:
#                 if service_data2['metrix_name'] == 'cpu_usage':
#                     cpu_data['cpu'] = float(service_data2['metrix_value'])  # Assuming API returns in percentage
#
#         return cpu_data
#     else:
#         print(f"API Request Failed: {response.status_code}")
#         return None
#
#
# # Compare CPU data and return the results
# def compare_data(ssh_data, api_data):
#     report_data = ""
#
#     # Fetch CPU data from SSH and API
#     ssh_cpu_usage = ssh_data['cpu']
#     api_cpu_usage = api_data.get('cpu', None)
#
#     # CPU Usage Comparison
#     if api_cpu_usage is not None:
#         tolerance_10_cpu = 0.1 * ssh_cpu_usage  # 10% tolerance
#         tolerance_20_cpu = 0.2 * ssh_cpu_usage  # 20% tolerance
#         difference_cpu = abs(ssh_cpu_usage - api_cpu_usage)
#
#         if difference_cpu <= tolerance_10_cpu:
#             result = f"CPU usage matches: SSH={ssh_cpu_usage}%, API={api_cpu_usage}% (within 10%)"
#         elif difference_cpu <= tolerance_20_cpu:
#             result = f"CPU usage partially matches: SSH={ssh_cpu_usage}%, API={api_cpu_usage}% (between 10%-20%)"
#         else:
#             result = f"CPU usage mismatch: SSH={ssh_cpu_usage}%, API={api_cpu_usage}% (difference > 20%)"
#     else:
#         result = "CPU data missing from API."
#
#     report_data += f"<p>{result}</p>"
#     return report_data
#
#
# # Function to generate the HTML report
# def generate_html_report(ssh_data, api_data, comparison_results):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
#     html_content = f"""
#     <html>
#     <head>
#         <title>CPU Usage Report</title>
#         <style>
#             body {{ font-family: Arial, sans-serif; }}
#             h1 {{ color: #333; }}
#             table {{ border-collapse: collapse; width: 50%; margin: 20px 0; }}
#             table, th, td {{ border: 1px solid black; }}
#             th, td {{ padding: 10px; text-align: left; }}
#             th {{ background-color: #f2f2f2; }}
#         </style>
#     </head>
#     <body>
#         <h1>CPU Usage Report</h1>
#         <p><strong>Generated on:</strong> {timestamp}</p>
#         <h2>SSH Data:</h2>
#         <p>CPU Usage: {ssh_data['cpu']}%</p>
#         <h2>API Data:</h2>
#         <p>CPU Usage: {api_data['cpu']}%</p>
#         <h2>Comparison Results:</h2>
#         {comparison_results}
#     </body>
#     </html>
#     """
#
#     with open("cpu_usage_report.html", "w") as file:
#         file.write(html_content)
#     print("HTML report generated: cpu_usage_report.html")
#
#
# # Main execution
# if __name__ == "__main__":
#     print("Fetching system data from SSH...")
#     ssh_data = fetch_system_data()
#     print(ssh_data)
#
#     print("Fetching system data from API...")
#     api_data = fetch_api_data()
#     print(api_data)
#
#     if api_data:
#         print("Comparing system data...")
#         comparison_results = compare_data(ssh_data, api_data)
#         generate_html_report(ssh_data, api_data, comparison_results)
#     else:
#         print("Failed to fetch API data.")



#88888888888888
#Generating good results

# import paramiko
# import requests
# from datetime import datetime
#
# # Define server connection details
# hostname = '192.168.1.81'
# port = 20202
# username = 'tulasi'
# password = 'Nop@ssw0rd'
#
# # API details
# api_url = 'https://staging-api-zoomview.zybisys.com/saas-zoomview/api/v1/infra/infra-livestate'  # Replace with your API endpoint
#
#
# def execute_remote_command(command):
#     try:
#         # Create an SSH client
#         client = paramiko.SSHClient()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect(hostname, port=port, username=username, password=password)
#         stdin, stdout, stderr = client.exec_command(command)
#         output = stdout.read().decode('utf-8')
#         error = stderr.read().decode('utf-8')
#         if error:
#             print(f"Error: {error}")
#         return output.strip()  # Stripping extra newlines/whitespace
#     except Exception as e:
#         print(f"Failed to connect: {e}")
#         return ""
#     finally:
#         client.close()
#
#
# # Fetch system data via SSH
# def fetch_system_data():
#     # Fetch CPU usage
#     cpu_command = "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'"
#     cpu_usage = execute_remote_command(cpu_command)
#
#     return {
#         "cpu": round(float(cpu_usage), 2) if cpu_usage else None  # Round to 2 decimal places
#     }
#
#
# # Fetch API data
# def fetch_api_data():
#     payload = {'host_name': 'zcsit', 'service_name': 'cpu'}
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI4ODc4ODYxNzUyLCJpYXQiOjE3Mjg4Nzg4NjEsImV4cCI6MTcyODk2NTI2MX0.Ef_o8MKUV3NuDN1w8QnqoK6esImiA6kghiTDzm_vJt8ZyWojlpGft4rnKv1LmdQD-WuwJNlpO09oLDIqUNhLjA"
#         # Replace with your actual token
#     }
#     try:
#         response = requests.get(url=api_url, params=payload, headers=headers, timeout=10)
#     except requests.exceptions.RequestException as e:
#         print(f"API Request Exception: {e}")
#         return None
#
#     if response.status_code == 200:
#         try:
#             api_data = response.json()
#             api_data2 = api_data.get('message', [])
#
#             cpu_data = {}
#             for serviceData in api_data2:
#                 service_data = serviceData.get('service_data', [])
#                 for service_data2 in service_data:
#                     if service_data2.get('metrix_name') == 'cpu_usage':
#                         cpu_data['cpu'] = float(service_data2.get('metrix_value', 0))  # Assuming API returns in percentage
#
#             return cpu_data
#         except ValueError:
#             print("Error parsing JSON from API response.")
#             return None
#     else:
#         print(f"API Request Failed: Status Code {response.status_code}")
#         return None
#
#
# # Compare CPU data and return the results
# def compare_data(ssh_data, api_data):
#     report_data = ""
#     ssh_cpu_usage = ssh_data.get('cpu')
#     api_cpu_usage = api_data.get('cpu') if api_data else None
#
#     if ssh_cpu_usage is None:
#         report_data += "<p style='color:red;'>SSH CPU data is missing or invalid.</p>"
#         return report_data
#
#     if api_cpu_usage is not None:
#         tolerance_10_cpu = 0.1 * ssh_cpu_usage  # 10% tolerance
#         tolerance_20_cpu = 0.2 * ssh_cpu_usage  # 20% tolerance
#         difference_cpu = abs(ssh_cpu_usage - api_cpu_usage)
#
#         if difference_cpu <= tolerance_10_cpu:
#             result = f"<span style='color:green;'>CPU usage matches: SSH={ssh_cpu_usage}%, API={api_cpu_usage}% (within 10%)</span>"
#         elif difference_cpu <= tolerance_20_cpu:
#             result = f"<span style='color:orange;'>CPU usage partially matches: SSH={ssh_cpu_usage}%, API={api_cpu_usage}% (between 10%-20%)</span>"
#         else:
#             result = f"<span style='color:red;'>CPU usage mismatch: SSH={ssh_cpu_usage}%, API={api_cpu_usage}% (difference > 20%)</span>"
#     else:
#         result = "<span style='color:red;'>CPU data missing from API.</span>"
#
#     report_data += f"<p>{result}</p>"
#     return report_data
#
#
# # Function to generate the pie chart data for CPU usage
# def generate_pie_chart_data(ssh_cpu_usage, api_cpu_usage):
#     labels = ['SSH CPU Usage', 'API CPU Usage']
#     values = [ssh_cpu_usage, api_cpu_usage if api_cpu_usage is not None else 0]
#     colors = ['#4CAF50', '#FF6347']  # Green and Red
#
#     return labels, values, colors
#
#
# # Function to generate the HTML report with embedded Chart.js pie chart
# def generate_html_report(ssh_data, api_data, comparison_results):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     ssh_cpu_usage = ssh_data.get('cpu', 0)
#     api_cpu_usage = api_data.get('cpu') if api_data else 0
#
#     labels, values, colors = generate_pie_chart_data(ssh_cpu_usage, api_cpu_usage)
#
#     # Prepare JavaScript data for Chart.js
#     chart_data = {
#         'labels': labels,
#         'datasets': [{
#             'data': values,
#             'backgroundColor': colors,
#             'hoverBackgroundColor': colors
#         }]
#     }
#
#     # Convert Python data structures to JavaScript-friendly JSON strings
#     import json
#     chart_data_json = json.dumps(chart_data)
#
#     html_content = f"""
#     <html>
#     <head>
#         <title>CPU Usage Report</title>
#         <style>
#             body {{ font-family: Arial, sans-serif; margin: 20px; }}
#             h1 {{ color: #333; }}
#             .comparison {{ margin: 20px 0; }}
#             .chart-container {{ width: 50%; margin: auto; }}
#             table {{ border-collapse: collapse; width: 50%; margin: 20px 0; }}
#             table, th, td {{ border: 1px solid black; }}
#             th, td {{ padding: 10px; text-align: left; }}
#             th {{ background-color: #f2f2f2; }}
#         </style>
#         <!-- Chart.js CDN -->
#         <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
#     </head>
#     <body>
#         <h1>CPU Usage Report</h1>
#         <p><strong>Generated on:</strong> {timestamp}</p>
#
#         <h2>SSH Data:</h2>
#         <p>CPU Usage: {ssh_cpu_usage}%</p>
#
#         <h2>API Data:</h2>
#         <p>CPU Usage: {api_cpu_usage}%</p>
#
#         <h2>Comparison Results:</h2>
#         <div class="comparison">
#             {comparison_results}
#         </div>
#
#         <h2>CPU Usage Comparison Pie Chart:</h2>
#         <div class="chart-container">
#             <canvas id="cpuChart"></canvas>
#         </div>
#
#         <script>
#             var ctx = document.getElementById('cpuChart').getContext('2d');
#             var cpuChart = new Chart(ctx, {{
#                 type: 'pie',
#                 data: {chart_data_json},
#                 options: {{
#                     responsive: true,
#                     plugins: {{
#                         legend: {{
#                             position: 'top',
#                         }},
#                         title: {{
#                             display: true,
#                             text: 'CPU Usage Comparison: SSH vs API'
#                         }}
#                     }}
#                 }},
#             }});
#         </script>
#     </body>
#     </html>
#     """
#
#     with open("cpu_usage_report.html", "w") as file:
#         file.write(html_content)
#     print("HTML report generated: cpu_usage_report.html")
#
#
# # Main execution
# if __name__ == "__main__":
#     print("Fetching system data from SSH...")
#     ssh_data = fetch_system_data()
#     print(ssh_data)
#
#     print("Fetching system data from API...")
#     api_data = fetch_api_data()
#     print(api_data)
#
#     if api_data:
#         print("Comparing system data...")
#         comparison_results = compare_data(ssh_data, api_data)
#         generate_html_report(ssh_data, api_data, comparison_results)
#     else:
#         print("Failed to fetch API data.")




#16-10-2024

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
# api_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI5MTY1MTY5Mjc4LCJpYXQiOjE3MjkxNjUxNjksImV4cCI6MTcyOTI1MTU2OX0.c0CKP9YlMYH2CVs61VgpAvTk0QkaHpf0jBOCv5jVK7rNa84RNVoC4knLPJ70bz1_CFJiF1lF9t-rIKZ-RJQZog"  # Replace with your valid API token
#
# # Windows CPU command
# windows_cpu_command = """
# Get-WmiObject -Query "SELECT LoadPercentage FROM Win32_Processor" |
# ForEach-Object { $_.LoadPercentage }
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
# # Fetch CPU data from Windows server
# def fetch_windows_cpu_data():
#     print("Fetching CPU usage from Windows server...")
#     cpu_usage = execute_windows_command(windows_cpu_command)
#
#     if cpu_usage:
#         # Split the CPU usage string and take the first value
#         cpu_values = cpu_usage.split()
#         cpu_value = float(cpu_values[0]) if cpu_values else None
#         return {"cpu_usage": cpu_value} if cpu_value is not None else None
#     return None
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
# def fetch_linux_cpu_data():
#     cpu_command = "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'"
#
#     print("Fetching CPU usage from Linux server...")
#     cpu_usage = execute_linux_command(cpu_command)
#
#     return {
#         "cpu_usage": float(cpu_usage) if cpu_usage else None
#     }
#
#
# # Fetch API data for each server
# def fetch_api_cpu_data(server_name):
#     payload = {'host_name': server_name, 'service_name': 'cpu'}
#     headers = {
#         "Authorization": f"Bearer {api_token}"
#     }
#     response = requests.get(api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()['message']
#         cpu_data = {}
#         for serviceData in api_data:
#             for service_data in serviceData['service_data']:
#                 if service_data['metrix_name'] == 'cpu_usage':
#                     cpu_data['cpu_usage'] = float(service_data['metrix_value'])
#         return cpu_data
#     else:
#         print(f"API Request Failed: {response.status_code}")
#         return None
#
#
# # Function to compare values
# def compare_values(ssh_value, api_value):
#     if api_value is None:
#         return "failed"
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
#     ssh_value = ssh_data['cpu_usage']
#     api_value = api_data.get('cpu_usage')
#     status = compare_values(ssh_value, api_value)
#     report_data.append({
#         "metric": "CPU Usage",
#         "ssh_value": f"{ssh_value}%",
#         "api_value": f"{api_value}%" if api_value is not None else "N/A",
#         "status": status
#     })
#
#     table.add_row(["CPU Usage", f"{ssh_value}%", f"{api_value}%" if api_value is not None else "N/A", status])
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
#         linux_fail_percentage=round((linux_fail_count / linux_total_tests) * 100, 2),
#     )
#
#     with open("cpu_system_report1.html", "w") as f:
#         f.write(html_content)
#     print("HTML report generated successfully.")
#
#
# # Main execution
# if __name__ == "__main__":
#     print("Fetching data from Windows Server...")
#     windows_data = fetch_windows_cpu_data()
#     print("Windows Data:", windows_data)
#
#     print("Fetching data from Linux Server...")
#     linux_data = fetch_linux_cpu_data()
#     print("Linux Data:", linux_data)
#
#     print("Fetching system data from API for Windows Server...")
#     windows_api_data = fetch_api_cpu_data('ZCS-SERVER')  # Replace with your Windows server name
#     print("Windows API Data:", windows_api_data)
#
#     print("Fetching system data from API for Linux Server...")
#     linux_api_data = fetch_api_cpu_data('zcsit')  # Replace with your Linux server name
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

#18-10-2024

# import requests
# from prettytable import PrettyTable
# from jinja2 import Environment, FileSystemLoader
# import os
# import winrm  # For connecting to the Windows server
# import paramiko  # For connecting to the Linux server
# import datetime  # For capturing the time
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
# api_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI5MTY1MTY5Mjc4LCJpYXQiOjE3MjkxNjUxNjksImV4cCI6MTcyOTI1MTU2OX0.c0CKP9YlMYH2CVs61VgpAvTk0QkaHpf0jBOCv5jVK7rNa84RNVoC4knLPJ70bz1_CFJiF1lF9t-rIKZ-RJQZog"  # Replace with your valid API token
#
# # Windows CPU command
# windows_cpu_command = """
# Get-WmiObject -Query "SELECT LoadPercentage FROM Win32_Processor" |
# ForEach-Object { $_.LoadPercentage }
# """
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
# # Fetch CPU data from Windows server
# def fetch_windows_cpu_data():
#     print("Fetching CPU usage from Windows server...")
#     cpu_usage = execute_windows_command(windows_cpu_command)
#
#     if cpu_usage:
#         cpu_values = cpu_usage.split()
#         cpu_value = float(cpu_values[0]) if cpu_values else None
#         return {"cpu_usage": cpu_value} if cpu_value is not None else None
#     return None
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
# # Fetch system data from Linux server
# def fetch_linux_cpu_data():
#     cpu_command = "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'"
#
#     print("Fetching CPU usage from Linux server...")
#     cpu_usage = execute_linux_command(cpu_command)
#
#     return {
#         "cpu_usage": float(cpu_usage) if cpu_usage else None
#     }
#
# # Fetch API data for each server
# def fetch_api_cpu_data(server_name):
#     payload = {'host_name': server_name, 'service_name': 'cpu'}
#     headers = {
#         "Authorization": f"Bearer {api_token}"
#     }
#     response = requests.get(api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()['message']
#         cpu_data = {}
#         for serviceData in api_data:
#             for service_data in serviceData['service_data']:
#                 if service_data['metrix_name'] == 'cpu_usage':
#                     cpu_data['cpu_usage'] = float(service_data['metrix_value'])
#         return cpu_data
#     else:
#         print(f"API Request Failed: {response.status_code}")
#         return None
#
# # Function to compare values
# def compare_values(ssh_value, api_value):
#     if api_value is None:
#         return "failed"
#     difference = abs(ssh_value - api_value) / ssh_value * 100
#     return "passed" if difference <= 10 else "failed"
#
# # Generate report
# def generate_report(ssh_data, api_data):
#     table = PrettyTable()
#     table.field_names = ["Metrics", "SSH Value", "API Value", "Status"]
#     report_data = []
#
#     ssh_value = ssh_data['cpu_usage']
#     api_value = api_data.get('cpu_usage')
#     status = compare_values(ssh_value, api_value)
#     report_data.append({
#         "metric": "CPU Usage",
#         "ssh_value": f"{ssh_value}%",
#         "api_value": f"{api_value}%" if api_value is not None else "N/A",
#         "status": status
#     })
#
#     table.add_row(["CPU Usage", f"{ssh_value}%", f"{api_value}%" if api_value is not None else "N/A", status])
#
#     print(table)
#     return report_data
#
# # Generate HTML report
# def generate_html_report(windows_report_data, linux_report_data, fetch_time):
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
#         linux_fail_percentage=round((linux_fail_count / linux_total_tests) * 100, 2),
#         fetch_time=fetch_time  # Pass fetch time to the template
#     )
#
#     with open("cpu_system_report1.html", "w") as f:
#         f.write(html_content)
#     print("HTML report generated successfully.")
#
# # Main execution
# if __name__ == "__main__":
#     # Capture the current time
#     fetch_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#
#     print(f"Fetching data from Windows Server at {fetch_time}...")
#     windows_data = fetch_windows_cpu_data()
#     print("Windows Data:", windows_data)
#
#     print(f"Fetching data from Linux Server at {fetch_time}...")
#     linux_data = fetch_linux_cpu_data()
#     print("Linux Data:", linux_data)
#
#     print(f"Fetching system data from API for Windows Server at {fetch_time}...")
#     windows_api_data = fetch_api_cpu_data('ZCS-SERVER')  # Replace with your Windows server name
#     print("Windows API Data:", windows_api_data)
#
#     print(f"Fetching system data from API for Linux Server at {fetch_time}...")
#     linux_api_data = fetch_api_cpu_data('zcsit')  # Replace with your Linux server name
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
#     generate_html_report(windows_report_data, linux_report_data, fetch_time)



import requests
from prettytable import PrettyTable
from jinja2 import Environment, FileSystemLoader
import os
import winrm  # For connecting to the Windows server
import paramiko  # For connecting to the Linux server
import datetime  # For capturing the time

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
api_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI5MTY1MTY5Mjc4LCJpYXQiOjE3MjkxNjUxNjksImV4cCI6MTcyOTI1MTU2OX0.c0CKP9YlMYH2CVs61VgpAvTk0QkaHpf0jBOCv5jVK7rNa84RNVoC4knLPJ70bz1_CFJiF1lF9t-rIKZ-RJQZog"  # Replace with your valid API token

# Windows CPU command
windows_cpu_command = """
Get-WmiObject -Query "SELECT LoadPercentage FROM Win32_Processor" |
ForEach-Object { $_.LoadPercentage }
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

# Fetch CPU data from Windows server
def fetch_windows_cpu_data():
    print("Fetching CPU usage from Windows server...")
    cpu_usage = execute_windows_command(windows_cpu_command)

    if cpu_usage:
        cpu_values = cpu_usage.split()
        cpu_value = float(cpu_values[0]) if cpu_values else None
        return {"cpu_usage": cpu_value} if cpu_value is not None else None
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
def fetch_linux_cpu_data():
    cpu_command = "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'"

    print("Fetching CPU usage from Linux server...")
    cpu_usage = execute_linux_command(cpu_command)

    return {
        "cpu_usage": float(cpu_usage) if cpu_usage else None
    }

# Fetch API data for each server
def fetch_api_cpu_data(server_name):
    payload = {'host_name': server_name, 'service_name': 'cpu'}
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(api_url, params=payload, headers=headers)
    if response.status_code == 200:
        api_data = response.json()['message']
        cpu_data = {}
        for serviceData in api_data:
            for service_data in serviceData['service_data']:
                if service_data['metrix_name'] == 'cpu_usage':
                    cpu_data['cpu_usage'] = float(service_data['metrix_value'])
        return cpu_data
    else:
        print(f"API Request Failed: {response.status_code}")
        return None

# Function to compare values
def compare_values(ssh_value, api_value):
    if api_value is None:
        return "failed"
    difference = abs(ssh_value - api_value) / ssh_value * 100
    return "passed" if difference <= 10 else "failed"

# Generate report
def generate_report(ssh_data, api_data):
    table = PrettyTable()
    table.field_names = ["Metrics", "SSH Value", "API Value", "Status"]
    report_data = []

    ssh_value = ssh_data['cpu_usage']
    api_value = api_data.get('cpu_usage')
    status = compare_values(ssh_value, api_value)
    report_data.append({
        "metric": "CPU Usage",
        "ssh_value": f"{ssh_value}%",
        "api_value": f"{api_value}%" if api_value is not None else "N/A",
        "status": status
    })

    table.add_row(["CPU Usage", f"{ssh_value}%", f"{api_value}%" if api_value is not None else "N/A", status])

    print(table)
    return report_data

# Generate HTML report
def generate_html_report(windows_report_data, linux_report_data, windows_fetch_time, linux_fetch_time):
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

    with open("cpu_system_report1.html", "w") as f:
        f.write(html_content)
    print("HTML report generated successfully.")

# Main execution
if __name__ == "__main__":
    # Capture the time just before fetching data from Windows server
    windows_fetch_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Fetching data from Windows Server at {windows_fetch_time}...")
    windows_data = fetch_windows_cpu_data()
    print("Windows Data:", windows_data)

    # Capture the time just before fetching data from Linux server
    linux_fetch_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Fetching data from Linux Server at {linux_fetch_time}...")
    linux_data = fetch_linux_cpu_data()
    print("Linux Data:", linux_data)

    # Fetch API data
    print(f"Fetching system data from API for Windows Server at {windows_fetch_time}...")
    windows_api_data = fetch_api_cpu_data('ZCS-SERVER')  # Replace with your Windows server name
    print("Windows API Data:", windows_api_data)

    print(f"Fetching system data from API for Linux Server at {linux_fetch_time}...")
    linux_api_data = fetch_api_cpu_data('zcsit')  # Replace with your Linux server name
    print("Linux API Data:", linux_api_data)

    # Generate reports for both servers
    windows_report_data = generate_report(windows_data, windows_api_data)
    linux_report_data = generate_report(linux_data, linux_api_data)

    # Generate final HTML report
    generate_html_report(windows_report_data, linux_report_data, windows_fetch_time, linux_fetch_time)









