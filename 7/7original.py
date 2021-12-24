"""
Base Brute Force Python Algo
"""

import time
start_time = time.time()

def isprime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

primes = []

count = 0

while len(primes) < 10003:
    if isprime(count) == True:
        primes.append(count)
    count += 1
print(primes[-1])
print("Program run time: " + str(time.time() - start_time))