# [Exercise 2.14](https://introtcs.org/public/lec_02_representation.html#exercises)

#### Author: Justin

## Task

Prove that there is a one-to-one mapping from $\mathbb{Z}^*$ to $\mathbb{N}$.

## Proof

Using just the set of ${\{1, 2, 3, 4, 5, 6\}}$ we can prove that there exists a one-to-one mappin from $\mathbb{Z}^*$ to $\mathbb{N}$.

For any sequence of integers $k$ from $\mathbb{Z}^*$ we can represent $k$ as a natural number by encoding each integer within $k$ individually.

<!-- First, we calculate the total number of digits that will be used in our encoding scheme. To do this we will use $D$ to represent the number of digits in the resulting natural number. Calculating the digits goes as follows:

$$
D(k) = \sum^{|k|}_{i=1} k_i + (1 \hspace{3pt}\texttt{if}\hspace{3pt} k_i < 0 \hspace{3pt}\texttt{else} \hspace{3pt}0)
$$ -->

<!-- For example, consider the set $k$ ${\{4, -2,3\}}$. We can calculate $D$ using the above equation. The integer $4$ will take 4 digits to represent while $-2$ will take 3 digits to represent due to its parity. Finally, $3$ takes 3 digits to represent for a total of $D=10$ (digits). -->

<!-- _Notice how negative numbers utilize one extra digit, the reason for this will be obvious in the next steps._ -->

We will need a modified prefix sum $P$ where $P_1 = \lvert k_1 \rvert$, $P_2 = \lvert k_1  \rvert + \lvert k_2 \rvert$, or more generally:

<!-- $$
P_i = \sum^{i}_{j=1}k_j\ if \ k_j >= 0 \ else \ \lvert k_j \rvert + 1
$$ -->

$$
P_i = \sum^{i}_{j=1} \lvert k_j \rvert
$$

We will also introduce a custom function $\rho$ which returns one of four digits from the set $\{1,2,3,4\}$.

$$
\rho(n, i) = 1 \ if \ n \ge 0 \ and \ i (\bmod 2) \equiv 0
\\
\rho(n, i) = 2 \ if \ n \ge 0 \ and \ i (\bmod 2) \equiv 1
\\
\rho(n, i) = 3 \ if \ n \lt 0 \ and \ \lvert i \rvert (\bmod 2) \equiv 0
\\
\rho(n, i) = 4 \ if \ n \lt 0 \ and \ \lvert i \rvert (\bmod 2) \equiv 1
\\
\rho(n, i) = 5 \ if \ n = 0 \ and \ \lvert i \rvert (\bmod 2) \equiv 0
\\
\rho(n, i) = 6 \ if \ n = 0 \ and \ \lvert i \rvert (\bmod 2) \equiv 1
$$

Now, consider the following $KtN$ encoding function which takes the constituents of $k$ and concatenates sequences of $1$, $2$, $3$, $4$, $5$, or $6$.

$$
KtN(k) =
\sum^{|k|}_{i=1}
\
\{\rho(k_i, i)\}^{\lvert k_i \rvert \ if \ k_i \ne 0 \ else \ 1} \
\times 10^{\ P_{|k|}-P_i}
$$

We now have a prefix-free one-to-one encoding of any set of integers to a natural number.

Q.E.D

Sunday, February 12, 2023 @ 04:32:17 PM
