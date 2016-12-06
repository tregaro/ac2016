import hashlib

puzzle_input = 'abbhdwsy'


def normal():
    password = ''
    index = 0

    # normal
    while len(password) < 8:
        hashed = hashlib.md5(puzzle_input + str(index)).hexdigest()
        is_valid = hashed[0:5] == 5 * '0'

        if is_valid:
            password += hashed[5:6]

        index += 1

    print password


def alt():
    password = [None] * 8
    index = 0

    while None in password:
        hashed = hashlib.md5(puzzle_input + str(index)).hexdigest()
        is_valid = hashed[0:5] == 5 * '0'

        if is_valid:
            position = int(hashed[5:6]) if hashed[5:6].isdigit() else -1
            if 0 <= position < len(password) and password[position] is None:
                password[position] = hashed[6:7]

                print ''.join(['-' if v is None else v for v in password])

        index += 1

    print ''.join(['-' if v is None else v for v in password])


alt()
