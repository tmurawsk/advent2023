import collections

from tasks.base import Task


def are_all_values_same(values) -> bool:
    for k in range(len(values) - 1):
        if values[k] != values[k + 1]:
            return False
    return True


class Task9(Task):
    def __init__(self, filename="input/9.txt"):
        super().__init__(filename)

    def run1(self):
        predictions = []
        for line in self.file:
            values: [int] = [int(x) for x in line.strip().split()]
            next_values = [values]
            i = 0
            while not are_all_values_same(next_values[i]):
                next_values.append([])
                for j in range(len(next_values[i]) - 1):
                    next_values[i + 1].append(next_values[i][j + 1] - next_values[i][j])
                i = i + 1
            for j in range(len(next_values) - 1, 0, -1):
                next_values[j - 1].append(next_values[j - 1][-1] + next_values[j][-1])
            predictions.append(next_values[0][-1])
        print(sum(predictions))

    def run2(self):
        predictions = []
        for line in self.file:
            values = collections.deque([int(x) for x in line.strip().split()])
            next_values: [collections.deque[int]] = [values]
            i = 0
            while not are_all_values_same(next_values[i]):
                next_values.append(collections.deque())
                for j in range(len(next_values[i]) - 1):
                    next_values[i + 1].append(next_values[i][j + 1] - next_values[i][j])
                i = i + 1
            for j in range(len(next_values) - 1, 0, -1):
                next_values[j - 1].appendleft(next_values[j - 1][0] - next_values[j][0])
            predictions.append(next_values[0][0])
        print(sum(predictions))
