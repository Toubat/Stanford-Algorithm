# Assignment 10
import sys
from structure_utils import Tree, MinHeap, Node

sys.setrecursionlimit(20000)

def huffmanCode(lst, minHeap=None):
    if minHeap is None:
        minHeap = MinHeap([Node(Tree(i), lst[i]) for i in range(len(lst))])
    if len(minHeap) == 1:
        return minHeap
    else:
        fuseSymbols(minHeap)
        return huffmanCode(lst, minHeap)


def findTreeDepth(root, level=0):
    if root is None:
        return level - 1, level - 1
    max_left, min_left = findTreeDepth(root.left, level + 1)
    max_right, min_right = findTreeDepth(root.right, level + 1)

    return max(max_left, max_right), min(min_left, min_right)


def fuseSymbols(minHeap):
    s1 = minHeap.deleteMin()
    s2 = minHeap.deleteMin()
    root = Tree(s1.key.value * 10 + s2.key.value)
    root.left = s1.key
    root.right = s2.key
    minHeap.insert(root, s1.value + s2.value)

    return 0


def maxWeightIndependentSet(weights):
    cache = [(0, False)] + [(0, False) for _ in weights]
    cache[1] = (weights[0], True)
    for i in range(1, len(weights)):
        node_idx = i + 1
        weight = max(cache[node_idx-1][0], cache[node_idx-2][0] + weights[i])
        considered = True if cache[node_idx-1][0] < cache[node_idx-2][0] + weights[i] else False
        cache[node_idx] = (weight, considered)

    return cache


def findMaxWeightISPath(cache):
    path = []
    idx = len(cache) - 1
    while idx > 0:
        if cache[idx][1]:
            path.append(idx)
            idx -= 2
        else:
            idx -= 1

    return path


def initInput(lst, path):
    with open(path, 'r') as f:
        f.readline()
        while True:
            line = f.readline()
            if not line:
                break
            num = int(line)
            lst.append(num)

    return 0


def main():
    lst = []
    initInput(lst, 'assign11_input_1.txt')
    minHeap = huffmanCode(lst)
    root = minHeap.deleteMin()
    max_len, min_len = findTreeDepth(root.key)
    print(max_len)
    print(min_len)

    lst = []
    initInput(lst, 'assign11_input_2.txt')
    cache = maxWeightIndependentSet(lst)
    path = findMaxWeightISPath(cache)
    byte = []
    for num in [1, 2, 3, 4, 17, 117, 517, 997]:
        if num in path:
            byte.append('1')
        else:
            byte.append('0')
    print(''.join(byte))


if __name__ == '__main__':
    main()