alphabet_val = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26
}

f = open("22/names.txt","r")
lines = f.readline()

x = lines.split(",")

numerical_alphabet = []

for name in x:
    name_length = len(name)
    brackets = []
    for character in range(1,name_length-1):
        value = alphabet_val[name[character].lower()]

        brackets.append(value)

    numerical_alphabet.append(brackets)

numerical_alphabet.sort()
print(numerical_alphabet)

total = 0
count = 1
for name in numerical_alphabet:
    sum = 0
    for num in name:
        sum = sum + num
    
    result = count * sum 
    count += 1
    total = total + result

print(total)

    

