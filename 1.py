list_of_num = []
num = 1
while num < 1000:
    if num % 3 == 0:
        list_of_num.append(num)
        num += 1
    elif num % 5 == 0:
        list_of_num.append(num)
        num += 1
    else:
        num += 1

print(list_of_num)
print(sum(list_of_num))