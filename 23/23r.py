import time 
start = time.time()
import math

def divisors(num):
    divisors = [1]
    for i in range(2, math.ceil(math.sqrt(num))+ 1):
        if num % i == 0:
            if i not in divisors and i != num:
                divisors.append(i)
                if num/i not in divisors:
                    if num/i != num:
                        divisors.append(num/i)
    return divisors

def sum_divisors(divisor_list):
    sum = 0 
    for num in divisor_list:
        sum += num
    return sum

abundant_numbers = []

original_abundant_numbers = []

for num in range(1,28124):
    if sum(divisors(num)) > num:
        for abundant_num in original_abundant_numbers:
            if num % abundant_num == 0:
                #abundant_numbers.append(num)
                break
        original_abundant_numbers.append(num)
        abundant_numbers.append(num)
        multiplier = 2
        while num * multiplier < 28124:
            abundant_numbers.append(num * multiplier)
            multiplier += 1

abundant_refined = list(dict.fromkeys(abundant_numbers))
abundant_refined.sort()
print(len(abundant_refined))


sum_combo = []
for abundant_num in abundant_refined:
    for abundant_num2 in abundant_refined:
        sum_combo.append(abundant_num + abundant_num2)

print(len(sum_combo))

real_sum = 0

for num in range(1,28124):
    if num not in sum_combo:
        real_sum += num

print(real_sum)
end = time.time()
print(end-start)
      
