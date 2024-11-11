import paramiko

# Define server connection details
hostname = '192.168.1.81'
port = 20202
username = 'tulasi'
password = 'Nop@ssw0rd'


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


# Fetch network data via SSH (Tx and Rx packets for interface 'lo')
def fetch_network_data():
    # Fetch network details: Tx and Rx packets for interface 'lo'
    network_command = "ifconfig lo | grep 'TX packets\\|RX packets'"
    network_data = execute_remote_command(network_command).strip().splitlines()

    # Check if we received the expected data
    if len(network_data) < 2:
        print("Error: Expected network data not found.")
        return {"tx_packets_lo": None, "rx_packets_lo": None}

    # Extracting Tx and Rx packets for interface lo
    tx_packets_lo = network_data[0].split()[1].split(':')[1]  # Transmit packets
    rx_packets_lo = network_data[1].split()[1].split(':')[1]  # Receive packets

    return {
        "tx_packets_lo": tx_packets_lo,  # Transmit packets for interface lo
        "rx_packets_lo": rx_packets_lo   # Receive packets for interface lo
    }


# Main execution
if __name__ == "__main__":
    print("Fetching network data from SSH...")
    network_data = fetch_network_data()
    print(network_data)

