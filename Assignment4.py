# Assignment 4
import random
import copy

class Graph:

    def __init__(self, input_list):
        self.vertices = {}
        self.num_vertices = 0
        self.constructGraph(input_list)

    def constructGraph(self, input_list):
        # input is a 2D list, where the first element of each row is a vertex, followed by nodes connected to it
        self.num_vertices = len(input_list)
        for row in input_list:
            vertex = row[0]
            connected_nodes = row[1:]
            self.vertices[vertex] = connected_nodes

        return 0

    def __str__(self):
        info = f"Graph with {self.num_vertices} vertices\n"

        return info + str(self.vertices)

    def randomContraction(self):
        vertices = copy.deepcopy(self.vertices)
        while len(vertices) > 2:
            v = list(vertices.keys())[random.randint(0, len(vertices) - 1)]
            u = vertices[v][random.randint(0, len(vertices[v]) - 1)]
            edge = (v, u)
            mergeVertices(vertices, edge)

        min_cut = len(vertices[list(vertices.keys())[1]])

        return min_cut


def mergeVertices(vertices, edge):
    head, tail = edge[0], edge[1]
    # merge head and tail into head, but keep duplicated connections
    vertices[head] = vertices[head] + vertices[tail]
    removeSelfLoop(vertices, head, tail)
    vertices.pop(tail)
    # remove tail from graph
    for vertex, nodes in vertices.items():
        for i in range(len(vertices[vertex])):
            if vertices[vertex][i] == tail:
                vertices[vertex][i] = head

    return 0

def removeSelfLoop(vertices, head, tail):
    i = 0
    while i < len(vertices[head]):
        node = vertices[head][i]
        if node == head or node == tail:
            vertices[head].pop(i)
        else:
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
    min_cuts = []
    for i in range(1, 100):
        if not i % 10:
            print(i)
        min_cuts.append(graph.randomContraction())

    print(min_cuts)
    print(min(min_cuts))

    return 0


if __name__ == '__main__':
    main()