# CPSC 439 Project #2
## Task #2
### Recognizing our Regular Language

To accomplish this task, we decided to use the purely functional programming
language: Miranda

Firstly, here's a "cheat" way of identifying our language using Miranda
built-ins.

```miranda
inp = [0, 1, 1, 0, 1]

threeOrMoreOnes i = (sum i) >= 3

main = show (threeOrMoreOnes inp)
```

Ok, here's a more lambda calculus-esque way of doing things. We define each
state as accepting a head `h` and a tail `t`. From each state you can progress
to a new state or stay in your current state. This behavior is described
succinctly in our DFA from `task1.md`.

```miranda
inp = [1, 1, 0, 0, 0, 1, 0, 0, 1]

noOne [0] = 0
noOne (h:t) = noOne  t, if h = 0
            = oneOne t, if h = 1

oneOne [0] = 0
oneOne (h:t) = oneOne t, if h = 0
             = twoOne t, if h = 1

twoOne [0] = 0
twoOne (h:t) = twoOne t, if h = 0
             = threeOrMoreOne t, if h = 1

threeOrMoreOne i = 1

main = noOne inp
```

*Note: Getting the Miranda interpreter up and running is a P.I.T.A!!!*
