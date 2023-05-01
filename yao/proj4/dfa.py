# run dfa and get language
from itertools import permutations
from sys import argv


length = int(argv[-1])

with open(argv[-2]) as f:
    input = f.read().split()

accepting_state = input[1]
starting_state = input[0]
dfa = {}
input = input[2:]

for i in range(0, len(input), 3):
    dfa[input[i]] = {"0": input[i + 1], "1": input[i + 2]}


def F(x, dfa, starting_state):
    current_state = starting_state
    for t in x:
        current_state = dfa[current_state][t]
    return current_state


for x in range(2**length):
    input = "{0:b}".format(x).zfill(length)
    result = F(input, dfa, starting_state)

    if result == accepting_state:
        print(input)
