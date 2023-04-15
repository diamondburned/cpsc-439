1. The result of the evaluation is `20`.
2. Here's the expression ported 1:1:

   $$
   \begin{aligned}
   a &= \lambda a \ . \ a \\
   g &= \lambda x \ . \ a \cdot x \\
   a &= 2 \\
   g &\ 10
   \end{aligned}
   $$

   or as one line:

   $$
   ((\lambda a \ . \ (\lambda x \ . \ a \cdot x)) \ 2) \ 10
   $$

3. The equivalent Python expression using `lambda` is:

   ```python
   (lambda a: lambda x: a * x)(2)(10)
   ```

4. The result of the above expression is the same: `20`.

5. Since we're expecting a different answer, let me just redo everything.
   Here's the lambda calculus version:

   $$
   \begin{aligned}
   a' &= \lambda a \ . \ a \\
   a  &= a' 7 \\
   g  &= \lambda x \ . \ a \cdot x \\
   a  &= a' 2 \\
   g  &\ 10
   \end{aligned}
   $$

   Here's the Python version of the lambda calculus expression:

   ```python
   a_ = (lambda a: a)
   a = a_(7)
   g = (lambda x: a * x)
   a = a_(2)
   g(10)
   ```

   This still gives me `20`. I don't know what I'm doing wrong :)
