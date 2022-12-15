from itertools import pairwise


class Cave():

    def __init__(self) -> None:
        self.topology: set = set()
        self.max_depth = 0

    def __str__(self) -> str:
        return str(self.topology)

    def add_geometry(self, path):
        for start, end in pairwise(path):
            match start, end:
                case start, end if start[0] == end[0] and start[1] < end[1]:
                    for y in range(start[1], end[1]+1):
                        self.topology.add((start[0], y))
                case start, end if start[0] == end[0] and start[1] > end[1]:
                    for y in range(start[1], end[1]-1, -1):
                        self.topology.add((start[0], y))
                case start, end if start[1] == end[1] and start[0] < end[0]:
                    for x in range(start[0], end[0]+1):
                        self.topology.add((x, start[1]))
                case start, end if start[1] == end[1] and start[0] > end[0]:
                    for x in range(start[0], end[0]-1, -1):
                        self.topology.add((x, start[1]))

    def freeze(self):
        self.topology = frozenset(self.topology)
        self.max_depth = max((x[1] for x in self.topology))


def sand_simulation(cave: Cave):
    start_x = 500
    start_y = 0
    sand = set()
    while True:
        x = start_x
        for i in range(start_y, cave.max_depth):
            if (x, i+1) not in cave.topology and (x, i+1) not in sand:
                continue
            elif (x-1, i+1) not in cave.topology and (x-1, i+1) not in sand:
                x -= 1
            elif (x+1, i+1) not in cave.topology and (x+1, i+1) not in sand:
                x += 1
            else:
                print(x, i)
                sand.add((x, i))
                break
        else:
            return sand


def full_sand_simulation(cave: Cave):
    start_x = 500
    start_y = 0
    sand = set()
    while True:
        x = start_x
        for i in range(start_y, cave.max_depth+2):
            if (x, i+1) not in cave.topology and (x, i+1) not in sand:
                continue
            elif (x-1, i+1) not in cave.topology and (x-1, i+1) not in sand:
                x -= 1
            elif (x+1, i+1) not in cave.topology and (x+1, i+1) not in sand:
                x += 1
            elif (x, i) == (start_x, start_y):
                sand.add((x, i))
                return sand
            else:
                sand.add((x, i))
                break
        else:
            print(x, i)
            sand.add((x, i))


def read_paths(file):
    for line in file:
        path = [(int(x), int(y)) for x, y in map(
            lambda l:l.strip().split(','), line.strip().split('->'))]
        yield path


if __name__ == '__main__':
    cave = Cave()
    with open('input.txt', 'r') as f:
        paths = list(read_paths(f))
        for path in paths:
            cave.add_geometry(path)
        cave.freeze()
        # print(len(sand_simulation(cave)))
        print(len(full_sand_simulation(cave)))
