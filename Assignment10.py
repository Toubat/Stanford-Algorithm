# Assignment 10
from structure_utils import UnionFind

def kClusteringMaxSpacing(lst, nodes, k):
    lst.sort(key=lambda x: x[2])
    union_find = UnionFind(nodes)
    idx = 0
    while union_find.num_components > k:
        u, v, spacing = lst[idx]
        union_find.union(u, v)
        idx += 1
    u, v, spacing = lst[idx]
    while union_find.find(u, v):
        idx += 1
        u, v, spacing = lst[idx]

    return spacing

def initInput(lst, path):
    with open(path, 'r') as f:
        num_nodes = f.readline()
        nodes = {}
        while True:
            line = f.readline()
            if not line:
                break
            u, v, cost = line.split()
            u, v, cost = int(u), int(v), int(cost)
            if u not in nodes:
                nodes[u] = True
            if v not in nodes:
                nodes[v] = True
            lst.append((u, v, cost))

    return int(num_nodes), list(nodes.keys())


def main():
    lst = []
    num_nodes, nodes = initInput(lst, 'assign10_input_1.txt')
    spacing = kClusteringMaxSpacing(lst, nodes, 4)
    print(spacing)


if __name__ == '__main__':
    main()