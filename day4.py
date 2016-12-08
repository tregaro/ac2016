from collections import Counter
from operator import itemgetter

from day4_input import puzzle_input

alphabet = "abcdefghijklmnopqrstuvwxyz"

puzzle_input = puzzle_input.splitlines()
num_real = 0
sector_sum = 0
for line in puzzle_input:
    room, check_sum = line.split('[')
    check_sum = check_sum[:-1]
    sector_index = room.rfind('-')
    sector = int(room[sector_index + 1:])
    dashed_room = room[:sector_index]
    room = dashed_room.replace('-', '')
    letters = Counter(room)

    sorted_letter = letters.most_common()
    sorted_letter.sort(key=itemgetter(0))
    sorted_letter.sort(key=itemgetter(1), reverse=True)

    is_real_room = True
    for index, letter in enumerate(check_sum):
        if letter != sorted_letter[index][0]:
            # this is a wrong room
            is_real_room = False

    if is_real_room:
        num_real += 1
        sector_sum += sector

        real_name = []
        for c in dashed_room:
            if c == '-':
                real_name.append(' ')
            else:
                real_name.append(alphabet[(alphabet.index(c) + sector) % len(alphabet)])
        real_name = ''.join(real_name)
        if 'north' in real_name:
            print "Name: ", real_name, " id: ", sector

print "num real: ", num_real
print "sector sum: ", sector_sum
