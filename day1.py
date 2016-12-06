puzzle_input = 'R5, L2, L1, R1, R3, R3, L3, R3, R4, L2, R4, L4, R4, R3, L2, L1, L1, R2, R4, R4, L4, R3, L2, R1, L4, R1, R3, L5, L4, L5, R3, L3, L1, L1, R4, R2, R2, L1, L4, R191, R5, L2, R46, R3, L1, R74, L2, R2, R187, R3, R4, R1, L4, L4, L2, R4, L5, R4, R3, L2, L1, R3, R3, R3, R1, R1, L4, R4, R1, R5, R2, R1, R3, L4, L2, L2, R1, L3, R1, R3, L5, L3, R5, R3, R4, L1, R3, R2, R1, R2, L4, L1, L1, R3, L3, R4, L2, L4, L5, L5, L4, R2, R5, L4, R4, L2, R3, L4, L3, L5, R5, L4, L2, R3, R5, R5, L1, L4, R3, L1, R2, L5, L1, R4, L1, R5, R1, L4, L4, L4, R4, R3, L5, R1, L3, R4, R3, L2, L1, R1, R2, R2, R2, L1, L1, L2, L5, L3, L1'

steps = puzzle_input.split(', ')

directions = {
    'north': (0, 1),
    'south': (0, -1),
    'east': (1, 0),
    'west': (-1, 0)
}

current_direction = 'north'
current_pos = (0, 0)

direction_map = {
    'north': {'R': 'east', 'L': 'west'},
    'south': {'R': 'west', 'L': 'east'},
    'east': {'R': 'south', 'L': 'north'},
    'west': {'R': 'north', 'L': 'south'}
}

visited_positions = [current_pos]
duplicated_point = None

for step in steps:
    direction = step[0]
    distance = int(step[1:])

    # turn first
    current_direction = direction_map[current_direction][direction]

    # then move in the new direction
    for i in xrange(0, distance):
        current_pos = (current_pos[0] + directions[current_direction][0],
                       current_pos[1] + directions[current_direction][1])

        print "current pos: ", current_pos
        if current_pos not in visited_positions:
            visited_positions.append(current_pos)
        else:
            duplicated_point = current_pos
            break

    if duplicated_point is not None:
        break

print "last pos: ", current_pos
print "distance: ", abs(current_pos[0]) + abs(current_pos[1])
