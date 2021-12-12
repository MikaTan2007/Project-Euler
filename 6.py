sum_of_squares = 0
total_sum = 0
for num in range(1,101):
    sum_of_squares += num * num
    total_sum += num

print(total_sum*total_sum - sum_of_squares)