# Introduction

Effective Procedure:

- Set of instructions
- Can be followed mechanically
- Always terminates
- Always eventually produces correct output


David Hilbert:

- Entscheidungsproblem
- Is there an algorithm that will eventually produce all the true
  mathematical statements?
	- No.
		- Kurt Goedel: incompleteness theorem
		- Alan Turing: incompletability


### TM vs. $\lambda$-calculus

Turing Machine:

- Mathematical Model of Computing

Alonzo Church

- Lambda calculus: defining and applying functions => LISP
	- Equivalent to Turing Machine
- Church-Turing Thesis: not proven

Since models are equivalent, this effectively defines computation.


### Models of Computation:

- As simple as possible
- Defined mathematically


### Explore Limits/Prove Theorems:

- Uncomputability (cannot be computed)
- Universality (anything that can be computed by one can be computed by another)
	- Universal Turing Machine:
		1. Define a Turing Machine: [...010[0]11...]
		2. Feed it to the Universal Turing Machine
		3. The Universal Turing Machine will simulate our Turing Machine


### How long must algorithms run?

- If it's possible, do they take forever to run?
- Big-O notation
	- O(1), O(log n), O(n), O(n log n), O(n^2), O(2^n), O(n!), ...
	- O(2^n) and O(n!) are "intractable" or unreasonably slow
- P vs. NP
	- P: polynomial time
	- NP: non-deterministic polynomial time
	- No (known) good (polynomial) algorithm for solving, but given a
	  solution someone tells us, we could verify it.
	- Big question:
		- Is it possible to have better algorithms, or has no one found
		  them yet?
		- Is $P = NP$?
