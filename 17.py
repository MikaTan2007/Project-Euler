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

common_occurences = ["hundred", "and", "ty"]

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

        if len(num) == 3:

            if num[1] == "0" and num[2] == "0":
                converted = number_dict[num[0]] + " " + common_occurences[0]
                return converted
            
            converted = number_dict[num[0]] + " " + common_occurences[0] + " " + common_occurences[1]

            num = num[1] + num[2]

            if num[0] == "0":
                num = num[1]

            try:
                converted += " " + number_dict[num]
            except:
                for key in number_dict:
                    if len(key) == 2:
                        if key[0] == num[0]:
                            converted += " " + number_dict[key] + " " + number_dict[num[1]]
        
        if len(num) == 4:
            converted = "one thousand"

    return converted

total = 0

for num in range(1,1001):
    conversion = convert_to_word(num)
    conversion = conversion.replace(" ","")
    total += len(conversion)

print(total)