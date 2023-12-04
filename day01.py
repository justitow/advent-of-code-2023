import re


number_word = {'one': 1,
               'two': 2,
               'three': 3,
               'four': 4,
               'five': 5,
               'six': 6,
               'seven': 7,
               'eight': 8,
               'nine': 9}



with open('day01.txt') as input_file:
    print('|'.join(['\d'] + list(number_word.keys())))
    ans = 0
    for line in input_file:
        digits = re.findall('(?=(' + '|'.join(['\d'] + list(number_word.keys())) + '))', line)
        first = number_word[digits[0]] if digits[0] in number_word else int(digits[0])
        last = number_word[digits[-1]] if digits[-1] in number_word else int(digits[-1])
        ans += int(str(first) + str(last))

    print(ans)

