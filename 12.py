"""
Problem Steps:
1.) Generate triangle number
2.) Triangle Num generated through adding each previous natural number including the place of the triangle number
3.) Find the divisors
4.) Determine if the number of divisors is greater than 500
5.) Repeat if not
"""

def triangle_num(place):
    triangle_number = 0
    for num in range(1,place+1):
        triangle_number += num 
    return triangle_number

def find_factor(num):
    limit = 0
    factor_num = 4

    for first_factor in range(2, num):
        if num % first_factor == 0:
            limit = num / first_factor
            break


    for factor in range(3, int(limit)):
        if num % factor == 0:
            factor_num += 1
    
    return factor_num

num_count = 12374

while find_factor(triangle_num(num_count)) < 500:

    print(num_count, triangle_num(num_count), find_factor(triangle_num(num_count)))
    
    num_count += 1
    
    