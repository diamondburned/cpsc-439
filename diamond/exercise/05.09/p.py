#!/usr/bin/env python3


def P(t0, t1, t2):
    t3 = NAND(t2, t2)
    t4 = NAND(t1, t1)
    t5 = NAND(t3, t4)
    t6 = NAND(t2, t1)
    t7 = NAND(t6, t6)
    t8 = NAND(t0, t0)
    t9 = NAND(t7, t8)
    t10 = NAND(t5, t0)
    t11 = NAND(t9, t10)
    return t11


def NAND(a, b):
    return not (a and b)


from itertools import product

print("| $t_0$ | $t_1$ | $t_2$ | $P(t_0, t_1, t_2)$ |")
print("|-------|-------|-------|--------------------|")
for (a, b, c) in product((0, 1), (0, 1), (0, 1)):
    print(f"| ${a}$ | ${b}$ | ${c}$ | {1 if P(a, b, c) else 0} |")
