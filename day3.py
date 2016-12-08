from day3_input import puzzle_input


lines = puzzle_input.splitlines()


def normal():
    num_possible = 0
    for line in lines:
        numbers = filter(None, line.split('  '))
        int_numbers = []
        for number in numbers:
            int_numbers.append(int(number))
        int_numbers.sort()
        if int_numbers[0] + int_numbers[1] > int_numbers[2]:
            num_possible += 1

    print "possible: ", num_possible
    print "total: ", len(lines)


def alt():
    alt_num_possible = 0
    numbers = [filter(None, line.split('  ')) for line in lines]
    import itertools

    merged_numbers = list(itertools.chain(*numbers))
    int_numbers = [int(num) for num in merged_numbers]

    for i in xrange(0, len(int_numbers) / 3):
        index = i + 6 * (i / 3)
        triangle = [int_numbers[index], int_numbers[index + 3], int_numbers[index + 6]]
        triangle.sort()
        if triangle[0] + triangle[1] > triangle[2]:
            alt_num_possible += 1

    print "alt: ", alt_num_possible


normal()
alt()
