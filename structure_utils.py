import random

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value

class MinHeap:

    def __init__(self, array):
        self.indices = {array[i].key: i for i in range(len(array))}
        self.heap = self.heapify(array)

    def heapify(self, array):
        firstParent_idx = (len(array) - 2) // 2
        for index in reversed(range(firstParent_idx + 1)):
            self.siftDown(index, array)

        return array

    def __len__(self):
        return len(self.heap)

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

    def parent(self, index):
        parent_idx = (index - 1) // 2
        if parent_idx >= 0:
            return self.heap[parent_idx]
        else:
            return None

    def peek(self):
        return self.heap[0].key

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
        parent = self.parent(index)
        while index > 0 and heap[index].value < parent.value:
            self.swap(index, (index - 1) // 2, heap)
            index = (index - 1) // 2
            parent = self.parent(index)

        return 0

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
        self.indices[heap[i].key], self.indices[heap[j].key] = self.indices[heap[j].key], self.indices[heap[i].key]

        return 0


def isMinHeapPropertySatisfied(array):
    for currentIdx in range(1, len(array)):
        parentIdx = (currentIdx - 1) // 2
        if array[parentIdx].value >= array[currentIdx].value:
            print(f"{array[parentIdx].value}  {array[currentIdx].value}")
            return False

    return True


def main():
    pass


if __name__ == '__main__':
    main()