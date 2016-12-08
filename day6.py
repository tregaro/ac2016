from collections import Counter

from day6_input import puzzle_input


def normal():
    output = ''
    pi = puzzle_input.splitlines()

    for index in xrange(0, len(pi[0])):
        row = [v[index] for v in pi]
        c = Counter(row)
        output += c.most_common(1)[0][0]

    print "normal: ", output


def alt():
    output = ''
    pi = puzzle_input.splitlines()

    for index in xrange(0, len(pi[0])):
        row = [v[index] for v in pi]
        c = Counter(row)
        output += c.most_common()[-1][0]

    print "alt: ", output


normal()
alt()
