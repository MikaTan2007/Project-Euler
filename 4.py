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

palindromes = []

for table in full_table:
    for number in table:
        if len(str(number)) == 6:
            str_product = str(number)
            fir_half = [str_product[0], str_product[1],str_product[2]]
            sec_half = [str_product[5], str_product[4],str_product[3]]
            if fir_half[0] == sec_half[0] and fir_half[1] == sec_half[1] and fir_half[2] == sec_half[2]:
                if number not in palindromes:
                    palindromes.append(number)

        else:
            str_product = str(number)
            fir_half = [str_product[0], str_product[1]]
            sec_half = [str_product[4], str_product[3]]
            if fir_half[0] == sec_half[0] and fir_half[1] == sec_half[1]:
                if number not in palindromes:
                    palindromes.append(number)

palindromes.sort()
print(palindromes)
            





