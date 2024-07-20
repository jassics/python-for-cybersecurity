import socket
import os
import requests
import nmap3 # pip install python3-nmap

"""
    First Python Program
    Just to see if we can run python3 successfully
    and modules are installed or not ;)
"""

name = "Sanjeev"
print("Hello "+name+"\n")
print("O.S. is: " + os.name)

hostname = socket.gethostname()
local_ip   = socket.gethostbyname(hostname)
public_ip = requests.get('https://checkip.amazonaws.com').text.strip()
print("Your Computer Name is:" + hostname)
print("Your Computer Local IP Address is:" + local_ip)
print("Your Computer Public IP Address is:" + public_ip)
print("\nChecking if nmap works:\nStarting nmap scan now...\n")

# make nmap object
nmap = nmap3.Nmap()

#nmap version
nmap_version = nmap.nmap_version()
print (f"Nmap version: {nmap_version}")

# scanning practical-devsecops.com
url = 'aliencoders.org'
""""
print("Starting nmap scan for url: " + url)
results = nmap.nmap_version_detection(url)
print(f"Here is the result for {url}: {results}")
"""
top_ports = nmap.scan_top_ports(url, args="-sV")
print(f"These are the top ports: {top_ports}")
