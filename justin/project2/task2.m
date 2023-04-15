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
