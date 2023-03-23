### Turing Machine

$$
\begin{align*}
&\text{Let }THREE\text{ be the function that accept }x\isin\lbrace0,1\rbrace^*\text{, outputs 1 if and only if }x\text{ has at least 3 1's.} \\
&M\text{ is a turing machine that can computes }THREE\text{, }M\text{'s alphabet is }\lbrace0,1,>,.\rbrace \\
&M\text{'s state as follow:}
\end{align*}
\newline
\begin{array}{c|c}
\text{state} & \text{label} \\
\hline
0 & \text{START} \\
1 & \text{LEFTMOST} \\
2 & \text{FOUND0} \\
3 & \text{FOUND1} \\
4 & \text{FOUND2} \\
5 & \text{FOUND3} \\
6 & \text{OUTPUT0} \\
7 & \text{OUTPUT1} \\
\end{array}
$$

To Describe what the turing machine **M** do is words
- **M** starts in state START and goes right, looking for the first symbol. If it is ".", it will move to state OUTPUT0 and halts the machine.
- If it found the symbol "1", it will move to state FOUND1 and goes right.
- It will keep going right, and found "1", move to state FOUND2, etc. Until it reachs FOUND3.
- If it reach to the end (when symbol is "."), it will move to state OUTPUT1 and halt the machine.
