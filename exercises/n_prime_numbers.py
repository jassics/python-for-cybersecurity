#!/usr/bin/python3

# Function to check If a number is prime against already given prime number list
def prime(num, primes):
    # loop to test if num is prime number against given primes list
    for prime in primes:
        if  (num % prime) == 0:
            return False
    # We got new prime number, add it in list primes[]
    primes.append(num)
    return True

def n_primes(n):
    primes = []
    start_num, prime_counter = 2, 0
    while True:
        if prime(start_num, primes):
            prime_counter += 1
            if prime_counter == n:
                return primes
        start_num += 1

try:
    nprimes = int(input("Enter how many prime numbers you want to display: "))
except:
    exit("Must be an integer only")


if nprimes < 0:
    exit("Number must be postive one!")
else:
    primes_list = n_primes(nprimes)
    print(primes_list)

