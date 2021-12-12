num_1 = 100
num_2 = 100

full_table = []

while num_1 <= 999:
    line_table = []

    while num_2 <= 999:
        line_table.append(num_1*num_2)
        num_2 += 1

    full_table.append(line_table)
    num_1 += 1
    num_2 = 100

for table in full_table:
    print(table)

