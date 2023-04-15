|| Goal: detect palindromes

inp = [1, 1]

removeLast [] = []
removeLast [x] = []
removeLast (h:t) = h : removeLast(t)

isPalindrome s = 1, if #s <= 1
               =  isPalindrome ( drop 1 ( removeLast s ) ), if s!0 = (last s)
               =  0, otherwise

main i = isPalindrome i
