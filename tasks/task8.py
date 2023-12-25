from typing import TextIO

from tasks.base import Task


def read_file(file: TextIO):
    directions = {}
    a_nodes = []
    path = file.readline().strip()
    file.readline()
    while line := file.readline().strip():
        [source, other] = line.split(' = ')
        [left, right] = other.removeprefix('(').removesuffix(')').split(', ')
        directions[source] = {'L': left, 'R': right}
        if source.endswith('A'):
            a_nodes.append(source)
    return path, directions, a_nodes


class Task8(Task):
    def __init__(self, filename="input/8.txt"):
        super().__init__(filename)

    def run1(self):
        path, directions, _ = read_file(self.file)
        current_state = 'AAA'
        next_direction_index = 0
        steps_count = 0
        while current_state != 'ZZZ':
            next_direction = path[next_direction_index]
            next_direction_index = (next_direction_index + 1) % len(path)
            current_state = directions[current_state][next_direction]
            steps_count += 1
        print(steps_count)

    def run2(self):
        path, directions, current_states = read_file(self.file)
        all_are_z = False
        steps_count = 0
        next_direction_index = 0
        while not all_are_z:
            next_direction = path[next_direction_index]
            next_direction_index = (next_direction_index + 1) % len(path)
            all_are_z = True
            for i in range(len(current_states)):
                current_states[i] = directions[current_states[i]][next_direction]
                all_are_z = all_are_z and current_states[i].endswith('Z')
            steps_count += 1
        print(steps_count)
