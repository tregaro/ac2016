from day7_input import puzzle_input


def check_for_abba(text):
    for i in xrange(0, len(text) - 3):
        left = text[i:i + 2]
        right = text[i + 3:i + 1:-1]

        if left[0] != left[1] and left == right:
            return True

    return False


def parse_line(line):
    is_square = False
    normal = []
    square = []
    while len(line) > 0:
        delimiter = '[' if not is_square else ']'
        splits = line.split(delimiter, 1)
        if is_square:
            square.append(splits[0])
        else:
            normal.append(splits[0])
        line = splits[1] if len(splits) == 2 else ''
        is_square = not is_square

    return normal, square


def normal():
    lines = puzzle_input.splitlines()
    num_abba = 0
    for line in lines:
        n, s = parse_line(line)
        s_abba = False
        n_abba = False

        for l in s:
            s_abba = check_for_abba(l)
            if s_abba:
                break

        if s_abba:
            continue

        for l in n:
            n_abba = check_for_abba(l)
            if n_abba:
                break

        if n_abba:
            num_abba += 1

    print 'Normal: ', num_abba


def get_aba(text):
    abas = []
    for i in xrange(0, len(text) - 2):
        if text[i] != text[i + 1] and text[i + 2] == text[i]:
            abas.append(text[i:i + 3])

    return abas


def alt():
    lines = puzzle_input.splitlines()
    num_ssl = 0
    for line in lines:
        n, s = parse_line(line)

        abas = []
        babs = []
        for l in n:
            abas.extend(get_aba(l))

        for l in s:
            babs.extend(get_aba(l))

        # reverse babs so we can compare with abas
        babs = [v[1] + v[0] + v[1] for v in babs]

        for aba in abas:
            if aba in babs:
                assert any(aba in x for x in n)
                assert any((aba[1] + aba[0] + aba[1]) in x for x in s)
                num_ssl += 1
                break

    print 'Alt: ', num_ssl


normal()
alt()
