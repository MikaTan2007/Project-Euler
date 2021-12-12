def even_fibonacci_numbers(limit, starting1, starting2):

    fibonacci_sequence = [starting1,starting2]

    num = 0

    while num <= limit:
        num = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(num)

    fibonacci_sequence.pop()

    even_num = []

    for fibonacci in fibonacci_sequence:
        if fibonacci % 2 == 0:
            even_num.append(fibonacci)

    return sum(even_num)

print(even_fibonacci_numbers(4000000, 1, 2))
