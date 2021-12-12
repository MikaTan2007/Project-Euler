def prime_numbers(num):
    the_primes = []
    count = 1
    while count <= num:
        sub_count = 1
        factors = []
        while sub_count <= count:
            if count % sub_count == 0:
                factors.append(sub_count)
            sub_count += 1
        if len(factors) == 2:
            the_primes.append(count)
        count += 1
    return the_primes

def prime_factors(num):
    all_primes = prime_numbers(num)
    prime_factors = []
    
    while num > 1:
        length = len(all_primes)
        count = 0
        while count < length:
            prime = all_primes[count]
            possible_num = num/prime
            if possible_num.is_integer() == True:
                num = possible_num
                prime_factors.append(prime)
            else: 
                possible_num = num
            
            count += 1
        
    return prime_factors
    

print(prime_factors(10000))

