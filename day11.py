from itertools import permutations

from day11_input import puzzle_input

GENERATOR = 'G'
MICROCHIP = 'M'
BOTH = 'B'


def floor_is_valid(floor):
    floor.sort()

    # valid if we are all generators
    all_generators = True
    for thing in floor:
        if thing[1] != GENERATOR:
            all_generators = False
            break

    if all_generators:
        return True

    # valid if we are all microchips
    all_microchips = True
    for thing in floor:
        if thing[1] != MICROCHIP:
            all_microchips = False
            break

    if all_microchips:
        return True

    # create list without any pairs
    without_pairs = []
    for thing in floor:
        is_pair = False
        for other_thing in floor:
            if thing != other_thing and thing[0] == other_thing[0]:
                is_pair = True
                break

        if not is_pair:
            without_pairs.append(thing)

    all_generators = True
    for thing in without_pairs:
        if thing[1] != GENERATOR:
            all_generators = False
            break

    if all_generators:
        return True

    # if we are a micro chip and there is a generator that is not ours then we are not valid
    for thing in without_pairs:
        if thing[1] == MICROCHIP:
            valid_thing = True

            for other_thing in floor:
                if thing != other_thing and other_thing[1] == GENERATOR:
                    valid_thing = False
                    break

            if not valid_thing:
                return False

    return True


def valid_moves(state, current_floor):
    possible_states = []

    new_floors = []
    # going up if we can
    if current_floor < 3:
        new_floors.append(current_floor + 1)

    # going down if we can
    if current_floor > 0:
        new_floors.append(current_floor - 1)

    for new_floor in new_floors:
        # moving one thing
        for thing in state[current_floor]:
            temp_floor_state = state[new_floor] + [thing]
            if floor_is_valid(temp_floor_state):
                possible_states.append(temp_floor_state)

        # moving two things
        things_permutations = list(permutations(state[current_floor], 2))
        for i in things_permutations:
            thing_permutations = list(i)
            if floor_is_valid(thing_permutations):
                temp_floor_state = state[new_floor] + thing_permutations
                if floor_is_valid(temp_floor_state):
                    possible_states.append(temp_floor_state)

    return possible_states


def normal():
    floors = puzzle_input.splitlines()
    for index, floor in enumerate(floors):
        floor = floor.split('a ')[1:]
        parts = []
        for part in floor:
            if 'generator' in part:
                parts.append(part.split(' ')[0][0] + GENERATOR)
            elif 'microchip' in part:
                parts.append(part.split('-')[0][0] + MICROCHIP)

        floors[index] = parts
        print "Floor: ", index + 1, floors[index]

    # You start on the first floor
    current_floor = 0
    valid_moves(floors, current_floor)

    # Rule 1: Have to have at least one chip or generator to go in lift.
    # Rule 2: Chips will be fried if on the same floor as a generator unless it's their generator
    # Goal: Bring everything to floor 4 in as few steps as possible


normal()
