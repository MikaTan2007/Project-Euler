"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 
 would be 
, which means that 
 is a perfect number.

A number 
 is called deficient if the sum of its proper divisors is less than 
 and it is called abundant if this sum exceeds 
.

As 
 is the smallest abundant number, 
, the smallest number that can be written as the sum of two abundant numbers is 
. By mathematical analysis, it can be shown that all integers greater than 
 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
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

for num in range(1, 28124):
    if sum_divisors(divisors(num)) > num:
        abundant_numbers.append(num)

#print(len(abundant_numbers))

list_of_sums = []

main_index = 0 

while main_index < 6965:
    for i in range(main_index,6965):
        sum = abundant_numbers[main_index] + abundant_numbers[i]
        if sum < 28123:
            list_of_sums.append(sum)
    main_index += 1

abundant_sum = 0
for i in list_of_sums:
    abundant_sum += i

total_sum = 0
for i in range(1,28124):
    total_sum += i

print(abundant_sum)
print(total_sum)


#print(list_of_sums)

    
    
"""
for abundant_num in abundant_numbers:
    #list_of_sums = []
    for abundant_2 in abundant_numbers:
        sum = abundant_num + abundant_2
        if sum < 28123 and sum not in sums:
            print(sum)
            sums.append(sum)
"""


"""
non_sums = []
for i in range(1,28124):
    if i not in sums:
        non_sums.append(i)

print("-------------------------------------------------------------")
print(non_sums)
"""
"""
for abundant in abundant_numbers:
    list_of_sums = []
    for number in abundant_numbers:
        sum = abundant + number
        if sum <= 28123:
            list_of_sums.append(sum)
    sums.append(list_of_sums)

print(sums)
"""


"""
for i in range (1,28123):
    divisor_list = divisors(i)
    sum = 0 
    for pair in divisor_list:
        for indi in pair:
            sum += indi 
"""

"""
for original_num in range (0,28123):
    for i in range (1, math.ceil(math.sqrt(original_num))):
        try:
            int(i/12)
        except:
            pass
"""
