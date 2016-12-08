from day8_input import puzzle_input


def rect(a, b, screen):
    """
    Turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.

    :param a: width
    :param b: height
    :param screen:
    """
    for x in xrange(b):
        for y in xrange(a):
            screen[x][y] = '#'


def rotate_row(a, b, screen):
    """
    Shifts all of the pixels in row A (0 is the top row) right by B pixels.
    Pixels that would fall off the right end appear at the left end of the row.

    :param a:
    :param b:
    :param screen:
    :return:
    """
    screen[a] = screen[a][-b:] + screen[a][:-b]


def rotate_column(a, b, screen):
    """
    Shifts all of the pixels in column A (0 is the left column) down by B pixels.
    Pixels that would fall off the bottom appear at the top of the column.

    :param a:
    :param b:
    :param screen:
    :return:
    """
    column = [screen[x][a] for x in xrange(len(screen))]
    column = column[-b:] + column[:-b]
    for y in xrange(len(screen)):
        screen[y][a] = column[y]


def normal():
    # 50 wide 6 tall. . = off, # = on
    screen = [['.' for _ in xrange(50)] for _ in xrange(6)]

    instructions = {
        'rotate column x=A by B': ''
    }
    operations = puzzle_input.splitlines()

    for op in operations:
        if op.startswith('rect'):
            a, b = op.split()[1].split('x')
            rect(int(a), int(b), screen)
        elif op.startswith('rotate row y='):
            a, b = op[len('rotate row y='):].split('by')
            rotate_row(int(a), int(b), screen)
        elif op.startswith('rotate column x='):
            a, b = op[len('rotate column x='):].split('by')
            rotate_column(int(a), int(b), screen)
        else:
            assert False

    for line in screen:
        print ''.join(line)

    num_pixels_on = 0
    for y in xrange(len(screen)):
        for x in xrange(len(screen[y])):
            if screen[y][x] == '#':
                num_pixels_on += 1

    print 'Num pixels: ', num_pixels_on


normal()
