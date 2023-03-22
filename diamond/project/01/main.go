package main

import (
	"flag"
	"os"
	"testing"
)

var tests []testing.InternalTest

func AddTest(name string, f func(*testing.T)) {
	tests = append(tests, testing.InternalTest{
		Name: name,
		F:    f,
	})
}

func main() {
	testing.Init()
	flag.CommandLine.Parse(append(os.Args[1:], "-test.v"))
	testing.Main(func(a, b string) (bool, error) { return a == b, nil }, tests, nil, nil)
}
