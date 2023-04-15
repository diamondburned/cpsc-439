# CPSC 439 Project #2
## Task #1


#### Regular language:
$\{w:w\text{ contains at least three 1s}\}\textbf{ } \Sigma = \{0, 1\}^*.$

DFA:
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

#### Irregular Language:

$\\{w:  w \text{ is a palindrome}\\}$ over the alphabet $\Sigma = \{a, b\}^*$

*See:* *[Our Proof of Irregularity](https://github.com/diamondburned/cpsc-439/blob/main/yao/proj1/task5.md) via the Pumping Lemma*
