$$\{w:w\text{ contains at least three 1s}\}.$$

### DFA Diagram

```graphviz
digraph {
    rankdir=LR;
    node [shape = circle];

    0  [label = " ", shape = point, width = 0];
    1 [label = "1"];
    2 [label = "2"];
    3 [label = "3"];
    4 [label = "4", peripheries = 2];

    0 -> 1;
    1 -> 1 [label = "0"];
    1 -> 2 [label = "1"];
    2 -> 2 [label = "0"];
    2 -> 3 [label = "1"];
    3 -> 3 [label = "0"];
    3 -> 4 [label = "1"];
    4 -> 4 [label = "0,1"];
    }
```

### Sipser's Definition

$$M=({\left\lbrace 1,2,3,4\right\rbrace},\left\lbrace0,1\right\rbrace,\delta,1,\left\lbrace 4\right\rbrace)\text{, where }\delta\text{ is defined as:}$$

$$
\begin{array}{c|c c}
\delta & 0 & 1 \\
\hline
1 & 1 & 2\\
2 & 2 & 3\\
3 & 3 & 4\\
4 & 4 & 4\\
\end{array}
$$
