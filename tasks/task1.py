from tasks.base import Task


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
        pass
