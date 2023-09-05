1. Integer factoring

   Integer factoring is in the $\bf{NP}$ class because there is a function $V$
   that verifies that a number is a factorization of $N$ in polynomial time.

   The function $V$ can simply check that the number $n$ is a factorization of
   $N$ by calculating $n(N/n)$ and checking that the result is $N$.

2. $01EQ$

   Since $01EQ$ can be reduced to $3SAT$ in polynomial time, $3SAT \leq_p 01EQ$
   (Theorem 14.2). We also know that $3SAT \in \bf{NP}$ (Example 15.3),
   therefore $01EQ \in \bf{NP}$.

   In other words, we can verify that a string $x$ is in $01EQ$ by reducing it
   to $3SAT$ and then verifying that the resulting string is in $3SAT$.
