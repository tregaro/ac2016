normal_input = '.^..^....^....^^.^^.^.^^.^.....^.^..^...^^^^^^.^^^^.^.^^^^^^^.^^^^^..^.^^^.^^..^.^^.^....^.^...^^.^.'
test_input = '.^^.^.^^^^'


def is_trap(left_center_right):
    assert len(left_center_right) == 3
    traps = [
        '^^.',  # Its left and center tiles are traps, but its right tile is not.
        '.^^',  # Its center and right tiles are traps, but its left tile is not.
        '^..',  # Only its left tile is a trap.
        '..^'  # Only its right tile is a trap.
    ]
    return left_center_right in traps


def generate_rows(firs_row, num_rows):
    rows = [firs_row]

    previous_row = firs_row
    while len(rows) < num_rows:
        new_row = ''

        safe_row = '.' + previous_row + '.'
        for i in xrange(1, len(safe_row) - 1):
            new_row += '^' if is_trap(safe_row[i - 1:i + 2]) else '.'

        rows.append(new_row)
        previous_row = new_row

    for row in rows:
        print row

    print 'Num safe: ', ''.join(rows).count('.')


generate_rows(normal_input, 400000)
