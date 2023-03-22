The topic of DFAs is really interesting. It makes me wonder, would a lexer or
parser count as a DFA? We could have a DFA that has an output of $\{0, 1\}$
where $0$ is a valid input and $1$ is an invalid input, but we would also have
another output that is the tokens that are being parsed. Would this extra output
that is potentially not finite make it not a DFA?
