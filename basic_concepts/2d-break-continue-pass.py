#!/usr/bin/python

# Example of pass, break, continue
# pass: does nothing. useful when testing something or when that code block is not required
# break: terminates the current loop and resumes execution at the next statement
# continue: returns the control to the beginning of the loop


port_details = {
    '21': 'ftp',
    '23': 'telnet',
    '80': 'http',
    '443': 'https',
    '3306': 'mysql'
}

print("====== Port Details ======")
for port in port_details:
    if port == '80' or port == '443':
        print("port {} is allowed web port".format(port))
        continue
    elif port == '22':
        print("ssh access seems allowed here")
        break
    else:
        pass
        print("Just passed and showing the port details below")
        print("{} -> {}".format(port, port_details[port]))
else:
    print("It came here means it finished everything in for loop")
print("============================")


