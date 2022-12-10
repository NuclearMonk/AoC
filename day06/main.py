def find_end_of_marker(line, marker_len):
    for i in range (marker_len, len(line.strip())):
        if len(set(line[i-marker_len:i]))==marker_len:
            return i

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        for line in f:
            print(find_end_of_marker(line,14))