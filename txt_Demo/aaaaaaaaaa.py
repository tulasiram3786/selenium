
#  RAM FREE CONVERT TO BYTES
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


# Fetch system data via SSH
def fetch_system_data():
    # Fetch CPU usage
    cpu_command = "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'"
    cpu_usage = execute_remote_command(cpu_command)

    # Fetch detailed memory usage (in MB)
    memory_command = "free -m | awk 'NR==2{printf \"%s %s %s %.2f\", $2,$3,$4,$3*100/$2 }'"
    memory_usage = execute_remote_command(memory_command).split()
    ram_total_ssh, ram_used_ssh, ram_free_ssh, ram_percent_used_ssh = map(float, memory_usage)

    # Convert RAM free from MB to bytes
    ram_free_bytes_ssh = ram_free_ssh * 1024 * 1024

    # Fetch disk usage for / partition
    disk_command = "df -h | awk '$6==\"/\" {print $3 \"/\" $2 \" (\" $5 \")\"}'"
    disk_usage = execute_remote_command(disk_command)

    return {
        "cpu": round(float(cpu_usage), 2),  # Round to 2 decimal places
        "ram_total": round(ram_total_ssh / 1024, 2),  # Convert MB to GB and round to 2 decimal places
        "ram_used": round(ram_used_ssh / 1024, 2),  # Convert MB to GB and round to 2 decimal places
        "ram_free_bytes": round(ram_free_bytes_ssh),  # RAM free in bytes (no decimals needed)
        "ram_percent": round(ram_percent_used_ssh, 2),  # Round to 2 decimal places
        "disk": disk_usage
    }


# Fetch API data
def fetch_api_data():
    ram_data = {}
    payload = {'host_name': 'zcsit', 'service_name': 'ram'}
    headers = {
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImphY2suZGVtb0BnbWFpbC5jb20iLCJ0aW1lc3RhbXBzIjoxNzI4ODc4ODYxNzUyLCJpYXQiOjE3Mjg4Nzg4NjEsImV4cCI6MTcyODk2NTI2MX0.Ef_o8MKUV3NuDN1w8QnqoK6esImiA6kghiTDzm_vJt8ZyWojlpGft4rnKv1LmdQD-WuwJNlpO09oLDIqUNhLjA"
        # Replace with your actual token
    }
    response = requests.get(url=api_url, params=payload, headers=headers)
    if response.status_code == 200:
        api_data = response.json()
        api_data2 = api_data['message']

        ram_data = {}
        for serviceData in api_data2:
            service_data = serviceData['service_data']
            for service_data2 in service_data:
                if service_data2['metrix_name'] == 'ram_used':
                    ram_data['ram_used'] = float(service_data2['metrix_value'])  # Assuming API returns in GB
                if service_data2['metrix_name'] == 'ram_total':
                    ram_data['ram_total'] = float(service_data2['metrix_value'])  # Assuming API returns in GB
                if service_data2['metrix_name'] == 'ram_free_bytes':
                    ram_data['ram_free_bytes'] = float(service_data2['metrix_value'])  # Assuming API returns in bytes

        return ram_data
    else:
        print(f"API Request Failed: {response.status_code}")
        return None


# Compare the values with 10%-20% tolerance for RAM used, RAM total, and RAM free (in bytes)
def compare_data(ssh_data, api_data):
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(f"SSH DATA: {ssh_data}")
    print(f"API DATA: {api_data}")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    ssh_ram_used = ssh_data['ram_used']
    ssh_ram_total = ssh_data['ram_total']
    ssh_ram_free_bytes = ssh_data['ram_free_bytes']

    api_ram_used = api_data.get('ram_used', None)
    api_ram_total = api_data.get('ram_total', None)
    api_ram_free_bytes = api_data.get('ram_free_bytes', None)

    # RAM Used Comparison
    if api_ram_used is not None:
        tolerance_10_used = 0.1 * ssh_ram_used  # 10% tolerance
        tolerance_20_used = 0.2 * ssh_ram_used  # 20% tolerance
        difference_used = abs(ssh_ram_used - api_ram_used)

        if difference_used <= tolerance_10_used:
            print(f"RAM used matches: SSH={ssh_ram_used}GB, API={api_ram_used}GB (within 10%)")
        elif difference_used <= tolerance_20_used:
            print(f"RAM used partially matches: SSH={ssh_ram_used}GB, API={api_ram_used}GB (between 10%-20%)")
        else:
            print(f"RAM used mismatch: SSH={ssh_ram_used}GB, API={api_ram_used}GB (difference > 20%)")
    else:
        print("RAM used data missing from API.")

    # RAM Total Comparison
    if api_ram_total is not None:
        tolerance_10_total = 0.1 * ssh_ram_total  # 10% tolerance
        tolerance_20_total = 0.2 * ssh_ram_total  # 20% tolerance
        difference_total = abs(ssh_ram_total - api_ram_total)

        if difference_total <= tolerance_10_total:
            print(f"RAM total matches: SSH={ssh_ram_total}GB, API={api_ram_total}GB (within 10%)")
        elif difference_total <= tolerance_20_total:
            print(f"RAM total partially matches: SSH={ssh_ram_total}GB, API={api_ram_total}GB (between 10%-20%)")
        else:
            print(f"RAM total mismatch: SSH={ssh_ram_total}GB, API={api_ram_total}GB (difference > 20%)")
    else:
        print("RAM total data missing from API.")

    # RAM Free (in Bytes) Comparison
    if api_ram_free_bytes is not None:
        tolerance_10_free_bytes = 0.1 * ssh_ram_free_bytes  # 10% tolerance
        tolerance_20_free_bytes = 0.2 * ssh_ram_free_bytes  # 20% tolerance
        difference_free_bytes = abs(ssh_ram_free_bytes - api_ram_free_bytes)

        if difference_free_bytes <= tolerance_10_free_bytes:
            print(f"RAM free matches: SSH={ssh_ram_free_bytes} bytes, API={api_ram_free_bytes} bytes (within 10%)")
        elif difference_free_bytes <= tolerance_20_free_bytes:
            print(
                f"RAM free partially matches: SSH={ssh_ram_free_bytes} bytes, API={api_ram_free_bytes} bytes (between 10%-20%)")
        else:
            print(
                f"RAM free mismatch: SSH={ssh_ram_free_bytes} bytes, API={api_ram_free_bytes} bytes (difference > 20%)")
    else:
        print("RAM free data missing from API.")


# Main execution
if __name__ == "__main__":
    print("Fetching system data from SSH...")
    ssh_data = fetch_system_data()
    print(ssh_data)
    print("Fetching system data from API...")
    api_data = fetch_api_data()
    print(api_data)

    if api_data:
        print("Comparing system data...")
        compare_data(ssh_data, api_data)
    else:
        print("Failed to fetch API data.")













