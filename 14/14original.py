"""
If n is even, n/2
If n is odd, 3n + 1

Unoptimized Code

Program run time: 43.70179033279419
837799 524 - Number, Highest Sequence
"""

import time
start_time = time.time()

longest_sequence = 0
longest_sequence_num = 0

for num in range(1,1000001):
    sequence = 0

    seq_num = num

    while seq_num > 1:
        if seq_num % 2 == 0:
            seq_num = seq_num / 2
            sequence += 1
        else:
            seq_num = 3 * seq_num + 1
            sequence += 1
    
    if sequence > longest_sequence:
        longest_sequence = sequence
        longest_sequence_num = num



print(longest_sequence_num, longest_sequence)
print("Program run time: " + str(time.time() - start_time))
