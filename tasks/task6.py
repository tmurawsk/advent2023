import math

from tasks.base import Task


class Task6(Task):
    def __init__(self, filename="input/6.txt"):
        super().__init__(filename)

    def run1(self):
        times = [int(x) for x in self.file.readline().strip().removeprefix('Time:').strip().split()]
        distances = [int(x) for x in self.file.readline().strip().removeprefix('Distance:').strip().split()]
        number_of_wins = [0 for _ in range(len(times))]
        for i in range(len(times)):
            limit = times[i]
            to_beat = distances[i]
            for t in range(int(limit/2), -1, -1):
                s = limit * t - t * t
                if s > to_beat:
                    number_of_wins[i] += 1
                else:
                    break
            for t in range(int(limit/2) + 1, limit + 1):
                s = limit * t - t * t
                if s > to_beat:
                    number_of_wins[i] += 1
                else:
                    break
        print(math.prod(number_of_wins))

    def run2(self):
        time = int(''.join(self.file.readline().strip().removeprefix('Time:').strip().split()))
        distance = int(''.join(self.file.readline().strip().removeprefix('Distance:').strip().split()))
        min_time = max_time = 0
        for t in range(int(time / 2)):
            s = t * time - t * t
            if s > distance:
                min_time = t
                break
        for t in range(time, int(time / 2), -1):
            s = t * time - t * t
            if s > distance:
                max_time = t
                break
        print(max_time - min_time + 1)
