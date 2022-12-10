import numpy as np
from itertools import takewhile


def read_file_to_ndarray(f):
    l = []
    for line in f:
        l.append([int(c) for c in line.strip()])
    return np.array(l)


def find_left_to_right_visibility(ndarray):
    out = []
    for row in ndarray:
        out.append([True if i == 0 else row[i] > max(row[0:i])
                   for i in range(len(row))])

    return np.array(out)

def visible_trees(iterable, max_height):
    count = 0
    for i in iterable:
        count+=1
        if i >= max_height:
            return count
    return count

def find_right_scenic_score(ndarray):
    out = []
    for row in ndarray:
            out.append([visible_trees(row[i+1:], row[i]) for i in range(len(row))])
    return np.array(out)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        m = read_file_to_ndarray(f)
        visibility = np.full_like(m, False)
        scenic = np.full_like(m, 1)
        for r in range(4):
            visibility += np.rot90(find_left_to_right_visibility(np.rot90(m, r)), -r)
            scenic *= np.rot90(find_right_scenic_score(np.rot90(m, r)), -r)
        print("Visible Count:", np.count_nonzero(visibility))
        print("Max Scenic Score:", np.max(scenic))
