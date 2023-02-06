import math

for n in range(1, 11):
    f = (2 * n) - 2 + (2 * n * (n - 1) * math.floor(1 + math.log2(n)))
    g = math.floor(1000 * n * math.log2(n))
    print(f"For n = {n}, $|E(G_n)| = {f}$ and $R(n) = {g}$")
