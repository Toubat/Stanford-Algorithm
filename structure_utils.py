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


class BST:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
    pass


if __name__ == '__main__':
    main()


'''
    array = [17, 13, 45, 34, 87, 31, 3, 10, 8, 2, 1, 9]
    minHeap = MaxHeap([Node(i, i) for i in array])
    assert isMaxHeapPropertySatisfied(minHeap.heap)
    assert checkIndex(minHeap.heap, minHeap.indices)
    assert minHeap.deleteMax().value == 87
    assert checkIndex(minHeap.heap, minHeap.indices)
    assert isMaxHeapPropertySatisfied(minHeap.heap)
    print("passed A")
    for i in range(1, 5000):
        value = random.randint(1, 1000)
        if isValueInHeap(value, minHeap.heap):
            continue
        minHeap.insert(value, value)
        assert checkIndex(minHeap.heap, minHeap.indices)
        assert isMaxHeapPropertySatisfied(minHeap.heap)
    print(minHeap)
    print("Passed B")
    for i in range(1, 5000):
        if len(minHeap) == 0:
            break
        node = minHeap.heap[random.randint(0, len(minHeap) - 1)]
        n = minHeap.removeKey(node.key)
        #  print(f"node.value: {node.value}  value: {va}")
        assert node.value == n.value
        assert len(minHeap) == len(minHeap.indices)
        assert checkIndex(minHeap.heap, minHeap.indices)
        assert isMaxHeapPropertySatisfied(minHeap.heap)
    print("Passed C")

    array = [i for i in range(1, 100)]
    random.shuffle(array)
    minHeap = MaxHeap([Node(i, i) for i in array])
    for i in range(1000):
        rand = random.randint(101, 2000)
        key = minHeap.heap[random.randint(0, len(minHeap) - 1)].key
        if isValueInHeap(rand, minHeap.heap):
            continue
        minHeap.update(key, rand)
        assert checkIndex(minHeap.heap, minHeap.indices)
        assert isMaxHeapPropertySatisfied(minHeap.heap)
    print("Passed D")
    while len(minHeap) > 0:
        minHeap.deleteMax()
        assert checkIndex(minHeap.heap, minHeap.indices)
'''