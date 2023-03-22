package main

import "testing"

type Result[T any] struct {
	Value   T
	Matched bool
}

func Ok[T any](v T) Result[T] { return Result[T]{v, true} }

func None[T any]() Result[T] {
	var z T
	return Result[T]{z, false}
}

func ResultIf[T any](cond bool, then_ T) Result[T] {
	if cond {
		return Ok(then_)
	}
	return None[T]()
}

// MatcherDFA is a DFA matcher.
type MatcherDFA[EnumT comparable] struct {
	δ map[EnumT]StateFunc[byte, EnumT]
	F Set[EnumT] // final states
	q EnumT      // start state
}

// Match returns true if the DFA matches the input.
func (m MatcherDFA[EnumT]) Match(v string) bool {
	current := Result[EnumT]{m.q, true}
	for current.Matched && len(v) > 0 {
		current = m.δ[current.Value](v[0])
		v = v[1:]
	}

	return current.Matched && m.F.Has(current.Value)
}

// StateFunc is a state function.
type StateFunc[StateT, EnumT any] func(StateT) Result[EnumT]

// Set is a set of values.
type Set[T comparable] map[T]struct{}

// NewSet returns a new set.
func NewSet[T comparable](values ...T) Set[T] {
	set := make(Set[T], len(values))
	for _, v := range values {
		set[v] = struct{}{}
	}
	return set
}

// Add adds a value to the set.
func (s Set[T]) Add(v T) {
	s[v] = struct{}{}
}

// Has returns true if the set contains the value.
func (s Set[T]) Has(v T) bool {
	_, ok := s[v]
	return ok
}

// Remove removes a value from the set.
func (s Set[T]) Remove(v T) {
	delete(s, v)
}

func Assert(t *testing.T, cond bool, msgf string, msgv ...any) {
	if !cond {
		t.Errorf(msgf, msgv...)
	}
}

func AssertMatch[EnumT comparable](t *testing.T, dfa MatcherDFA[EnumT], input string, matches bool) {
	msgOk := "expected %q to match"
	msgFail := "expected %q to not match"
	if !matches {
		msgOk, msgFail = msgFail, msgOk
	}

	if dfa.Match(input) == matches {
		if matches {
			t.Logf("%q matches", input)
		} else {
			t.Logf("%q does not match", input)
		}
	} else {
		if matches {
			t.Errorf("expected %q to match", input)
		} else {
			t.Errorf("expected %q to not match", input)
		}
	}
}
