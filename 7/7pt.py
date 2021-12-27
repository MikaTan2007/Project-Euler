"""
Python

Primality Test Optimization

Problem 7 Project Euler

Mika
"""

import time
start_time = time.time()

def isprime(num):
    if num == 1 or num == 0:
        return False
    elif num % 2 == 0 and num > 2:
        return False
    else:
        for pot_num in range(3, int(num**(1/2))+1, 2):
            if num % pot_num == 0:
                return False
        return True

primes = []

num = 0

while len(primes) < 10001:
    if isprime(num) == True:
        primes.append(num)
    num += 1

print(primes[-1])
print("Program run time: " + str(time.time() - start_time))