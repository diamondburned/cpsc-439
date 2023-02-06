package main

import (
	"fmt"
	"math"
	"strings"
)

func main() {
	test := func(n int, E [][2]int) {
		max := maxLengthAllowed(n)

		fmt.Printf("Graph G_%d with E = %v\n", n, E)

		e_0 := encodeGraphToE_0(n, E)
		fmt.Printf("  E_0: %s\n", e_0)
		if e_0.Length() <= max {
			fmt.Printf("    => PASS (max %d)\n", max)
		} else {
			fmt.Printf("    => FAIL (max %d)\n", max)
		}

		e := encodeGraphToE(n, E)
		fmt.Printf("  E:   %s\n", e)
		if e.Length() <= max {
			fmt.Printf("    => PASS (max %d)\n", max)
		} else {
			fmt.Printf("    => FAIL (max %d)\n", max)
		}

		fmt.Println()
	}

	test(1, [][2]int{})
	test(2, [][2]int{{0, 1}})
	test(3, [][2]int{{0, 1}, {1, 0}, {1, 2}})

	// generate list of edges for n = 10
	var n10Edges [][2]int
	for i := 0; i < 10; i++ {
		for j := 0; j < 10; j++ {
			if i != j {
				n10Edges = append(n10Edges, [2]int{i, j})
			}
		}
	}
	test(10, n10Edges)
}

func maxLengthAllowed(n int) int {
	nf := float64(n)
	return int(math.Floor(1000 * nf * math.Log2(nf)))
}

type BitString []uint8

func (s BitString) String() string {
	var out strings.Builder
	for _, b := range s {
		fmt.Fprintf(&out, "%d", b)
	}
	return out.String()
}

// E is the encoding scheme E.
type E []EWord

type EWord string

const (
	EWord0 EWord = "00"
	EWord1 EWord = "11"
	EWord2 EWord = "01" // | in E_0
	EWord3 EWord = "10" // , in E_0
)

func (e E) String() string {
	var out strings.Builder
	for _, w := range e {
		out.WriteString(string(w))
		out.WriteByte(' ')
	}
	return out.String()
}

func (e E) Length() int {
	return len(e) * 2
}

func encodeGraphToE(n int, edges [][2]int) E {
	e_0 := encodeGraphToE_0(n, edges)
	out := make(E, 0, len(e_0))
	for _, b := range e_0 {
		switch b {
		case E_0Word0:
			out = append(out, EWord0)
		case E_0Word1:
			out = append(out, EWord1)
		case E_0Word2:
			out = append(out, EWord2)
		case E_0Word3:
			out = append(out, EWord3)
		}
	}
	return out
}

// E_0 is the encoding scheme E_0.
type E_0 []E_0Word

type E_0Word byte

const (
	E_0Word0 E_0Word = '0'
	E_0Word1 E_0Word = '1'
	E_0Word2 E_0Word = '|'
	E_0Word3 E_0Word = ','
)

func (e0 E_0) Length() int {
	return len(e0)
}

// encodeGraphToE_0 encodes the given graph G_n where n is the number of
// vertices using the encoding scheme E_0. E is the list of edges.
func encodeGraphToE_0(n int, edges [][2]int) E_0 {
	var out E_0
	for i := 0; i < n; i++ {
		// Collect all edges that start at vertex i.
		outneighbors := make([]int, 0, len(edges))
		for _, e := range edges {
			if e[0] == i {
				outneighbors = append(outneighbors, e[1])
			}
		}

		for j, e := range outneighbors {
			out = append(out, encodeVertexToE_0(e)...)
			if j < len(outneighbors)-1 {
				out = append(out, E_0Word3)
			}
		}

		if i < n-1 {
			out = append(out, E_0Word2)
		}
	}

	return out
}

// encodeVertexToE_0 encodes a vertex i as a bit vector of length ceil(log2(n)).
// It implements encoding scheme E_0.
func encodeVertexToE_0(i int) E_0 {
	if i == 0 {
		return E_0{E_0Word0}
	}

	out := make(E_0, 0, int(math.Ceil(math.Log2(float64(i)))))
	// See Remark 2.1 (Binary representation in Python) in the book.
	for i := i; i > 0; i /= 2 {
		if i%2 == 0 {
			out = append(out, E_0Word0)
		} else {
			out = append(out, E_0Word1)
		}
	}

	return out
}
