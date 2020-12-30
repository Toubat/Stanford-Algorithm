# Assignment 5
from collections import deque

# global variables of finishing time - t and most recent source vertex - src
time = 0
src = 0

class DirectedGraph:

    def __init__(self, input_list, reverse=False):
        self.list = input_list
        self.graph = {}
        self.num_vertices = 0
        self.constructGraph(input_list, reverse)
        self.orders = [0 for _ in range(self.num_vertices + 1)]  # finishing time -> vertex
        self.explored = [False for _ in range(self.num_vertices + 1)]  # vertex -> explored ? 1 : 0

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
        for i in range(1, 10):
            info += f"Vertex {i} : {str(self.graph[i])}\n"

        return info

    def computeTopSSCs(self, topN=5):
        global time, src

        topNs = [0 for _ in range(topN + 1)]
        for v in range(1, self.num_vertices + 1):
            if not self.explored[v]:
                self.iterativeDFS(v, topNs, first=True)
        print("Processing ... The 1st DFS-Loop finished!")
        self.reset()
        for time in reversed(range(1, self.num_vertices + 1)):
            v = self.orders[time]
            if not self.explored[v]:
                src = v
                self.iterativeDFS(v, topNs, first=False)
        print("Processing ... The 2nd DFS-Loop finished!")

        return f"Top {topN} strongly connected components are of size {str(topNs[:-1])}"

    def iterativeDFS(self, start, topNs, first=True):
        global time, src

        self.explored[start] = True
        size_component = 1
        stack = deque()
        stack.append(start)
        while len(stack):
            while self.graph[stack[-1]]:
                v = stack[-1]
                # delete the last connected vertex to v if it has been explored
                while self.graph[v] and self.explored[self.graph[v][-1]]:
                    self.graph[v].pop()
                if self.graph[v]:
                    # let v be an new vertex never explored before
                    v = self.graph[v].pop()
                    self.explored[v] = True
                    size_component += 1
                    stack.append(v)
            # let v be vertex where all its connected nodes has been exhausted
            v = stack.pop()
            if first:
                time += 1
                self.orders[time] = v
        if not first:
            topNs[-1] = size_component
            topNs.sort(reverse=True)

        return 0

    def recursiveDFS(self, start, arr):
        global time
        self.explored[start] = True
        arr.append(start)
        for node in reversed(self.graph[start]):
            if not self.explored[node]:
                self.recursiveDFS(node, arr)
        time += 1
        self.orders[time] = start

        return 0

    def reset(self, reverse=False):
        global time, src
        time, src = 0, 0
        self.graph = {}
        self.num_vertices = 0
        self.constructGraph(self.list, reverse)
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
    initInput(lst, 'assign5_input.txt')
    graph = DirectedGraph(lst, reverse=True)
    '''
    for i in range(1, 10):
        arr1, arr2 = [], []
        graph.iterativeDFS(i, arr1)
        order1 = graph.orders[:]
        graph.reset()
        graph.recursiveDFS(i, arr2)
        order2 = graph.orders[:]
        graph.reset()
        assert len(arr1) == len(arr2)
        print(f"i : {i}")

        for j in range(len(arr1)):
            assert arr1[j] == arr2[j]
        for j in range(len(order1)):
            assert order1[j] == order2[j]

    print("All Success!")
    '''
    print(graph.computeTopSSCs(5))
    # print(graph.orders)
    # print(graph.leaders)

    return 0


if __name__ == '__main__':
    main()