"""
If n is even, n/2
If n is odd, 3n + 1
"""
import time
start_time = time.time()
longest_sequence = 0
seq_num = 0

for num in range(1,100):
    sequence = 1
    
    n = num
    while n > 1:
        if n % 2 == 0:
            n = n/2
            sequence += 1
        else:
            n = 3*n + 1
            sequence += 1
    
    if sequence > longest_sequence:
        longest_sequence = sequence
        seq_num = num
<<<<<<< Updated upstream

print(seq_num, longest_sequence)
=======
    print(seq_num, longest_sequence)
    
print("Program run time: " + str(time.time() - start_time))
>>>>>>> Stashed changes
