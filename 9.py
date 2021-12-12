m = 1
n = 1

for num1 in range(1,1001):
    for num2 in range(1,1001):
        if num1 > num2:
            m = num1
            n = num2
        elif num1 < num2:
            m = num2
            n = num1

        a = m ** 2 - n ** 2
        b = 2*m*n
        c = m ** 2 + n ** 2
        sum = a + b + c
    
        if sum == 1000:
            print(a,b,c,sum, a*b*c)
            break





