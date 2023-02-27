#!/usr/bin/env python3
def NAND(a, b):
    return not (a and b)


def MAJ(a, b, c):
    ab = NAND(a, b)
    bc = NAND(b, c)
    ac = NAND(a, c)
    abbc = NAND(ab, bc)
    abbcac = NAND(abbc, ac)
    return NAND(abbcac, ac)


# Stolen from Justin's.
from itertools import product

v = (0, 1)
for (a, b, c) in product(v, v, v):
    print(f"{a} {b} {c} --> {MAJ(a, b, c)}")
