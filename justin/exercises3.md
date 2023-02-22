# Exercises 3.3, 3.6, 3.8, and 3.9

#### Author: Justin

## 3.3

To prove that the set {OR, NOT} is universal we just need to show that it has the same **power** as NAND alone.

Since the NAND gate is provably universal, our proof that the set {OR, NOT} is equivalently powerful will suffice.

For starters, A and B simply equates to NOT(NOT A OR NOT B). This expression only uses 1) NOT and 2) OR.

Therefore, we have shown that we can construct an AND gate with {OR, NOT} alone. Recall that a NAND gate is simply a NOT applied to an AND gate.

We have shown that we can construct equivalent gates to NAND using the set {OR, NOT}.

## 3.6

To prove that {MAJ, NOT, 1} is a universal set of gates we just need to show its equivalence to any boolean circuit.
Consider A, B:

First, apply NOT gate to A
Then apply NOT gate to B
Then use the MAJ gate on A, B, 1
Lastly, apply NOT to the previous circuits output.

I've constructed an AND gate because the last circuit only outputs `1` iff A is 1 and B is 1.

We can use similar logic for an OR gate which shows that our set of {MAJ, NOT, 1} is universal.

## 3.8

To prove that {NOR} is a universal set of gates we just need to show we can construct any boolean circuit using just {NOR}.

* A AND B = NOR(NOR(A, NOR(A, B)), NOR(B, NOR(A, B)))
* A OR B = NOR(NOR(A, A), NOR(B, B))

Since we know that {AND, OR} is a universal set and {NOR} can construct this set equivocally, then we've proven {NOR} is universal.

## 3.9
We can show that {LOOKUP, 0, 1} is a universal set of gates by showing it's power to represent any boolean circuit.

It is enough to show that we can represent NAND using the LOOKUP function since NAND is universal.

NAND(A, B) = LOOKUP(1, 0, LOOKUP(0, B, A))
