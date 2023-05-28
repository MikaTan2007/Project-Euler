"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import math

def divisor(n):
    i = 2
    n_sqr = math.sqrt(n)
    divisors = [1]
    while i <= n_sqr:
        if n % i == 0:
            divisors.append(i)
            divisors.append(int(n/i))
        i += 1
    try:
        if divisors[-1] == divisors[-2]:
            divisors.pop(-1)
    except:
        return sum(divisors)
    
    return sum(divisors)

i = 1
while i <= 10000:
    a = divisor(i) #THIS IS EQUAL TO B
    b = divisor(a)

    if b == i and a != b:
        print(a, b)
    i += 1

    
"""
220 + 284 + 1210 + 1184 + 2924 + 2620 + 5564 + 5020 + 6368 + 6232
"""