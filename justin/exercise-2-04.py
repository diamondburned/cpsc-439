import math

Graph = dict[int, list[int]]  # custom type
bitstring = str

G: Graph = {1: [1, 3, 4], 2: [2, 3], 3: [4, 5], 4: [6, 7, 8], 9: [10]}
N: int = max([x for y in G.values() for x in y] + list(G.keys()))  # largest index
K: int = math.floor(math.log2(N)) + 1  # bits required to represent largest index
kMAX_DEGREE = 10

upperBound = lambda N: math.floor(N * math.log2(N) * 1000)
block = lambda x: bin(x)[2:].zfill(K)


def GtoB(graph: Graph) -> bitstring:
    global N
    buffer = ["0"] * N + ["1"]  # start off with N 0's then a delim '1'
    for idx in range(1, N + 1):
        buffer.append(block(idx))
        adj = graph.get(idx, [])
        filled = adj + [0 for _ in range(kMAX_DEGREE - len(adj))]
        assert len(filled) == kMAX_DEGREE, "ADJ LIST MUST BE 10 BLOCKS"
        for neighbor in filled:
            buffer.append(block(neighbor))
    return "".join(buffer)


def BtoG(binary: bitstring) -> Graph:
    # scan to first 1
    first_one = binary.index("1")
    vertex_count = first_one
    block_width = (len(binary) - first_one) // 11 // vertex_count
    new_graph = {}
    count = 0
    idx = None
    for bidx in range(first_one + 1, len(binary), block_width):
        block = binary[bidx : bidx + block_width]
        as_num = int(block, base=2)
        if count % 11 == 0:  # read in index
            index = as_num
            idx = index
            new_graph[index] = []
        elif as_num:
            new_graph[idx].append(as_num)
        count += 1
    return {k: v for (k, v) in new_graph.items() if len(v)}


if __name__ == "__main__":
    as_binary = GtoB(G)
    print(f"{as_binary=}")
    new_graph = BtoG(as_binary)
    print(f"{new_graph=}")
    print(f"{G == new_graph=}")
