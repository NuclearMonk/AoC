from itertools import filterfalse

def read_pairs_to_tuple(iterable):
    for s in iterable:
        a, b = s.strip().split(',')
        yield tuple(a.split('-')), tuple(b.split('-'))

def to_int_tuple(iterable):
    for pair in iterable:
        x = (int(pair[0][0]), int(pair[0][1]))
        y = (int(pair[1][0]), int(pair[1][1]))
        yield x[0],x[1],y[0],y[1]

def check_full_overlaps(iterable):
    for t in iterable:
        if t[0]<= t[2] and t[1]>= t[3]:
            yield True
        elif t[0]>= t[2] and t[1]<= t[3]:
            yield True
        else:
            yield False       

def check_overlaps(iterable):
    for t in iterable:
        yield len([x for x in range(t[0], t[1]+1) if x in range(t[2], t[3]+1)])

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        # print(len(list(filterfalse(lambda x: not x,check_full_overlaps(to_int_tuple(read_pairs_to_tuple(f)))))))
        print(len(list(filterfalse(lambda x: not x,check_overlaps(to_int_tuple(read_pairs_to_tuple(f)))))))
