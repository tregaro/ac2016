from day9_input import puzzle_input


def normal(puzzle_text):
    output = []

    index = 0
    while index < len(puzzle_text):
        if puzzle_text[index] == '(':
            right_index = puzzle_text.find(')', index)
            num_chars, num_repeat = puzzle_text[index + 1:right_index].split('x')
            num_chars = int(num_chars)
            num_repeat = int(num_repeat)
            output.extend(puzzle_text[right_index + 1:right_index + 1 + num_chars] * num_repeat)
            index = right_index + 1 + num_chars
        else:
            output.append(puzzle_text[index])
            index += 1

    return output


# ADVENT == ADVENT - Length of 6.
output = normal('ADVENT')
assert ''.join(output) == 'ADVENT'

# A(1x5)BC == ABBBBBC - Length of 7.
output = normal('A(1x5)BC')
assert ''.join(output) == 'ABBBBBC'

# (3x3)XYZ == XYZXYZXYZ - Length of 9.
output = normal('(3x3)XYZ')
assert ''.join(output) == 'XYZXYZXYZ'

# A(2x2)BCD(2x2)EFG == ABCBCDEFEFG - Length of 11.
output = normal('A(2x2)BCD(2x2)EFG')
assert ''.join(output) == 'ABCBCDEFEFG'

# (6x1)(1x3)A simply becomes (1x3)A - Length of 6.
output = normal('(6x1)(1x3)A')
assert ''.join(output) == '(1x3)A'

# X(8x2)(3x3)ABCY
output = normal('X(8x2)(3x3)ABCY')
assert ''.join(output) == 'X(3x3)ABC(3x3)ABCY'

output = normal(puzzle_input)
print "Normal: ", len(output)


def alt(puzzle_text, multiplier=1):
    length = 0

    if '(' not in puzzle_text:
        return len(puzzle_text) * multiplier

    index = 0
    while index < len(puzzle_text):
        if puzzle_text[index] == '(':
            right_index = puzzle_text.find(')', index)
            num_chars, num_repeat = puzzle_text[index + 1:right_index].split('x')
            num_chars, num_repeat = int(num_chars), int(num_repeat)
            current_text = ''.join(puzzle_text[right_index + 1:right_index + 1 + num_chars])
            length += alt(current_text, num_repeat * multiplier)
            index = right_index + 1 + num_chars
        else:
            length += multiplier
            index += 1

    return length


# print "Alt: ", alt('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN')
print "Alt: ", alt(puzzle_input)
