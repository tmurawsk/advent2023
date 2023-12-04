from tasks.base import Task


STRING_DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0
}


class Task1(Task):
    def __init__(self, filename="input/1.txt"):
        super().__init__(filename)

    def run1(self):
        sum_numbers = 0
        for line in self.file:
            line = line.strip()
            first_digit = -1
            last_digit = -1
            for char in line:
                if char.isdigit():
                    if first_digit < 0:
                        first_digit = int(char)
                    last_digit = int(char)
            number = 10 * first_digit + last_digit
            sum_numbers += number
        print(sum_numbers)

    def run2(self):
        sum_numbers = 0
        for line in self.file:
            line = line.strip()
            first_digit, last_digit, first_index, last_index, i = -1, -1, -1, -1, 0
            last_digit = -1
            first_index = -1
            last_index = -1
            for char in line:
                if char.isdigit():
                    if first_digit < 0:
                        first_digit = int(char)
                        first_index = i
                    last_digit = int(char)
                    last_index = i
                i += 1
            for string_digit in STRING_DIGITS.keys():
                first_found = line.find(string_digit)
                last_found = line.rfind(string_digit)
                if 0 <= first_found < first_index or first_index < 0:
                    first_index = first_found
                    first_digit = STRING_DIGITS[string_digit]
                if last_found > last_index or last_index < 0:
                    last_index = last_found
                    last_digit = STRING_DIGITS[string_digit]
            print(f'{first_digit}{last_digit}')
            sum_numbers += 10 * first_digit + last_digit
        print('===', sum_numbers)
