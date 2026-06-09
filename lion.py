import socket
import sys
import os
from concurrent.futures import ThreadPoolExecutor

def show_menu():
    print(r"                  _      _____  ____  _   _ ")
    print(r"                 | |    |_   _|/ __ \| \ | |")
    print(r"                 | |      | | | |  | |  \| |")
    print(r"                 | |      | | | |  | | . ` |")
    print(r"                 | |____ _| |_| |__| | |\  |")
    print(r"                 |______|_____|\____/|_| \_|")
    print("                     SECURITY SCANNER v1.1")
    print("=" * 59)
    print(" [1] Ping / Check if Host/IP is Alive")
    print(" [2] Scan Common Ports (21, 22, 80, 443, 8080)")
    print(" [3] Scan Custom Port Range")
    print(" [4] Exit LION Tool")
    print("=" * 59)

def check_host(ip):
    print(f" [*] Pinging {ip}...")
    # Executes system ping command (Works on Linux/Termux)
    # -c 1 sends 1 packet, -W 2 sets timeout to 2 seconds
    response = os.system(f"ping -c 1 -W 2 {ip} > /dev/null 2>&1")
    if response == 0:
        print(f" ✅ Host {ip} is [ ALIVE / ONLINE ]")
    else:
        print(f" ❌ Host {ip} is [ DEAD / OFFLINE or blocking ICMP ]")

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f" [+] Port {port:5} : [ OPEN ]")
    s.close()

def get_target_ip():
    target = input(" [>] Enter Target Host/IP (e.g., google.com): ").strip()
    if not target:
        print(" [!] Error: Target cannot be empty!")
        return None
    try:
        print(" [*] Resolving target hostname...")
        target_ip = socket.gethostbyname(target)
        print(f" [*] Target IP Address: {target_ip}")
        return target_ip
    except socket.gaierror:
        print(" [!] Error: Could not resolve hostname or no internet access.")
        return None

def main():
    print("\n" * 80)

    show_menu()

    while True:
        choice = input(" [>] Select an option (1-4): ").strip()

        if choice == '4':
            print("\n [*] Exiting LION. Happy Hunting, Hunter! 🦁\n")
            sys.exit()

        if choice == '1':
            target_ip = get_target_ip()
            if target_ip:
                print("-" * 50)
                check_host(target_ip)
                print("-" * 50)

        elif choice == '2':
            target_ip = get_target_ip()
            if target_ip:
                print(" [*] Scanning started (Fast Mode)...")
                print("-" * 50)
                common_ports = [21, 22, 80, 443, 8080]
                with ThreadPoolExecutor(max_workers=5) as executor:
                    executor.map(lambda p: scan_port(target_ip, p), common_ports)
                print("-" * 50)
                print(" [*] LION Scan Completed.")

        elif choice == '3':
            target_ip = get_target_ip()
            if target_ip:
                try:
                    start_port = int(input(" [>] Enter Start Port: "))
                    end_port = int(input(" [>] Enter End Port: "))

                    if start_port > end_port or start_port < 1 or end_port > 65535:
                        print(" [!] Error: Invalid port range (1 - 65535).")
                        continue

                    print(f" [*] Scanning ports from {start_port} to {end_port}...")
                    print("-" * 50)
                    ports = list(range(start_port, end_port + 1))
                    with ThreadPoolExecutor(max_workers=100) as executor:
                        executor.map(lambda p: scan_port(target_ip, p), ports)
                    print("-" * 50)
                    print(" [*] LION Scan Completed.")
                except ValueError:
                    print(" [!] Error: Please enter valid numbers only.")
        else:
            print(" [!] Error: Invalid option. Please select between 1 and 4.")

def main():
    # Print menu and logo once at startup
    show_menu()

    while True:
        choice = input(" [>] Select an option (1-4): ").strip()

        if choice == '4':
            print("\n [*] Exiting LION. Happy Hunting, Hunter! 🦁\n")
            sys.exit()

        elif choice == '1':
            target_ip = get_target_ip()
            if target_ip:
                print("-" * 50)
                check_host(target_ip)
                print("-" * 50)

        elif choice == '2':
            target_ip = get_target_ip()
            if target_ip:
                print(" [*] Scanning started...")
                print("-" * 50)
                common_ports = [21, 22, 80, 443, 8080]
                for port in common_ports:
                    scan_port(target_ip, port)
                print("-" * 50)
                print(" [*] LION Scan Completed.")

        elif choice == '3':
            target_ip = get_target_ip()
            if target_ip:
                try:
                    start_port = int(input(" [>] Enter Start Port: "))
                    end_port = int(input(" [>] Enter End Port: "))

                    if start_port > end_port or start_port < 1 or end_port > 65535:
                        print(" [!] Error: Invalid port range (1 - 65535).")
                        continue

                    print(f" [*] Scanning ports from {start_port} to {end_port}...")
                    print("-" * 50)
                    for port in range(start_port, end_port + 1):
                        scan_port(target_ip, port)
                    print("-" * 50)
                    print(" [*] LION Scan Completed.")
                except ValueError:
                    print(" [!] Error: Please enter valid numbers only.")
        else:
            print(" [!] Error: Invalid option. Please select between 1 and 4.")

if __name__ == "__main__":
    main()


