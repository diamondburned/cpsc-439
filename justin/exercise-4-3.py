def NAND(a, b):
    return not (a and b)


def MAJOR(a, b, c):
    t = NAND(a, b)
    u = NAND(a, c)
    v = NAND(b, c)
    r = NAND(t, u)  # t or u
    return NAND(NAND(r, r), v)

    # r1 = NAND(NAND(a, b), NAND(a, c))
    # r2 = NAND(NAND(a, b), NAND(b, c))
    # r3 = NAND(NAND(a, c), NAND(b, c))
    # result = NAND(NAND(r1, r1), NAND(r2, r2))
    # return NAND(result, NAND(r3, r3)) # idk
    # return NAND(NAND(result, result), NAND(r3, r3))


def test():
    from itertools import product

    v = (0, 1)
    for a, b, c in product(v, v, v):
        print(f"{a} {b} {c} --> {MAJOR(a, b, c)}")


test()
