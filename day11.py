from collections import deque, namedtuple

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

easy_start_state = [1, 1, 1, 1, 1, 1]
normal_start_state = [1, 1, 1, 1, 3, 2, 2, 2, 2, 2]
alt_start_state = [1, 1, 1, 1, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1]
use_tuple = True

if use_tuple:
    FloorState = namedtuple('FloorState', ['state', 'elevator_floor', 'cost'])


    def is_valid(state):
        index = 0
        for chip_floor_num in state[::2]:
            current_index = index
            index += 2
            # if we are not on the same floor as our generator
            if chip_floor_num != state[current_index + 1]:
                # if there are any other generators on this floor
                if any(chip_floor_num == gen_floor_num for gen_floor_num in state[1::2]):
                    return False

        return True


    def state_hash(state):
        # all items are equivalent so we count the number of generators and chips per floor
        items_per_floor = ''
        for floor_index in xrange(1, 5):
            num_chips = 0
            num_gens = 0
            for item_index in xrange(len(state.state) / 2):
                chip_index = item_index * 2
                gen_index = chip_index + 1
                if state.state[chip_index] == floor_index:
                    num_chips += 1
                if state.state[gen_index] == floor_index:
                    num_gens += 1

            items_per_floor += str(num_chips)
            items_per_floor += str(num_gens)

        return hash(items_per_floor + str(state.elevator_floor))


    def valid_states(state):
        # This is a generator because why not :)
        for first_index in range(len(state.state)):
            # If we are not on the right floor
            if state.state[first_index] != state.elevator_floor:
                continue

            temp_state = list(state.state)
            temp_elevator = state.elevator_floor
            # move one thing down
            temp_state[first_index] -= 1
            temp_elevator -= 1
            if 1 <= temp_state[first_index] <= 4 and is_valid(temp_state):
                yield FloorState(list(temp_state), temp_elevator, state.cost + 1)

            # move one thing up
            temp_state[first_index] += 2
            temp_elevator += 2
            if 1 <= temp_state[first_index] <= 4 and is_valid(temp_state):
                yield FloorState(list(temp_state), temp_elevator, state.cost + 1)

            # reset to our initial state
            temp_state[first_index] -= 1
            temp_elevator -= 1

            for second_index in range(first_index + 1, len(state.state)):
                # If we are not on the right floor
                if state.state[second_index] != state.elevator_floor:
                    continue

                # move two things down
                temp_state[first_index] -= 1
                temp_state[second_index] -= 1
                temp_elevator -= 1
                if 1 <= temp_state[first_index] <= 4 and 1 <= temp_state[second_index] <= 4:
                    if is_valid(temp_state):
                        yield FloorState(list(temp_state), temp_elevator, state.cost + 1)

                # move two things up
                temp_state[first_index] += 2
                temp_state[second_index] += 2
                temp_elevator += 2
                if 1 <= temp_state[first_index] <= 4 and 1 <= temp_state[second_index] <= 4:
                    if is_valid(temp_state):
                        yield FloorState(list(temp_state), temp_elevator, state.cost + 1)

                # reset to our initial state
                temp_state[first_index] -= 1
                temp_state[second_index] -= 1
                temp_elevator -= 1


    def reached_goal(state):
        return all(floor == 4 for floor in state.state)

else:
    class FloorState(object):
        __slots__ = ('state', 'elevator_floor', 'cost')

        def __init__(self, state, elevator_floor, cost):
            self.state = state
            self.elevator_floor = elevator_floor
            self.cost = cost

        def __str__(self):
            return str(self.__dict__)

        def __hash__(self):
            return hash(''.join(map(str, self.state)) + str(self.elevator_floor))

        def __ne__(self, other):
            return not (self == other)

        def __eq__(self, other):
            if self.elevator_floor == other.elevator_floor:
                return self.state == other.state
            return False

        def reached_goal(self):
            return all(floor == 4 for floor in self.state)

        def is_valid(self):
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

                new_state = FloorState(list(self.state), self.elevator_floor, 0)
                # move one thing down
                new_state.state[first_index] -= 1
                new_state.elevator_floor -= 1
                if 1 <= new_state.state[first_index] <= 4 and new_state.is_valid():
                    yield FloorState(list(new_state.state), new_state.elevator_floor, 0)

                # move one thing up
                new_state.state[first_index] += 2
                new_state.elevator_floor += 2
                if 1 <= new_state.state[first_index] <= 4 and new_state.is_valid():
                    yield FloorState(list(new_state.state), new_state.elevator_floor, 0)

                # reset to our initial state
                new_state.state[first_index] -= 1
                new_state.elevator_floor -= 1

                for second_index in range(first_index + 1, len(self.state)):
                    # If we are not on the right floor
                    if self.state[second_index] != self.elevator_floor:
                        continue

                    # move two things down
                    new_state.state[first_index] -= 1
                    new_state.state[second_index] -= 1
                    new_state.elevator_floor -= 1
                    if 1 <= new_state.state[first_index] <= 4 and 1 <= new_state.state[second_index] <= 4:
                        if new_state.is_valid():
                            yield FloorState(list(new_state.state), new_state.elevator_floor, 0)

                    # move two things up
                    new_state.state[first_index] += 2
                    new_state.state[second_index] += 2
                    new_state.elevator_floor += 2
                    if 1 <= new_state.state[first_index] <= 4 and 1 <= new_state.state[second_index] <= 4:
                        if new_state.is_valid():
                            yield FloorState(list(new_state.state), new_state.elevator_floor, 0)

                    # reset to our initial state
                    new_state.state[first_index] -= 1
                    new_state.state[second_index] -= 1
                    new_state.elevator_floor -= 1

if use_tuple:
    def a_star_search(start):
        goal_cost = None
        seen = set()

        que = deque()
        que.append(start)

        while len(que) > 0:
            current = que.popleft()
            if state_hash(current) in seen:
                continue

            seen.add(state_hash(current))
            if reached_goal(current):
                return current.cost

            for child_state in valid_states(current):
                que.append(child_state)

        return goal_cost

else:
    def a_star_search(start):
        goal_cost = None
        seen = set()

        que = deque()
        que.append(start)

        while len(que) > 0:
            current = que.popleft()
            if current in seen:
                continue

            seen.add(current)
            if current.reached_goal():
                return current.cost

            for child_state in current.valid_states():
                child_state.cost = current.cost + 1
                que.append(child_state)

        return goal_cost

# print "Normal steps to goal: ", a_star_search(FloorState(normal_start_state, 1, 0))
print "Alt steps to goal: ", a_star_search(FloorState(alt_start_state, 1, 0))
# print "Easy steps to goal: ", a_star_search(FloorState(easy_start_state, 1))
