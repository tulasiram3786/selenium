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
#     # Fetch detailed memory usage (in MB)
#     memory_command = "free -m | awk 'NR==2{printf \"%s %s %s %.2f\", $2,$3,$4,$3*100/$2 }'"
#     memory_usage = execute_remote_command(memory_command).split()
#     ram_total_ssh, ram_used_ssh, ram_free_ssh, ram_percent_used_ssh = map(float, memory_usage)
#
#     # Convert RAM free from MB to bytes
#     ram_free_bytes_ssh = ram_free_ssh * 1024 * 1024
#
#     # Fetch disk usage for / and /boot partitions
#     disk_command = "df -B1 --output=source,size,used,avail,pcent,target | grep '/\\|/boot'"
#     disk_usage = execute_remote_command(disk_command)
#
#     disk_info = {}
#     for line in disk_usage.splitlines()[1:]:  # Skip the header
#         parts = line.split()
#         disk_name = parts[-1]
#         disk_info[disk_name] = {
#             "size": float(parts[1]),  # Size in bytes
#             "used": float(parts[2]),  # Used in bytes
#             "available": float(parts[3]),  # Available in bytes
#             "percent_used": parts[4].strip('%'),  # Percentage used
#         }
#
#     return {
#         "cpu": round(float(cpu_usage), 2),  # Round to 2 decimal places
#         "ram_total": round(ram_total_ssh / 1024, 2),  # Convert MB to GB and round to 2 decimal places
#         "ram_used": round(ram_used_ssh / 1024, 2),  # Convert MB to GB and round to 2 decimal places
#         "ram_free_bytes": round(ram_free_bytes_ssh),  # RAM free in bytes (no decimals needed)
#         "ram_percent": round(ram_percent_used_ssh, 2),  # Round to 2 decimal places
#         "disk": disk_info
#     }
#
#
# # Fetch API data
# def fetch_api_data():
#     ram_data = {}
#     disk_data = {}
#     payload = {'host_name': 'zcsit', 'service_name': 'disk'}
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI4Mzg5Njc2NDcyLCJpYXQiOjE3MjgzODk2NzYsImV4cCI6MTcyODQ3NjA3Nn0.dyTuqdGW2pjhTfsgyiQy5zB2zuypyxNunZnvSiTXx5B83BpWITbnqCR_thbK-XdGGwaaEUegJ-NYtEQ5e1RbJA"
#         # Replace with your actual token
#     }
#     response = requests.get(url=api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()
#         api_data2 = api_data['message']
#
#         for serviceData in api_data2:
#             service_data = serviceData['service_data']
#             for service_data2 in service_data:
#                 if service_data2['metrix_name'] == 'ram_used':
#                     ram_data['ram_used'] = float(service_data2['metrix_value'])  # Assuming API returns in GB
#                 if service_data2['metrix_name'] == 'ram_total':
#                     ram_data['ram_total'] = float(service_data2['metrix_value'])  # Assuming API returns in GB
#                 if service_data2['metrix_name'] == 'ram_free_bytes':
#                     ram_data['ram_free_bytes'] = float(service_data2['metrix_value'])  # Assuming API returns in bytes
#                 if service_data2['metrix_name'] == 'disk_usage':
#                     for disk_info in service_data2['disk_data']:
#                         disk_name = disk_info['name']
#                         disk_data[disk_name] = {
#                             "size": float(disk_info['size']),
#                             "used": float(disk_info['used']),
#                             "available": float(disk_info['available']),
#                             "percent_used": disk_info['percent_used'],
#                         }
#
#         return ram_data, disk_data
#     else:
#         print(f"API Request Failed: {response.status_code}")
#         return None, None
#
#
# # Compare the values with 10%-20% tolerance for RAM and Disk
# def compare_data(ssh_data, api_data):
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#     print(f"SSH DATA: {ssh_data}")
#     print(f"API DATA: {api_data}")
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#
#     ssh_ram_used = ssh_data['ram_used']
#     ssh_ram_total = ssh_data['ram_total']
#     ssh_ram_free_bytes = ssh_data['ram_free_bytes']
#
#     api_ram_used = api_data[0].get('ram_used', None)
#     api_ram_total = api_data[0].get('ram_total', None)
#     api_ram_free_bytes = api_data[0].get('ram_free_bytes', None)
#
#     # RAM Used Comparison
#     if api_ram_used is not None:
#         tolerance_10_used = 0.1 * ssh_ram_used  # 10% tolerance
#         tolerance_20_used = 0.2 * ssh_ram_used  # 20% tolerance
#         difference_used = abs(ssh_ram_used - api_ram_used)
#
#         if difference_used <= tolerance_10_used:
#             print(f"RAM used matches: SSH={ssh_ram_used}GB, API={api_ram_used}GB (within 10%)")
#         elif difference_used <= tolerance_20_used:
#             print(f"RAM used partially matches: SSH={ssh_ram_used}GB, API={api_ram_used}GB (between 10%-20%)")
#         else:
#             print(f"RAM used mismatch: SSH={ssh_ram_used}GB, API={api_ram_used}GB (difference > 20%)")
#     else:
#         print("RAM used data missing from API.")
#
#     # RAM Total Comparison
#     if api_ram_total is not None:
#         tolerance_10_total = 0.1 * ssh_ram_total  # 10% tolerance
#         tolerance_20_total = 0.2 * ssh_ram_total  # 20% tolerance
#         difference_total = abs(ssh_ram_total - api_ram_total)
#
#         if difference_total <= tolerance_10_total:
#             print(f"RAM total matches: SSH={ssh_ram_total}GB, API={api_ram_total}GB (within 10%)")
#         elif difference_total <= tolerance_20_total:
#             print(f"RAM total partially matches: SSH={ssh_ram_total}GB, API={api_ram_total}GB (between 10%-20%)")
#         else:
#             print(f"RAM total mismatch: SSH={ssh_ram_total}GB, API={api_ram_total}GB (difference > 20%)")
#     else:
#         print("RAM total data missing from API.")
#
#     # RAM Free (in Bytes) Comparison
#     if api_ram_free_bytes is not None:
#         tolerance_10_free_bytes = 0.1 * ssh_ram_free_bytes  # 10% tolerance
#         tolerance_20_free_bytes = 0.2 * ssh_ram_free_bytes  # 20% tolerance
#         difference_free_bytes = abs(ssh_ram_free_bytes - api_ram_free_bytes)
#
#         if difference_free_bytes <= tolerance_10_free_bytes:
#             print(f"RAM free matches: SSH={ssh_ram_free_bytes} bytes, API={api_ram_free_bytes} bytes (within 10%)")
#         elif difference_free_bytes <= tolerance_20_free_bytes:
#             print(f"RAM free partially matches: SSH={ssh_ram_free_bytes} bytes, API={api_ram_free_bytes}")



import paramiko
import requests

# Define server connection details
# hostname = '192.168.1.81'
# port = 20202
# username = 'tulasi'
# password = 'Nop@ssw0rd'
#
# # API details
# api_url = 'https://staging-api-zoomview.zybisys.com/saas-zoomview/api/v1/infra/infra-livestate'  # Replace with your API endpoint
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
# # Fetch system storage data via SSH
# def fetch_system_data():
#     # Fetch Disk usage (for root partition "/")
#     disk_command = "df -h / | grep '/' | awk '{print $3, $4, $5}'"  # Used space, Available space, Percentage
#     disk_usage = execute_remote_command(disk_command).split()
#
#     return {
#         "disk_used": disk_usage[0],
#         "disk_available": disk_usage[1],
#         "disk_usage_percentage": disk_usage[2].replace('%', '')  # Remove % and convert to float if needed
#     }
#
#
# # Fetch storage data from API
# def fetch_api_data():
#     payload = {'host_name': 'zcsit', 'service_name': 'disk'}
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI4ODc4ODYxNzUyLCJpYXQiOjE3Mjg4Nzg4NjEsImV4cCI6MTcyODk2NTI2MX0.Ef_o8MKUV3NuDN1w8QnqoK6esImiA6kghiTDzm_vJt8ZyWojlpGft4rnKv1LmdQD-WuwJNlpO09oLDIqUNhLjA"
#         # Replace with your actual token
#     }
#     response = requests.get(url=api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()
#         api_data2 = api_data['message']
#
#         storage_data = {}
#         for serviceData in api_data2:
#             service_data = serviceData['service_data']
#             for service_data2 in service_data:
#                 if 'disk_used' in service_data2['metrix_name']:
#                     storage_data['disk_used'] = service_data2['metrix_value']
#                 elif 'disk_available' in service_data2['metrix_name']:
#                     storage_data['disk_available'] = service_data2['metrix_value']
#                 elif 'disk_usage_percentage' in service_data2['metrix_name']:
#                     storage_data['disk_usage_percentage'] = service_data2['metrix_value']
#
#         return storage_data
#     else:
#         print(f"API Request Failed: {response.status_code}")
#         return None
#
#
# # Compare Disk (Storage) data
# def compare_data(ssh_data, api_data):
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#     print(f"SSH DATA: {ssh_data}")
#     print(f"API DATA: {api_data}")
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#
#     # Disk Data Comparison
#     ssh_disk_used = ssh_data.get('disk_used')
#     api_disk_used = api_data.get('disk_used', None)
#
#     if api_disk_used is not None:
#         if ssh_disk_used == api_disk_used:
#             print(f"Disk used matches: SSH={ssh_disk_used}, API={api_disk_used}")
#         else:
#             print(f"Disk used mismatch: SSH={ssh_disk_used}, API={api_disk_used}")
#
#     ssh_disk_available = ssh_data.get('disk_available')
#     api_disk_available = api_data.get('disk_available', None)
#
#     if api_disk_available is not None:
#         if ssh_disk_available == api_disk_available:
#             print(f"Disk available matches: SSH={ssh_disk_available}, API={api_disk_available}")
#         else:
#             print(f"Disk available mismatch: SSH={ssh_disk_available}, API={api_disk_available}")
#
#     ssh_disk_usage_percentage = ssh_data.get('disk_usage_percentage')
#     api_disk_usage_percentage = api_data.get('disk_usage_percentage', None)
#
#     if api_disk_usage_percentage is not None:
#         if ssh_disk_usage_percentage == api_disk_usage_percentage:
#             print(f"Disk usage percentage matches: SSH={ssh_disk_usage_percentage}%, API={api_disk_usage_percentage}%")
#         else:
#             print(f"Disk usage percentage mismatch: SSH={ssh_disk_usage_percentage}%, API={api_disk_usage_percentage}%")
#     else:
#         print("Disk usage percentage data missing from API.")
#
#
# # Main execution
# if __name__ == "__main__":
#     print("Fetching system storage data from SSH...")
#     ssh_data = fetch_system_data()
#     print(ssh_data)
#     print("Fetching storage data from API...")
#     api_data = fetch_api_data()
#     print(api_data)
#
#     if api_data:
#         print("Comparing storage data...")
#         compare_data(ssh_data, api_data)
#     else:
#         print("Failed to fetch API data.")



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

import paramiko
import requests

# Define server connection details
# hostname = '192.168.1.81'
# port = 20202
# username = 'tulasi'
# password = 'Nop@ssw0rd'
#
# # API details
# api_url = 'https://staging-api-zoomview.zybisys.com/saas-zoomview/api/v1/infra/infra-livestate'  # Replace with your API endpoint
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
# # Fetch system storage data via SSH
# def fetch_system_data():
#     # Fetch Disk usage in percentage (for root partition "/")
#     disk_command = "df -h / | grep '/' | awk '{print $5}'"  # Fetch the usage percentage directly
#     disk_usage_percentage = execute_remote_command(disk_command).replace('%', '')  # Remove % and convert to float if needed
#
#     return {
#         "disk_usage_percentage": disk_usage_percentage  # Disk usage in percentage
#     }
#
#
# # Fetch storage data from API
# def fetch_api_data():
#     payload = {'host_name': 'zcsit', 'service_name': 'disk'}
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI4ODc4ODYxNzUyLCJpYXQiOjE3Mjg4Nzg4NjEsImV4cCI6MTcyODk2NTI2MX0.Ef_o8MKUV3NuDN1w8QnqoK6esImiA6kghiTDzm_vJt8ZyWojlpGft4rnKv1LmdQD-WuwJNlpO09oLDIqUNhLjA"
#         # Replace with your actual token
#     }
#     response = requests.get(url=api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()
#         api_data2 = api_data['message']
#
#         storage_data = {}
#         for serviceData in api_data2:
#             service_data = serviceData['service_data']
#             for service_data2 in service_data:
#                 if 'disk_used' in service_data2['metrix_name']:
#                     storage_data['disk_usage_percentage'] = service_data2['metrix_value']  # Store the percentage directly
#
#         return storage_data
#     else:
#         print(f"API Request Failed: {response.status_code}")
#         return None
#
#
# # Compare Disk (Storage) data
# def compare_data(ssh_data, api_data):
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#     print(f"SSH DATA: {ssh_data}")
#     print(f"API DATA: {api_data}")
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#
#     # Disk Usage Percentage Comparison
#     ssh_disk_usage_percentage = float(ssh_data.get('disk_usage_percentage', 0))
#     api_disk_usage_percentage = float(api_data.get('disk_usage_percentage', 0))
#
#     if api_disk_usage_percentage is not None:
#         if abs(ssh_disk_usage_percentage - api_disk_usage_percentage) <= 5:  # Allow a tolerance of 5%
#             print(f"Disk usage percentage matches: SSH={ssh_disk_usage_percentage}%, API={api_disk_usage_percentage}% (within 5%)")
#         else:
#             print(f"Disk usage percentage mismatch: SSH={ssh_disk_usage_percentage}%, API={api_disk_usage_percentage}% (difference > 5%)")
#     else:
#         print("Disk usage percentage data missing from API.")
#
#
# # Main execution
# if __name__ == "__main__":
#     print("Fetching system storage data from SSH...")
#     ssh_data = fetch_system_data()
#     print(ssh_data)
#     print("Fetching storage data from API...")
#     api_data = fetch_api_data()
#     print(api_data)
#
#     if api_data:
#         print("Comparing storage data...")
#         compare_data(ssh_data, api_data)
#     else:
#         print("Failed to fetch API data.")


#**************

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
# # Fetch system storage data via SSH
# def fetch_system_data():
#     # Fetch Disk usage in bytes and percentage (for root partition "/")
#     disk_bytes_command = "df --block-size=1 / | grep '/' | awk '{print $3}'"  # Fetch the used space in bytes
#     disk_used_bytes = execute_remote_command(disk_bytes_command)
#
#     disk_percentage_command = "df -h / | grep '/' | awk '{print $5}'"  # Fetch the usage percentage directly
#     disk_usage_percentage = execute_remote_command(disk_percentage_command).replace('%', '')  # Remove %
#
#     return {
#         "disk_used_bytes": disk_used_bytes,  # Disk used in bytes
#         "disk_usage_percentage": disk_usage_percentage  # Disk usage in percentage
#     }
#
#
# # Fetch storage data from API
# def fetch_api_data():
#     payload = {'host_name': 'zcsit', 'service_name': 'disk'}
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI4ODc4ODYxNzUyLCJpYXQiOjE3Mjg4Nzg4NjEsImV4cCI6MTcyODk2NTI2MX0.Ef_o8MKUV3NuDN1w8QnqoK6esImiA6kghiTDzm_vJt8ZyWojlpGft4rnKv1LmdQD-WuwJNlpO09oLDIqUNhLjA"
#         # Replace with your actual token
#     }
#     response = requests.get(url=api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()
#         api_data2 = api_data['message']
#
#         storage_data = {}
#         for serviceData in api_data2:
#             service_data = serviceData['service_data']
#             for service_data2 in service_data:
#                 if 'disk_used_bytes' in service_data2['metrix_name']:
#                     storage_data['disk_used_bytes'] = service_data2['metrix_value']
#                 elif 'disk_usage_percentage' in service_data2['metrix_name']:
#                     storage_data['disk_usage_percentage'] = service_data2['metrix_value']
#
#         return storage_data
#     else:
#         print(f"API Request Failed: {response.status_code}")
#         return None
#
#
# # Compare Disk (Storage) data
# def compare_data(ssh_data, api_data):
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#     print(f"SSH DATA: {ssh_data}")
#     print(f"API DATA: {api_data}")
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#
#     # Disk Usage Bytes Comparison
#     ssh_disk_used_bytes = int(ssh_data.get('disk_used_bytes', 0))
#     api_disk_used_bytes = int(api_data.get('disk_used_bytes', 0))
#
#     if api_disk_used_bytes:
#         if abs(ssh_disk_used_bytes - api_disk_used_bytes) <= (ssh_disk_used_bytes * 0.05):  # Allow 5% tolerance
#             print(f"Disk used bytes matches: SSH={ssh_disk_used_bytes} bytes, API={api_disk_used_bytes} bytes (within 5%)")
#         else:
#             print(f"Disk used bytes mismatch: SSH={ssh_disk_used_bytes} bytes, API={api_disk_used_bytes} bytes (difference > 5%)")
#
#     # Disk Usage Percentage Comparison
#     ssh_disk_usage_percentage = float(ssh_data.get('disk_usage_percentage', 0))
#     api_disk_usage_percentage = float(api_data.get('disk_usage_percentage', 0))
#
#     if api_disk_usage_percentage:
#         if abs(ssh_disk_usage_percentage - api_disk_usage_percentage) <= 5:  # Allow 5% tolerance
#             print(f"Disk usage percentage matches: SSH={ssh_disk_usage_percentage}%, API={api_disk_usage_percentage}% (within 5%)")
#         else:
#             print(f"Disk usage percentage mismatch: SSH={ssh_disk_usage_percentage}%, API={api_disk_usage_percentage}% (difference > 5%)")
#     else:
#         print("Disk usage percentage data missing from API.")
#
#
# # Main execution
# if __name__ == "__main__":
#     print("Fetching system storage data from SSH...")
#     ssh_data = fetch_system_data()
#     print(ssh_data)
#     print("Fetching storage data from API...")
#     api_data = fetch_api_data()
#     print(api_data)
#
#     if api_data:
#         print("Comparing storage data...")
#         compare_data(ssh_data, api_data)
#     else:
#         print("Failed to fetch API data.")



#%%%%%%%%%%%%%%
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
# # Fetch system storage data via SSH
# def fetch_system_data():
#     # Fetch Disk usage in bytes and percentage (for root partition "/")
#     disk_bytes_command = "df --block-size=1 / | grep '/' | awk '{print $3}'"  # Fetch the used space in bytes
#     disk_used_bytes = execute_remote_command(disk_bytes_command)
#
#     disk_percentage_command = "df -h / | grep '/' | awk '{print $5}'"  # Fetch the usage percentage directly
#     disk_usage_percentage = execute_remote_command(disk_percentage_command).replace('%', '')  # Remove %
#
#     return {
#         "disk_used_bytes": disk_used_bytes,  # Disk used in bytes
#         "disk_usage_percentage": disk_usage_percentage  # Disk usage in percentage
#     }
#
#
# # Fetch storage data from API
# def fetch_api_data():
#     payload = {'host_name': 'zcsit', 'service_name': 'disk'}
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI4ODc4ODYxNzUyLCJpYXQiOjE3Mjg4Nzg4NjEsImV4cCI6MTcyODk2NTI2MX0.Ef_o8MKUV3NuDN1w8QnqoK6esImiA6kghiTDzm_vJt8ZyWojlpGft4rnKv1LmdQD-WuwJNlpO09oLDIqUNhLjA"
#         # Replace with your actual token
#     }
#     response = requests.get(url=api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()
#         api_data2 = api_data['message']
#
#         storage_data = {}
#         for serviceData in api_data2:
#             service_data = serviceData['service_data']
#             for service_data2 in service_data:
#                 if 'disk_used_bytes' in service_data2['metrix_name']:
#                     storage_data['disk_used_bytes'] = service_data2['metrix_value']
#                 elif 'disk_usage_percentage' in service_data2['metrix_name']:
#                     storage_data['disk_usage_percentage'] = service_data2['metrix_value']
#
#         return storage_data
#     else:
#         print(f"API Request Failed: {response.status_code}")
#         return None
#
#
# # Compare Disk (Storage) data for both bytes and percentage
# def compare_data(ssh_data, api_data):
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#     print(f"SSH DATA: {ssh_data}")
#     print(f"API DATA: {api_data}")
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#
#     # Disk Usage Bytes Comparison
#     ssh_disk_used_bytes = int(ssh_data.get('disk_used_bytes', 0))
#     api_disk_used_bytes = int(api_data.get('disk_used_bytes', 0))
#
#     if api_disk_used_bytes:
#         if abs(ssh_disk_used_bytes - api_disk_used_bytes) <= (ssh_disk_used_bytes * 0.05):  # Allow 5% tolerance
#             print(f"Disk used bytes matches: SSH={ssh_disk_used_bytes} bytes, API={api_disk_used_bytes} bytes (within 5%)")
#         else:
#             print(f"Disk used bytes mismatch: SSH={ssh_disk_used_bytes} bytes, API={api_disk_used_bytes} bytes (difference > 5%)")
#     else:
#         print("Disk used bytes data missing from API.")
#
#     # Disk Usage Percentage Comparison
#     ssh_disk_usage_percentage = float(ssh_data.get('disk_usage_percentage', 0))
#     api_disk_usage_percentage = float(api_data.get('disk_usage_percentage', 0))
#
#     if api_disk_usage_percentage:
#         if abs(ssh_disk_usage_percentage - api_disk_usage_percentage) <= 5:  # Allow 5% tolerance
#             print(f"Disk usage percentage matches: SSH={ssh_disk_usage_percentage}%, API={api_disk_usage_percentage}% (within 5%)")
#         else:
#             print(f"Disk usage percentage mismatch: SSH={ssh_disk_usage_percentage}%, API={api_disk_usage_percentage}% (difference > 5%)")
#     else:
#         print("Disk usage percentage data missing from API.")
#
#
# # Main execution
# if __name__ == "__main__":
#     print("Fetching system storage data from SSH...")
#     ssh_data = fetch_system_data()
#     print(ssh_data)
#     print("Fetching storage data from API...")
#     api_data = fetch_api_data()
#     print(api_data)
#
#     if api_data:
#         print("Comparing storage data for disk_used_bytes and disk_usage_percentage...")
#         compare_data(ssh_data, api_data)
#     else:
#         print("Failed to fetch API data.")


#****************************

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
# # Fetch system storage data via SSH
# def fetch_system_data():
#     # Fetch Disk usage in bytes and percentage (for root partition "/")
#     disk_bytes_command = "df --block-size=1 / | grep '/' | awk '{print $3}'"  # Fetch the used space in bytes
#     disk_used_bytes = execute_remote_command(disk_bytes_command)
#
#     disk_percentage_command = "df -h / | grep '/' | awk '{print $5}'"  # Fetch the usage percentage directly
#     disk_usage_percentage = execute_remote_command(disk_percentage_command).replace('%', '')  # Remove %
#
#     return {
#         "disk_used_bytes": disk_used_bytes,  # Disk used in bytes
#         "disk_usage_percentage": disk_usage_percentage  # Disk usage in percentage
#     }
#
#
# # Fetch storage data from API
# def fetch_api_data():
#     payload = {'host_name': 'zcsit', 'service_name': 'disk'}
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI4ODc4ODYxNzUyLCJpYXQiOjE3Mjg4Nzg4NjEsImV4cCI6MTcyODk2NTI2MX0.Ef_o8MKUV3NuDN1w8QnqoK6esImiA6kghiTDzm_vJt8ZyWojlpGft4rnKv1LmdQD-WuwJNlpO09oLDIqUNhLjA"
#         # Replace with your actual token
#     }
#     response = requests.get(url=api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()
#         api_data2 = api_data['message']
#
#         storage_data = {}
#         for serviceData in api_data2:
#             service_data = serviceData['service_data']
#             for service_data2 in service_data:
#                 if 'disk_used_bytes' in service_data2['metrix_name']:
#                     storage_data['disk_used_bytes'] = service_data2['metrix_value']
#                 elif 'disk_usage_percentage' in service_data2['metrix_name']:
#                     storage_data['disk_usage_percentage'] = service_data2['metrix_value']
#
#         return storage_data
#     else:
#         print(f"API Request Failed: {response.status_code}")
#         return None
#
#
# # Compare Disk (Storage) data for both bytes and percentage
# def compare_data(ssh_data, api_data):
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#     print(f"SSH DATA: {ssh_data}")
#     print(f"API DATA: {api_data}")
#     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
#
#     # Disk Usage Bytes Comparison
#     ssh_disk_used_bytes = int(ssh_data.get('disk_used_bytes', 0))
#     api_disk_used_bytes = int(api_data.get('disk_used_bytes', 0))
#
#     if api_disk_used_bytes:
#         if abs(ssh_disk_used_bytes - api_disk_used_bytes) <= (ssh_disk_used_bytes * 0.05):  # Allow 5% tolerance
#             print(f"Disk used bytes matches: SSH={ssh_disk_used_bytes} bytes, API={api_disk_used_bytes} bytes (within 5%)")
#         else:
#             print(f"Disk used bytes mismatch: SSH={ssh_disk_used_bytes} bytes, API={api_disk_used_bytes} bytes (difference > 5%)")
#     else:
#         print("Disk used bytes data missing from API.")
#
#     # Disk Usage Percentage Comparison
#     ssh_disk_usage_percentage = float(ssh_data.get('disk_usage_percentage', 0))
#     api_disk_usage_percentage = float(api_data.get('disk_usage_percentage', 0))
#
#     if api_disk_usage_percentage:
#         if abs(ssh_disk_usage_percentage - api_disk_usage_percentage) <= 5:  # Allow 5% tolerance
#             print(f"Disk usage percentage matches: SSH={ssh_disk_usage_percentage}%, API={api_disk_usage_percentage}% (within 5%)")
#         else:
#             print(f"Disk usage percentage mismatch: SSH={ssh_disk_usage_percentage}%, API={api_disk_usage_percentage}% (difference > 5%)")
#     else:
#         print("Disk usage percentage data missing from API.")
#
#
# # Main execution
# if __name__ == "__main__":
#     print("Fetching system storage data from SSH...")
#     ssh_data = fetch_system_data()
#     print(ssh_data)
#     print("Fetching storage data from API...")
#     api_data = fetch_api_data()
#     print(api_data)
#
#     if api_data:
#         print("Comparing storage data for disk_used_bytes and disk_usage_percentage...")
#         compare_data(ssh_data, api_data)
#     else:
#         print("Failed to fetch API data.")

#17-10-2024

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
# api_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI5MDc5NDY2MTAxLCJpYXQiOjE3MjkwNzk0NjYsImV4cCI6MTcyOTE2NTg2Nn0.YDUNhxIniCE7mBYmof_jEkoz6aYY06d-uipSJMguy8ENMNb1xJQm8NaokaVReynz-t3by_gZQlBTJYEYoD9pww"  # Replace with your valid API token
#
# # Windows Commands for Disk
# windows_disk_command = """
# Get-WmiObject Win32_LogicalDisk | ForEach-Object {
#     @{'DeviceID' = $_.DeviceID;
#       'FreeSpace' = [math]::round($_.FreeSpace / 1GB, 2);
#       'Size' = [math]::round($_.Size / 1GB, 2);
#       'UsedSpace' = [math]::round(($_.Size - $_.FreeSpace) / 1GB, 2)}
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
# # Fetch disk data from Windows server
# def fetch_windows_disk_data():
#     print("Fetching disk usage from Windows server...")
#     disk_usage = execute_windows_command(windows_disk_command)
#
#     if disk_usage:
#         disk_data = []
#         for disk in disk_usage.splitlines():
#             if disk.startswith("@{"):
#                 fields = {}
#                 for entry in disk.replace("@{", "").replace("}", "").split(';'):
#                     key, value = entry.split('=')
#                     fields[key.strip()] = float(value.strip())
#                 disk_data.append(fields)
#
#         return disk_data
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
# # Fetch disk data from Linux server
# def fetch_linux_disk_data():
#     disk_command = "df -h --output=source,size,used,avail | tail -n +2"
#
#     print("Fetching disk usage from Linux server...")
#     disk_usage = execute_linux_command(disk_command).splitlines()
#
#     disk_data = []
#     for line in disk_usage:
#         disk_info = line.split()
#         disk_data.append({
#             "DeviceID": disk_info[0],
#             "Size": disk_info[1],
#             "UsedSpace": disk_info[2],
#             "FreeSpace": disk_info[3]
#         })
#
#     return disk_data
#
#
# # Fetch API data for each server (disk-related)
# def fetch_api_disk_data(server_name):
#     payload = {'host_name': server_name, 'service_name': 'disk'}
#     headers = {
#         "Authorization": f"Bearer {api_token}"
#     }
#     response = requests.get(api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()['message']
#         disk_data = []
#         for serviceData in api_data:
#             for service_data in serviceData['service_data']:
#                 if 'disk_total' in service_data['metrix_name']:
#                     disk_data.append({
#                         "disk_total": float(service_data['metrix_value'])
#                     })
#                 if 'disk_used' in service_data['metrix_name']:
#                     disk_data.append({
#                         "disk_used": float(service_data['metrix_value'])
#                     })
#                 if 'disk_free' in service_data['metrix_name']:
#                     disk_data.append({
#                         "disk_free": float(service_data['metrix_value'])
#                     })
#         return disk_data
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
# # Generate disk report
# def generate_disk_report(ssh_data, api_data):
#     table = PrettyTable()
#     table.field_names = ["Metrics", "SSH Value", "API Value", "Status"]
#     report_data = []
#
#     for disk in ssh_data:
#         ssh_size = disk['Size']
#         ssh_used = disk['UsedSpace']
#         ssh_free = disk['FreeSpace']
#
#         # We assume API returns a similar disk structure, adjust comparison accordingly
#         api_disk = next((api for api in api_data if api.get('disk_total') == ssh_size), None)
#
#         api_size = api_disk['disk_total'] if api_disk else None
#         api_used = api_disk['disk_used'] if api_disk else None
#         api_free = api_disk['disk_free'] if api_disk else None
#
#         report_data.append({
#             "metric": f"Disk {disk['DeviceID']} Size",
#             "ssh_value": f"{ssh_size} GB",
#             "api_value": f"{api_size} GB" if api_size else "N/A",
#             "status": compare_values(ssh_size, api_size)
#         })
#         report_data.append({
#             "metric": f"Disk {disk['DeviceID']} Used Space",
#             "ssh_value": f"{ssh_used} GB",
#             "api_value": f"{api_used} GB" if api_used else "N/A",
#             "status": compare_values(ssh_used, api_used)
#         })
#         report_data.append({
#             "metric": f"Disk {disk['DeviceID']} Free Space",
#             "ssh_value": f"{ssh_free} GB",
#             "api_value": f"{api_free} GB" if api_free else "N/A",
#             "status": compare_values(ssh_free, api_free)
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
#     html_content = template.render(
#         windows_table=windows_report_data,
#         linux_table=linux_report_data,
#     )
#
#     with open("disk_report.html", "w") as f:
#         f.write(html_content)
#     print("HTML report generated successfully.")
#
#
# # Main execution
# if __name__ == "__main__":
#     print("Fetching disk data from Windows Server...")
#     windows_disk_data = fetch_windows_disk_data()
#     print("Windows Disk Data:", windows_disk_data)
#
#     print("Fetching disk data from Linux Server...")
#     linux_disk_data = fetch_linux_disk_data()
#     print("Linux Disk Data:", linux_disk_data)
#
#     print("Fetching disk data from API for Windows Server...")
#     windows_api_disk_data = fetch_api_disk_data('ZCS-SERVER')  # Replace with your Windows server name
#     print("Windows API Disk Data:", windows_api_disk_data)
#
#     print("Fetching disk data from API for Linux Server...")
#     linux_api_disk_data = fetch_api_disk_data('zcsit')  # Replace with your Linux server name
#     print("Linux API Disk Data:", linux_api_disk_data)
#
#     # Generate reports for both servers
#     windows_report_data = generate_disk_report(windows_disk_data, windows_api_disk_data)
#     linux_report_data = generate_disk_report(linux_disk_data, linux_api_disk_data)
#
#     print("Windows Report Data:", windows_report_data)
#     print("Linux Report Data:", linux_report_data)
#
#     # Generate HTML report
#     generate_html_report(windows_report_data, linux_report_data)


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
# api_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI5MDc5NDY2MTAxLCJpYXQiOjE3MjkwNzk0NjYsImV4cCI6MTcyOTE2NTg2Nn0.YDUNhxIniCE7mBYmof_jEkoz6aYY06d-uipSJMguy8ENMNb1xJQm8NaokaVReynz-t3by_gZQlBTJYEYoD9pww"  # Replace with your valid API token
#
# # Windows Commands for Disk C:\
# windows_disk_command = """
# Get-WmiObject Win32_LogicalDisk | Where-Object { $_.DeviceID -eq 'C:' } | ForEach-Object {
#     @{'DeviceID' = $_.DeviceID;
#       'FreeSpace' = [math]::round($_.FreeSpace / 1GB, 2);
#       'Size' = [math]::round($_.Size / 1GB, 2);
#       'UsedSpace' = [math]::round(($_.Size - $_.FreeSpace) / 1GB, 2)}
# }
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
# # Fetch disk data from Windows server for C:\
# def fetch_windows_disk_data():
#     print("Fetching disk usage from Windows server...")
#     disk_usage = execute_windows_command(windows_disk_command)
#
#     if disk_usage:
#         disk_data = []
#         for disk in disk_usage.splitlines():
#             if disk.startswith("@{"):
#                 fields = {}
#                 for entry in disk.replace("@{", "").replace("}", "").split(';'):
#                     key, value = entry.split('=')
#                     fields[key.strip()] = float(value.strip())
#                 disk_data.append(fields)
#         return disk_data
#     else:
#         return None
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
# # Fetch disk data from Linux server for root "/"
# def fetch_linux_disk_data():
#     disk_command = "df -h --output=source,size,used,avail | grep '^/dev/' | grep ' /$'"
#     print("Fetching disk usage from Linux server...")
#     disk_usage = execute_linux_command(disk_command).splitlines()
#
#     disk_data = []
#     for line in disk_usage:
#         disk_info = line.split()
#         disk_data.append({
#             "DeviceID": disk_info[0],
#             "Size": disk_info[1],
#             "UsedSpace": disk_info[2],
#             "FreeSpace": disk_info[3]
#         })
#     return disk_data
#
# # Fetch API data for each server (disk-related)
# def fetch_api_disk_data(server_name):
#     payload = {'host_name': server_name, 'service_name': 'disk'}
#     headers = {
#         "Authorization": f"Bearer {api_token}"
#     }
#     response = requests.get(api_url, params=payload, headers=headers)
#     if response.status_code == 200:
#         api_data = response.json()['message']
#         disk_data = []
#         for serviceData in api_data:
#             for service_data in serviceData['service_data']:
#                 if 'disk_total' in service_data['metrix_name']:
#                     disk_data.append({
#                         "disk_total": float(service_data['metrix_value'])
#                     })
#                 if 'disk_used' in service_data['metrix_name']:
#                     disk_data.append({
#                         "disk_used": float(service_data['metrix_value'])
#                     })
#                 if 'disk_free' in service_data['metrix_name']:
#                     disk_data.append({
#                         "disk_free": float(service_data['metrix_value'])
#                     })
#         return disk_data
#     else:
#         print(f"API Request Failed: {response.status_code}")
#         return None
#
# # Function to compare values
# def compare_values(ssh_value, api_value):
#     if api_value is None:
#         return "fail"
#     difference = abs(ssh_value - api_value) / ssh_value * 100
#     return "passed" if difference <= 10 else "failed"
#
# # Generate disk report
# def generate_disk_report(ssh_data, api_data):
#     table = PrettyTable()
#     table.field_names = ["Metrics", "SSH Value", "API Value", "Status"]
#     report_data = []
#
#     for disk in ssh_data:
#         ssh_size = disk['Size']
#         ssh_used = disk['UsedSpace']
#         ssh_free = disk['FreeSpace']
#
#         # We assume API returns a similar disk structure, adjust comparison accordingly
#         api_disk = next((api for api in api_data if api.get('disk_total') == ssh_size), None)
#
#         api_size = api_disk['disk_total'] if api_disk else None
#         api_used = api_disk['disk_used'] if api_disk else None
#         api_free = api_disk['disk_free'] if api_disk else None
#
#         report_data.append({
#             "metric": f"Disk {disk['DeviceID']} Size",
#             "ssh_value": f"{ssh_size} GB",
#             "api_value": f"{api_size} GB" if api_size else "N/A",
#             "status": compare_values(ssh_size, api_size)
#         })
#         report_data.append({
#             "metric": f"Disk {disk['DeviceID']} Used Space",
#             "ssh_value": f"{ssh_used} GB",
#             "api_value": f"{api_used} GB" if api_used else "N/A",
#             "status": compare_values(ssh_used, api_used)
#         })
#         report_data.append({
#             "metric": f"Disk {disk['DeviceID']} Free Space",
#             "ssh_value": f"{ssh_free} GB",
#             "api_value": f"{api_free} GB" if api_free else "N/A",
#             "status": compare_values(ssh_free, api_free)
#         })
#
#     for row in report_data:
#         table.add_row([row['metric'], row['ssh_value'], row['api_value'], row['status']])
#
#     print(table)
#     return report_data
#
# # Generate HTML report
# def generate_html_report(windows_report_data, linux_report_data):
#     env = Environment(loader=FileSystemLoader('.'))
#     template = env.get_template('report_template.html')
#
#     html_content = template.render(
#         windows_table=windows_report_data,
#         linux_table=linux_report_data,
#     )
#
#     with open("disk_report.html", "w") as f:
#         f.write(html_content)
#     print("HTML report generated successfully.")
#
# # Main execution
# if __name__ == "__main__":
#     print("Fetching disk data from Windows Server (C:)...")
#     windows_disk_data = fetch_windows_disk_data()
#     print("Windows Disk Data:", windows_disk_data)
#
#     print("Fetching disk data from Linux Server (/)...")
#     linux_disk_data = fetch_linux_disk_data()
#     print("Linux Disk Data:", linux_disk_data)
#
#     print("Fetching disk data from API for Windows Server...")
#     windows_api_disk_data = fetch_api_disk_data('ZCS-SERVER')  # Replace with your Windows server name
#     print("Windows API Disk Data:", windows_api_disk_data)
#
#     print("Fetching disk data from API for Linux Server...")
#     linux_api_disk_data = fetch_api_disk_data('zcsit')  # Replace with your Linux server name
#     print("Linux API Disk Data:", linux_api_disk_data)
#
#     # Generate reports for both servers
#     windows_report_data = generate_disk_report(windows_disk_data, windows_api_disk_data)
#     linux_report_data = generate_disk_report(linux_disk_data, linux_api_disk_data)
#
#     print("Windows Report Data:", windows_report_data)
#     print("Linux Report Data:", linux_report_data)
#
#     # Generate HTML report
#     generate_html_report(windows_report_data, linux_report_data)


# import paramiko
# import winrm
# from jinja2 import Environment, FileSystemLoader
#
# # Configuration for SSH
# windows_hostname = "10.192.1.77"
# windows_username = "tulsiram"
# windows_password = "nMuZ3XcF87zq4tsG65NfkA"
# linux_hostname = "192.168.1.81"
# linux_username = "tulasi"
# linux_password = "Nop@ssw0rd"
# linux_port = 20202  # SSH port for Linux
#
# # Fetch disk data from Windows Server
# def execute_windows_command(command):
#     session = winrm.Session(f'http://{windows_hostname}:5985/wsman', auth=(windows_username, windows_password), transport='ntlm')
#     try:
#         result = session.run_ps(command)
#         output = result.std_out.decode('utf-8').strip()
#         print(f"Raw Windows SSH Output: {output}")
#         return output
#     except Exception as e:
#         print(f"Failed to connect to Windows server: {e}")
#         return None
#
# # Fetch disk data from Linux Server
# def execute_linux_command(command):
#     try:
#         client = paramiko.SSHClient()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect(linux_hostname, port=linux_port, username=linux_username, password=linux_password)
#         stdin, stdout, stderr = client.exec_command(command)
#         output = stdout.read().decode('utf-8')
#         print(f"Raw Linux SSH Output: {output}")
#         client.close()
#         return output.strip()
#     except Exception as e:
#         print(f"Failed to connect to Linux server: {e}")
#         return None
#
# # Fetch Windows disk data via PowerShell
# def fetch_windows_disk_data():
#     command = """
#     Get-WmiObject Win32_LogicalDisk | Where-Object { $_.DeviceID -eq 'C:' } | ForEach-Object {
#         @{'DeviceID' = $_.DeviceID;
#           'FreeSpace' = [math]::round($_.FreeSpace / 1GB, 2);
#           'Size' = [math]::round($_.Size / 1GB, 2);
#           'UsedSpace' = [math]::round(($_.Size - $_.FreeSpace) / 1GB, 2)}
#     }
#     """
#     return execute_windows_command(command)
#
# # Fetch Linux disk data via SSH (for root partition '/')
# def fetch_linux_disk_data():
#     command = "df -h --output=source,size,used,avail | grep '^/dev/' | grep ' /$'"
#     return execute_linux_command(command)
#
# # Fetch API disk data (dummy data used for example)
# def fetch_api_disk_data_for_windows():
#     # Simulating API response data
#     return [
#         {'disk_total': 106728255488.0, 'disk_free': 67599990784.0, 'disk_used': 39128264704.0}
#     ]
#
# def fetch_api_disk_data_for_linux():
#     # Simulating API response data
#     return [
#         {'disk_total': 50000000000.0, 'disk_free': 20000000000.0, 'disk_used': 30000000000.0}
#     ]
#
# # Prepare data for report
# def prepare_report_data(disk_data_ssh, disk_data_api):
#     report_data = []
#     if disk_data_ssh and disk_data_api:
#         # Assuming API returns total, free, and used space in bytes
#         ssh_values = disk_data_ssh.split()  # Process SSH raw output here
#         report_data.append({
#             'Metrics': 'Disk Total (GB)',
#             'SSH Value': ssh_values[1],  # Modify based on your data structure
#             'API Value': round(disk_data_api[0]['disk_total'] / (1024**3), 2),
#             'Status': 'Pass' if ssh_values[1] == round(disk_data_api[0]['disk_total'] / (1024**3), 2) else 'Fail'
#         })
#         # Add more comparisons for free and used space
#     return report_data
#
# # Generate HTML report
# def generate_html_report(windows_data, linux_data):
#     env = Environment(loader=FileSystemLoader('.'))
#     template = env.get_template('report_template.html')
#
#     output = template.render(windows_data=windows_data, linux_data=linux_data)
#     with open('disk_report.html', 'w') as f:
#         f.write(output)
#     print("HTML report generated successfully.")
#
# # Main logic
# def main():
#     print("Fetching disk data from Windows Server (C:)...")
#     windows_ssh_data = fetch_windows_disk_data()
#     print("Fetching disk data from Linux Server (/)...")
#     linux_ssh_data = fetch_linux_disk_data()
#
#     print("Fetching disk data from API for Windows Server...")
#     windows_api_data = fetch_api_disk_data_for_windows()
#     print("Fetching disk data from API for Linux Server...")
#     linux_api_data = fetch_api_disk_data_for_linux()
#
#     # Prepare report data
#     windows_report_data = prepare_report_data(windows_ssh_data, windows_api_data)
#     linux_report_data = prepare_report_data(linux_ssh_data, linux_api_data)
#
#     # Generate HTML report
#     generate_html_report(windows_report_data, linux_report_data)
#
# if __name__ == "__main__":
#     main()


#--------------------------

import paramiko
import subprocess
import psutil
from jinja2 import Environment, FileSystemLoader
import os


# Function to execute SSH commands on a Linux server
def execute_linux_command(command):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname='192.168.1.81', port=20202, username='your_username', password='your_password')

        stdin, stdout, stderr = client.exec_command(command)
        result = stdout.read().decode()
        client.close()
        return result.strip()
    except Exception as e:
        print(f"Error executing command on Linux: {e}")
        return ""


# Function to fetch disk data from Linux
def fetch_linux_disk_data():
    # You can change this command to suit your environment
    command = "df -h --output=source,size,used,avail | grep '^/dev/' | grep ' /$'"
    return execute_linux_command(command)


# Function to fetch disk data from Windows via PowerShell
def fetch_windows_disk_data():
    try:
        command = "powershell \"Get-PSDrive -PSProvider FileSystem | Where-Object { $_.DeviceID -eq 'C:' } | Select-Object FreeSpace, Size, DeviceID, @{Name='UsedSpace';Expression={[math]::round(($_.Used/1GB),2)}}\""
        result = subprocess.check_output(command, shell=True)
        return result.decode().strip()
    except Exception as e:
        print(f"Error executing command on Windows: {e}")
        return ""


# Dummy API function to fetch disk data from an API
def fetch_api_disk_data(os_type):
    # You should replace this with actual API calls
    if os_type == 'windows':
        return [{'disk_total': 106728255488.0, 'disk_free': 67599990784.0, 'disk_used': 39128264704.0}]
    elif os_type == 'linux':
        return [{'disk_total': 40763392.0, 'disk_free': 1652318208.0, 'disk_used': 263905280.0}]
    return []


# Function to prepare report data
def prepare_report_data(disk_data_ssh, disk_data_api):
    report_data = []

    # Handling Windows SSH data
    if disk_data_ssh and disk_data_api:
        ssh_lines = disk_data_ssh.splitlines()
        ssh_data = {}

        # Parsing SSH data from Windows
        for line in ssh_lines:
            if "FreeSpace" in line:
                ssh_data['disk_free'] = float(line.split()[-1])
            elif "Size" in line:
                ssh_data['disk_total'] = float(line.split()[-1])
            elif "UsedSpace" in line:
                ssh_data['disk_used'] = float(line.split()[-1])

        # Prepare comparison data
        report_data.append({
            'Metrics': 'Disk Total (GB)',
            'SSH Value': ssh_data.get('disk_total', 0),
            'API Value': round(disk_data_api[0]['disk_total'] / (1024 ** 3), 2),
            'Status': 'Pass' if ssh_data.get('disk_total', 0) == round(disk_data_api[0]['disk_total'] / (1024 ** 3),
                                                                       2) else 'Fail'
        })
        report_data.append({
            'Metrics': 'Disk Free (GB)',
            'SSH Value': ssh_data.get('disk_free', 0),
            'API Value': round(disk_data_api[0]['disk_free'] / (1024 ** 3), 2),
            'Status': 'Pass' if ssh_data.get('disk_free', 0) == round(disk_data_api[0]['disk_free'] / (1024 ** 3),
                                                                      2) else 'Fail'
        })
        report_data.append({
            'Metrics': 'Disk Used (GB)',
            'SSH Value': ssh_data.get('disk_used', 0),
            'API Value': round(disk_data_api[0]['disk_used'] / (1024 ** 3), 2),
            'Status': 'Pass' if ssh_data.get('disk_used', 0) == round(disk_data_api[0]['disk_used'] / (1024 ** 3),
                                                                      2) else 'Fail'
        })

    return report_data


# Function to generate an HTML report using Jinja2
def generate_html_report(windows_report_data, linux_report_data):
    # Load the Jinja2 template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('report_template.html')

    # Render the HTML with the provided data
    html_content = template.render(windows_report_data=windows_report_data, linux_report_data=linux_report_data)

    # Save the HTML to a file
    with open('disk_report.html', 'w') as f:
        f.write(html_content)

    print("HTML report generated successfully.")


# Main function to run the process
def main():
    print("Fetching disk data from Windows Server (C:)...")
    windows_ssh_output = fetch_windows_disk_data()
    print(f"Raw Windows SSH Output: {windows_ssh_output}")

    print("Fetching disk data from Linux Server (/)...")
    linux_ssh_output = fetch_linux_disk_data()
    print(f"Raw Linux SSH Output: {linux_ssh_output}")

    print("Fetching disk data from API for Windows Server...")
    windows_api_data = fetch_api_disk_data('windows')

    print("Fetching disk data from API for Linux Server...")
    linux_api_data = fetch_api_disk_data('linux')

    # Prepare the report data for both Windows and Linux
    windows_report_data = prepare_report_data(windows_ssh_output, windows_api_data)
    linux_report_data = prepare_report_data(linux_ssh_output, linux_api_data)

    # Generate the HTML report
    generate_html_report(windows_report_data, linux_report_data)


if __name__ == "__main__":
    main()





