# Assignment 10










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


if __name__ == '__main__':
    main()