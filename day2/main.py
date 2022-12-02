
points = {'X': 1, 'Y': 2, 'Z': 3}  # lookup table for scores


def inputs_as_tuples(stream):
    # Reads a iterable of strings into tuples that represent them in a cleaner way
    for l in stream:
        yield tuple(l.strip().split())


def calculate_points(iterable):
    # Calculates the points the player makes in a given game for every game in a iterable
    for t in iterable:
        match t:
            case ('A', 'X') | ('B', 'Y') | ('C', 'Z'):  # Case of a tie we yield 3 + the play score
                yield 3 + points[t[1]]
            case ('A', 'Y'):
                yield 6 + points['Y']  # Case of a win with paper
            case ('B', 'Z'):
                yield 6 + points['Z']  # Case of a win with scissors
            case ('C', 'X'):
                yield 6 + points['X']  # Case of a win with paper
            case _:  # All other cases are Losses
                yield points[t[1]]


def calculate_move(input, desired_outcome):
    # Calculate the move that will lead to the desired outcome
    match input, desired_outcome:
        case 'A', 'Tie':
            return 'X'
        case 'B', 'Tie':
            return 'Y'
        case 'C', 'Tie':
            return 'Z'
        case 'A', 'Win':
            return 'Y'
        case 'B', 'Win':
            return 'Z'
        case 'C', 'Win':
            return 'X'
        case 'A', 'Lose':
            return 'Z'
        case 'B', 'Lose':
            return 'X'
        case 'C', 'Lose':
            return 'Y'


def calculate_points_forced_result(iterable):
    #Calculates the points for the forced result version for a iterable of inputs
    for t in iterable:
        match t:
            case a, 'X':  # induce a loss
                yield 0 + points[calculate_move(a, 'Lose')]
            case a, 'Y':  # induce a tie
                yield 3 + points[calculate_move(a, 'Tie')]
            case a, 'Z':  # induce a win
                yield 6 + points[calculate_move(a, 'Win')]


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        print(sum(calculate_points(inputs_as_tuples(f))))
