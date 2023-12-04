import re

f = open("day1input.txt", "r")

summed = 0
#added for part 2
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for x in f:
    # part 1
    # first = re.search(r"\d{1,9}", x).group()[0]
    # last = re.search(r"\d{1,9}", x[::-1]).group()[0]
    # currentDigit = int(first+last)
    # summed += currentDigit
    #
    # part 2

    foundDigits = []
    for i, char in enumerate(x):
        if char.isdigit():
            foundDigits.append(char)
        else:
            for j, num in enumerate(numbers):
                if x[i: i + len(num)] == num:
                    foundDigits.append(str(j))

    summed += int(foundDigits[0]+foundDigits[-1])

print(summed)
