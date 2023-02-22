## 3.3

We'll prove that the set of operations $\{\text{NOT}, \text{OR}\}$ are universal
by showing that a $\text{NAND}$ gate can be built from them.

We have:

$$
\begin{aligned}
\text{NAND}(a, b) &= \text{NOT}(\text{AND}(a, b)) &&\text{(definition of NAND)} \\
                  &= \text{OR}(\text{NOT}(a), \text{NOT}(b)) &&\text{(De Morgan's Law)} \\
\end{aligned}
$$

Therefore, we can build a $\text{NAND}$ gate by doing $\text{OR}(\text{NOT}(a),
\text{NOT}(b))$ using only $\{\text{NOT}, \text{OR}\}$.

## 3.6

Let $\text{MAJ}_1 : \{0, 1\}^3 \to \{0, 1\}$ be $\text{MAJ}(a, b, c, 1)$. Since
$\text{MAJ}$ is 1 when at least three out of the four inputs are 1 and one of
our inputs is always 1, our $\text{MAJ}_1$ function will be 1 when at least one
of the inputs is 1.

We obtain the following truth table for our $\text{MAJ}_1$ as well as
$\text{OR}(a, b, c)$:

| a | b | c | $\text{MAJ}_1(a, b, c)$ | $\text{OR}(a, b, c)$ |
|---|---|---|-------------------------|----------------------|
| 0 | 0 | 0 | 0                       | 0                    |
| 0 | 0 | 1 | 1                       | 1                    |
| 0 | 1 | 0 | 1                       | 1                    |
| 0 | 1 | 1 | 1                       | 1                    |
| 1 | 0 | 0 | 1                       | 1                    |
| 1 | 0 | 1 | 1                       |	1                    |
| 1 | 1 | 0 | 1                       | 1                    |
| 1 | 1 | 1 | 1                       | 1                    |

From this table, we can see that $\text{MAJ}_1(a, b, c)$ is equivalent to
$\text{OR}(a, b, c)$.

Since the set $\{\text{NOT}, \text{OR}\}$ is universal (as we've shown in 3.3),
we can say that $\{\text{NOT}, \text{MAJ}_1\}$ is also universal.

Since $\text{MAJ}_1$ is $\{\text{MAJ}, 1\}$, we can also say that the set
$\{\text{NOT}, \text{MAJ}, 1\}$ is universal.

## 3.8

From 3.3, we know that $\{\text{NOT}, \text{OR}\}$ is universal. We can use this
to build a $\text{NOR}$ gate.

$$
\begin{aligned}
\text{NOR}(a, b) &= \text{NOT}(\text{OR}(a, b)) &&\text{(definition of NOR)} \\
\end{aligned}
$$

Since we can build a $\text{NOR}$ gate using $\{\text{NOT}, \text{OR}\}$, we can
say that $\text{NOR}$ is universal.

## 3.9

The function $\text{LOOKUP}_1$ is defined as:

- $a$ if $c = 0$, and
- $b$ if $c = 1$.

We can reason that if $NOT(c) = 1$ then $a$, otherwise if $c = 1$ then $b$.
We'll write this as:

- $AND(a, NOT(c))$, and
- $AND(b, c)$.

We can then write the function as:

$$
\text{LOOKUP}_1(a, b, c) = \text{OR}(\text{AND}(a, \text{NOT}(c)), \text{AND}(b, c))
$$

To confirm this, we construct the following truth table:

| a | b | c | $\text{LOOKUP}_1(a, b, c)$  | $\text{OR}(\text{AND}(a, \text{NOT}(c)), \text{AND}(b, c))$ |
|---|---|---|-----------------------------|-------------------------------------------------------------|
| 0 | 0 | 0 | 0                           | 0                                                           |
| 0 | 0 | 1 | 0                           | 0                                                           |
| 0 | 1 | 0 | 0                           | 0                                                           |
| 0 | 1 | 1 | 1                           | 1                                                           |
| 1 | 0 | 0 | 1                           | 1                                                           |
| 1 | 0 | 1 | 0                           | 0                                                           |
| 1 | 1 | 0 | 1                           | 1                                                           |
| 1 | 1 | 1 | 1                           | 1                                                           |

To further prove that $\{\text{LOOKUP}_1, 1, 0\}$ is universal, we can show that
we can build a $\text{NAND}$ gate using $\{\text{LOOKUP}_1, 1, 0\}$.


$$
\begin{aligned}
\text{LOOKUP}_1(a, b, c) &= \text{OR}(\text{AND}(a, \text{NOT}(c)), \text{AND}(b, c)) \\
                         &= \text{OR}(\text{NOT}(\text{OR}(\text{NOT}(a), c)), \text{AND}(b, c)) &&\text{(De Morgan's Law)} \\
						 &= \text{OR}(\text{NOT}(\text{OR}(\text{NOT}(a), c)), \text{NOT}(\text{OR}(\text{NOT}(b), \text{NOT}(c)))) &&\text{(De Morgan's Law)} \\
\end{aligned}
$$

Since we know that we can construct the $\text{NOT}(a)$ gate by doing
$\text{NOR}(a, a)$ as well as the $\text{OR}(a, b)$ gate by doing
$\text{NOT}(\text{NOR}(a, b))$, we can say that $\{\text{NOT}, \text{OR},
\text{NOR}\}$ is universal.

Since we can implement $\text{LOOKUP}_1$ using $\{\text{NOT}, \text{OR},
\text{NOR}\}$, we can say that $\{\text{LOOKUP}_1, 1, 0\}$ is universal.
