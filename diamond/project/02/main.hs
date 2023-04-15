data Bit = Zero | One deriving (Eq, Show)

charToBit :: Char -> Bit
charToBit '0' = Zero
charToBit '1' = One
charToBit x = error ("Invalid bit: " ++ show x)

data List = Nil | Pair (Bit, List)

strToList :: String -> List
strToList str =
  let go :: String -> List
      go str =
        if null str
          then Nil
          else Pair (charToBit (head str), go (tail str))
   in go str

state0 :: List -> Bool
state0 Nil = True
state0 (Pair (Zero, xs)) = state2 xs
state0 (Pair (One, xs)) = state1 xs

state1 :: List -> Bool
state1 Nil = True
state1 (Pair (_, xs)) = state0 xs

state2 :: List -> Bool
state2 Nil = False
state2 (Pair (_, xs)) = state2 xs

dfa :: List -> Bool
dfa = state0

main = do
  input <- getLine
  print (dfa (strToList input))

{-
 - 0 = lambda x, y . x
 - 1 = lambda x, y . y
 - state0 = lambda x . x state1 state2
 - state1 = lambda x . x state0 state0
 - state2 = lambda x . x state2 state 2
 - -}
