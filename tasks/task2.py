from tasks.base import Task

RED, GREEN, BLUE = 'red', 'green', 'blue'
RED_LIMIT, GREEN_LIMIT, BLUE_LIMIT = 12, 13, 14


class Task2(Task):
    def __init__(self, filename="input/2.txt"):
        super().__init__(filename)

    def run1(self):
        possible_games = 0
        for line in self.file:
            line = line.strip().removeprefix('Game ')
            [game_no, game_info] = line.split(': ')
            is_possible = True
            for step in game_info.split('; '):
                rgb = {RED: 0, GREEN: 0, BLUE: 0}
                for ball in step.split(', '):
                    [cnt, color] = ball.split()
                    rgb[color] = int(cnt)
                if rgb[RED] > RED_LIMIT or rgb[GREEN] > GREEN_LIMIT or rgb[BLUE] > BLUE_LIMIT:
                    is_possible = False
            if is_possible:
                possible_games += int(game_no)
        print(possible_games)

    def run2(self):
        possible_games_sum = 0
        for line in self.file:
            line = line.strip().removeprefix('Game ')
            [game_no, game_info] = line.split(': ')
            rgb = {RED: 0, GREEN: 0, BLUE: 0}
            for step in game_info.split('; '):
                for ball in step.split(', '):
                    [cnt, color] = ball.split()
                    rgb[color] = max(int(cnt), rgb[color])
            possible_games_sum += rgb[RED] * rgb[GREEN] * rgb[BLUE]
        print(possible_games_sum)
