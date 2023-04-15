# Goal: Unit Test Miranda script: task3.m

import subprocess
import argparse
from random import choice, randint

kCMD = 'echo "main []" | mira task3'
kTRUTH = lambda s: s == s[::-1]  # Source of Truth palindrome function
kALPHABET = "01"

parser = argparse.ArgumentParser(description="Task3 Miranda Unit Tests")

parser.add_argument(
    "-n",
    "--num-fuzzy-tests",
    default=100,
    type=int,
    help="How many fuzzy tests to run.",
)

parser.add_argument(
    "-v", "--verbose", default=False, action="store_true", help="Print each test."
)

parser.add_argument(
    "-s",
    "--stop-on-fail",
    action="store_true",
    default=False,
    help="Stop future tests on first failed test.",
)


def main(
    *, verbose: bool = False, num_fuzzy_tests: int = 100, stop_on_fail: bool = True
):
    # fuzzy tests
    fuzzy_pass: int = 0  # how many tests do we pass
    for fuzzy_test_idx in range(num_fuzzy_tests):
        fuzzy_test_input_size = randint(1, 8)
        fuzzy_test_input = [choice(kALPHABET) for _ in range(fuzzy_test_input_size)]

        subprocess_command = kCMD.replace("[]", str(fuzzy_test_input))

        result = subprocess.run(
            subprocess_command, shell=True, stdout=subprocess.PIPE, text=True
        )

        test_result = result.stdout.strip()

        actual_result = "1" if kTRUTH(fuzzy_test_input) else "0"

        test_passed = test_result == actual_result
        fuzzy_pass += 1 if test_passed else 0

        if stop_on_fail and not test_passed:
            print(
                f"Failed Fuzzy Test {fuzzy_test_idx} [{fuzzy_test_input}] where {test_result=} and {actual_result=}"
            )
            exit(0)

        if verbose:
            print(
                f"Fuzzy Test {fuzzy_test_idx} = {fuzzy_test_input}",
                test_passed,
            )

    print(f"Passed {fuzzy_pass}/{num_fuzzy_tests}")


if __name__ == "__main__":
    args = parser.parse_args()
    main(**args.__dict__)
