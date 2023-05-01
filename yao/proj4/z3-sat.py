from z3 import *
import sys

input = [
    l.split(" ") for l in list(filter("".__ne__, sys.stdin.read().strip().split("\n")))
]
I = sorted(list(set(["".join([x for x in l if x[0] == "I"]) for l in input])))[1:]
s = Solver()

for i in input:
    s.add(Or([Not(Bool(x[1:])) if x[0] == "~" else Bool(x) for x in i]))

while s.check() == sat:
    print("".join(["1" if s.model()[Bool(x)] else "0" for x in I]))
    s.add(
        Or(
            [
                Bool(x) != s.model()[Bool(x)]
                if s.model()[Bool(x)] != None
                else Bool(x) != False
                for x in I
            ]
        )
    )
