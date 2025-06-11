import socket
from datetime import datetime

def scan_ports(target, start_port, end_port):
    print(f"\nStarting scan on target: {target}")
    print(f"Scanning ports from {start_port} to {end_port}...")

    # Record the start time
    start_time = datetime.now()

    try:
        # Loop through the specified port range
        for port in range(start_port, end_port + 1):
            # Create a socket object
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)  # Set timeout for the connection

            # Attempt to connect to the target on the specified port
            result = sock.connect_ex((target, port))

            # If the result is 0, the port is open
            if result == 0:
                print(f"Port {port}: OPEN")

            # Close the socket
            sock.close()

    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        return

    except socket.gaierror:
        print("\nError: Hostname could not be resolved.")
        return

    except socket.error:
        print("\nError: Unable to connect to the target.")
        return

    # Record the end time
    end_time = datetime.now()
    total_time = end_time - start_time

    print(f"\nScan completed in {total_time}")

if __name__ == "__main__":
    # Input target and port range
    target = input("Enter the target IP or hostname: ").strip()
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    # Run the port scanner
    scan_ports(target, start_port, end_port)
