from tasks.base import Task


class Range:
    def __init__(self, smin, smax, dmin, dmax):
        self.smin = smin
        self.smax = smax
        self.dmin = dmin
        self.dmax = dmax


class Task5(Task):
    def __init__(self, filename="input/5.txt"):
        super().__init__(filename)

    def run1(self):
        i = 0
        ranges: [[Range]] = [[], [], [], [], [], [], []]
        line = self.file.readline().strip()
        seeds = [int(x) for x in line.removeprefix('seeds: ').split()]
        self.file.readline()
        while self.file.readline().strip():
            while len(line := self.file.readline().strip().split()) > 0:
                [dmin, smin, diff] = [int(x) for x in line]
                ranges[i].append(Range(smin, smin + diff - 1, dmin, dmin + diff - 1))
            i += 1

        min_location = 1000000000
        for seed in seeds:
            current_number = seed
            next_number = seed
            for current_ranges in ranges:
                matching_ranges = list(filter(lambda r: r.smin <= current_number <= r.smax, current_ranges))
                if len(matching_ranges) > 0:
                    mr = matching_ranges[0]
                    next_number = mr.dmin + (current_number - mr.smin)
                else:
                    next_number = current_number
                current_number = next_number
            min_location = min(min_location, next_number)
        print(min_location)

    def run2(self):
        i = 0
        seeds = []
        ranges: [[Range]] = [[], [], [], [], [], [], []]
        line = self.file.readline().strip()
        seed_ranges = [int(z) for z in line.removeprefix('seeds: ').split()]
        for x in range(0, len(seed_ranges), 2):
            for y in range(seed_ranges[x], seed_ranges[x] + seed_ranges[x + 1]):
                seeds.append(y)
        self.file.readline()
        while self.file.readline().strip():
            while len(line := self.file.readline().strip().split()) > 0:
                [dmin, smin, diff] = [int(x) for x in line]
                ranges[i].append(Range(smin, smin + diff - 1, dmin, dmin + diff - 1))
            i += 1

        min_location = 1000000000
        seeds_count = 1
        for seed in seeds:
            print(f'progress: {round(seeds_count * 100 / len(seeds))}')
            seeds_count += 1
            current_number = seed
            next_number = seed
            for current_ranges in ranges:
                matching_ranges = list(filter(lambda r: r.smin <= current_number <= r.smax, current_ranges))
                if len(matching_ranges) > 0:
                    mr = matching_ranges[0]
                    next_number = mr.dmin + (current_number - mr.smin)
                else:
                    next_number = current_number
                current_number = next_number
            min_location = min(min_location, next_number)
        print(min_location)
