from collections import deque

from day13_input import puzzle_input


def is_wall(pos):
    x, y = pos
    if x < 0 or y < 0:
        return True

    bin_num = str(bin(x * x + 3 * x + 2 * x * y + y + y * y + puzzle_input))[2:]
    return bin_num.count('1') % 2 == 1


def find_path(start, goal, max_cost=-1):
    front = deque()
    seen = set()
    front.append((start, None, 0))

    while front:
        current_state = front.popleft()
        current_pos = current_state[0]
        current_cost = current_state[2]

        if current_pos in seen or 0 < max_cost < current_cost:
            continue

        if current_pos == goal:
            return current_state

        seen.add(current_pos)

        directions = [
            (current_pos[0], current_pos[1] + 1),
            (current_pos[0], current_pos[1] - 1),
            (current_pos[0] - 1, current_pos[1]),
            (current_pos[0] + 1, current_pos[1])
        ]

        for direction in directions:
            if not is_wall(direction):
                front.append((direction, current_state, current_cost + 1))

    print 'Number of objects seen:', len(seen)
    return seen


def build_path(path):
    if path is None:
        return []

    steps = [path[0]]
    path = path[1]
    while path != None:
        steps.append(path[0])
        path = path[1]

    return steps


def normal():
    puzzle_start = (1, 1)
    puzzle_goal = (31, 39)
    puzzle_path = find_path(puzzle_start, puzzle_goal)

    path = build_path(puzzle_path)
    print path
    print len(path) - 1


def alt():
    puzzle_start = (1, 1)
    puzzle_goal = (50, 50)
    puzzle_path = find_path(puzzle_start, puzzle_goal, 50)

    num_coords = 0
    for y in xrange(50):
        line = ''
        for x in xrange(50):
            if (x, y) in puzzle_path:
                assert not is_wall((x, y))
                line += 'O'
                num_coords += 1
            else:
                line += '#' if is_wall((x, y)) else '.'

        print line

    assert len(puzzle_path) == num_coords


alt()
