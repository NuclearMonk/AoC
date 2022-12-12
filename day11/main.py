from __future__ import annotations
from collections import deque
from typing import Callable, Dict, List
from itertools import takewhile


class Monkey():

    def __init__(self, inventory: List[int], operation: Callable[[int], int],worry_mod:int, on_true: int, on_fail) -> None:
        self.inventory: deque[int] = deque(inventory)
        self.operation:Callable[[int],int] = operation
        self.worry_mod:int = worry_mod
        self.on_true:int = on_true
        self.on_false:int = on_fail
        self.inspection_count:int = 0

    def add_item(self, item):
        self.inventory.append(item)

    def tick(self, monkeys: Dict[int, Self], common=1):
        for item in self.inventory:
            # print('item:',item)
            self.inspection_count+=1
            if common==1:
                #part 1
                new_worry_level = self.operation(item) // 3 
            else:
                #part 2
                new_worry_level = self.operation(item) % common
            # print('new_worry_level:',new_worry_level)
            if new_worry_level% self.worry_mod ==0:
                # print('throwing to:',self.on_true)
                monkeys[self.on_true].add_item(new_worry_level)
            else:
                # print('throwing to:',self.on_false)
                monkeys[self.on_false].add_item(new_worry_level)
        self.inventory = deque()

    def __str__(self) -> str:
        return ', '.join(map(lambda x: str(x), self.inventory))
    
    @staticmethod
    def starting_items_from_string(item_line: str)-> List[int]:
        _, values = item_line.strip().split(':')
        return [int(value) for value in values.split(',')]

    @staticmethod
    def operation_from_string(operation_line: str)-> Callable[[int],int]:
        _, l = operation_line.split('=')
        return eval('lambda old:' + l.strip())

    @staticmethod
    def test_from_string(test_line: str)-> Callable[[int],bool]:
        _, l = test_line.split('by')
        return int(l.strip())

    @staticmethod
    def get_throw_target_from_string(test_line: str)->int:
        _, l = test_line.split('monkey')
        return int(l)

    @staticmethod
    def monkeys_from_iterable(f):
        for _ in f:
            lines = list(takewhile(lambda x: x.strip(), f))
            yield Monkey(
                Monkey.starting_items_from_string(lines[0]),
                Monkey.operation_from_string(lines[1]),
                Monkey.test_from_string(lines[2]),
                Monkey.get_throw_target_from_string(lines[3]),
                Monkey.get_throw_target_from_string(lines[4]),
            )

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        #PART 1
        # monkeys= { key:value for (key,value) in enumerate(Monkey.monkeys_from_iterable(f))}
        # for i in range(20):
        #     for id, monkey in monkeys.items():
        #         monkey.tick(monkeys)
        # for id, monkey in monkeys.items():
        #     print(id,monkey,monkey.inspection_count, sep=': ')
            
        # x,y = sorted([monkey.inspection_count for monkey in monkeys.values()])[-2:]
        # print(x,y)
        # print(x*y)
        monkeys= { key:value for (key,value) in enumerate(Monkey.monkeys_from_iterable(f))}
        common_divisor = 1
        for _,monkey in monkeys.items():
            common_divisor *= monkey.worry_mod
        for i in range(10000):
            for id, monkey in monkeys.items():
                monkey.tick(monkeys, common=common_divisor)
        for id, monkey in monkeys.items():
            print(id,monkey.inspection_count, sep=': ')
        x,y = sorted([monkey.inspection_count for monkey in monkeys.values()])[-2:]
        print(x,y)
        print(x*y)