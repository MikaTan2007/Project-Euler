number_dict = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety"
}

common_occurences = ["hundred", "and", "ty", "teen"]

def convert_to_word(num):
    converted = ""
    num = str(num)
    try:
        converted = number_dict[num]
    except:
        if len(num) == 2:
            for key in number_dict:
                if len(key) == 2:
                    if key[0] == num[0]:
                        converted = number_dict[key] + " " + number_dict[num[1]]

    return converted

for num in range(1,100):
    print(num, convert_to_word(num))

"""
249 = two hundred and forty nine

371 = three hundred and seventy one

369 = three hundred and sixty nine

111 = one hundred and eleven
"""