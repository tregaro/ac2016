from day12_input import puzzle_input

test_case = '''cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a'''


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


def normal(instructions):
    registers = {
        'a': 0,
        'b': 0,
        'c': 1,
        'd': 0
    }

    instructions = instructions.splitlines()
    index = 0
    while index < len(instructions):
        index_inc = 1
        instruction = instructions[index]
        if 'cpy' in instruction:
            value, target = instruction[3:].split()
            if check_int(value):
                registers[target] = int(value)
            else:
                registers[target] = registers[value]
        elif 'inc' in instruction:
            target = instruction[4:]
            registers[target] += 1
        elif 'dec' in instruction:
            target = instruction[4:]
            registers[target] -= 1
        elif 'jnz' in instruction:
            value, offset = instruction[3:].split()
            if (check_int(value) and int(value) != 0) or registers[value] != 0:
                index_inc = int(offset)

        index += index_inc

    print registers


normal(puzzle_input)
