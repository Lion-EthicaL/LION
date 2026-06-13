#LION Security Scanner v1.1
A fast network scanner built with python and Multi-threading.
## Features
- Host ping Check
- Fast Common Ports Scan
- Multi-threaded Custom Range Scan

## Installation & Usage

To install and run **LION Security Scanner**, follow these commands Terminal:

```bash
# Clone the repository
https://github.com/Lion-EthicaL/LION.git

# Change to the directory
cd LION

# Install dependencies
pip install -r requirements.txt

# Run the Tools
python3 lion.py
```

## 🛠 How to Use (Usage Guide)

 When you launch the tool, you will see an interactive menu with 4 main option

* **[1] Ping/Check if Host/IP is Alive**: Enter this option, the type you target hostname (e.x.,`google.com`) or IP Address. The tool will resolve the host and instantly check if the server is active (`ALIVE`) or down (`DEAD/OFFLINE/BLOCKING ICMP`).
* **[2] Scan Common Ports**: Automatically scans the most critical standard network ports(21, 22, 80, 443, 8080) on you target.
* **[3] Scan Custom Port Range**: Allows you to specity a custom range of ports to scan manually.
* **[4] Exit LION Tool**: Safely closes the scanner and returns you to you local TerminaL.

