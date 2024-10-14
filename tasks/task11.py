from typing import TextIO

from tasks.base import Task

class Galaxy:
    def __init__(self, r: int, c: int):
        self.r = r
        self.c = c

    def distance(self, other: 'Galaxy', empty_rows: [int], empty_columns: [int], empty_multiplier: int = 2):
        vertical = horizontal = 0
        for v in range(min(self.r, other.r), max(self.r, other.r), 1):
            vertical += empty_multiplier if v in empty_rows else 1
        for h in range(min(self.c, other.c), max(self.c, other.c), 1):
            horizontal += empty_multiplier if h in empty_columns else 1
        return vertical + horizontal


def read_file(file: TextIO):
    galaxy_map = []
    galaxies = []
    r = 0
    for line in file:
        c = 0
        galaxy_map.append([])
        for position in line.strip():
            if position == '#':
                galaxies.append(Galaxy(r, c))
            galaxy_map[r].append(1 if position == '#' else 0)
            c += 1
        r += 1
    row_index = 0
    empty_rows = []
    for row in galaxy_map:
        if sum(row) == 0:
            empty_rows.append(row_index)
        row_index += 1
    empty_columns = []
    for column_index in range(len(galaxy_map[0])):
        if sum([row[column_index] for row in galaxy_map]) == 0:
            empty_columns.append(column_index)
    return galaxy_map, galaxies, empty_rows, empty_columns


class Task11(Task):
    def __init__(self, filename="input/11.txt"):
        super().__init__(filename)

    def run1(self):
        galaxy_map, galaxies, empty_rows, empty_columns = read_file(self.file)
        distance_sum = 0
        for i in range(len(galaxies) - 1):
            for j in range(i + 1, len(galaxies)):
                distance = galaxies[i].distance(galaxies[j], empty_rows, empty_columns)
                distance_sum += distance
        print(distance_sum)

    def run2(self):
        galaxy_map, galaxies, empty_rows, empty_columns = read_file(self.file)
        distance_sum = 0
        for i in range(len(galaxies) - 1):
            for j in range(i + 1, len(galaxies)):
                distance = galaxies[i].distance(galaxies[j], empty_rows, empty_columns, 1000000)
                distance_sum += distance
        print(distance_sum)
