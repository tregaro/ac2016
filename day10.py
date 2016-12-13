from day10_input import puzzle_input


class Bot(object):
    def __init__(self, bot_id, chip_num=None, low=None, high=None):
        self.bot_id = bot_id
        self.chip_nums = [chip_num] if chip_num is not None else []
        self.low = low
        self.high = high

    @property
    def is_ready(self):
        return len(self.chip_nums) == 2


def normal(instructions, a, b):
    """

    :type instructions: list of str
    :param instructions:
    :return:
    """

    bots = {}

    for instruction in instructions:
        if instruction.startswith('value'):
            value, bot_id = instruction[len('value'):].split('goes to bot')
            value, bot_id = int(value), int(bot_id)
            if bot_id in bots:
                bots[bot_id].chip_nums.append(value)
            else:
                bots[bot_id] = Bot(bot_id, value)
        elif instruction.startswith('bot'):
            bot_id, low, high = (
                int(instruction[len('bot'):instruction.find('gives')]),
                (instruction[instruction.find('to') + len('to '):instruction.find('and')]).split(),
                (instruction[instruction.rfind('to') + len('to '):]).split()
            )
            if bot_id in bots:
                bots[bot_id].low = low
                bots[bot_id].high = high
            else:
                bots[bot_id] = Bot(bot_id, low=low, high=high)

    have_any_ready_bots = True
    outputs = {}
    result = None
    while have_any_ready_bots:
        have_any_ready_bots = False
        for bot_id in bots:
            if bots[bot_id].is_ready:
                have_any_ready_bots = True
                bot = bots[bot_id]
                bot.chip_nums.sort()

                if result is None and a in bot.chip_nums and b in bot.chip_nums:
                    result = bot_id

                high_index = int(bot.high[1])
                low_index = int(bot.low[1])

                if bot.high[0] == 'bot':
                    bots[high_index].chip_nums.append(bot.chip_nums.pop())
                elif bot.high[0] == 'output':
                    if high_index in outputs:
                        outputs[high_index].append(bot.chip_nums.pop())
                    else:
                        outputs[high_index] = [bot.chip_nums.pop()]
                else:
                    assert False

                if bot.low[0] == 'bot':
                    bots[low_index].chip_nums.append(bot.chip_nums.pop())
                elif bot.low[0] == 'output':
                    if low_index in outputs:
                        outputs[low_index].append(bot.chip_nums.pop())
                    else:
                        outputs[low_index] = [bot.chip_nums.pop()]
                else:
                    assert False

    print "Alt: ", outputs[0][0] * outputs[1][0] * outputs[2][0]
    return result


test_instructions = '''value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2'''

print "Bot it is: ", normal(puzzle_input.splitlines(), 61, 17)
