import collections

letters = collections.Counter('aaaaa-bbb-z-y-x-123')

sorted_letter = letters.most_common()
# sorted_letter.sort(key=itemgetter(1), reverse=True)
# sorted_letter.sort(key=itemgetter(0), reverse=False)

print sorted_letter
