tm = {
    "START": {">": ["GORIGHT", "R", ""]},
    "GORIGHT": {
        ".": ["OUTPUT0", "L", ""],
        "0": ["FOUND0_1", "R", "."],
        "1": ["FOUND1_1", "R", "."],
    },
    "FOUND0_1": {
        ".": ["OUTPUT0", "L", ""],
        "0": ["FOUND0_1", "R", "."],
        "1": ["FOUND1_1", "R", "."],
    },
    "FOUND1_1": {
        ".": ["OUTPUT0", "L", ""],
        "0": ["FOUND1_1", "R", "."],
        "1": ["FOUND2_1", "R", "."],
    },
    "FOUND2_1": {
        ".": ["OUTPUT0", "L", ""],
        "0": ["FOUND2_1", "R", "."],
        "1": ["FOUND3_1", "R", "."],
    },
    "FOUND3_1": {
        ".": ["OUTPUT1", "L", ""],
        "0": ["FOUND3_1", "R", "."],
        "1": ["FOUND3_1", "R", "."],
    },
    "OUTPUT0": {".": ["OUTPUT0", "L", ""], ">": ["WRITE0", "R", ""]},
    "OUTPUT1": {".": ["OUTPUT1", "L", ""], ">": ["WRITE1", "R", ""]},
    "WRITE0": {".": ["WRITE0", "H", "0"]},
    "WRITE1": {".": ["WRITE1", "H", "1"]},
}

starting_state = "START"


def M(x):
    tape = ">" + x + "."
    i = 0
    state = starting_state

    while True:
        # print(tape)
        state, move, sym = tm[state][tape[i]]

        if sym:
            tape = tape[:i] + sym + tape[i + 1 :]

        match move:
            case "L":
                i -= 1
            case "R":
                i += 1
            case "S":
                i += 0
            case "H":
                break

    return tape[1 : tape.index(".")]


result = M("1000101")

if result == "1":
    print("Accepted")
else:
    print("Rejected")
