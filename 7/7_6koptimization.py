"""
Uses the 6k+-1
"""

import time
start_time = time.time()

def isprime(num):
    if num <= 3:
        if num > 1:
            return True
        else:
            return False

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5

    while i ** 2 <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True

primes = []

count = 0

while len(primes) < 10001:
    if isprime(count) == True:
        primes.append(count)
    count += 1

print(primes[-1])
print("Program run time: " + str(time.time() - start_time))
    

