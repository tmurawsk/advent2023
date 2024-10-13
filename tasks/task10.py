from typing import TextIO

from tasks.base import Task


HAS_DOWN = ['|', 'F', '7']
HAS_UP = ['|', 'J', 'L']
HAS_LEFT = ['-', '7', 'J']
HAS_RIGHT = ['-', 'L', 'F']

PIPE_MAP = {
    '|': {'up': HAS_DOWN, 'right': [], 'down': HAS_UP, 'left': []},
    '-': {'up': [], 'right': HAS_LEFT, 'down': [], 'left': HAS_RIGHT},
    'J': {'up': HAS_DOWN, 'right': [], 'down': [], 'left': HAS_RIGHT},
    'L': {'up': HAS_DOWN, 'right': HAS_LEFT, 'down': [], 'left': []},
    '7': {'up': [], 'right': [], 'down': HAS_UP, 'left': HAS_RIGHT},
    'F': {'up': [], 'right': HAS_LEFT, 'down': HAS_UP, 'left': []},
    '.': {'up': [], 'right': [], 'down': [], 'left': []},
    'S': {'up': HAS_DOWN, 'right': HAS_LEFT, 'down': HAS_UP, 'left': HAS_RIGHT}
}

SHOULD_COUNT = {
    'F': 'J',
    'L': '7'
}


class Pipe:
    def __init__(self, r: int, c: int, prev_r: int = -1, prev_c: int = -1):
        self.r = r
        self.c = c
        self.prev = Pipe(prev_r, prev_c) if prev_r >= 0 else None

    def __eq__(self, other: 'Pipe'):
        return self.r == other.r and self.c == other.c

    def __ne__(self, other: 'Pipe'):
        return not self.__eq__(other)

    def next_step(self, pipes):
        value = pipes[self.r][self.c]
        pipe1, pipe2 = find_neighbour_pipes(pipes, value, self.r, self.c)
        next_pipe = pipe1 if pipe2 is None or pipe1 != self.prev else pipe2
        self.prev = Pipe(self.r, self.c)
        self.r = next_pipe.r
        self.c = next_pipe.c


def read_file(file: TextIO):
    lines = []
    r = start_r = start_c = 0
    for line in file:
        line = line.strip()
        if 'S' in line:
            start_r = r
            start_c = line.index('S')
        lines.append(line)
        r += 1
    return lines, start_r, start_c


def find_neighbour_pipes(pipes, pipe_value: str, r: int, c: int):
    coords: [int] = []
    has_up = has_down = has_left = has_right = False
    if c > 0 and pipes[r][c - 1] in PIPE_MAP[pipe_value]['left']:
        coords.append(r)
        coords.append(c - 1)
        if pipe_value == 'S':
            has_left = True
    if c < len(pipes[0]) - 1 and pipes[r][c + 1] in PIPE_MAP[pipe_value]['right']:
        coords.append(r)
        coords.append(c + 1)
        if pipe_value == 'S':
            has_right = True
    if r > 0 and pipes[r - 1][c] in PIPE_MAP[pipe_value]['up']:
        coords.append(r - 1)
        coords.append(c)
        if pipe_value == 'S':
            has_up = True
    if r < len(pipes) - 1 and pipes[r + 1][c] in PIPE_MAP[pipe_value]['down']:
        coords.append(r + 1)
        coords.append(c)
        if pipe_value == 'S':
            has_down = True
    if pipe_value == 'S':
        if not has_up:
            PIPE_MAP['S']['up'] = []
        if not has_down:
            PIPE_MAP['S']['down'] = []
        if not has_right:
            PIPE_MAP['S']['right'] = []
        if not has_left:
            PIPE_MAP['S']['left'] = []
    return Pipe(coords[0], coords[1], r, c), (None if len(coords) < 4 else Pipe(coords[2], coords[3], r, c))


class Task10(Task):
    def __init__(self, filename="input/10.txt"):
        super().__init__(filename)

    def run1(self):
        pipes, start_r, start_c = read_file(self.file)
        pipe1, pipe2 = find_neighbour_pipes(pipes, 'S', start_r, start_c)
        pipes[start_r] = pipes[start_r].replace('S', '7')
        steps_count = 1
        while pipe1 != pipe2:
            pipe1.next_step(pipes)
            pipe2.next_step(pipes)
            steps_count += 1
        print(steps_count)

    def run2(self):
        pipes, start_r, start_c = read_file(self.file)
        pipe1, pipe2 = find_neighbour_pipes(pipes, 'S', start_r, start_c)
        pipes[start_r] = pipes[start_r].replace('S', 'F') # need to manually set starting pipe
        pipes_coords = [(start_r, start_c), (pipe1.r, pipe1.c), (pipe2.r, pipe2.c)]
        while pipe1 != pipe2:
            pipe1.next_step(pipes)
            pipe2.next_step(pipes)
            pipes_coords.append((pipe1.r, pipe1.c))
            pipes_coords.append((pipe2.r, pipe2.c))
        inside_pipes = 0
        for r in range(len(pipes)):
            are_inside = False
            last_pipe = None
            for c in range(len(pipes[r])):
                pipe = pipes[r][c]
                if (r, c) in pipes_coords:
                    if pipe in ['L', 'J', 'F', '7']:
                        if last_pipe is None:
                            last_pipe = pipe
                        else:
                            are_inside = not are_inside if pipe == SHOULD_COUNT[last_pipe] else are_inside
                            last_pipe = None
                    elif pipe != '-':
                        are_inside = not are_inside
                elif are_inside:
                    inside_pipes += 1
        print(inside_pipes)
