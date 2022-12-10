from itertools import islice

def read_backpack_list(iterable):
    # reads a backpack into 2 strings in a tuples
    for backpack in iterable:
        s = backpack.strip()
        first, second = s[:len(s)//2], s[len(s)//2:]
        yield (first,second)

def backpack_tuple_to_set(iterable):
    #converts a tuple of strings into a tuple of sets
    for backpack in iterable:
        f = set()
        s = set()
        for c in backpack[0]:
            f.add(ord(c))

        for c in backpack[1]:
            s.add(ord(c))
        yield (f,s)

def list_intersections(iterable):
    #finds the first intersection of  any amount of sets
    for tuple_sets in iterable:
        yield tuple(set.intersection(*tuple_sets))[0]

def char_to_priority(char):
    #converts a int that represents a char into it's rule defined priority
    if ord('a')<=char<=ord('z'):
        return char-ord('a') +1
    elif ord('A')<= char <=ord('Z'):
        return char - ord('A') + 27
    return 0

def backpack_string_to_set(iterable):
    #Converts a backpack into a single set
    for backpack in iterable:
        s = backpack.strip()
        x = set()
        for c in s:
            x.add(ord(c))
        yield x
            
def form_groups(iterable):
    #Groups an iterable into tuples if 3 elements, fails if theres not enough elements
    for element in iterable:
        yield (element, next(iterable),next(iterable))

 
if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        # print(sum(map(char_to_priority, list_intersections(backpack_tuple_to_set(read_backpack_list(f))))))
        print(sum(map(char_to_priority,list_intersections(form_groups(backpack_string_to_set(f))))))