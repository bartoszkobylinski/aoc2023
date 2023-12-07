import time

FILE_NAME = "adventofcode.com_2023_day_1_input.txt"

# Mapping of number words to digits
digits_words = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}


def word_to_digit(word):
    return digits_words.get(word.lower(), None)


def find_and_combine(input_string):
    elements = []
    word = ''
    for char in input_string:
        if char.isdigit():
            if word:
                digit = word_to_digit(word)
                if digit is not None:
                    elements.append(digit)
                word = ''
            elements.append(char)
        elif char.isalpha():
            word += char
            digit = word_to_digit(word)
            if digit is not None:
                elements.append(digit)
                word = ''

    if len(elements) == 1:
        elements.append(elements[0])

    if elements:
        combined = elements[0] + elements[-1]
        return int(combined)
    else:
        return 0


digits_list = []


def separate_string_numbers(input_string):
    result = []
    current_element = ''
    is_digit = input_string[0].isdigit()

    for char in input_string:
        if char.isdigit() == is_digit:
            current_element += char
        else:
            if is_digit:
                result.append(current_element)
            else:
                result.append(current_element)
            current_element = char
            is_digit = not is_digit

    if current_element:
        if is_digit:
            result.append(current_element)
        else:
            result.append(current_element)

    return result


def find_first_digit_word(s):
    digit_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    first_pos = len(s)
    first_word = None

    for word in digit_words:
        pos = s.find(word)
        if pos != -1 and pos < first_pos:
            first_pos = pos
            first_word = word

    return first_word


def find_last_digit_word(s):
    digit_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    last_pos = -1
    last_word = None

    for word in digit_words:
        pos = s.rfind(word)
        if pos != -1 and pos > last_pos:
            last_pos = pos
            last_word = word

    return last_word


with open(FILE_NAME, "r") as input_file:
    for line in input_file:
        line = line.strip()
        print(line)

        line = separate_string_numbers(line)
        print(line)

        first, second = None, None

        for element in line:
            if element.isdigit():
                first = element[0] if len(element) > 1 else element
                break
            elif (digit := find_first_digit_word(element)) in digits_words:
                first = digits_words[digit]
                break

        last_digit_word = None
        for element in reversed(line):
            if element.isdigit():
                second = element[-1] if len(element) > 1 else element
                break
            elif (digit := find_last_digit_word(element)) in digits_words:
                last_digit_word = digits_words[digit]

        if last_digit_word:
            second = last_digit_word

        print(f"first: {first}, second: {second}")
        number = first + second
        number = int(number)
        print(f"type {type(number)}, number: {number}")

        digits_list.append(number)

total_sum = sum(digits_list)
print("Combined numbers:", digits_list)
print("Total sum:", total_sum)
