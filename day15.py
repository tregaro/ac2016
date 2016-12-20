puzzle_input = '''Disc #1 has 13 positions; at time=0, it is at position 10.
Disc #2 has 17 positions; at time=0, it is at position 15.
Disc #3 has 19 positions; at time=0, it is at position 17.
Disc #4 has 7 positions; at time=0, it is at position 1.
Disc #5 has 5 positions; at time=0, it is at position 0.
Disc #6 has 3 positions; at time=0, it is at position 1.'''

normal_discs = [
    (13, 10),
    (17, 15),
    (19, 17),
    (7, 1),
    (5, 0),
    (3, 1)
]

alt_discs = normal_discs + [(11, 0)]

test_case = [
    (5, 4),
    (2, 1)
]


def state_at_time_is_valid(t, input_state):
    for index in xrange(len(input_state)):
        positions, start_pos = input_state[index]
        disc_time = index + t + 1
        current_pos = (start_pos + disc_time) % positions
        if current_pos != 0:
            return False

    return True


def solve_puzzle(discs):
    time = 0
    while not state_at_time_is_valid(time, discs):
        time += 1

    print 'Valid at time: ', time


solve_puzzle(alt_discs)
