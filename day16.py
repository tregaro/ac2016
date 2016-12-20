def create_longer_state(state):
    a = str(state)
    b = str(a)
    b = ''.join(reversed(b))
    b = b.replace('0', '2').replace('1', '0').replace('2', '1')

    return a + '0' + b


def calc_checksum(state):
    checksum = ''
    for i in xrange(0, len(state), 2):
        checksum += '1' if state[i] == state[i + 1] else '0'
    return checksum


def normal(disk_size, initial_state):
    # longify if needed
    while len(initial_state) < disk_size:
        initial_state = create_longer_state(initial_state)

    # shortify if needed
    initial_state = initial_state[:disk_size]

    # calculate check sum
    check_sum = calc_checksum(initial_state)
    while len(check_sum) % 2 != 1:
        check_sum = calc_checksum(check_sum)

    print check_sum


normal(35651584, '11100010111110100')
