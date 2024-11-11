# import paramiko
#
# # Define server connection details
# hostname = '192.168.1.81'
# port = 20202
# username = 'tulasi'  # replace with your username on the server
# password = 'Nop@ssw0rd'  # replace with your password (or use key-based authentication)
#
# def execute_remote_command(command):
#     try:
#         # Create an SSH client
#         client = paramiko.SSHClient()
#
#         # Automatically add the server's SSH key (insecure, for testing purposes)
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#         # Connect to the server
#         client.connect(hostname, port=port, username=username, password=password)
#
#         # Execute the command
#         stdin, stdout, stderr = client.exec_command(command)
#
#         # Read the results
#         output = stdout.read().decode('utf-8')
#         error = stderr.read().decode('utf-8')
#
#         if error:
#             print(f"Error: {error}")
#         return output
#     except Exception as e:
#         print(f"Failed to connect: {e}")
#     finally:
#         # Close the connection
#         client.close()
#
# # Fetch CPU usage
# cpu_command = "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'"
# cpu_usage = execute_remote_command(cpu_command)
# print(f"CPU Usage: {cpu_usage}%")
#
# # Fetch memory usage
# memory_command = "free -m | awk 'NR==2{printf \"Memory Usage: %s/%sMB (%.2f%%)\", $3,$2,$3*100/$2 }'"
# memory_usage = execute_remote_command(memory_command)
# print(memory_usage)
#
# # Fetch disk usage
# disk_command = "df -h --total | grep 'total' | awk '{print $3 \"/\" $2 \" (\" $5 \")\"}'"
# disk_usage = execute_remote_command(disk_command)
# print(f"Disk Usage: {disk_usage}")

#======================

# import paramiko
#
# # Define server connection details
# hostname = '192.168.1.81'
# port = 20202
# username = 'tulasi'  # replace with your username on the server
# password = 'Nop@ssw0rd'  # replace with your password (or use key-based authentication)
#
# def execute_remote_command(command):
#     try:
#         # Create an SSH client
#         client = paramiko.SSHClient()
#
#         # Automatically add the server's SSH key (insecure, for testing purposes)
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#         # Connect to the server
#         client.connect(hostname, port=port, username=username, password=password)
#
#         # Execute the command
#         stdin, stdout, stderr = client.exec_command(command)
#
#         # Read the results
#         output = stdout.read().decode('utf-8')
#         error = stderr.read().decode('utf-8')
#
#         if error:
#             print(f"Error: {error}")
#         return output
#     except Exception as e:
#         print(f"Failed to connect: {e}")
#     finally:
#         # Close the connection
#         client.close()
#
# # Fetch CPU usage
# cpu_command = "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'"
# cpu_usage = execute_remote_command(cpu_command)
# print(f"CPU Usage: {cpu_usage}%")
#
# # Fetch memory usage
# memory_command = "free -m | awk 'NR==2{printf \"Memory Usage: %s/%sMB (%.2f%%)\", $3,$2,$3*100/$2 }'"
# memory_usage = execute_remote_command(memory_command)
# print(memory_usage)
#
# # Fetch disk usage for / and /boot partitions
# disk_command = "df -h | grep -E '^(/dev/|Filesystem)' | awk '$6==\"/\" || $6==\"/boot\" {print $6 \": \" $3 \"/\" $2 \" (\" $5 \")\"}'"
# disk_usage = execute_remote_command(disk_command)
# print("Disk Usage:")
# print(disk_usage)


#====================
import paramiko

# Define server connection details
hostname = '192.168.1.81'
port = 20202
username = 'tulasi'  # replace with your username on the server
password = 'Nop@ssw0rd'  # replace with your password (or use key-based authentication)

def execute_remote_command(command):
    try:
        # Create an SSH client
        client = paramiko.SSHClient()

        # Automatically add the server's SSH key (insecure, for testing purposes)
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the server
        client.connect(hostname, port=port, username=username, password=password)

        # Execute the command
        stdin, stdout, stderr = client.exec_command(command)

        # Read the results
        output = stdout.read().decode('utf-8')
        error = stderr.read().decode('utf-8')

        if error:
            print(f"Error: {error}")
        return output
    except Exception as e:
        print(f"Failed to connect: {e}")
    finally:
        # Close the connection
        client.close()

# Fetch CPU usage
cpu_command = "top -bn1 | grep 'Cpu(s)' | sed 's/.*, *\\([0-9.]*\\)%* id.*/\\1/' | awk '{print 100 - $1}'"
cpu_usage = execute_remote_command(cpu_command)
print(f"CPU Usage: {cpu_usage}%")

# Fetch detailed memory usage
memory_command = """
free -m | awk 'NR==2{printf "RAM Total: %sMB, RAM Used: %sMB, RAM Free: %sMB, RAM Used(%%): %.2f%%\\n", $2,$3,$4,$3*100/$2 }' &&
free -m | awk 'NR==3{printf "Swap Total: %sMB, Swap Used: %sMB, Swap Free: %sMB, Swap Used(%%): %.2f%%\\n", $2,$3,$4,$3*100/$2 }'
"""
memory_usage = execute_remote_command(memory_command)
print("Memory Usage:")
print(memory_usage)

# Fetch disk usage for / and /boot partitions
disk_command = "df -h | grep -E '^(/dev/|Filesystem)' | awk '$6==\"/\" || $6==\"/boot\" {print $6 \": \" $3 \"/\" $2 \" (\" $5 \")\"}'"
disk_usage = execute_remote_command(disk_command)
print("Disk Usage:")
print(disk_usage)

