inp = [0, 1, 1, 0, 1]

threeOrMoreOnes i = (sum i) >= 3

main = show (threeOrMoreOnes inp)
