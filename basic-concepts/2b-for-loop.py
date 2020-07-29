#!/usr/bin/python

# for loop syntax
# for iterating_var in sequence:
#   statements(s)
# You can use else block with for loop just like we used with while loop in previous example
# for <variable> in <sequence>:
#	<statements>
# else:
#	<statements>

port_details = {
    '22': 'ssh',
    '21': 'ftp',
    '23': 'telnet',
    '80': 'http',
    '443': 'https'
}

print("====== Port Details ======")
for port in port_details:
    print("{} -> {}".format(port, port_details[port]))

print("============================")


