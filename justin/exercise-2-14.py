def parity(v: int, i: int) -> int:
    neg = v <= 0
    isodd = abs(i) & 1

    if v == 0 and not isodd:
        return 5
    elif v == 0:
        return 6
    if neg and isodd:
        return 4
    elif neg and not isodd:
        return 3
    return isodd + 1


def prefixSum(k: list[int]) -> list[int]:
    _k = [abs(x) for x in k]
    prefix_sum = [sum(_k[: i + 1]) for i in range(len(_k))]
    return prefix_sum


def ktn(k: list[int]) -> int:
    natural = ""
    P = prefixSum(k)
    assert len(P) == len(k), "prefix sum length must be same as k length"

    for (idx, digit) in enumerate(k):
        par = parity(digit, idx)
        if par == 5 or par == 6:
            natural = natural + str(par)
            continue
        natural = natural + f"{par}" * abs(digit)
        # leading = int(
        #     f"{parity(digit, idx)}" * abs(digit if digit != 0 else 1)
        #     + "0" * (P[len(k) - 1] - P[idx])
        # )
    return int(natural)


def ntk(n) -> list[int]:
    s = str(n)
    i, j = 0, 0
    rebuild = []
    while i <= j:
        if j < len(s) and s[i] == s[j]:
            j += 1
            continue
        delta = j - i
        if s[i] in "56":
            rebuild.append(0)
            i = j
            if j >= len(s):
                break
            continue
        rebuild.append(delta * -1 if s[i] in "34" else delta)
        i = j
        if j >= len(s):
            break

    return rebuild


def test(n, /, *, lower_bound=-30, upper_bound=30, do_print=True):
    from random import sample

    bounds = range(lower_bound, upper_bound)
    passed = 0
    for c in range(n):
        r = sample(bounds, n)
        ktn_result = ktn(r)
        ntk_result = ntk(ktn_result)
        good = r == ntk_result
        passed += good
        if do_print:
            print(f"Test {c+1}: {r} == {ntk_result} {'✅' if good else '❌'}")

    print(f"{passed}/{n} : {passed/n*100:.0f}%")


if __name__ == "__main__":
    # result = ktn([0, 0, 0, -2, -2, 0, 0])
    # print(f"{result=}")
    # result = ntk(result)
    # print(f"{result=}")
    # print(ntk(ktn([66, 11, -12, 5, -12, 4])))
    test(20)
