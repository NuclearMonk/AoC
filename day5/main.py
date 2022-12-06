from itertools import takewhile


class CrateMover9000():

    def __init__(self, lists) -> None:
        self.stacks = lists

    def move(self, count, src, dest):
        for i in range(count):
            # We repeat the following operation COUNT times,
            # Pop the top of SRC stack, and append it to the top of destination
            self.stacks[dest-1].append(self.stacks[src-1].pop())

    def __str__(self) -> str:
        return "\n".join(f"{i}: {l}" for i, l in enumerate(self.stacks))


class CrateMover9001(CrateMover9000):

    def move(self, count, src, dest):
        self.stacks[dest-1] += self.stacks[src-1][-count:]
        for i in range(count):
            self.stacks[src-1].pop()


def read_initial_state(f):
    # Read input till we find a new line the empty line
    input_data = [x for x in takewhile(lambda x: x.strip(), f)]
    # Read the int value of the last row
    last_row = int(input_data[-1].split()[-1])
    # Create a bunch of empty lists to hold our data
    stacks = [[] for _ in range(last_row)]
    for l in input_data[:-1]:  # ignore the last line cause it will be the column ID line
        # skip 4 because there are 3 empty spaces between each collumn
        for x, i in enumerate(range(1, len(l), 4)):
            if l[i] != ' ':  # check if position isn't blank space
                # insert into the start of the corresponding list, doing start saves a reverse operation later
                stacks[x].insert(0, l[i])
    return stacks


def read_instructions(f):
    for l in f:
        yield tuple(int(x) for x in l.split() if x.isnumeric())


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        c = CrateMover9000(read_initial_state(f))
        for instruction in read_instructions(f):
            c.move(*instruction)
    print(*(x[-1] if x else '_' for x in c.stacks), sep='')
