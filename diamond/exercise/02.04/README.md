### Encoding

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

### Proof

We will prove that given a graph $G_n$ where each vertex has at most a degree of
10, our encoding scheme $E$ satisfies the requirement $E : G_n \to \{0,
1\}^{\lfloor 1000n \log_2 n \rfloor}$. We will define $R(n) = \lfloor 1000n
\log_2 n \rfloor$.

According to our encoding scheme, we will need one $\texttt|$ to separate every
vertex in our list $L$. For $E_0$, this implies that we will need $n - 1$
"$\texttt|$" for $n$ vertices. For $E$, this will require $2(n - 1)$ bits.

Within the graph $G_n$, the number of out-neighbors of any vertex $i$ in list
$L_i$ can be at most $\text{min}(n-1, 10)$. Since each vertex is an integer, we
will need $n \lfloor 1 + \log_2 n \rfloor$ bits to encode $n$ vertices.
Together, this will require $n\ \text{min}(n-1, 10) \lfloor 1 + \log_2 n
\rfloor$ bits to encode all out-neighbors of a vertex $i$. For $E$, this
implies that we will need $2n\ \text{min}(n-1, 10) \lfloor 1 + \log_2 n
\rfloor$ bits.

We will also need one "$\texttt,$" to separate every out-neighbor of a vertex
$i$ in list $L_i$, except for when $L_i$ contains only one item, in which case
we will not need any "$\texttt,$". So we need $n\ \text{max}(0, \text{min}(n-1,
10) - 1)$ "$\texttt,$" for $n$ vertices. For $E$, this will require $2n
\ \text{max}(0, \text{min}(n-1, 10) - 1)$ bits.

Combining all these expressions, we get:

$$
\begin{aligned}
|E(G_n)| = &\ 2(n - 1) + 2n\ \text{min}(n-1, 10) \lfloor 1 + \log_2 n \rfloor + 2n\ \text{max}(0, \text{min}(n-1, 10) - 1) \\
         = &\ 2n - 2 + 2n \ \text{min}(n-1, 10) \lfloor 1 + \log_2 n \rfloor + 2n\ \text{max}(0, \text{min}(n-1, 10) - 1) \\
\end{aligned}
$$

We will be proving that $|E(G_n)| \leq R(n)$ for two cases: when $1 \leq n \leq
10$ and when $n \gt 10$.

For $1 \leq n \leq 10$, we can observe that $\text{min}(n-1, 10) = n - 1$ and
$\text{max}(0, \text{min}(n-1, 10) - 1) = 0$. Therefore, we have:

$$
\begin{aligned}
|E(G_n)| = &\ 2n - 2 + 2n \ \text{min}(n-1, 10) \lfloor 1 + \log_2 n \rfloor + 2n\ \text{max}(0, \text{min}(n-1, 10) - 1) \\
         = &\ 2n - 2 + 2n \ (n - 1) \lfloor 1 + \log_2 n \rfloor + 2n\cdot 0 \\
         = &\ 2n - 2 + 2n \ (n - 1) \lfloor 1 + \log_2 n \rfloor \\
\end{aligned}
$$

For $n = 1$, we have:

$$
\begin{aligned}
|E(G_n)| = &\ 2n - 2 + 2n \ (n - 1) \lfloor 1 + \log_2 n \rfloor \\
|E(G_1)| = &\ 2 - 2 + 2 \ (1 - 1) \lfloor 1 + \log_2 1 \rfloor \\
         = &\ 0 \\
\end{aligned}
$$

The our requirement $R$ for $n = 1$ is:

$$
\begin{aligned}
R(n) = &\ \lfloor 1000n \log_2 n \rfloor \\
R(1) = &\ \lfloor 1000 (1) \log_2 1 \rfloor \\
     = &\ \lfloor 1000 (0) \rfloor \\
     = &\ 0 \\
\end{aligned}
$$

We can calculate this for all $n$ in $1 \leq n \leq 10$ as well:

- For n = 1, $|E(G_n)| = 0$ and $R(n) = 0$
- For n = 2, $|E(G_n)| = 10$ and $R(n) = 2000$
- For n = 3, $|E(G_n)| = 28$ and $R(n) = 4754$
- For n = 4, $|E(G_n)| = 78$ and $R(n) = 8000$
- For n = 5, $|E(G_n)| = 128$ and $R(n) = 11609$
- For n = 6, $|E(G_n)| = 190$ and $R(n) = 15509$
- For n = 7, $|E(G_n)| = 264$ and $R(n) = 19651$
- For n = 8, $|E(G_n)| = 462$ and $R(n) = 24000$
- For n = 9, $|E(G_n)| = 592$ and $R(n) = 28529$
- For n = 10, $|E(G_n)| = 738$ and $R(n) = 33219$

Using the above table, we can see that $|E(G_n)| \leq R(n)$ for all $n$ in
$1 \leq n \leq 10$. Therefore, our encoding scheme $E$ satisfies the
requirement $E : G_n \to \{0, 1\}^{\lfloor 1000n \log_2 n \rfloor}$ for all
$n$ in $1 \leq n \leq 10$.

For $n > 10$, we can observe that $\text{min}(n-1, 10) = 10$ and
$\text{max}(0, \text{min}(n-1, 10) - 1) = 9$. Therefore, we have:

$$
\begin{aligned}
|E(G_n)| = &\ 2n - 2 + 2n \ \text{min}(n-1, 10) \lfloor 1 + \log_2 n \rfloor + 2n\ \text{max}(0, \text{min}(n-1, 10) - 1) \\
		 = &\ 2n - 2 + 2n \ 10 \lfloor 1 + \log_2 n \rfloor + 2n\cdot 9 \\
		 = &\ 2n - 2 + 2n \ 10 \lfloor 1 + \log_2 n \rfloor + 18n \\
		 = &\ 20n - 2 + 20n \lfloor 1 + \log_2 n \rfloor \\
		 = &\ 20n + 20n \lfloor 1 + \log_2 n \rfloor - 2 \\
		 = &\ 20n + 20n (1 + \lfloor \log_2 n \rfloor) - 2 \\
		 = &\ 20n + 20n + 20n \lfloor \log_2 n \rfloor - 2 \\
		 = &\ 40n + 20n \lfloor \log_2 n \rfloor - 2 \\
\end{aligned}
$$

We will use proof by contradiction to show that $|E(G_n)| \leq R(n)$ for all
$n > 10$. We will assume that $|E(G_n)| \gt R(n)$ for some $n > 10$. We will
then show that this assumption leads to a contradiction.

$$
\begin{aligned}
&&|E(G_n)| &\gt R(n) \\
&\implies& 40n + 20n \lfloor \log_2 n \rfloor - 2 &\gt \lfloor 1000n \log_2 n \rfloor \\
&\implies& 40n + 20n \lfloor \log_2 n \rfloor - 2 &\gt \lfloor 980n \log_2 n + 20n \log_2 n \rfloor \\
\end{aligned}
$$

<!-- Since $\lceil \log_2 n \rceil \geq \lfloor \log_2 n \rfloor$ for all $n \gt 1$, -->
<!-- it follows that $40n + 20n \lceil \log_2 n \rceil - 1 \geq 40n + 20n \lfloor -->
<!-- \log_2 n \rfloor - 1$. -->

Also, since $n \in \mathbb{N}$ and $n > 1$, we can assume that $n = \lfloor n
\rfloor$. This also holds true for $cn$ with $c \in \mathbb{N}$ and $c \gt 0$.

Therefore, we have:

$$
\lfloor 40n \rfloor + \lfloor 20n \rfloor \lfloor \log_2 n \rfloor - 1 \gt \lfloor 980n \log_2 n + 20n \log_2 n \rfloor \\
$$

Since $\lfloor 980n \log_2 n + 20n \log_2 n \rfloor \geq \lfloor 980n \log_2 n
\rfloor + \lfloor 20n \log_2 n \rfloor$, we have:

$$
\lfloor 40n \rfloor + \lfloor 20n \rfloor \lfloor \log_2 n \rfloor - 1 \gt \lfloor 980n \log_2 n \rfloor + \lfloor 20n \log_2 n \rfloor \\
$$

Conversely, $\lfloor 20n\log_2 n \rfloor \geq \lfloor 20n \rfloor \lfloor \log_2
n \rfloor$. Therefore, we have:

$$
\begin{aligned}
&& \lfloor 40n \rfloor + \lfloor 20n \log_2 n \rfloor - 1 &\gt \lfloor 980n \log_2 n \rfloor + \lfloor 20n \log_2 n \rfloor \\
&\implies& \lfloor 40n \rfloor - 1 &\gt \lfloor 980n \log_2 n \rfloor
\end{aligned}
$$


Since $40 > 980 \log_2 n$ is false, $\lfloor 40n \rfloor \gt \lfloor 980n \log_2
n \rfloor$ is also false.

It then follows that $\lfloor 40n \rfloor \leq \lfloor 980n \log_2 n \rfloor$
must be true. This implies that $\lfloor 40n \rfloor - 1 \leq \lfloor 980n
\log_2 n \rfloor$ must also be true. Therefore, $|E(G_n)| \gt R(n)$ is false.

It is then concluded that $|E(G_n)| \leq R(n)$ for all $n > 10$.

Therefore, our encoding scheme $E$ satisfies the requirement $E : G_n \to
\{0, 1\}^{\lfloor 1000n \log_2 n \rfloor}$ for all $n > 10$.

We can now conclude that our encoding scheme $E$ satisfies the requirement
$E : G_n \to \{0, 1\}^{\lfloor 1000n \log_2 n \rfloor}$ for all $n \geq 1$.
