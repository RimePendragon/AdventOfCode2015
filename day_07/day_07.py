# solution from https://blog.jverkamp.com/2015/12/07/advent-of-code-day-7/
import operator
import re

filename = "input2.txt"
data = open(filename, "r")

mono_operators = {
    'NOT': lambda x: ~x & 0xFFFF,
}

binary_operators = {
    'AND': operator.and_,
    'OR': operator.or_,
    'LSHIFT': operator.lshift,
    'RSHIFT': operator.rshift,
}

machine = {}

for line in data:
    line = line.strip()

    m = (
            re.match(r'(\w+) -> (\w+)', line)
            or re.match(r'(\w+) (\w+) (\w+) -> (\w+)', line)
            or re.match(r'(\w+) (\w+) -> (\w+)', line)
    ).groups()

    machine[m[-1]] = m[:-1]


def evaluate(register_or_value):
    try:
        return int(register_or_value)
    except:
        return run(register_or_value)


def run(register, state={}):
    if register not in state:
        command = machine[register]

        if len(command) == 1:
            value, = command
            state[register] = evaluate(value)

        elif len(command) == 2:
            monop, input = command
            state[register] = mono_operators[monop](evaluate(input))

        elif len(command) == 3:
            input_1, binop, input_2 = command
            state[register] = binary_operators[binop](evaluate(input_1), evaluate(input_2))

    return state[register]


print(run('a'))
