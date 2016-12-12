import heapq
from copy import deepcopy
from itertools import permutations

from day11_input import puzzle_input


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


class FloorState(object):
    def __init__(self, state, current_floor):
        self.state = state
        assert len(state) == 4
        self.current_floor = current_floor

    def valid_moves(self):
        current_state, current_floor = self.state, self.current_floor
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
            for thing in current_state[current_floor]:
                temp_floor_state = current_state[new_floor] + [thing]
                if floor_is_valid(temp_floor_state):
                    new_floor_state = deepcopy(self.state)
                    new_floor_state[new_floor] = temp_floor_state
                    new_floor_state[current_floor].remove(thing)
                    possible_states.append(FloorState(new_floor_state, new_floor))

            # moving two things
            things_permutations = list(permutations(current_state[current_floor], 2))
            for i in things_permutations:
                thing_permutations = list(i)
                if floor_is_valid(thing_permutations):
                    temp_floor_state = current_state[new_floor] + thing_permutations
                    if floor_is_valid(temp_floor_state):
                        new_floor_state = deepcopy(self.state)
                        new_floor_state[new_floor] = temp_floor_state
                        new_floor_state[current_floor].remove(thing_permutations[0])
                        new_floor_state[current_floor].remove(thing_permutations[1])
                        possible_states.append(FloorState(new_floor_state, new_floor))

        return possible_states


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


def heuristic(a, b):
    return len(a.state[3]) - len(b.state[3])


def a_star_search(start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in current.valid_moves():  # graph.neighbors(current):
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


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
    goal = [[], [], [], []]
    for floor in floors:
        goal[3].extend(floor)

    print a_star_search(FloorState(floors, 0), FloorState(goal, 3))

    # Rule 1: Have to have at least one chip or generator to go in lift.
    # Rule 2: Chips will be fried if on the same floor as a generator unless it's their generator
    # Goal: Bring everything to floor 4 in as few steps as possible


normal()
