# Assignment 6
from structure_utils import *

class WeightedGraph:

    def __init__(self, adjacency_list):
        self.graph = adjacency_list
        self.num_vertices = len(adjacency_list)

    def __str__(self):
        info = f"Graph with {self.num_vertices} vertices\n"
        for i in range(1, self.num_vertices):
            info += f"Vertex {i} : {str(self.graph[i])}\n"

        return info

    def fastDijkstraShortestPath(self, start):
        visited = {start: True}
        min_distances = {vertex: float('inf') for vertex in self.graph.keys()}
        min_distances[start] = 0
        minHeap = MinHeap([Node(key, float('inf')) for key in self.graph.keys()])
        minHeap.update(start, 0)
        while len(visited) < self.num_vertices:
            node = minHeap.deleteMin()
            vertex, min_distance = node.key, node.value
            visited[vertex] = True
            for v in self.graph[vertex]:
                if v not in visited:
                    edge_length = self.graph[vertex][v]
                    d = min_distance + edge_length
                    current_distance = min_distances[v]
                    if d < current_distance:
                        min_distances[v] = d
                        minHeap.update(v, d)

        return min_distances

    def dijkstraShortestPath(self, start):
        visited = {start: 0}
        shortest_paths = {start: [start]}
        while len(visited) < self.num_vertices:
            min_distance, min_path = self.chooseMinEdge(visited)
            visited[min_path[1]] = min_distance
            shortest_paths[min_path[1]] = shortest_paths[min_path[0]] + [min_path[1]]

        return visited, shortest_paths

    def chooseMinEdge(self, visited):
        min_distance, min_path = float('inf'), None
        for v in self.graph:
            if v not in visited:
                continue
            edges = self.graph[v]
            for u in edges:
                if u not in visited:
                    d = visited[v] + edges[u]
                    min_distance = min(min_distance, d)
                    min_path = (v, u) if min_distance == d else min_path

        return min_distance, min_path


def initInput(adjacency_list, path):
    file = open(path, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        line = line.split()
        vertex = int(line[0])
        edges = {}
        for i in line[1:]:
            i = i.split(',')
            node, length = int(i[0]), int(i[1])
            edges[node] = length
        adjacency_list[vertex] = edges

    return 0


def main():
    adjacency_list = {}
    initInput(adjacency_list, 'assign6_input.txt')

    info = []
    graph = WeightedGraph(adjacency_list)
    shortest_paths = graph.fastDijkstraShortestPath(1)
    vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    for vertex in vertices:
        info.append(str(shortest_paths[vertex]))
    info = ','.join(info)
    print(f'Shortest-path of selected vertices are: {info}')  # info = 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068

    info = []
    shortest_paths, _ = graph.dijkstraShortestPath(1)
    vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    for vertex in vertices:
        info.append(str(shortest_paths[vertex]))
    info = ','.join(info)
    print(f'Shortest-path of selected vertices are: {info}')  # info = 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068

    return 0


if __name__ == '__main__':
    main()