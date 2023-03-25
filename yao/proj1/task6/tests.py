import sys
from task6 import TuringMachine

tm = TuringMachine()

kKNOWN_TRUE_TESTS = [
    lambda: tm.solve("b") == True,
    lambda: tm.solve("aba") == True,
    lambda: tm.solve("abba") == True,
    lambda: tm.solve("abbba") == True,
    lambda: tm.solve("a") == True,
    lambda: tm.solve("aaaaaaaaaaaaaa") == True,
    lambda: tm.solve("abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbba") == True,
]

kKNOWN_FALSE_TESTS = [
    lambda: tm.solve("ba") == False,
    lambda: tm.solve("bba") == False,
    lambda: tm.solve("abab") == False,
    lambda: tm.solve("bbaa") == False,
    lambda: tm.solve("bbbbbbbbbbbbbbbba") == False,
    lambda: tm.solve("baaaaaaaaaaaaaaaa") == False,
    lambda: tm.solve("babababababababababaaaaaaaaaaaa") == False,
]


def run_all_tests(*, stop_on_fail=False):
    total = len(kKNOWN_TRUE_TESTS) + len(kKNOWN_FALSE_TESTS)
    passed = 0
    failed = {"known_true": [], "known_false": []}  # list of failures
    for i, test in enumerate(kKNOWN_TRUE_TESTS):
        result = test()
        if stop_on_fail:
            assert (
                result
            ), f"Failed a known True test case: {i}, {test=}. Expected True, Result {result}"
        if result:
            passed += 1
            continue
        failed["known_true"].append((i, test))

    for i, test in enumerate(kKNOWN_FALSE_TESTS):
        # counter-intuitive, but a True result here means pass (i'm bad at writing tests)
        result = test()
        if stop_on_fail:
            assert (
                result
            ), f"Failed a known False test case: {i}, {test=}. Expected False, Result {result}"

        if result:
            passed += 1
            continue
        failed["known_false"].append((i, test))

    return passed / total, failed


if __name__ == "__main__":
    import inspect

    results, failed = run_all_tests(stop_on_fail=False)
    print(f"{results*100:.2f}%")
    if results == 1.0:
        sys.exit(0)

    print("❗FAILED TESTS  ❗")
    for test_type in failed.keys():
        for i, test in failed[test_type]:
            print(f"[{i}] {inspect.getsource(test)}")
