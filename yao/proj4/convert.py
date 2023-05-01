# convert dfa to 3sat
from itertools import combinations
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

# xor state in each step
xor = ""
for i in range(length + 1):
    for s in dfa.keys():
        xor += "Q{}-{} ".format(s, i)
    xor = xor.strip() + "\n"

    for x in combinations(dfa.keys(), 2):
        xor += "~Q{}-{} ~Q{}-{}\n".format(x[0], i, x[1], i)

print(xor)

# add transition
transition = ""
for s, t in dfa.items():
    for s_, t_ in t.items():
        for i in range(length):
            transition += "~Q{}-{} {}I{} Q{}-{}\n".format(
                s,
                i,
                "" if s_ == "0" else "~",
                i,
                t_,
                i + 1,
            )

print(transition)

# starting and accepting states
print("Q{}-0".format(starting_state))
print("Q{}-{}".format(accepting_state, length))
