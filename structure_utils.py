import random
from abc import *

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


class Tree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(Tree):

    def __init__(self, value):
        super().__init__(value)
        self.frequency = None

    def insert(self, value):
        node = self
        while True:
            if value < node.value:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = BST(value)
                    break
            else:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = BST(value)
                    break

        return 0

    def contains(self, value):
        node = self
        while node is not None:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return True

        return False

    def remove(self, value):
        parent, node = None, self
        while node is not None:
            if value < node.value:
                parent = node
                node = node.left
            elif value > node.value:
                parent = node
                node = node.right
            else:
                break
        if node is not None:
            # if node has two children
            if node.left is not None and node.right is not None:
                node.value = node.right.deleteMin(node)
            # if node is root node
            elif parent is None:
                # root has left child
                if node.left is not None:
                    node.value = node.left.value
                    node.right = node.left.right
                    node.left = node.left.left
                # root has right child
                elif node.right is not None:
                    node.value = node.right.value
                    node.left = node.right.left
                    node.right = node.right.right
            # node has left child
            elif node.left is not None:
                parent.replace(node, node.left)
            # node has right child
            elif node.right is not None:
                parent.replace(node, node.right)
            # node is leave node
            else:
                parent.replace(node, None)

        # Do not edit the return statement of this method.
        return self

    def replace(self, node, new_node):
        if node is self.left:
            self.left = new_node
        else:
            self.right = new_node

        return 0

    def deleteMin(self, parent):
        node = self
        while node.left is not None:
            parent = node
            node = node.left
        parent.replace(node, None)

        return node.value

    def optimalBinaryTree(self, frequency):
        self.setFrequency(frequency)
        cache = [[0 for _ in frequency] for _ in frequency]
        for i in range(len(frequency)):
            cache[i][i] = frequency[i]
        for s in range(1, len(frequency)):
            for i in range(len(frequency)):
                if i + s == len(frequency):
                    break
                values = []
                for r in range(i, i+s+1):
                    left = cache[i][r-1] if r >= 0 else 0
                    right = cache[r+1][i+s] if r + 1 < len(frequency) else 0
                    values.append(left + right)
                cache[i][i+s] = sum(frequency[i:i+s+1]) + min(values)

        return cache[0][-1]

    def setFrequency(self, frequency):
        self.frequency = frequency


class Heap:

    def __init__(self, array):
        self.indices = {array[i].key: i for i in range(len(array))}
        self.heap = self.heapify(array)

    @abstractmethod
    def heapify(self, array):
        raise NotImplementedError("Subclass must implement this method!")

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        info = []
        count = 1
        for node in self.heap:
            node_info = f'{node.key}: {node.value}'
            if count % 10 == 0:
                node_info += '\n'
            else:
                node_info += '     '
            count += 1
            info.append(node_info)

        return ''.join(info)

    __repr__ = __str__

    def peek(self):
        return self.heap[0].key

    @staticmethod
    def leftChild(index, heap):
        leftChild_idx = index * 2 + 1
        if leftChild_idx < len(heap):
            return heap[leftChild_idx]
        else:
            return None

    @staticmethod
    def rightChild(index, heap):
        rightChild_idx = index * 2 + 2
        if rightChild_idx < len(heap):
            return heap[rightChild_idx]
        else:
            return None

    @staticmethod
    def parent(index, heap):
        parent_idx = (index - 1) // 2
        if parent_idx >= 0:
            return heap[parent_idx]
        else:
            return None

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
        self.indices[heap[i].key], self.indices[heap[j].key] = self.indices[heap[j].key], self.indices[heap[i].key]

        return 0


class MinHeap(Heap):

    def __init__(self, array):
        super().__init__(array)

    def heapify(self, array):
        firstParent_idx = (len(array) - 2) // 2
        for index in reversed(range(firstParent_idx + 1)):
            self.siftDown(index, array)

        return array

    def insert(self, key, value):
        node = Node(key, value)
        self.heap.append(node)
        self.indices[key] = len(self) - 1
        self.siftUp(len(self) - 1, self.heap)

    def deleteMin(self):
        self.swap(0, len(self) - 1, self.heap)
        min_node = self.heap.pop()
        self.indices.pop(min_node.key)
        self.siftDown(0, self.heap)

        return min_node

    def removeKey(self, key):
        index = self.indices[key]

        return self.delete(index)

    def delete(self, index):
        self.swap(index, len(self) - 1, self.heap)
        node = self.heap.pop()
        self.indices.pop(node.key)
        if index < len(self):
            self.siftUp(index, self.heap)
            self.siftDown(index, self.heap)

        return node

    def update(self, key, value):
        index = self.indices[key]
        self.heap[index].value = value
        self.siftDown(index, self.heap)
        self.siftUp(index, self.heap)

    def siftDown(self, index, heap):
        leftChild = self.leftChild(index, heap)
        while leftChild is not None:
            rightChild = self.rightChild(index, heap)
            if rightChild is not None and rightChild.value < leftChild.value:
                swap_idx = index * 2 + 2
            else:
                swap_idx = index * 2 + 1
            if heap[swap_idx].value < heap[index].value:
                self.swap(swap_idx, index, heap)
                index = swap_idx
                leftChild = self.leftChild(index, heap)
            else:
                break

        return 0

    def siftUp(self, index, heap):

        parent = self.parent(index, heap)
        while index > 0 and heap[index].value < parent.value:
            self.swap(index, (index - 1) // 2, heap)
            index = (index - 1) // 2
            parent = self.parent(index, heap)

        return 0


class MaxHeap(Heap):

    def __init__(self, array):
        super().__init__(array)

    def heapify(self, array):
        firstParent_idx = (len(array) - 2) // 2
        for index in reversed(range(firstParent_idx + 1)):
            self.siftDown(index, array)

        return array

    def insert(self, key, value):
        node = Node(key, value)
        self.heap.append(node)
        self.indices[key] = len(self) - 1
        self.siftUp(len(self) - 1, self.heap)

    def deleteMax(self):
        self.swap(0, len(self) - 1, self.heap)
        max_node = self.heap.pop()
        self.indices.pop(max_node.key)
        self.siftDown(0, self.heap)

        return max_node

    def removeKey(self, key):
        index = self.indices[key]

        return self.delete(index)

    def delete(self, index):
        self.swap(index, len(self) - 1, self.heap)
        node = self.heap.pop()
        self.indices.pop(node.key)
        if index < len(self):
            self.siftUp(index, self.heap)
            self.siftDown(index, self.heap)

        return node

    def update(self, key, value):
        index = self.indices[key]
        self.heap[index].value = value
        self.siftDown(index, self.heap)
        self.siftUp(index, self.heap)

    def siftDown(self, index, heap):
        leftChild = self.leftChild(index, heap)
        while leftChild is not None:
            rightChild = self.rightChild(index, heap)
            if rightChild is not None and rightChild.value > leftChild.value:
                swap_idx = index * 2 + 2
            else:
                swap_idx = index * 2 + 1
            if heap[swap_idx].value > heap[index].value:
                self.swap(swap_idx, index, heap)
                index = swap_idx
                leftChild = self.leftChild(index, heap)
            else:
                break

        return 0

    def siftUp(self, index, heap):
        parent = self.parent(index, heap)
        while index > 0 and heap[index].value > parent.value:
            self.swap(index, (index - 1) // 2, heap)
            index = (index - 1) // 2
            parent = self.parent(index, heap)

        return 0


class UnionFind:

    def __init__(self, nodes):
        self.leaders = {node: node for node in nodes}
        self.components = {root: [root] for root in nodes}
        self.num_components = len(nodes)

    def find(self, node_i, node_j):
        return self.leaders[node_i] == self.leaders[node_j]

    def union(self, node_i, node_j):
        if self.find(node_i, node_j):
            return 0

        leader_i, leader_j = self.leaders[node_i], self.leaders[node_j]
        if len(self.components[leader_i]) < len(self.components[leader_j]):
            old, new = leader_i, leader_j
        else:
            old, new = leader_j, leader_i

        self.components[new] += self.components[old]
        self.changeLeader(old, new)
        self.components.pop(old)
        self.num_components -= 1

        return 0

    def changeLeader(self, old_leader, new_leader):
        for node in self.components[old_leader]:
            self.leaders[node] = new_leader

        return 0


class Graph:

    def __init__(self, edges=None):
        self.graph = self.buildAdjacencyList(edges)
        self.num_vertices = len(self.graph)
        self.num_edges = len(edges)

    def buildAdjacencyList(self, edges):
        if edges is None:
            return []
        for edge in edges:
            u, v = edge
            if u not in self.graph:
                self.graph[u] = {v: True}
            else:
                self.graph[u][v] = True
            if v not in self.graph:
                self.graph[v] = {u: True}
            else:
                self.graph[v][u] = True


def isMinHeapPropertySatisfied(array):
    for currentIdx in range(1, len(array)):
        parentIdx = (currentIdx - 1) // 2
        if array[parentIdx].value >= array[currentIdx].value:
            return False

    return True


def isMaxHeapPropertySatisfied(array):
    for currentIdx in range(1, len(array)):
        parentIdx = (currentIdx - 1) // 2
        if array[parentIdx].value < array[currentIdx].value:
            return False

    return True


def checkIndex(array, indices):
    for key, idx in indices.items():
        if array[idx].key != key:
            return False

    return True


def isValueInHeap(value, heap):
    for node in heap:
        if value == node.value:
            return True

    return False


def main():
    bst = BST(0)
    a = bst.optimalBinaryTree([0.2, 0.05, 0.17, 0.1, 0.2, 0.03, 0.25])
    print(a)

if __name__ == '__main__':
    main()