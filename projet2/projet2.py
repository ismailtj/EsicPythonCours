import socket

def scan_ports(ip_address, ports):
    results = {}
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Timeout of 1 second
            result = s.connect_ex((ip_address, port))
            results[port] = 'open' if result == 0 else 'closed'
    return results

def main():
    ip_address = "127.0.0.1"
    ports_input = "80,3306,4000,".strip()
    
    try:
        ports = [int(port) for port in ports_input.split(',') if port.strip().isdigit()]
    except ValueError:
        print("Invalid port list. Please ensure all ports are integers.")
        return

    print(f"Scanning {ip_address} on ports: {ports}")
    results = scan_ports(ip_address, ports)
    for port, status in results.items():
        print(f"Port {port}: {status}")

if __name__ == "__main__":
    main()
