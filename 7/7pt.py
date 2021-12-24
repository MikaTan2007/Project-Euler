"""
Uses Primality Test Optimization
"""

import time
start_time = time.time()
def isprime(num):
    # 0, 1, even numbers greater than 2 are NOT PRIME
    if num==1 or num==0 or (num % 2 == 0 and num > 2):
        return "Not prime"
    else:
        # Not prime if divisable by another number less
        # or equal to the square root of itself.
        # n**(1/2) returns square root of n
        for i in range(3, int(num**(1/2))+1, 2):
            if num%i == 0:
                return False
        return True

primes = []

count = 0

while len(primes) < 10001:
    if isprime(count) == True:
        primes.append(count)
    count += 1

print(primes[-1])
print("Program run time: " + str(time.time() - start_time))