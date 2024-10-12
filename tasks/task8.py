import math
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

    def run2_too_slow(self):
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

    def run2(self):
        path, directions, a_states = read_file(self.file)
        steps_to_state_z = {}
        for a_state in a_states:
            visited_states = {}
            current_state = a_state
            i = 0
            steps_count = 0
            while True:
                if current_state not in visited_states:
                    visited_states[current_state] = []
                if i in visited_states[current_state]:
                    break
                if current_state.endswith('Z'):
                    if a_state not in steps_to_state_z:
                        steps_to_state_z[a_state] = steps_count
                visited_states[current_state].append(i)
                current_state = directions[current_state][path[i]]
                i = (i + 1) % len(path)
                steps_count += 1
        print(math.lcm(*[steps_to_state_z[x] for x in steps_to_state_z]))
