from tasks.base import Task


def read_map(file) -> [str]:
    engine_map = []
    for line in file:
        line = line.strip()
        engine_map.append(line)
    return engine_map


def has_neighbour(engine_map: [str], r: int, c: int) -> bool:
    has = False
    max_r = len(engine_map) - 1
    max_c = len(engine_map[0]) - 1
    points_to_check = []
    for r1 in range(r - 1, r + 2):
        for c1 in range(c - 1, c + 2):
            points_to_check.append([r1, c1])
    filtered = filter(lambda x: 0 <= x[0] <= max_r and 0 <= x[1] <= max_c, points_to_check)
    for [r1, c1] in filtered:
        has = has or (engine_map[r1][c1] != '.' and not engine_map[r1][c1].isdigit())
    return has


def get_neighbour(engine_map: [str], r: int, c: int) -> (int, int) or None:
    max_r = len(engine_map) - 1
    max_c = len(engine_map[0]) - 1
    points_to_check = []
    for r1 in range(r - 1, r + 2):
        for c1 in range(c - 1, c + 2):
            points_to_check.append([r1, c1])
    filtered = filter(lambda x: 0 <= x[0] <= max_r and 0 <= x[1] <= max_c, points_to_check)
    for [r1, c1] in filtered:
        if engine_map[r1][c1] == '*':
            return r1, c1
    return None


class Task3(Task):
    def __init__(self, filename="input/3.txt"):
        super().__init__(filename)

    def run1(self):
        engine_sum = 0
        engine_map = read_map(self.file)
        is_num = False
        should_count = False

        for r in range(len(engine_map)):
            row = engine_map[r]
            num_str = ''
            for c in range(len(row)):
                char: str = engine_map[r][c]
                if char.isdigit():
                    num_str += char
                    is_num = True
                    should_count = should_count or has_neighbour(engine_map, r, c)
                elif char == '.':
                    if not is_num:
                        continue
                    if should_count:
                        engine_sum += int(num_str)
                        print(num_str)
                    should_count = is_num = False
                    num_str = ''
                else:
                    if not is_num:
                        continue
                    if should_count:
                        engine_sum += int(num_str)
                        print(num_str)
                    should_count = is_num = False
                    num_str = ''
            if is_num:
                if should_count:
                    engine_sum += int(num_str)
                    print(num_str)
                should_count = is_num = False
        print(f'\n{engine_sum}')

    def run2(self):
        engine_sum = 0
        engine_map = read_map(self.file)
        is_num = False
        last_gear = None
        gears = {}

        for r in range(len(engine_map)):
            row = engine_map[r]
            num_str = ''
            for c in range(len(row)):
                char: str = engine_map[r][c]
                if char.isdigit():
                    num_str += char
                    is_num = True
                    neighbour = get_neighbour(engine_map, r, c)
                    if neighbour is not None:
                        last_gear = neighbour
                elif char == '.':
                    if not is_num:
                        continue
                    if last_gear is not None:
                        key = f'{last_gear[0]: 04d}_{last_gear[1]: 04d}'
                        if key not in gears.keys():
                            gears[key] = []
                        gears[key].append(int(num_str))
                        print(num_str)
                    last_gear = None
                    is_num = False
                    num_str = ''
                else:
                    if not is_num:
                        continue
                    if last_gear is not None:
                        key = f'{last_gear[0]: 04d}_{last_gear[1]: 04d}'
                        if key not in gears.keys():
                            gears[key] = []
                        gears[key].append(int(num_str))
                        print(num_str)
                    last_gear = None
                    is_num = False
                    num_str = ''
            if is_num:
                if last_gear is not None:
                    key = f'{last_gear[0]: 04d}_{last_gear[1]: 04d}'
                    if key not in gears.keys():
                        gears[key] = []
                    gears[key].append(int(num_str))
                    print(num_str)
                last_gear = None
                is_num = False

        for gear in gears.values():
            if len(gear) == 2:
                engine_sum += gear[0] * gear[1]
        print(f'\n{engine_sum}')
