from collections import deque
from hashlib import md5

normal_puzzle_input = 'pslxynzg'
test_case1 = 'ihgpwlah'
test_case2 = 'kglvqrro'
test_case3 = 'ulqzkmiv'

test_case1_answer = 'DDRRRD'
test_case2_answer = 'DDUDRLRRUDRD'
test_case3_answer = 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'


def next_moves(current):
    puzzle_input, path, position, parent, steps = current
    x, y = position

    door_hash = md5(puzzle_input + path).hexdigest()[:4]
    directions = ['U', 'D', 'L', 'R']
    door_state = {}
    for index, direction in enumerate(directions):
        door_state[direction] = door_hash[index] in ['b', 'c', 'd', 'e', 'f']

    movement = {
        'U': (0, -1),
        'D': (0, 1),
        'L': (-1, 0),
        'R': (1, 0)
    }

    for direction in directions:
        if door_state[direction]:
            new_pos = movement[direction][0] + x, movement[direction][1] + y
            if 0 <= new_pos[0] < 4 and 0 <= new_pos[1] < 4:
                yield (puzzle_input, path + direction, new_pos, current, steps + 1)


def normal(text):
    frontier = deque()
    start = (text, '', (0, 0), None, 0)
    frontier.append(start)
    results = []

    while frontier:
        current = frontier.popleft()

        if current[2] == (3, 3):
            results.append(current)
        else:
            for next_move in next_moves(current):
                frontier.append(next_move)

    return results


print normal(test_case1)[0][1] == test_case1_answer
print normal(test_case2)[0][1] == test_case2_answer
print normal(test_case3)[0][1] == test_case3_answer

for result in normal(normal_puzzle_input):
    print len(result[1])
