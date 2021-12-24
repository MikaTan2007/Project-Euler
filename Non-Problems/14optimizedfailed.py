"""
If n is even, n/2
If n is odd, 3n + 1

Store amounts in list,
When iterating, compare num to list, add list num, compare to highest sequence, proceed
"""
import time
start_time = time.time()

combinedSequence = []

for num in range(1,100):

    sequenceLength = 0
    placementNum = num
    while placementNum > 1:
        if placementNum % 2 == 0:
            placementNum = placementNum/2
            sequenceLength += 1
        else:
            placementNum = 3 * placementNum + 1
            sequenceLength += 1
        
        if len(combinedSequence) > placementNum-1:
            optimizedLength = combinedSequence[int(placementNum-1)] + sequenceLength
            print("Optimized ", num, optimizedLength)

            """sequenceLength = combinedSequence[int(placementNum-1)] + sequenceLength
            combinedSequence.append(sequenceLength)
            break"""

    combinedSequence.append(sequenceLength)

    print(num, sequenceLength)

print("Program run time: " + str(time.time() - start_time))


