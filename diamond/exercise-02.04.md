# Exercise 2.4

## Encoding

We will define an example encoding scheme $E_0$ where we will encode our set
$G_n$ as an adjacency list.
 
Our encoding will encode each vertex as bits. In other words, for each vertex
$i$ in $G_n$, $i$ will be represented within $\{ 0, 1 \}^*$.

Our encoding scheme will use the alphabet $\Sigma_{E_0} = \{ \texttt0, \texttt1,
\texttt|, \texttt, \}$.

We start with a list $L$, where $|L| = n$. Each $i$-th item in this list will be
another list $L_i$, where each $i$ corresponds to the vertex $i$. If list $L$
contains more than one item, then we will add a "$\texttt|$" between each item.

Each $j$-th item in list $L_i$ will be an out-neighbor of vertex $i$. If list
$L_i$ contains more than one item, then we will add a "$\texttt,$" between each
item.

For example, the following graphs will be encoded like so:

- $G_1 = (\{0\}, \{\}) \to \texttt{}$
- $G_2 = (\{0, 1\}, \{(0, 1), (1, 0)\}) \to \texttt{1|0}$
- $G_3 = (\{0, 1, 2\}, \{(0, 1), (0, 2), (2, 0)\}) \to \texttt{1,10||0}$

We now define another encoding scheme $E$ such that $E : E_0 \to \{0, 1\}^*$. We
can do this by defining a new alphabet $\Sigma_E = \{00, 11, 01, 10\}$
that corresponds to $\Sigma_{E_0}$.

With that, we can form the following output for our $G_3$:

	Output: 11 10 11 00 01 01 00
	  Note:  1  ,  1  0  |  |  0

## Proof

We will prove that given a graph $G_n$ where each vertex has at most a degree of
10, our encoding scheme $E$ satisfies the requirement $E : G_n \to \{0,
1\}^{\lfloor 1000n \log_2 n \rfloor}$.

According to our encoding scheme, we will need one $\texttt|$ to separate every
vertex in our list $L$. For $E_0$, this implies that we will need $n - 1$
"$\texttt|$" for $n$ vertices. For $E$, this will require $2(n - 1)$ bits.

Within the graph $G_n$, the number of out-neighbors of any vertex $i$ in list
$L_i$ can be at most $\text{min}(n-1, 10)$. Since each vertex is an integer, we
will need $n (1 + \lfloor \log_2 n \rfloor)$ bits to encode $n$ vertices.
Together, this will require $n\ \text{min}(n-1, 10)(1 + \lfloor \log_2 n
\rfloor)$ bits to encode all out-neighbors of a vertex $i$. For $E$, this
implies that we will need $2n\ \text{min}(n-1, 10)(1 + \lfloor \log_2 n
\rfloor)$ bits.

We will also need one "$\texttt,$" to separate every out-neighbor of a vertex
$i$ in list $L_i$, except for when $L_i$ contains only one item, in which case
we will not need any "$\texttt,$". So we need $n\ \text{max}(0, \text{min}(n-1,
10) - 1)$ "$\texttt,$" for $n$ vertices. For $E$, this will require $2n\
\text{max}(0, \text{min}(n-1, 10) - 1)$ bits.

Combining all these expressions, we get:

$$
\begin{aligned}
  &\ 2(n - 1) + 2n\ \text{min}(n-1, 10)(1 + \lfloor \log_2 n \rfloor) + 2n\ \text{max}(0, \text{min}(n-1, 10) - 1) \\
= &\ 2n - 2 + 2n \ \text{min}(n-1, 10)(1 + \lfloor \log_2 n \rfloor) + 2n\ \text{max}(0, \text{min}(n-1, 10) - 1) \\
= &\ 2n (1 + \text{min}(n-1, 10)(1 + \lfloor \log_2 n \rfloor) + \text{max}(0, \text{min}(n-1, 10) - 1)) - 2 \\
\end{aligned}
$$

We will be using proof by iduction to prove that:

$$
2n (1 + \text{min}(n-1, 10)(1 + \lfloor \log_2 n \rfloor) +
\text{max}(0, \text{min}(n-1, 10) - 1)) - 2 \leq \lfloor 1000n \log_2 n
\rfloor
$$

Let $n = 1$ be the base case. We will have:

$$
\begin{aligned}
  &\ 2 (1) (1 + \text{min}(1-1, 10)(1 + \lfloor \log_2 1 \rfloor) + \text{max}(0, \text{min}(1-1, 10) - 1)) - 2 \\
= &\ 2 (1) (1 + \text{min}(0, 10)(1 + 0) + \text{max}(0, \text{min}(0, 10) - 1)) - 2 \\
= &\ 2 (1) (1 + 0 + \text{max}(0, -1)) - 2 \\
= &\ 2 (1) (1 + 0 + 0) - 2 \\
= &\ 2 (1 + 0 + 0) - 2 \\
= &\ 2 - 2 \\
= &\ 0 \\
\\
  &\ \lfloor 1000n \log_2 n \rfloor \\
= &\ \lfloor 1000 (1) \log_2 1 \rfloor \\
= &\ \lfloor 1000 (0) \rfloor \\
= &\ 0 \\
\end{aligned}
$$

Since $0 \leq 0$, we have proven that the base case is true.

Assuming that the inductive hypothesis is true, we will prove that the inductive
step is true. We will prove that our hypothesis also is true for $n = k + 1$.

$$
\begin{aligned}
  &\ 2(n + 1) (1 + \text{min}(n, 10)(1 + \lfloor \log_2 (n + 1) \rfloor) + \text{max}(0, \text{min}(n, 10) - 1)) - 2 \\
= &\ 2(n + 1) (1 + \text{min}(n, 10)(1 + \lfloor \log_2 n + \log_2 2 \rfloor) + \text{max}(0, \text{min}(n, 10) - 1)) - 2 \\
\end{aligned}
$$

**WHAT DO I DO NEXT?!??!**
