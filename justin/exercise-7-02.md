# Exercise 7.2

## Author: Justin

Remark 7.7 states: "As we will see, adding loops and arrays to
NAND-CIRC is enough to capture the full power of all programming languages!
Hence we could replace “NAND-TM” with any of Python, C, Javascript, OCaml,
etc."

Due to this, I will simply write each algorithm in `Python` to prove that it is
possible in NAND-TM.

```py
INC = lambda n : n + 1
ADD = lambda n, m : n + m
MULT = lambda n, m : n * m
SORT = lambda lst : sorted(lst)
```

Q.E.D
