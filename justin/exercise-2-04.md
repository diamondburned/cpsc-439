# [Exercise 2.4](https://introtcs.org/public/lec_02_representation.html#exercises)

#### Author: Justin

## Proof

We are tasked with representing Graphs using at most $\lfloor 1000n \log(n)\rfloor$ bits. These Graphs, however, are directed and have a degree of at most $10$.

Formally,

$\forall n \in \mathbb{N} \texttt{, the set} \hspace{2pt} G_n \texttt{ contains all directed graphs over the vertex set } [n] \\ \texttt{ where every vertex has a degree at most } 10$.

Prove,

$\texttt{For every sufficiently large } n \texttt{ there exists a one-to-one function: }\\ E: G_n \to {0, 1}^{\lfloor 1000n \log{n} \rfloor}$

Naively we could opt for an Adjacency Matrix encoding scheme which would result in each vertex requiring a bitstring of length $n$ where a $0$ represents no edge and $1$ representing an edge. This yields an approximate total bit usage of $n^2$ which does not satisfy the inequality $n^2 \le \lfloor 1000n\log{n} \rfloor$ for sufficiently large $n$.

Optimally, an Adjacency List encoding scheme should be used. In this scheme each vertex holds a list of its neighbors (vertices that it shares an edge with). Each vertex's list is comprised of the indices to the neighboring vertices.

Since there are $n$ we will assign indices as $[n]$ , i.e: ${1, 2, 3, ..., n_{i-1}, n_i}$. With this relationship, any arbitrary index $n_i$ requires $\lceil{\log_2{n_i}}\rceil$ bits to represent. Each vertex may potentially have an out-degree of $10$ which results in a maximum usage of $10 \times \lceil{\log_2{n}}\rceil$ bits per vertex. With $n$ vertices we are using $10 \times \lceil{\log_2{n}}\rceil \times n$ bits total, it is clear to see that the following inequality holds `true` for all $n$: $10 \times \lceil{\log_2{n}} \rceil \times n \le \lfloor 1000 \times n \log{n}\rfloor$

However, to ensure that our Adjacency List encoding function $E$ is one-to-one we must ensure that it is `prefix_free` i.e: $E \texttt{ is prefix-free if } E(o) \neq \varnothing \texttt{ for every o} \in O  \texttt{ and there does not exist a distinct pair of objects } o, o' \in O \texttt{ such that } E(o) \texttt{is a prefix of } E(o')$

<!-- To show this, we need to expand our encoding language from ${\{0, 1\}}$ to ${\{00, 11, 01, 10\}} \texttt{ wherein } 00 \to 0, 11 \to 1, 01 \to |, 10 \to ||$ -->

To ensure this, we will use a fixed bit width to represent vertices and their neighbors. Our bit width will be equivalent to the number of bits required to represent the largest index of any vertex $(B)$ as, i.e: $\lceil \log_2{n} \rceil$. We will then structure our encoding scheme into blocks of $B$ bits. Each vertex will be allocated $11$ blocks, the first of which being the index of the vertex itself. For this and all future index representations, we will left-pad our bitstring with $0$'s to ensure each index takes precisely $B$ bits to represent. The following $10$ blocks contain the index of a neighboring vertex, if a vertex has an out-degree $<10$ then entire blocks may consist entirely of $0$'s i.e: ${\{0\}}^B$ for which there is no neighboring vertex.

### Finally,

Each of the $n$ vertices requires $11 \times B$ bits. Which yields $11 \times B \times n$ total bits. Expanding $B$ yields: $11 \times \lceil\log_2{n}\rceil \times n$

which has the property,

$11 \times \lceil\log_2{n}\rceil \times n$ $\le$ $\lfloor 1000n \log(n)\rfloor$

To prove that our encoding function $E$ is one-to-one we must show that $E(u) = E(v) \rightarrow u = v$.

$\texttt{I have no idea how to do this part}$

$Q.E.D$

:)
