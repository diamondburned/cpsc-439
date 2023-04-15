$$
\begin{aligned}
zip &= \lambda \ I \ L \ . \\
	&\ \ \ \ \ \ \ \begin{aligned}
	               \text{IF} \ &\text{ISEMPTY}(I) \\
	               	 &\text{NIL} \\
	               	 &zip \ \text{PAIR}(\text{PAIR}(\text{HEAD}(I), \text{HEAD}(L)), \ zip \ TAIL(I), TAIL(L)) \\
	               \end{aligned}
\end{aligned}
$$

or

$\text{RECURSE}$ version:

$$
\begin{aligned}
\text{RECURSE}(
	&\lambda \ zip, \ I, \ L \ . \\
	&\ \ \ \ \begin{aligned}
	\text{IF} \ &\text{ISEMPTY}(I) \\
	 &\text{NIL} \\
	 &zip \ \text{PAIR}(\text{PAIR}(\text{HEAD}(I), \text{HEAD}(L)), \ zip \ \text{TAIL}(I), \text{TAIL}(L)) \\
	\end{aligned} \\)
\end{aligned}
$$
