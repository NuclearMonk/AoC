from itertools import islice


def cpu(iterable):
    register = 1
    for instruction in iterable:
        match instruction.strip().split():
            case 'noop', :
                yield register
            case 'addx', x:
                yield register
                yield register
                register += int(x)
    yield register


def part1(f):
    register_values = cpu(f)
    pairs = enumerate(register_values)
    offset_pairs = map(lambda p: (p[0]+1, p[1]), pairs)
    filtered = filter(lambda p: p[0] in range(20, 221, 40), offset_pairs)
    ins_times_value = map(lambda p: p[0]*p[1], filtered)
    print(sum(ins_times_value))


def part2(f):
    register_values = cpu(f)
    crt_cpu_pairs = enumerate(register_values)
    pixel_state = map(
        lambda pair: '█' if pair[1]-1 <= pair[0] % 40 <= pair[1]+1 else ' ', crt_cpu_pairs)
    for _ in range(6):
        print(* islice(pixel_state, 40), sep='', end='\n')


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        part2(f)
