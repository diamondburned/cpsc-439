class NAND:
    def __init__(self, lhs=None, rhs=None):
        self.lhs = lhs
        self.rhs = rhs

    def evaluate(self):
        a = self.lhs
        b = self.rhs
        if type(a) is NAND:
            a = a.evaluate()
        if type(b) is NAND:
            b = b.evaluate()

        return not (a and b)


def solve(program, inputs, num_outputs):
    results = [*inputs]
    for _, lhs, rhs in program[2]:
        results.append(NAND(results[lhs], results[rhs]))

    output = "".join([str(x.evaluate()) for x in results[-num_outputs:]])
    return output


if __name__ == "__main__":
    from itertools import product

    program = eval(input().rstrip())
    num_outputs = program[1]

    v = (0, 1)
    for a, b, c in product(v, v, v):
        result = solve(program, (a, b, c), num_outputs)
        print(f"{a=}, {b=}, {c=} | --> {result}")
