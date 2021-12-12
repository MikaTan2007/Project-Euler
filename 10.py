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

sum = 0

for num in range(1,2000000):
    if isprime(num) == True:
        sum += num

print(sum)