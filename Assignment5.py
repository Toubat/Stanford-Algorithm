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

    def firstDFS(self, start, arr):
        global time
        self.explored[start] = True
        arr.append(start)
        stack = deque()
        stack.append(start)
        while len(stack):
            while self.graph[stack[-1]]:
                v = stack[-1]
                # delete the last connected vertex to v iff it has been explored
                while self.graph[v] and self.explored[self.graph[v][-1]]:
                    self.graph[v].pop()
                if self.graph[v]:
                    # let v be an new vertex never explored before
                    v = self.graph[v].pop()
                    self.explored[v] = True
                    arr.append(v)
                    stack.append(v)
            # let v be vertex where all its connected nodes has been exhausted
            v = stack.pop()
            time += 1
            self.orders[v] = time

        return 0

    def recursiveDFS(self, start, arr):
        global time
        self.explored[start] = True
        arr.append(start)
        for node in reversed(self.graph[start]):
            if not self.explored[node]:
                self.recursiveDFS(node, arr)
        time += 1
        self.orders[start] = time

        return 0

    def computeSSCs(self):
        pass

    def reset(self, input_list, reverse=False):
        global time, src
        time, src = 0, 0
        self.graph = {}
        self.num_vertices = 0
        self.constructGraph(input_list, reverse)
        self.orders = [0 for _ in range(self.num_vertices + 1)]
        self.explored = [False for _ in range(self.num_vertices + 1)]


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
    initInput(lst, '2.txt')
    graph = DirectedGraph(lst)
    print(graph)

    for i in range(1, 13):
        arr1, arr2 = [], []
        graph.firstDFS(i, arr1)
        order1 = graph.orders[:]
        graph.reset(lst)
        graph.recursiveDFS(i, arr2)
        order2 = graph.orders[:]
        graph.reset(lst)
        assert len(arr1) == len(arr2)
        for j in range(len(arr1)):
            assert arr1[j] == arr2[j]
        for j in range(len(order1)):
            assert order1[j] == order2[j]

    print("All Success!")

    return 0


if __name__ == '__main__':
    main()