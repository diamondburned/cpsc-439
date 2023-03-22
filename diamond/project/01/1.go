package main

import "testing"

type DFA_2_13_1_State byte

const (
	DFA_2_13_1_A DFA_2_13_1_State = iota
	DFA_2_13_1_B
	DFA_2_13_1_C
	DFA_2_13_1_D
)

var DFA_2_13_1 = MatcherDFA[DFA_2_13_1_State]{
	δ: map[DFA_2_13_1_State]StateFunc[byte, DFA_2_13_1_State]{
		DFA_2_13_1_A: func(v byte) Result[DFA_2_13_1_State] {
			switch v {
			case '0':
				return Ok(DFA_2_13_1_A)
			case '1':
				return Ok(DFA_2_13_1_B)
			default:
				return None[DFA_2_13_1_State]()
			}
		},
		DFA_2_13_1_B: func(v byte) Result[DFA_2_13_1_State] {
			switch v {
			case '0':
				return Ok(DFA_2_13_1_B)
			case '1':
				return Ok(DFA_2_13_1_C)
			default:
				return None[DFA_2_13_1_State]()
			}
		},
		DFA_2_13_1_C: func(v byte) Result[DFA_2_13_1_State] {
			switch v {
			case '0':
				return Ok(DFA_2_13_1_C)
			case '1':
				return Ok(DFA_2_13_1_D)
			default:
				return None[DFA_2_13_1_State]()
			}
		},
		DFA_2_13_1_D: func(v byte) Result[DFA_2_13_1_State] {
			switch v {
			case '0', '1':
				return Ok(DFA_2_13_1_D)
			default:
				return None[DFA_2_13_1_State]()
			}
		},
	},
	q: DFA_2_13_1_A,
	F: NewSet(DFA_2_13_1_D),
}

func TestDFA_2_13_1(t *testing.T) {
	AssertMatch(t, DFA_2_13_1, "110", false)
	AssertMatch(t, DFA_2_13_1, "0", false)
	AssertMatch(t, DFA_2_13_1, "1", false)
	AssertMatch(t, DFA_2_13_1, "11", false)
	AssertMatch(t, DFA_2_13_1, "1111", true)
	AssertMatch(t, DFA_2_13_1, "111", true)
	AssertMatch(t, DFA_2_13_1, "01110", true)
	AssertMatch(t, DFA_2_13_1, "01101", true)
	AssertMatch(t, DFA_2_13_1, "01100", false)
}

func init() {
	AddTest("DFA_2_13_1", TestDFA_2_13_1)
}
