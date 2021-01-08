# Assignment 9
from functools import cmp_to_key
from structure_utils import Node, MinHeap

class WeightedGraph:

    def __init__(self, adjacency_list):
        self.graph = adjacency_list
        self.num_vertices = len(adjacency_list)

    def __str__(self):
        info = f"Graph with {self.num_vertices} vertices\n"
        for i in range(1, min(10, self.num_vertices)):
            info += f"Vertex {i} : {str(self.graph[i])}\n"

        return info

    # Optimal: O(mlogn) time | O(n) space
    def computeMST(self, start):
        visited = {}
        min_cost = 0
        edge_lengths = {v: float('inf') for v in self.graph.keys()}
        edge_lengths[start] = 0
        minHeap = MinHeap([Node(v, length) for v, length in edge_lengths.items()])

        while len(visited) < self.num_vertices:
            node = minHeap.deleteMin()
            vertex, distance = node.key, node.value
            visited[vertex] = True
            min_cost += distance
            for u in self.graph[vertex]:  # O(n + mlogn) in total
                if u not in visited:
                    edge_lengths[u] = min(edge_lengths[u], self.graph[vertex][u])
                    minHeap.update(u, edge_lengths[u])

        return min_cost


# O(nlogn) time | O(n) space
def weightedSumCompletionTime(weights, lengths, compareFunc):
    jobs = []
    sum_completionTime = 0
    current_time = 0
    for i in range(len(weights)):
        w, l = weights[i], lengths[i]
        jobs.append((w, l))

    jobs.sort(key=cmp_to_key(compareFunc))
    for job in jobs:
        sum_completionTime += job[0] * (job[1] + current_time)
        current_time += job[1]

    return sum_completionTime


def compareScoreByDifference(job1, job2):
    w1, l1 = job1
    w2, l2 = job2
    s1, s2 = w1 - l1, w2 - l2
    if s1 < s2:
        return 1
    elif s1 > s2:
        return -1
    if w1 < w2:
        return 1
    elif w1 > w2:
        return -1

    return 1


def compareScoreByRatio(job1, job2):
    w1, l1 = job1
    w2, l2 = job2
    s1, s2 = w1 / l1, w2 / l2
    if s1 < s2:
        return 1
    else:
        return -1


def init_input(weights, lengths, graph, path_1, path_2):
    file_1 = open(path_1, 'r')
    total = file_1.readline()
    while True:
        line = file_1.readline()
        if not line:
            break
        w, l = line.split()
        weights.append(int(w))
        lengths.append(int(l))
    file_2 = open(path_2, 'r')
    num_vertices, num_edges = file_2.readline().split()
    while True:
        line = file_2.readline()
        if not line:
            break
        line = line.split()
        u, v, weight = int(line[0]), int(line[1]), int(line[2])
        if u not in graph:
            graph[u] = {v: weight}
        else:
            graph[u][v] = weight
        if v not in graph:
            graph[v] = {u: weight}
        else:
            graph[v][u] = weight

    return total, num_vertices, num_edges


def main():
    weights, lengths = [], []
    adjacency_list = {}
    total, num_vertices, num_edges = init_input(
        weights,
        lengths,
        adjacency_list,
        'assign9_input_1.txt',
        'assign9_input_2.txt'
    )

    min_completion_difference = weightedSumCompletionTime(weights, lengths, compareScoreByDifference)
    min_completion_ratio = weightedSumCompletionTime(weights, lengths, compareScoreByRatio)
    print(f'Minimum Completion Time by comparing score (weight-length): {min_completion_difference}\n'
          f'Minimum Completion Time by comparing score (weight/length): {min_completion_ratio}')

    graph = WeightedGraph(adjacency_list)
    min_cost = graph.computeMST(1)
    print(f'Minimum Spanning Tree has cost: {min_cost}')

    return 0


if __name__ == '__main__':
    main()