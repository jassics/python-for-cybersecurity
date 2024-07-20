import sys
import requests
import socket
import whois
import validators
import nmap # pip install python-nmap

if len(sys.argv) != 2:
    print('You need to pass the url')
    print('Ex: python {} <url>'.format(sys.argv[0]))
    exit(0)

url = sys.argv[1]

if not validators.domain(url):
    exit("Please pass the valid domain name")

print('Website info gathering for "{}"'.format(url))

# Get url's IP
try:
    ip_address = socket.gethostbyname(url)
    print("IP Address: {}".format(ip_address))
except:
    exit('Something went wrong with the url')

# Get Whois details
#domain_details = whois.query(url)
#print(domain_details.__dict__)

# Get Wappalyzer details


# Get Port status using pythonic nmap
nmScan = nmap.PortScanner()

print("Starting nmap scan for url: " + url)
nmScan.scan(url, '21-443')

print('nmap command line version is: ' + nmScan.command_line())

# run a loop to print all the found result about the ports
for host in nmScan.all_hosts():
    print('Host : %s (%s)' % (host, nmScan[host].hostname()))
    print('State : %s' % nmScan[host].state())

    for proto in nmScan[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

    lport = nmScan[host][proto].keys()
    sorted(lport)

    for port in lport:
        print('port : %s\tstate : %s\tproduct : %s\tversion : %s' % (port, nmScan[host][proto][port]['state'], nmScan[host][proto][port]['product'], nmScan[host][proto][port]['version']))

print('\nResult in CSV format as well\n')
print(nmScan.csv())
