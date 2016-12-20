from hashlib import md5

puzzle_input = 'ahsbgdzn'


def find_special_substring(s, num_chars=3):
    for index, char in enumerate(s):
        if s[index:index + num_chars] == char * 3:
            return char

    return None


def hash_at_index(i):
    return md5(puzzle_input + str(i)).hexdigest().lower()


crazy_hash_cache = {}


def crazy_hash_at_index(i):
    global crazy_hash_cache
    if i in crazy_hash_cache:
        return crazy_hash_cache[i]

    h = hash_at_index(i)
    for _ in xrange(2016):
        h = md5(h).hexdigest().lower()

    crazy_hash_cache[i] = h
    return h


def normal():
    found_keys = []

    outer_index = 0
    while len(found_keys) < 64:
        h = hash_at_index(outer_index)

        c = find_special_substring(h, 3)
        if c is not None:
            for index in xrange(outer_index + 1, outer_index + 1000):
                th = hash_at_index(index)
                if c * 5 in th:
                    found_keys.append(outer_index)
                    print 'Found key at index: ', outer_index
                    print 'Hash: ', h
                    print 'Inner hash: ', index, th
                    print ''
                    break

        outer_index += 1

    print len(found_keys)
    print 'Last key at index: ', found_keys[-1]


def alt():
    found_keys = []

    outer_index = 0
    while len(found_keys) < 64:
        h = crazy_hash_at_index(outer_index)

        c = find_special_substring(h, 3)
        if c is not None:
            for index in xrange(outer_index + 1, outer_index + 1000):
                th = crazy_hash_at_index(index)
                if c * 5 in th:
                    found_keys.append(outer_index)
                    print 'Found key at index: ', outer_index
                    print 'Hash: ', h
                    print 'Inner hash: ', index, th
                    print ''
                    break

        outer_index += 1

    print len(found_keys)
    print 'Last key at index: ', found_keys[-1]


alt()
