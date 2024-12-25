import socket
import os
import requests
import nmap3  # pip install python3-nmap

"""
    Python Script for Testing Environment
    Checks system information, IPs, and nmap functionality.
"""

name = "Sanjeev"
print(f"Hello {name}\n")
print(f"O.S. is: {os.name}")

# Retrieve host information
try:
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"Your Computer Name is: {hostname}")
    print(f"Your Computer Local IP Address is: {local_ip}")
except Exception as e:
    print(f"Error retrieving local IP: {e}")

# Retrieve public IP
try:
    public_ip = requests.get('https://checkip.amazonaws.com').text.strip()
    print(f"Your Computer Public IP Address is: {public_ip}")
except Exception as e:
    print(f"Error retrieving public IP: {e}")

print("\nChecking if nmap works:\nStarting nmap scan now...\n")

# Initialize nmap object
nmap = nmap3.Nmap()

# Get nmap version
try:
    nmap_version = nmap.nmap_version()
    print(f"Nmap version: {nmap_version}")
except Exception as e:
    print(f"Error retrieving nmap version: {e}")

# Perform a top ports scan
url = 'aliencoders.org'
try:
    print(f"Starting nmap scan for URL: {url}")
    top_ports = nmap.scan_top_ports(url, args="-sV")
    print(f"Top ports for {url}: {top_ports}")
except Exception as e:
    print(f"Error during nmap scan: {e}")
