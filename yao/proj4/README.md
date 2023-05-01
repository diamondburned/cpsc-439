# How to run this code

`FILE=dfas/atleast-3-1s.txt;LENGTH=5;diff3 <(python3 dfa.py $FILE $LENGTH | sort) <(python3 convert.py $FILE $LENGTH | python3 z3-sat.py | sort) <(python3 convert.py $FILE $LENGTH | python3 simple-sat.py | sort) -A`
