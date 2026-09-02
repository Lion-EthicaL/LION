import socket
import sys
import os
from concurrent.futures import ThreadPoolExecutor
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
RESET = "\033[0m"
RED = "\033[91m"
SERVICES = {
    21: "FTP",
    22: "SSH",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP-Proxy"
}

def show_menu():
    print(fr"{GREEN}                * ___     _____  ____ ___ ___ *  {RESET}")
    print(fr"{YELLOW}               ** | |    |_   _|/ __ \| \ | | ** {RESET}")
    print(fr"{YELLOW}               ** | |      | | | |  | |  \| | ** {RESET}")
    print(fr"{YELLOW}               ** | |      | | | |  | | . ` | ** {RESET}")
    print(fr"{YELLOW}               ** | |____ _| |_| |__| | |\  | ** {RESET}")
    print(fr"{YELLOW}               ** |______|_____|\____/|_| \_| ** {RESET}")
    print(fr"               {GREEN} *     SECURITY SCANNER v1.1   *   {RESET}")
    print(fr"{RED}                         Lion-EthicaL           {RESET}")
    print(f"{BLUE}{'=' * 59}{RESET}")
    print(f"{BLUE}[1]{RESET} Ping / Check if Host/IP is Alive:")
    print(f"{BLUE}[2]{RESET} Scan Common Ports (21, 22, 80, 443, 8080):")
    print(f"{BLUE}[3]{RESET} Scan Custom Port Range:")
    print(f"{BLUE}[4]{RESET} Exit LION Tool:")
    print(f"{BLUE}{'=' * 59}{RESET}")

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
        service_name = SERVICES.get(port, "unknown")
        print(f"{GREEN}[+] Port {port:<5} : ✅ [ OPEN ] ({service_name.upper()}){RESET}")
        try:
            s.send(b"HEAD / HTTP/1.1\r\nHost: target\r\n\r\n")
            banner = s.recv(1024).decode('utf-8', errors='ignore')
            for line in banner.split('\n'):
                if "Server:" in line:
                    print(f"     └── 🔍 Info: {line.strip()}")
                    break
        except:
            pass

    s.close()

def get_target_ip():
    target = input(f"[{RED}>{RESET}] Enter Target Host/IP (e.x., google.com): ").strip()
    if not target:
        print("[{YELLOW}!{RESET}] Error: Target cannot be empty!")
        return None
    try:
        print(" [*] Resolving target hostname...")
        target_ip = socket.gethostbyname(target)
        print(f"[{GREEN}*{RESET}] Target IP Address: {target_ip}")
        return target_ip
    except socket.gaierror:
        print(f"[{YELLOW}!{RESET}] Error: Could not resolve hostname or no internet access.")
        return None

def main():
    print("\n" * 80)

    show_menu()

    while True:
        choice = input(f"{RED}[>]{RESET} Select An Option (1-4): ").strip()

        if choice == '4':
            print("\n [*] Exiting LION. Happy Hunting, Hunter! 🦁\n")
            sys.exit()

        if choice == '1':
            target_ip = get_target_ip()
            if target_ip:
                print(f"{BLUE}{'=' * 59}{RESET}")
                check_host(target_ip)
                print(f"{BLUE}{'=' * 59}{RESET}")

        elif choice == '2':
            target_ip = get_target_ip()
            if target_ip:
                print(" [*] Scanning started (Fast Mode)...")
                print(f"{BLUE}{'=' * 59}{RESET}")
                ports = [21, 22, 80, 443, 8080]
                with ThreadPoolExecutor(max_workers=5) as executor:
                    executor.map(lambda p: scan_port(target_ip, p), [21, 22, 80, 443, 8080])
                    print(f"{BLUE}{'=' * 59}{RESET}")
                print(f" [{GREEN}*{RESET}]{GREEN} LION Scan Completed...{RESET}")

        elif choice == '3':
            target_ip = get_target_ip()
            if target_ip:
                try:
                    start_port = int(input(f"{RED}[>]{RESET} Enter Start Port: "))
                    end_port = int(input(f"{RED}[>]{RESET} Enter End Port: "))

                    if start_port > end_port or start_port < 1 or end_port > 65535:
                        print(f"[{YELLOW}!{RESET}] Error: Invalid port range (1 - 65535).")
                        continue

                    print(f" [*] Scanning ports from {start_port} to {end_port}...")
                    print(f"{BLUE}{'=' * 59}{RESET}")
                    ports = list(range(start_port, end_port + 1))
                    with ThreadPoolExecutor(max_workers=100) as executor:
                        executor.map(lambda p: scan_port(target_ip, p), ports)
                    print(f"{BLUE}{'=' * 59}{RESET}")
                    print(f" [{GREEN}*{RESET}]{GREEN} LION Scan Completed...{RESET}")
                except ValueError:
                    print(f"[{YELLOW}!{RESET}] Error: Please enter valid numbers only.")
        else:
            print(f"[{YELLOW}!{RESET}] Error: Invalid option. Please select between 1 and 4.")

def main():
    # Print menu and logo once at startup
    show_menu()

    while True:
        try:
           choice = input(f"{RED}[>]{RESET} Select An Option (1-4): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n[!] Exiting LION.👋 Goodbye!")
            sys.exit()

        if choice == '4':
            print("\n [*] Exiting LION. Happy Hunting, Hunter! 🦁\n")
            sys.exit()

        elif choice == '1':
            target_ip = get_target_ip()
            if target_ip:
                print(f"{BLUE}{'=' * 59}{RESET}")
                check_host(target_ip)
                print(f"{BLUE}{'=' * 59}{RESET}")

        elif choice == '2':
            target_ip = get_target_ip()
            if target_ip:
                print(" [*] Scanning started...")
                print(f"{BLUE}{'=' * 59}{RESET}")
                common_ports = [21, 22, 80, 443, 8080]
                with ThreadPoolExecutor(max_workers=5) as executor:
                    executor.map(lambda p: scan_port(target_ip, p), common_ports)
                print(f"{BLUE}{'=' * 59}{RESET}")
                print(f" [{GREEN}*{RESET}]{GREEN} LION Scan Completed...{RESET}")

        elif choice == '3':
            target_ip = get_target_ip()
            if target_ip:
                try:
                    start_port = int(input(f"{RED}[>]{RESET} Enter Start Port: "))
                    end_port = int(input(f"{RED}[>]{RESET} Enter End Port: "))

                    if start_port > end_port or start_port < 1 or end_port > 65535:
                        print(f"[{YELLOW}!{RESET}] Error: Invalid port range (1 - 65535).")
                        continue

                    print(f" [*] Scanning ports from {start_port} to {end_port}...")
                    print(f"{BLUE}{'=' * 59}{RESET}")
                    ports = list(range(start_port, end_port + 1))
                    with ThreadPoolExecutor(max_workers=100) as executor:
                        executor.map(lambda p: scan_port(target_ip, p), ports)
                    print(f"{BLUE}{'=' * 59}{RESET}")
                    print(f" [*]{GREEN} LION Scan Completed...{RESET}")
                except ValueError:
                    print("[{YELLOW}!{RESET}] Error: Please enter valid numbers only.")
        else:
            print(f"[{YELLOW}!{RESET}] Error: Invalid option. Please select between 1 and 4.")

if __name__ == "__main__":
    main()


