from __future__ import annotations
from dataclasses import dataclass
from math import sqrt


@dataclass
class Point():
    x: int
    y: int

    def __add__(self, o):
        return Point(self.x+o.x, self.y + o.y)

    def __sub__(self, o):
        return Point(self.x-o.x, self.y - o.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)

    def __iadd__(self, o):
        self.x = self.x + o.x
        self.y = self.y + o.y
        return self

    def __isub__(self, o):
        self.x = self.x - o.x
        self.y = self.y - o.y
        return self

    @staticmethod
    def distance(a, b):
        return abs(a-b)


@dataclass
class RopePoint():
    id: int
    position: Point
    tail: RopePoint
    positions: set

    def __init__(self, id=0, length: int = 1) -> None:
        self.id = id
        self.position = Point(0, 0)
        self.tail = RopePoint(id+1, length) if id < length-1 else None
        self.positions = set()
        self.positions.add((0, 0))

    def update(self, parent_pos: Point):
        if Point.distance(parent_pos, self.position) < 2:
            return
        match parent_pos, self.position:
            case h, t if h.x > t.x and h.y > t.y:
                self.position += Point(1, 1)
            case h, t if h.x > t.x and h.y < t.y:
                self.position += Point(1, -1)
            case h, t if h.x < t.x and h.y > t.y:
                self.position += Point(-1, 1)
            case h, t if h.x < t.x and h.y < t.y:
                self.position += Point(-1, -1)
            case h, t if h.x == t.x and h.y > t.y:
                self.position += Point(0, 1)
            case h, t if h.x == t.x and h.y < t.y:
                self.position += Point(0, -1)
            case h, t if h.x > t.x and h.y == t.y:
                self.position += Point(1, 0)
            case h, t if h.x < t.x and h.y == t.y:
                self.position += Point(-1, 0)
        self.positions.add((self.position.x, self.position.y))
        if self.tail:
            self.tail.update(self.position)


class RopeHead(RopePoint):

    def move(self, direction, count):
        for i in range(count):
            match direction:
                case 'U':
                    self.position += Point(0, 1)
                case 'D':
                    self.position -= Point(0, 1)
                case 'R':
                    self.position += Point(1, 0)
                case 'L':
                    self.position -= Point(1, 0)
            self.tail.update(self.position)

    def get_last(self):
        x = self
        while x.tail != None:
            x = x.tail
        return x

    def __iter__(self):
        x = self
        while x != None:
            yield x
            x = x.tail


def read_moves(f):
    for l in f:
        direction, count = l.strip().split()
        yield direction, int(count)


if __name__ == '__main__':
    r = RopeHead(length=10)
    with open('input.txt', 'r') as f:
        for move in read_moves(f):
            r.move(*move)
        print(len(r.get_last().positions))
