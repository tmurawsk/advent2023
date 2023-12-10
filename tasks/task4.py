from tasks.base import Task


class Task4(Task):
    def __init__(self, filename="input/4.txt"):
        super().__init__(filename)

    def run1(self):
        points_sum = 0
        for line in self.file:
            line = line.strip().split(': ')[1].strip().split(' | ')
            targets = line[0].split()
            values = line[1].split()
            score = 1
            for target in targets:
                if target in values:
                    score *= 2
            points_sum += int(score/2)
        print(points_sum)

    def run2(self):
        lines = self.file.readlines()
        cards_count = [1 for i in range(len(lines))]

        for line in lines:
            line_parts = line.strip().split(': ')
            card_number = int(line_parts[0].removeprefix('Card ').strip()) - 1
            numbers_part = line_parts[1].strip().split(' | ')
            targets = numbers_part[0].split()
            values = numbers_part[1].split()
            pairs = 0
            for target in targets:
                if target in values:
                    pairs += 1
            for i in range(pairs):
                cards_count[card_number + i + 1] += cards_count[card_number]
        print(sum(cards_count))
