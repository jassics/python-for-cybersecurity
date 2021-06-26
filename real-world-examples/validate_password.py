#!/usr/bin/python
import re

# Password Criteria
# 1. Should contain alphanumeric
# 2. At least one Capital Letter
# 3. At least one small letter
# 4. 8-20 characters
# 5. at least one special character !@#$%^&*_
# 6. No whitespace please

passwords = ['JassiSidhu', 'Jassi Sidhu0$','JassiSidhu0$', 'Jalantu_123*', '12Falcon#', 'Sh0rt5!','Sh0rt5!89***^AWS+', 'short']
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '_']

# Using Regular Expression
pattern = '^((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*_])(?=.*[\S])[0-9a-zA-Z!@#$%^&*_]{8,20})$'
for password in passwords:
    print(password)
    result = re.match(pattern,password)
    if result:
        print("Password Accepted")
    else:
        print("Password Denied")
