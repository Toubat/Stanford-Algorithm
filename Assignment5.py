# Assignment 5
from collections import deque

# global variables of finishing time - t and most recent source vertex - src
time = 0
src = 0

class DirectedGraph:

    def __init__(self, input_list, reverse=False):
        self.graph = {}
        self.num_vertices = 0
        self.constructGraph(input_list, reverse)
        self.orders = [0 for _ in range(self.num_vertices + 1)]
        self.explored = [False for _ in range(self.num_vertices + 1)]

    def constructGraph(self, input_list, reverse=False):
        self.graph = {}

        for edge in input_list:
            if reverse:
                head, tail = edge[0], edge[1]
            else:
                tail, head = edge[0], edge[1]
            if tail in self.graph:
                self.graph[tail].append(head)
            else:
                self.graph[tail] = [head]
                self.num_vertices += 1
            if head not in self.graph:
                self.graph[head] = []
                self.num_vertices += 1

        return 0

    def __str__(self):
        info = f"Graph with {self.num_vertices} vertices\n"
        for i in range(1, 11):
            info += f"Vertex {i} : {str(self.graph[i])}\n"

        return info

    def DFS(self, start):
        self.explored[start] = True
        self.orders[start] = src
        stack = deque()
        stack.append(start)
        while len(stack):
            v = stack.pop()
            #for u in self.graph[v]


        return 0

    def computeSSCs(self):
        pass


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
    initInput(lst, 'assign5_input.txt')
    graph = DirectedGraph(lst, reverse=False)
    print(graph)

    return 0


if __name__ == '__main__':
    main()