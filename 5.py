number = 20
while True:
    num_count = 0
    for count in range(1,21):
        if number % count == 0:
            num_count += 1
    if num_count == 20:
        print(number)
        break
    else:
        print(num_count, number)
        number += 20
    
    