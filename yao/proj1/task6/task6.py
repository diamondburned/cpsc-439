from tkinter import EXCEPTION


kBLANK = " "
kA = "A"
kB = "B"

state_map = dict[str, dict[str, list[str]]]  # for type anno


class TuringMachine:
    def __init__(self):
        self.tm = {
            "START": {
                kA: ["SAW_A", "R", kBLANK],
                kB: ["SAW_B", "R", kBLANK],
                kBLANK: ["START", "H", kBLANK],
            },
            "SAW_A": {
                kA: ["SAW_A", "R", kA],
                kB: ["SAW_A", "R", kB],
                kBLANK: ["SAW_A_PRIME", "L", kBLANK],
            },
            "SAW_A_PRIME": {
                kA: ["MOVING_LEFT", "L", kBLANK],
                kB: ["SAW_A_PRIME", "H", kB],  # kB is reject
                kBLANK: ["SAW_A_PRIME", "H", kA],  # kA is accept
            },
            "SAW_B": {
                kA: ["SAW_B", "R", kA],
                kB: ["SAW_B", "R", kB],
                kBLANK: ["SAW_B_PRIME", "L", kBLANK],
            },
            "SAW_B_PRIME": {
                kA: ["SAW_B_PRIME", "H", kB],  # kB is reject
                kB: ["MOVING_LEFT", "L", kBLANK],
                kBLANK: ["SAW_B_PRIME", "H", kA],  # kA is accept
            },
            "MOVING_LEFT": {
                kA: ["MOVING_LEFT", "L", kA],
                kB: ["MOVING_LEFT", "L", kB],
                kBLANK: ["START", "R", kBLANK],
            },
        }

    def solve(self, inp: str):
        pass
        tape = [" "] + [x.upper() for x in inp] + [" "]
        i = 1
        state, move, sym = self.tm["START"][tape[i]]

        while move != "H":
            # print(state, move, sym if sym in (kA, kB) else "' '", tape[i])
            # replace symbol
            tape[i] = sym
            # move cursor
            if move == "L":
                i -= 1
            elif move == "R":
                i += 1

            # get new state
            state, move, sym = self.tm[state][tape[i]]

        res = "".join(tape).replace(" ", "")
        return (
            len(res) == 0
        )  # tape is empty (full of blanks) if accepted, else rejected


if __name__ == "__main__":
    import sys

    args = sys.argv
    kKNOWN = "i"
    for arg in args[1:]:
        if "-" in arg and arg[1:] not in kKNOWN:
            raise (Exception(f"Unknown arg: {arg}"))
    try:
        input_idx = args.index("-i")
    except:
        raise (Exception('Please provide input. i.e: $python3 task6.py -i "aba"'))
    to_check = args[input_idx + 1]
    tm = TuringMachine()
    result = tm.solve(to_check)
    print("ACCEPTED" if result else "REJECTED")
