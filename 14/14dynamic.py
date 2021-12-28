"""
If n is even, n/2
If n is odd, 3n + 1

Optimized using dynamic programming
"""

import time
start_time = time.time()

longest_sequence = 0
longest_sequence_num = 0

stored_lib_values = []

for num in range(1,1000001):
    sequence = 0

    seq_num = num

    while seq_num > 1:

        if len(stored_lib_values) > seq_num:
            sequence = int(stored_lib_values[int(seq_num-1)]) + seq_num
            print("Optimized", num, sequence)
            break

        if seq_num % 2 == 0:
            seq_num = seq_num / 2
            sequence += 1
        else:
            seq_num = 3 * seq_num + 1
            sequence += 1
    
    stored_lib_values.append(seq_num)

    print(num, seq_num)

    if sequence > longest_sequence:
        longest_sequence = sequence
        longest_sequence_num = num

print(longest_sequence_num, longest_sequence)
print("Program run time: " + str(time.time() - start_time))
