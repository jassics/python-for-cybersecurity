# Generate 6 digit OTP
import string
import secrets

number = string.digits
otp = ''

for i in range (6):
    otp += ''.join(secrets.choice(number))

print(otp)
