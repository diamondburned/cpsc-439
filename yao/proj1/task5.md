### Irregular Language

Consider the language $\{w:  w \text{ is a palindrome}\}$ over the alphabet $\Sigma = \{a, b\}^*$

Intuitively, determining palindromes requires an external memory buffer, of
which we do **not** have in a DFA or NFA.


Formally, we can show that $w$ is irregular through a **Proof by
Contradiction** utilizing the [Pumping
Lemma](https://introtcs.org/public/lec_05_infinite.html#limitations-of-regular-expressions-and-the-pumping-lemma).

The Pumping Lemma states that given any palindrome $p$ in our language $w$
there exists some pumping length $n$ such that $|p|$ of length greater than or
equal to $n$ can be written as $p = xyz$ where

1. $|y| > 0$

2. $|xy| <= n$

3. $\text{For any }n >= 0, \text{ the string } xy^k z \text{ is also a palindrome in } w$

Consider the string $a^pba^p$ which is clearly a palindrome. e.g: $aaabaaa$
where the pumping length $p$ is $3$

By the Pumping Lemma, we can write $p = xyz$ where $|y| > 0$, and for any $k >=
0$ $xy^kz$ is also a palindrome in $w$. We can write $y = a^k$ for any $k > 0$
since $y$ is non-empty and must consist entirely of symbols from our alphabet
$\Sigma$ i.e: $\{a, b\}$. Following this, we know $x$ can only containt at most
$n-k$ $a$'s due to $|xy| <= n$. Meanwhile, $z$ contains the rest of the
remaining $a$'s and $b$'s. Post concatenation, with the formula $xy^kz$ shows
us that the resulting string will have more $a$'s on the left side (of the $b$) than the
right. Which is clearly not a palindrome. Hence, our initial assumption that
$w$ is a regular language is incorrect which leads us to understand that $w$
itself is an irregular language.


Extra visual example:

```
p = aaaabaaaa

choose n = 4

choose y as two a's near the middle = aa[aa]baaaa

that means x is = [aa]aabaaaa

check that |xy| <= n ... 3 + 1 = 4 ... 4 <= 4 ✔

concatenate via xy^kz where k > 0

choose k = 2

(using + as concatenation)
resulting_string = aa + (aa)^2 + baaaa
resulting_string = aa + aaaa + baaaa
resulting_string = aaaaaabaaaa

this is not a palindrome.
```
