import heapq

obj_indices = [
    'strontium',
    'strontium generator',
    'plutonium',
    'plutonium generator',
    'thulium',
    'thulium generator',
    'ruthenium',
    'ruthenium generator',
    'curium',
    'curium generator',
    'elerium',
    'elerium generator',
    'dilithium',
    'dilithium generator',
]

normal_start_state = [1, 1, 1, 1, 3, 2, 2, 2, 2, 2]
alt_start_state = [1, 1, 1, 1, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1]


class FloorState(object):
    def __init__(self, state, elevator_floor):
        self.state = state
        self.elevator_floor = elevator_floor

    def __str__(self):
        return str(self.__dict__)

    def __hash__(self):
        return hash(str(self.__dict__))

    def __ne__(self, other):
        return not (self == other)

    def __eq__(self, other):
        if self.elevator_floor == other.elevator_floor:
            return self.state == other.state
        return False

    def reached_goal(self):
        return all(floor == 4 for floor in self.state)

    def is_valid(self):
        # if the elevator is on an invalid floor
        if not 1 <= self.elevator_floor <= 4:
            return False

        # if any element is on an invalid floor
        if any(not 1 <= element <= 4 for element in self.state):
            return False

        index = 0
        for chip_floor_num in self.state[::2]:
            current_index = index
            index += 2
            # if we are not on the same floor as our generator
            if chip_floor_num != self.state[current_index + 1]:
                # if there are any other generators on this floor
                if any(chip_floor_num == gen_floor_num for gen_floor_num in self.state[1::2]):
                    return False

        return True

    def valid_states(self):
        # This is a generator because why not :)
        for first_index in range(len(self.state)):
            # If we are not on the right floor
            if self.state[first_index] != self.elevator_floor:
                continue

            new_state = FloorState(list(self.state), self.elevator_floor)
            # move one thing down
            new_state.state[first_index] -= 1
            new_state.elevator_floor -= 1
            if new_state.is_valid():
                yield FloorState(list(new_state.state), new_state.elevator_floor)

            # move one thing up
            new_state.state[first_index] += 2
            new_state.elevator_floor += 2
            if new_state.is_valid():
                yield FloorState(list(new_state.state), new_state.elevator_floor)

            # reset to our initial state
            new_state.state[first_index] -= 1
            new_state.elevator_floor -= 1

            for second_index in range(first_index + 1, len(self.state)):
                # move two things down
                new_state.state[first_index] -= 1
                new_state.state[second_index] -= 1
                new_state.elevator_floor -= 1
                if new_state.is_valid():
                    yield FloorState(list(new_state.state), new_state.elevator_floor)

                # move two things up
                new_state.state[first_index] += 2
                new_state.state[second_index] += 2
                new_state.elevator_floor += 2
                if new_state.is_valid():
                    yield FloorState(list(new_state.state), new_state.elevator_floor)

                # reset to our initial state
                new_state.state[first_index] -= 1
                new_state.state[second_index] -= 1
                new_state.elevator_floor -= 1


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def heuristic(b):
    val = 0
    for floor in b.state:
        val += 4 - floor
    return pow(val, 2)


def a_star_search(start):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    cost_so_far = {start: 0}

    while not frontier.empty():
        current = frontier.get()
        if current.reached_goal():
            return cost_so_far[current]

        for next in current.valid_states():
            new_cost = cost_so_far[current] + 1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next)
                frontier.put(next, priority)

    return None


# print "Normal steps to goal: ", a_star_search(FloorState(normal_start_state, 1))
print "Alt steps to goal: ", a_star_search(FloorState(alt_start_state, 1))
