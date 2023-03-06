There are probably different ways that you could do to hack in the 3 gates with
just 3 variables, but a naive way would be to just add a new variable.

Assuming you want to represent $\text{NOT}$, $\text{AND}$ and $\text{OR}$ as
another extra variable in our tuple, we now have a 4-tuple $(t_3, t_0, t_1,
t_2)$ where $t_0$ can be 0, 1, or 2 which correlates to $\text{NOT}$,
$\text{AND}$ or $\text{OR}$.

Given this, the variables would probably take up $\lceil \log_2(4s) \rceil$
bits instead of $\lceil \log_2(3s) \rceil$ bits with $\text{NAND}$.
