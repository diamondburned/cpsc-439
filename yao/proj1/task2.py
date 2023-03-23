dfa = {
    "1": {"0": "1", "1": "2"},
    "2": {"0": "2", "1": "3"},
    "3": {"0": "3", "1": "4"},
    "4": {"0": "4", "1": "4"},
}

starting_state = "1"
accepting_state = "4"


def F(x):
    current_state = starting_state
    for t in x:
        current_state = dfa[current_state][t]
    return current_state


result = F("1000001")


if result == accepting_state:
    print("Accepted")
else:
    print("Rejected")
