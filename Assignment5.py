# Assignment 5
from collections import deque

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
    initInput(lst, "assign5_input.txt")
    print(len(lst))
    print(lst[:20])

    return 0


if __name__ == '__main__':
    main()