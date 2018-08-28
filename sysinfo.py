#!/usr/bin/python
import platform
import sys
import os
import socket
import time
from uuid import getnode as get_mac

mac = get_mac()
unumber = os.getuid()
pnumber = os.getpid()
login   = os.getlogin()
group   = os.getgroups()
where   = os.getcwd()
now     = time.time()
means   = time.ctime(now)

print ("User number",unumber)
print ("Process ID",pnumber)
print ("Login Name", login)
print ("Current Directory",where)
print ("Group", group)

print ("Name: " +socket.gethostname( )) 
print ("FQDN: " +socket.getfqdn())
print ("System Platform: "+sys.platform)
print ("Machine: " +platform.machine())
print ("Node " +platform.node())
print ("Platform: "+platform.platform())
print ("Pocessor: " +platform.processor())
print ("System OS: "+platform.system())
print ("Release: " +platform.release())
print ("Version: " +platform.version())
print ("Python Version: " +platform.python_version())
print ("MacOS Version: " +platform.mac_ver()[0])
print ("Mac Address: " ,hex(mac))
