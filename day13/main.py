from json import loads

def read_packet_pairs(f):
    pairs = f.read().split('\n\n')
    for pair in pairs:
        a, b = pair.strip().split('\n')
        yield loads(a), loads(b)


def read_packets(f):
    for line in f.readlines():
        line = line.strip()
        if line:
            yield loads(line)

def special_compare(a,b):
    match (isinstance(a, int), isinstance(b, int)):
        case (True, True):
            return b-a
        case (False, True):
            return special_compare(a, [b])
        case (True, False):
            return special_compare([a], b)
        case (False, False):
            for p in zip(a, b):
                v = special_compare(*p)
                if v != 0:
                    return v
            return len(b)-len(a)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        # print(sum(map(lambda x: x[0]+1 if x[1] == abs(x[1]) else 0,
        #       enumerate(map(lambda x :special_compare(*x), read_packet_pairs(f))))))
        
        l = list(read_packets(f))
        l.append([[2]])
        l.append([[6]])
        for i in range(len(l)):
            for j in range(0,len(l)-i-1):
                if special_compare(l[j],l[j+1])<0:
                    l[j],l[j+1] = l[j+1], l[j]
                    
        start = l.index([[2]])+1
        end = l.index([[6]])+1
        print(start*end)