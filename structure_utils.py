import random

class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value

class MinHeap:

    def __init__(self, array):
        self.indices = {array[i]: i for i in range(len(array))}
        self.heap = self.constructHeap(array)

    def constructHeap(self, array):
        firstParent_idx = (len(array) - 2) // 2
        for index in reversed(range(firstParent_idx + 1)):
            self.moveDown(index, array)

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
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.indices[value] = len(self) - 1
        self.moveUp(len(self) - 1, self.heap)

    def deleteMin(self):
        self.swap(0, len(self) - 1, self.heap)
        min_value = self.heap.pop()
        self.indices.pop(min_value)
        self.moveDown(0, self.heap)

        return min_value

    def removeValue(self, value):
        index = self.indices[value]

        return self.delete(index)

    def delete(self, index):
        self.swap(index, len(self) - 1, self.heap)
        value = self.heap.pop()
        self.indices.pop(value)
        if index < len(self):
            self.moveUp(index, self.heap)
            self.moveDown(index, self.heap)

        return value

    def moveDown(self, index, heap):
        leftChild = self.leftChild(index, heap)
        while leftChild is not None:
            rightChild = self.rightChild(index, heap)
            if rightChild is not None and rightChild < leftChild:
                swap_idx = index * 2 + 2
            else:
                swap_idx = index * 2 + 1
            if heap[swap_idx] < heap[index]:
                self.swap(swap_idx, index, heap)
                index = swap_idx
                leftChild = self.leftChild(index, heap)
            else:
                break

        return 0

    def moveUp(self, index, heap):
        parent = self.parent(index)
        while index > 0 and heap[index] < parent:
            self.swap(index, (index - 1) // 2, heap)
            index = (index - 1) // 2
            parent = self.parent(index)

        return 0

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
        self.indices[heap[i]], self.indices[heap[j]] = self.indices[heap[j]], self.indices[heap[i]]

        return 0


def isMinHeapPropertySatisfied(array):
    for currentIdx in range(1, len(array)):
        parentIdx = (currentIdx - 1) // 2
        if array[parentIdx] > array[currentIdx]:
            return False

    return True

def checkIndex(array, indices):
    for value, idx in indices.items():
        if array[idx] != value:
            return False

    return True

def main():
    minHeap = MinHeap([17, 13, 45, 34, 87, 31, 3, 10, 8, 2, 1, 9])
    assert checkIndex(minHeap.heap, minHeap.indices)
    minHeap.deleteMin()
    assert checkIndex(minHeap.heap, minHeap.indices)
    for i in range(1, 5000):
        value = random.randint(1, 1000)
        if value in minHeap.indices:
            continue
        minHeap.insert(value)
        assert checkIndex(minHeap.heap, minHeap.indices)
        assert isMinHeapPropertySatisfied(minHeap.heap)
    for i in range(1, 5000):
        if len(minHeap) == 0:
            break
        value = minHeap.heap[random.randint(0, len(minHeap) - 1)]
        val = minHeap.removeValue(value)
        assert val == value
        assert len(minHeap) == len(minHeap.indices)
        assert checkIndex(minHeap.heap, minHeap.indices)
        assert isMinHeapPropertySatisfied(minHeap.heap)


if __name__ == '__main__':
    main()