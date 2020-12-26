# Assignment 4
import random
import copy

class Graph:

    def __init__(self, input_list):
        self.vertices = {}
        self.edges = {}
        self.num_vertices = 0
        self.num_edges = 0
        self.constructGraph(input_list)

    def constructGraph(self, input_list):
        # input is a 2D list, where the first element of each row is a vertex, followed by nodes connected to it
        self.num_vertices = len(input_list)
        for row in input_list:
            vertex = row[0]
            connected_nodes = row[1:]
            self.vertices[vertex] = connected_nodes
            for node in connected_nodes:
                if (vertex, node) in self.edges or (node, vertex) in self.edges:
                    continue
                else:
                    self.edges[(vertex, node)] = True
                    self.num_edges += 1

        return 0

    def __str__(self):
        info = f"Graph with {self.num_edges} edges and {self.num_vertices} vertices\n"

        return info + str(self.vertices) + "\n" + str(self.edges)

    def randomContraction(self, seed):
        random.seed(seed)
        vertices = copy.deepcopy(self.vertices)
        edges = copy.deepcopy(self.edges)
        while len(vertices) > 2:
            edge = random.choice(list(edges.keys()))
            vertices, edges = mergeVertices(vertices, edges, edge)
        min_cut = len(vertices[list(vertices.keys())[1]])

        return min_cut


def mergeVertices(vertices, edges, edge):
    head, tail = edge[0], edge[1]
    # merge head and tail into head, but keep duplicated connections
    assert head in vertices
    assert tail in vertices
    vertices[head] = vertices[head] + vertices[tail]
    removeSelfLoop(vertices, head, tail)
    vertices.pop(tail)
    # remove tail from graph
    for vertex, nodes in vertices.items():
        if head in nodes and tail in nodes:
            vertices[vertex].remove(tail)
        elif tail in nodes:
            vertices[vertex].remove(tail)
            vertices[vertex].append(head)
    i = 0
    keys = list(edges.keys())
    while i < len(keys):
        pair = keys[i]
        if head in pair or tail in pair:
            keys.pop(i)
            i -= 1
        i += 1
    edges = {key: True for key in keys}
    for pair in edges.keys():
        assert tail not in pair
    # reconstruct edges
    for node in vertices[head]:
        edges[(head, node)] = True

    return vertices, edges


def removeSelfLoop(vertices, head, tail):
    cache = {}
    i = 0
    while i < len(vertices[head]):
        node = vertices[head][i]
        if node == head or node == tail or node in cache:
            vertices[head].pop(i)
            i -= 1
        else:
            cache[node] = True
        i += 1

    return 0


def initInput(lst, path):
    file = open(path, 'r')

    while True:
        line = file.readline().split()
        if not line:
            break
        line = [int(num) for num in line]
        lst.append(line)

    return 0


def main():
    lst = []
    initInput(lst, "assign4_input.txt")
    graph = Graph(lst)
    min_cuts = graph.randomContraction(1)
    print(min_cuts)

    return 0


if __name__ == '__main__':
    main()