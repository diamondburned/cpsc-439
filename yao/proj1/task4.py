starting_state = "START"


def at_least_3_ones(state, sym, move=""):
    if sym == ">" and state == "START":
        state, move = "LEFTMOST", "R"
    elif state == "LEFTMOST":
        if sym == ".":
            state, move = "OUTPUT0", "H"
        else:
            state = "FOUND0" if sym == "0" else "FOUND1"
            move = "R"
    elif sym == "1" and state == "FOUND0":
        state, move = "FOUND1", "R"
    elif sym == "1" and state == "FOUND1":
        state, move = "FOUND2", "R"
    elif sym == "1" and state == "FOUND2":
        state, move = "FOUND3", "R"
    elif state == "FOUND3":
        if sym == ".":
            state, move = "OUTPUT1", "H"
    elif sym == "." and state in ["FOUND0", "FOUND1", "FOUND2"]:
        state, move = "OUTPUT0", "H"
    else:
        state, move = state, "R"

    return state, move


def TM(x):
    tape = ">" + x + "."
    i = 0
    state = starting_state

    while True:
        state, move = at_least_3_ones(state, tape[i])

        if move == "R":
            i += 1
        elif move == "L":
            i -= 1
        else:
            break

    if state == "OUTPUT0":
        return "0"
    elif state == "OUTPUT1":
        return "1"


result = TM("10001")

if result == "1":
    print("Accepted")
else:
    print("Rejected")
