1. $INC: \{0, 1\}^* \to \{0, 1\}^*$

   To keep it simple, we'll assume that our "natural number" $n$ is an unsigned
   integer that is represented as a binary string of length $|n|$.

   Our Turing Machine will have this binary string in its tape. On the left of
   this binary string is an infinite number of $0$s (or as many as our tape can
   hold).

   Our Turing Machine will do the following:

   1. First, we move our head to the rightmost position of the tape (or to the
      rightmost position of $n$).
   2. If the bit at this position is $0$, we write $1$ and halt, otherwise we
      write $0$ and move the head to the left.
   3. We repeat step 2 until we reach the leftmost position of the tape.
   4. At the leftmost position, we halt. The tape now contains the binary
      representation of $n + 1$.

2. $ADD: \{0, 1\}^* \to \{0, 1\}^*$

   We can use our $INC$ Turing Machine that we defined above to implement
   addition.

   Since $\text{NAND-TM}$ has loops defined with a counter $i$, we'll also
   borrow that.

   We'll keep the same assumptions as before, however this time, we'll also
   store the **unary** representation of $m$ in the tape on the right of $n$.
   This means there will be $m$ $1$s on the right of $n$ which ends with a $0$.
   These two numbers are separated by a symbol $|$. There's also one $|$ to the
   right of $m$.

   We'll define some small procedures to help with our steps:

   1. $COMPARE$, which compares $i$ to $m$. To do this, we will:

      1. Move the head to the rightmost position of $m$ by looking for two $|$
         symbols.
      2. Move left $i$ times.
      3. Do a $MODANDJUMP(v, v)$, where $v$ is the current value on our reading
         head.

   2. $MODANDJUMP(a, b)$, which is actually defined as part of $\text{NAND-TM}$.

   Our Turing Machine will do the following:

   1. First, run `COMPARE`. If $v$ in `COMPARE` was $0$, then this would've
      halted the program, and we've finished adding. If it's $1$, then $i$ is
      incremented, and we're not done yet.

   2. Move to the rightmost position of $n$ by moving left until we find a $|$
      and moving left once more.

   3. Run $INC$ on $n$.

   4. Repeat 1 until we halt. Once we halt, the tape will contain the binary
      representation of $n + m$.

3. $MULT: \{0, 1\}^* \to \{0, 1\}^*$

   Our $ADD$ Turing Machine can be used to implement multiplication.

   We'll do the same thing as before, but this time, instead of just calling
   $INC$ on $n$, we'll call $ADD$ on $n$ and $m$.
